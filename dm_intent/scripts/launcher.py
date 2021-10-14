#!/usr/bin/python3
# -*- coding: utf-8 -*-
import json
import rospkg
import rospy, time
from std_msgs.msg import String
from intent_classifier import Model
from google.protobuf import json_format
import os, json
from dtroslib.helpers import get_package_path, get_module_configuration, get_key_path
from dtroslib.dialogflow import DialogflowClient


test_path = get_package_path('dm_intent')
# test_path = '..'

# set homecare or reception
version = 'homecare'

model = Model(test_path + '/model/model_ckpt.ckpt')
publisher = rospy.Publisher('/taskCompletion', String, queue_size=10)


configuration = get_module_configuration('dm_intent', version)

key_path = get_key_path('dm_intent', configuration['authorization']['key'])

dialogflow_client = DialogflowClient(project_id=configuration['project-id'],
                                     session_id=configuration['session-id'],
                                     key_path=key_path,
                                     language_code=configuration['language-code'])


def get_information(human_speech):
    response = dialogflow_client.detect_intent_text(human_speech)
    information = {}

    for key, val in response.query_result.parameters.items():
        if type(val) != str:
            val = list(val)
        information[key] = val

    return information


def classify_intent(msg):
    ros_input = json.loads(msg.data, encoding='utf-8')
    if "dialog_intent" in ros_input['header']['target']:
        text = ros_input['human_speech']['speech']
        out = model.inference(text) # res는 최종 label output
        info = get_information(text)

        out_msg = make_response_json(out, text, info)
        print(out_msg)
    
        publisher.publish(json.dumps(out_msg))


def make_response_json(label, human_speech, information):
    label_list = {0: '정보전달', 1: '인사', 2: '질문', 3: '요청', 4: '약속', 5: '수락', 6: '거부'}
    final_response = {
        "header": {
            "content": [
                "dialog_intent"
            ],
            "source": "dialog_intent",
            "target": [
                "planning"
            ],
            "timestamp": str(time.time())
        },
        "dialog_intent": {
            "intent": label_list[label],
            "speech": human_speech,
            "name": "",
            "information": information
        }
    }
    return final_response


if __name__ == '__main__':
    rospy.init_node('dm_intent_node')
    rospy.loginfo('Start DM(intent)')

    rospy.Subscriber('/taskExecution', String, classify_intent)

    rospy.spin()
