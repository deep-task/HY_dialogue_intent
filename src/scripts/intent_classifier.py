import rospkg

# test_path = rospkg.RosPack().get_path('dm_intent')
test_path = '..'

class Model:
    def __init__(self, ckpt):
        self.model = load(ckpt) # 학습된 모델 불러오기

    def inference(self, text):
        result = self.model.run(text) # 학습된 모델에 텍스트 입력해서 나온 결과
        return result