import json
import os

import datasets
from datasets.tasks import TextClassification

logger = datasets.logging.get_logger(__name__)


class FinancialReport(datasets.GeneratorBasedBuilder):
    VERSION = datasets.Version("1.0.0")

    BUILDER_CONFIGS = [
        datasets.BuilderConfig(
            name="financial_report",
            version=VERSION,
            description="基金年报问答数据集",
        ),
    ]

    def __init__(self, *args, **kwargs):
        self._data_dir = kwargs["data_dir"]
        self._base_path = kwargs["base_path"]
        self._data_path = os.path.join(
            self._base_path, "data", "financial_report.jsonl"
        )
        super().__init__(*args, **kwargs)

    def _info(self) -> datasets.DatasetInfo:
        features = datasets.Features(
            {
                "text": datasets.Value("string"),
                "label": datasets.ClassLabel(
                    names=[
                        "年报基础信息问答",
                        "财务指标计算",
                        "专业名称解释",
                        "报告解读分析",
                        "统计对比分析",
                    ]
                ),
            }
        )
        return datasets.DatasetInfo(
            features=features,
            description="基金年报问答数据集",
            task_templates=[
                TextClassification(text_column="text", label_column="label")
            ],
        )

    def _split_generators(self, dl_manager):
        return [
            datasets.SplitGenerator(
                name=datasets.Split.TRAIN, gen_kwargs={"filepath": self._data_path}
            ),
        ]

    def _generate_examples(self, filepath):
        """Snips built in intent examples."""
        num_examples = 0
        with open(filepath, "r", encoding="utf-8") as f:
            for idx, line in enumerate(f):
                data = json.loads(line)
                yield idx, {
                    "text": data["question"],
                    "label": data["intent"],
                }
                num_examples += 1
