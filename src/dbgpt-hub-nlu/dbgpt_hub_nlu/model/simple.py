import json

import torch
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from torch import nn
from tqdm import tqdm
from transformers import AutoModel, AutoTokenizer, Trainer, TrainingArguments


class SimpleIntentClassifier(nn.Module):
    def __init__(self, input_dim: int, num_classes: int):
        super(SimpleIntentClassifier, self).__init__()
        self.fc1 = nn.Linear(input_dim, 128)
        self.fc2 = nn.Linear(128, num_classes)
        self.relu = nn.ReLU()

    def forward(self, input_ids, intent_label_ids):
        x = self.fc1(input_ids)
        x = self.relu(x)
        logits = self.fc2(x)
        if intent_label_ids is not None:
            loss_fct = nn.CrossEntropyLoss()
            loss = loss_fct(logits, intent_label_ids)
            return loss, logits
        return None, logits

    def save_pretrained(self, save_directory):
        torch.save(self.state_dict(), f"{save_directory}/pytorch_model.bin")
        config = {
            "input_dim": self.fc1.in_features,
            "num_classes": self.fc2.out_features,
        }
        with open(f"{save_directory}/config.json", "w") as f:
            json.dump(config, f)

    @classmethod
    def from_pretrained(cls, model_path):
        with open(f"{model_path}/config.json", "r") as f:
            config = json.load(f)
        model = cls(config["input_dim"], config["num_classes"])
        state_dict = torch.load(f"{model_path}/pytorch_model.bin")
        model.load_state_dict(state_dict)
        return model


def batch_sentence_embeddings(batch, tokenizer, model, device):
    encoded_input = tokenizer(batch, padding=True, truncation=True, return_tensors="pt").to(device)
    with torch.no_grad():
        model_output = model(**encoded_input)
        sentence_embeddings = model_output[0][:, 0]
        sentence_embeddings = torch.nn.functional.normalize(
            sentence_embeddings, p=2, dim=1
        )
        return sentence_embeddings
