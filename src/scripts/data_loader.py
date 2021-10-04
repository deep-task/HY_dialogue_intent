import torch.utils.data


class DT_Dataset(torch.utils.data.Dataset):
    def __init__(self, data, max_len):
        self.input_ids, self.labels = self.preprocessing(data, max_len)

    def __len__(self):
        return len(self.input_ids)

    def __getitem__(self, idx):
        return(torch.tensor(self.input_ids[idx]),
               torch.tensor(self.labels[idx]))

    def preprocessing(self, data, max_len):
        input_ids = []
        labels = []
        for ele in data:
            if not len(ele[0]) > max_len:
                input_ids.append(ele[0])
                labels.append(int(ele[1]))
        return input_ids, labels




""" Intention data collate_fn """
def DT_collate_fn(inputs):
    enc_inputs, dec_inputs = list(zip(*inputs))

    enc_inputs = torch.nn.utils.rnn.pad_sequence(enc_inputs, batch_first=True, padding_value=1)
    dec_inputs = torch.tensor(dec_inputs)
    batch = [
        enc_inputs,
        dec_inputs,
    ]
    return batch


def build_data_loader(data, batch_size=5, shuffle=True, max_len=56):
    dataset = DT_Dataset(data, max_len)
    # print(f'dataset length : {len(dataset)}', end='\n\n')
    loader = torch.utils.data.DataLoader(dataset, batch_size=batch_size, shuffle=shuffle,
                                         collate_fn=DT_collate_fn)
    return loader


if __name__ == '__main__':

    data_loader = build_data_loader()