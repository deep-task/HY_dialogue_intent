import rospkg
import rospy
from std_msgs.msg import String
from intent_classifier import Model

# test_path = rospkg.RosPack().get_path('dm_intent')
test_path = '..'

model = Model(test_path + '/model/model_ckpt.ckpt')
publisher = rospy.Publisher('/dialog', String, queue_size=10)

def classify_intent(msg):
    text = msg.data['human_speech']['speech']
    res = model.inference(text) # res는 최종 label output
    # TODO res format check
    publisher.publish(res)

if __name__ == '__main__':
    rospy.init_node('dm_intent_node')
    rospy.loginfo('Start DM(intent)')

    rospy.Subscriber('/dialog/intent', String, classify_intent)

    rospy.spin()