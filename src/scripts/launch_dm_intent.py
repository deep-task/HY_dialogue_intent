import rospkg
import rospy, time
from std_msgs.msg import String
from intent_classifier import Model

# test_path = rospkg.RosPack().get_path('dm_intent')
test_path = '..'

model = Model(test_path + '/model/model_ckpt.ckpt')
publisher = rospy.Publisher('/dialog', String, queue_size=10)

def classify_intent(msg):
    text = msg.data['human_speech']['speech']
    out = model.inference(text) # res는 최종 label output
    out_msg = make_response_json(out, text)
    publisher.publish(out_msg)


def make_response_json(label, human_speech):
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
            "name": ""
        }
    }
    return final_response


if __name__ == '__main__':
    rospy.init_node('dm_intent_node')
    rospy.loginfo('Start DM(intent)')

    rospy.Subscriber('/dialog/intent', String, classify_intent)

    rospy.spin()