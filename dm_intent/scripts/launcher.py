#!/usr/bin/python3
# -*- coding: utf-8 -*-
import json
import rospkg
import rospy
import time
from std_msgs.msg import String
from intent_classifier import Model
from google.protobuf import json_format
import os
import json
from dtroslib.helpers import get_package_path, get_module_configuration, get_key_path
from dtroslib.dialogflow import DialogflowClient
from proto.marshal.collections.maps import MapComposite

test_path = get_package_path('dm_intent')
# test_path = '..'

# set homecare or reception
version = 'homecare'

model = Model(test_path + '/model/model_ckpt.ckpt')
publisher = rospy.Publisher('/dialogResult', String, queue_size=10)


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
        if isinstance(val, MapComposite):
            val = dict(val)
        elif type(val) != str:
            val = list(val)
        information[key] = val

    return information


def classify_intent(msg):
    ros_input = json.loads(msg.data, encoding='utf-8')
    # if "dialog" in ros_input['header']['target']:
    #     #df_intent = ros_input['dialog_generation']['intent']
    #     print("1111111111")
    #     df_intent = 'check_information_disease'
    #     #if df_intent == 'check_information_disease' or df_intent == 'check_information_sleep_2' or df_intent == 'check_information_drink' or df_intent == 'check_information_smoke':
    #     #    dialogflow_client.trigger_intent_event('check_information_health')
    if "dialog" in ros_input['header']['target']:
        print("22222222222222222222")
        text = ros_input['human_speech']['speech']
        # id = ros_input['header']['id']
        id = 31
        print("/recognitionResult : 사람 발화 수신 완료")
        out = model.inference(text)  # res는 최종 label output
        info = get_information(text)

        out_msg = make_response_json(out, text, id, info)
        print(out_msg)

        publisher.publish(json.dumps(out_msg))


def make_response_json(label, human_speech, id, information):
    label_list = {0: '정보전달', 1: '인사', 2: '질문',
                  3: '요청', 4: '약속', 5: '수락', 6: '거부'}
    final_response = {
        "header": {
            "id": id,
            "timestamp": str(time.time()),
            "source": "dialog_intent",
            "target": [
                "planning"
            ],
            "content": [
                "dialog_intent"
            ]
        },
        "dialog_intent": {
            "speech": human_speech,
            "intent": label_list[label],
            "information": information
        }
    }
    return final_response


if __name__ == '__main__':
    rospy.init_node('dm_intent_node')
    rospy.loginfo('Start DM(intent)')

    rospy.Subscriber('/recognitionResult', String, classify_intent)

    rospy.spin()
