import rospkg
import torch
import pickle
from gluonnlp.data import SentencepieceTokenizer
from kobert.utils import get_tokenizer

# test_path = rospkg.RosPack().get_path('dm_intent')
test_path = '..'

class Model:
    def __init__(self, ckpt):
        # check map_location whether cpu or gpu
        self.kobert = torch.load('ckpt/kobert/kobert.pt', map_location=torch.device('cpu')) # 학습된 모델 불러오기
        self.kobert.eval()
        self.sp = SentencepieceTokenizer(get_tokenizer())
        with open('data/word2id.pkl', 'rb') as f:
            self.word2id = pickle.load(f)
    def inference(self, text):
        
        # word to id
        inp =[[word2id[ele] for ele in ['[CLS]']+sp(text)+['[SEP]']]]
        inp = torch.tensor(inp)
        out = self.kobert.run(inp) # 학습된 모델에 텍스트 입력해서 나온 결과
        _, result = torch.max(out, 1)   # result는 1d-tensor. tensor to list : .tolist()
        
        return result.tolist()[0]