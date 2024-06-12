import logging
import os
from typing import Optional, Type

import torch
from datasets import DatasetDict
from sklearn.metrics import accuracy_score
from transformers import Trainer

from .config.model_args import ModelArguments, NLUTrainingArguments

logger = logging.getLogger(__name__)


def _load_base_model(model_args: ModelArguments, device: torch.device):
    from transformers import AutoModel, AutoTokenizer

    tokenizer = AutoTokenizer.from_pretrained(
        model_args.base_tokenizer_name or model_args.base_model_name_or_path
    )
    model = AutoModel.from_pretrained(model_args.base_model_name_or_path)
    model = model.to(device)
    model.eval()
    return tokenizer, model


def compute_metrics(p):
    preds = torch.argmax(torch.Tensor(p.predictions), axis=1)
    return {"accuracy": accuracy_score(p.label_ids, preds)}


class NLUTrainer:
    def __init__(
        self,
        dataset: DatasetDict,
        model,
        training_args: NLUTrainingArguments,
        model_cls: Optional[Type] = None,
    ):
        self.dataset = dataset
        self.model = model
        self.model_cls = model_cls or model.__class__
        self.training_args = training_args
        self.trainer = Trainer(
            model=model,
            args=training_args,
            train_dataset=self.dataset["train"] if training_args.do_train else None,
            eval_dataset=self.dataset["valid"] if training_args.do_eval else None,
            compute_metrics=compute_metrics,
        )

    def load_model(self, model_path: Optional[str] = None):
        if not model_path:
            return
        model_file = os.path.join(model_path, "pytorch_model.bin")
        if not os.path.exists(model_file):
            return
        # Load the saved model weights
        model = self.model_cls.from_pretrained(model_path)
        model = model.to(self.training_args.device)
        self.model = model
        self.trainer.model = model
        logger.info(f"Model loaded from {model_path}")

    def train(self):
        self.trainer.train()
        self.model.save_pretrained(self.training_args.output_dir)
        self.trainer.save_model()

    def evaluate(self):
        eval_result = self.trainer.evaluate()
        logger.info(f"Evaluation result: {eval_result}")

    def infer(self, input_ids, label_features):
        model = self.model
        model.eval()
        label_features = label_features or self._get_label_features()
        with torch.no_grad():
            input_ids = input_ids.to(self.training_args.device)
            _, logits = model(input_ids, None)
            prediction = torch.argmax(logits, axis=1).item()
            prediction_label = label_features.int2str([prediction])
            logger.info(f"Prediction: {prediction_label[0]}")
            return prediction

    def _get_label_features(self):
        return self.dataset["train"].features["label"]
