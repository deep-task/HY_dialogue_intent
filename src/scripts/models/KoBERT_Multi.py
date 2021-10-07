import torch
from torch import nn
from kobert.pytorch_kobert import get_pytorch_kobert_model


class BERTClassifier(nn.Module):
    def __init__(self,
                 hidden_size=768,
                 num_classes=7,
                 dr_rate=None,
                 params=None):
        super(BERTClassifier, self).__init__()
        bert, _ = get_pytorch_kobert_model()
        self.bert = bert
        self.dr_rate = dr_rate
        self.classifier = nn.Linear(hidden_size, num_classes)
        if dr_rate:
            self.dropout = nn.Dropout(p=dr_rate)

    def gen_attention_mask(self, token_ids):
        attn_mask = ~torch.eq(token_ids, 1)
        return attn_mask.float()

    def forward(self, token_ids):
        attention_mask = self.gen_attention_mask(token_ids)

        _, pooler = self.bert(input_ids=token_ids, attention_mask=attention_mask.float().to(token_ids.device))
        if self.dr_rate:
            out = self.dropout(pooler)
        return self.classifier(out)