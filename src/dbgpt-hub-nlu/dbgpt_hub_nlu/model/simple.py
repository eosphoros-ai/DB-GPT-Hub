import json
from typing import Dict, List, Tuple

import torch
from torch import nn


class SimpleIntentClassifier(nn.Module):
    def __init__(self, input_dim: int, num_classes: int):
        super(SimpleIntentClassifier, self).__init__()
        self.fc1 = nn.Linear(input_dim, 128)
        self.fc2 = nn.Linear(128, num_classes)
        self.relu = nn.ReLU()
        self._label_dict = None
        self._id2label = None

    def forward(self, input_ids, intent_label_ids):
        x = self.fc1(input_ids)
        x = self.relu(x)
        logits = self.fc2(x)
        if intent_label_ids is not None:
            loss_fct = nn.CrossEntropyLoss()
            loss = loss_fct(logits, intent_label_ids)
            return loss, logits
        return None, logits

    @property
    def device(self):
        return next(self.parameters()).device

    def save_pretrained(self, save_directory: str, label_dict: Dict[str, int]):
        current_device = self.device
        # Move model to CPU before saving
        self.to(torch.device("cpu"))
        torch.save(self.state_dict(), f"{save_directory}/pytorch_model.bin")
        config = {
            "architectures": ["SimpleIntentClassifier"],
            "input_dim": self.fc1.in_features,
            "hidden_size": self.fc2.out_features,
            "model_type": "simple",
        }
        tokenizer_config = {"labels": label_dict}
        with open(f"{save_directory}/config.json", "w") as f:
            json.dump(config, f, ensure_ascii=False)

        with open(f"{save_directory}/tokenizer_config.json", "w") as f:
            json.dump(tokenizer_config, f, ensure_ascii=False)
        self.to(current_device)

    @classmethod
    def from_pretrained(cls, model_path, map_location=None):
        with open(f"{model_path}/config.json", "r") as f:
            config = json.load(f)

        with open(f"{model_path}/tokenizer_config.json", "r") as f:
            tokenizer_config = json.load(f)

        model = cls(config["input_dim"], config["hidden_size"])

        if map_location is None:
            map_location = torch.device("cpu")

        state_dict = torch.load(
            f"{model_path}/pytorch_model.bin", map_location=map_location
        )
        model.load_state_dict(state_dict)

        model._label_dict = tokenizer_config["labels"]
        model._id2label = {v: k for k, v in model._label_dict.items()}
        return model

    def predict(self, input_ids, device) -> Tuple[List[str], List[Dict]]:
        _id2label = self._id2label
        device = device or self.device
        with torch.no_grad():
            input_ids = input_ids.to(device)
            _, logits = self(input_ids, None)
            probs = torch.argmax(logits, axis=1)
            predictions = []
            for p in probs:
                label = _id2label.get(p.item(), "Unknown")
                predictions.append(label)
            return predictions, []


def batch_sentence_embeddings(sentences, tokenizer, model, device, batch_size):
    from tqdm import tqdm

    embeddings = []
    for i in tqdm(range(0, len(sentences), batch_size), desc="Generating Embeddings"):
        batch = sentences[i : i + batch_size]
        encoded_input = tokenizer(
            batch, padding=True, truncation=True, return_tensors="pt"
        ).to(device)
        with torch.no_grad():
            model_output = model(**encoded_input)
            sentence_embeddings = model_output[0][:, 0]
            sentence_embeddings = torch.nn.functional.normalize(
                sentence_embeddings, p=2, dim=1
            )
            embeddings.append(sentence_embeddings)
    return torch.cat(embeddings)
