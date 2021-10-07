#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospkg
import rospy, time
from std_msgs.msg import String
from intent_classifier import Model
from google.protobuf import json_format
import os, json

test_path = rospkg.RosPack().get_path('dm_intent')
# test_path = '..'

# set homecare or reception
version = 'homecare'

model = Model(test_path + '/model/model_ckpt.ckpt')
publisher = rospy.Publisher('/intentCompletion', String, queue_size=10)

AUTH_KEY_HOMECARE_PATH = test_path + "/authkey/socialrobot-hyu-xdtlug-7fe2505e00b7.json"
AUTH_KEY_RECEPTION_PATH = test_path + "/authkey/socialrobot-hyu-reception-nyla-a093501276ce.json"

if version == "homecare":
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = AUTH_KEY_HOMECARE_PATH
else:
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = AUTH_KEY_RECEPTION_PATH

# [START dialogflow_detect_intent_text]
def detect_intent_texts(project_id, session_id, texts, language_code):
    """Returns the result of detect intent with texts as inputs.
    Using the same `session_id` between requests allows continuation
    of the conversation."""

    from google.cloud import dialogflow_v2 as dialogflow
    session_client = dialogflow.SessionsClient()

    session = session_client.session_path(project_id, session_id)
    print('Session path: {}\n'.format(session))

    for text in texts:
        text_input = dialogflow.types.TextInput(
            text=text, language_code=language_code)

        query_input = dialogflow.types.QueryInput(text=text_input)

        response = session_client.detect_intent(
            session=session, query_input=query_input)

        print('=' * 20)
        print('Query text: {}'.format(response.query_result.query_text))

        entities = response.query_result.parameters
        print(entities)
        # entities_dic = json_format.MessageToDict(entities)
        entities_dic = None
        return entities_dic


def classify_intent(msg):
    ros_input = json.loads(msg.data, encoding='utf-8')
    text = ros_input['dialog_intent']['human_speech']
    out = model.inference(text) # res는 최종 label output

    if version == "homecare":
        info = detect_intent_texts('socialrobot-hyu-xdtlug', 'socialrobot-hyu-xdtlug', [text], 'ko')  # homecare ko
    else:
        info = detect_intent_texts('socialrobot-hyu-reception-nyla', 'socialrobot-hyu-reception-nyla', [text], 'ko')  # reception ko
    # info = None

    out_msg = make_response_json(out, text, info)
    print(out_msg)
    publisher.publish(out_msg)


def make_response_json(label, human_speech, information):
    label_list = {0: '정보전달', 1: '인사', 2: '질문', 3: '요청', 4: '약속', 5: '수락', 6: '거부'}
    final_response = {
        "header": {
            "content": [
                "dialog_intent"
            ],
            "source": "dialog",
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

    rospy.Subscriber('/intentExecution', String, classify_intent)

    rospy.spin()
