import torch
import pickle, os, time

from data_loader import build_data_loader
from models.KoBERT_Multi import BERTClassifier

from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score


# device = torch.device("cuda:0")


# load bert model
# bertmodel, vocab = get_pytorch_kobert_model()

# load dataset
data_path = 'data/processing/data_kobert.pkl'
with open(data_path, 'rb') as f:
    data = pickle.load(f)
train = data['trainingSamples']
valid = data['validSamples']
test = data['testSamples']
id2word = data['id2word']
word2id = data['word2id']
del data

# Setting parameters
batch_size = 10
warmup_ratio = 0.1
num_epochs = 20
max_grad_norm = 1
log_interval = 200
learning_rate = 5e-5
inp_max_len = 56
dr_rate = 0.1

train_dataloader = build_data_loader(train, batch_size=batch_size, max_len=inp_max_len)
test_dataloader = build_data_loader(test, batch_size=batch_size, max_len=inp_max_len)
valid_dataloader = build_data_loader(valid, batch_size=batch_size, max_len=inp_max_len)

# load bert multi label calssification model
t_total = len(train_dataloader) * num_epochs


def comparision():
    # model = BERTClassifier(dr_rate=0.3)
    # model.load_state_dict(torch.load(f'ckpt/kobert/model_20epoch.pth', map_location=torch.device('cpu')))
    # model.eval()  # 평가 모드로 변경

    model2 = torch.load('ckpt/kobert/kobert.pt', map_location=torch.device('cpu'))
    model2.eval()

    # y_true = []
    # y_pred = []
    # for batch_id, (token_ids, labels) in enumerate(test_dataloader):
    #     token_ids = token_ids.long().cuda()
    #     y_true += labels.tolist()
    #     out = model(token_ids)
    #     _, indices = torch.max(out, 1)
    #     y_pred += indices.tolist()
    # print('f1 score')
    # print(f1_score(y_true, y_pred, average=None))
    # print('\nrecall score')
    # print(recall_score(y_true, y_pred, average=None))
    # print('\nprecision score')
    # print(precision_score(y_true, y_pred, average=None))
    # print('\nmodel accuracy')
    # print(accuracy_score(y_true, y_pred))
    # print('\nmodel f1 macro score')
    # print(f1_score(y_true, y_pred, average='macro'))

    print('\n\n')
    print('='*100)
    print('\n\n')
    y_true = []
    y_pred = []
    for batch_id, (token_ids, labels) in enumerate(test_dataloader):
        token_ids = token_ids.long()
        y_true += labels.tolist()
        out = model2(token_ids)
        _, indices = torch.max(out, 1)
        y_pred += indices.tolist()
    print('f1 score')
    print(f1_score(y_true, y_pred, average=None))
    print('\nrecall score')
    print(recall_score(y_true, y_pred, average=None))
    print('\nprecision score')
    print(precision_score(y_true, y_pred, average=None))
    print('\nmodel accuracy')
    print(accuracy_score(y_true, y_pred))
    print('\nmodel f1 macro score')
    print(f1_score(y_true, y_pred, average='macro'))





epoch = 20
# cal_accu()
# cal_f1(epoch)
# model_save()
comparision()