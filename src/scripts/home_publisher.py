# -*- coding: utf-8 -*-
import rospy
from std_msgs.msg import String


def talker():
    pub = rospy.Publisher('/taskExecution', String, queue_size=10)

    rospy.init_node('dm_intent_node', anonymous=True)
    rate = rospy.Rate(10)  # 10hz

    # KO Homecare
    publish_str_ko_home = []

    # publish_str_ko_home.append(
    #     '{"header": {"timestamp": "1563980674.262554407", "target": ["intent"], "content": ["dialog_intent"],"source": "planning"},"dialog_intent": {"name": "이병현", "intent": "saying_hello", "id": 196, "human_speech": "안녕","social_context": {"appellation":"어르신"}}}')
    # publish_str_ko_home.append(
    #     '{"header": {"timestamp": "1563980674.262554407", "target": ["intent"], "content": ["dialog_intent"], "source": "planning"}, "dialog_intent": {"name": "이병현", "intent": "check_information_sleep", "id": 197, "human_speech": "응 그래.","social_context": {}}}')
    # publish_str_ko_home.append(
    #     '{"header": {"timestamp": "1563980674.262554407", "target": ["intent"], "content": ["dialog_intent"], "source": "planning"}, "dialog_intent": {"name": "이병현", "intent": "transmit_information_reaction", "id": 198, "human_speech": "응 푹 잤지", "social_context": {}}}')
    # publish_str_ko_home.append(
    #     '{"header": {"timestamp": "1563980674.262554407", "target": ["intent"], "content": ["dialog_intent"], "source": "planning"},  "dialog_intent": {"name": "이병현", "intent": "check_information_disease", "id": 199, "human_speech": "그래 고마워", "social_context": {"disease_name":"고혈압"}}}')
    # publish_str_ko_home.append(
    #     '{"header": {"timestamp": "1563980674.262554407", "target": ["intent"], "content": ["dialog_intent"], "source": "planning"}, "dialog_intent": {"name": "이병현", "intent": "check_information_meal", "id": 200, "human_speech": "좋아졌어. 괜찮아.", "social_context": {}}}')
    # publish_str_ko_home.append(
    #     '{"header": {"timestamp": "1563980674.262554407", "target": ["intent"], "content": ["dialog_intent"], "source": "planning"}, "dialog_intent": {"name": "이병현", "intent": "transmit_information_disease_advise", "id": 201, "human_speech": "싱겁게 먹었어", "social_context": {"disease_name":"고혈압", "disease_advice":"싱거운 음식과 가벼운 운동"}}}')
    # publish_str_ko_home.append(
    #     '{"header": {"timestamp": "1563980674.262554407", "target": ["intent"], "content": ["dialog_intent"], "source": "planning"}, "dialog_intent": {"name": "이병현", "intent": "check_information_health", "id": 202, "human_speech": "그럼 알지. 네가 늘 말해주는데.", "social_context": {"task":"약 복용"}}}')
    # publish_str_ko_home.append(
    #     '{"header": {"timestamp": "1563980674.262554407", "target": ["intent"], "content": ["dialog_intent"], "source": "planning"}, "dialog_intent": {"name": "이병현", "intent": "transmit_information_health_advice", "id": 203, "human_speech": "먹었어.", "social_context": {"medicine_schedule":"식후 30분에 복용"}}}')
    # publish_str_ko_home.append(
    #     '{"header": {"timestamp": "1563980674.262554407", "target": ["intent"], "content": ["dialog_intent"], "source": "planning"}, "dialog_intent": {"name": "이병현", "intent": "saying_good_bye", "id": 204, "human_speech": "알겠어. 고마워.", "social_context": {}}}')
    # publish_str_ko_home.append(
    #     '{"header": {"timestamp": "1563980674.262554407", "target": ["intent"], "content": ["dialog_intent"], "source": "planning"}, "dialog_intent": {"name": "이병현", "intent": "saying_hello", "id": 205, "human_speech": "또 보는구나", "social_context": {"appellation":"어르신"}}}')
    # publish_str_ko_home.append(
    #     '{"header": {"timestamp": "1563980674.262554407", "target": ["intent"], "content": ["dialog_intent"], "source": "planning"}, "dialog_intent": {"name": "이병현", "intent": "check_information_schedule", "id": 205, "human_speech": "잘 지냈지", "social_context": {"visit_place":"병원"}}}')
    # publish_str_ko_home.append(
    #     '{"header": {"timestamp": "1563980674.262554407", "target": ["intent"], "content": ["dialog_intent"], "source": "planning"}, "dialog_intent": {"name": "이병현", "intent": "transmit_information_disease_regard", "id": 206, "human_speech": "응 다녀왔지", "social_context": {"disease_name":"고혈압","disease_status":"positive", "appellation":"어르신"}}}')
    # publish_str_ko_home.append(
    #     '{"header": {"timestamp": "1563980674.262554407", "target": ["intent"], "content": ["dialog_intent"], "source": "planning"}, "dialog_intent": {"name": "이병현", "intent": "transmit_information_medicine", "id": 207, "human_speech": "그렇지?", "social_context": {"disease_name":"고혈압", "disease_status":"positive", "appellation":"어르신"}}}')
    # publish_str_ko_home.append(
    #     '{"header": {"timestamp": "1563980674.262554407", "target": ["intent"], "content": ["dialog_intent"], "source": "planning"}, "dialog_intent": {"name": "이병현", "intent": "saying_good_bye", "id": 208, "human_speech": "알겠어. 고마워.", "social_context": {}}}')

    # publish_str_ko_home.append(
    #     '{"header": {"timestamp": "1563980674.262554407", "target": ["intent"], "content": ["dialog_intent"],"source": "planning"},"dialog_intent": {"name": "이병현", "intent": "saying_hello", "id": 196, "human_speech": "안녕","social_context": {"appellation":"할아버지"}}}')
    # publish_str_ko_home.append(
    #     '{"header": {"timestamp": "1563980674.262554407", "target": ["intent"], "content": ["dialog_intent"], "source": "planning"}, "dialog_intent": {"name": "이병현", "intent": "check_information_sleep", "id": 197, "human_speech": "응 그래.","social_context": {}}}')
    # publish_str_ko_home.append(
    #     '{"header": {"timestamp": "1563980674.262554407", "target": ["intent"], "content": ["dialog_intent"], "source": "planning"}, "dialog_intent": {"name": "이병현", "intent": "transmit_information_reaction", "id": 198, "human_speech": "잘 못 잤어", "social_context": {}}}')
    # publish_str_ko_home.append(
    #     '{"header": {"timestamp": "1563980674.262554407", "target": ["intent"], "content": ["dialog_intent"], "source": "planning"},  "dialog_intent": {"name": "이병현", "intent": "check_information_disease", "id": 199, "human_speech": "그래 고마워", "social_context": {"disease_name":"당뇨"}}}')
    # publish_str_ko_home.append(
    #     '{"header": {"timestamp": "1563980674.262554407", "target": ["intent"], "content": ["dialog_intent"], "source": "planning"}, "dialog_intent": {"name": "이병현", "intent": "check_information_meal", "id": 200, "human_speech": "안 좋아졌어. 나빠.", "social_context": {}}}')
    # publish_str_ko_home.append(
    #     '{"header": {"timestamp": "1563980674.262554407", "target": ["intent"], "content": ["dialog_intent"], "source": "planning"}, "dialog_intent": {"name": "이병현", "intent": "transmit_information_disease_advice", "id": 201, "human_speech": "싱겁게 먹었어", "social_context": {"disease_name":"당뇨", "disease_advice":"가벼운 운동과 싱거운 음식"}}}')
    # publish_str_ko_home.append(
    #     '{"header": {"timestamp": "1563980674.262554407", "target": ["intent"], "content": ["dialog_intent"], "source": "planning"}, "dialog_intent": {"name": "이병현", "intent": "check_information_health", "id": 202, "human_speech": "아니 몰라.", "social_context": {"task":"주사 복용"}}}')
    # publish_str_ko_home.append(
    #     '{"header": {"timestamp": "1563980674.262554407", "target": ["intent"], "content": ["dialog_intent"], "source": "planning"}, "dialog_intent": {"name": "이병현", "intent": "transmit_information_health_advice", "id": 203, "human_speech": "안 먹었어.", "social_context": {"medicine_schedule":"식후 3시간 후 복용"}}}')
    # publish_str_ko_home.append(
    #     '{"header": {"timestamp": "1563980674.262554407", "target": ["intent"], "content": ["dialog_intent"], "source": "planning"}, "dialog_intent": {"name": "이병현", "intent": "saying_good_bye", "id": 204, "human_speech": "알겠어. 고마워.", "social_context": {}}}')
    publish_str_ko_home.append(
        '{"header": {"timestamp": "1563980674.262554407", "target": ["intent"], "content": ["dialog_intent"], "source": "planning"},    \
            "dialog_intent": {"name": "이병현", "intent": "saying_hello", "id": 205, "human_speech": "또 보는구나", "social_context": {"appellation":"할아버지"}}}')
    publish_str_ko_home.append(
        '{"header": {"timestamp": "1563980674.262554407", "target": ["dialog"], "content": ["dialog_intent"], "source": "planning"},    \
            "dialog_intent": {"name": "이병현", "intent": "check_information_schedule", "id": 205, "human_speech": "잘 지냈어", "social_context": {"visit_place":"약국"}}}')
    publish_str_ko_home.append(
        '{"header": {"timestamp": "1563980674.262554407", "target": ["intent"], "content": ["dialog_intent"], "source": "planning"},  \
            "dialog_intent": {"name": "이병현", "intent": "transmit_information_disease_regard", "id": 206, "human_speech": "안 갔어", "social_context": {"disease_name":"당뇨","disease_status":"negative", "appellation":"할아버지"}}}')
    # publish_str_ko_home.append(
    #     '{"header": {"timestamp": "1563980674.262554407", "target": ["intent"], "content": ["dialog_intent"], "source": "planning"}, "dialog_intent": {"name": "이병현", "intent": "transmit_information_medicine", "id": 207, "human_speech": "그래?", "social_context": {"disease_name":"당뇨", "disease_status":"negative", "appellation":"할아버지"}}}')
    # publish_str_ko_home.append(
    #     '{"header": {"timestamp": "1563980674.262554407", "target": ["intent"], "content": ["dialog_intent"], "source": "planning"}, "dialog_intent": {"name": "이병현", "intent": "saying_good_bye", "id": 208, "human_speech": "알겠어. 고마워.", "social_context": {}}}')

    rospy.sleep(2)
    for k in range(0, len(publish_str_ko_home)):
        rospy.loginfo(publish_str_ko_home[k])
        pub.publish(publish_str_ko_home[k])
        rospy.sleep(11)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass