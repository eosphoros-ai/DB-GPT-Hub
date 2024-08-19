from typing import List

from setuptools import find_packages, setup


class SetupSpec:
    def __init__(self) -> None:
        self.extras: dict = {}
        self.install_requires: List[str] = []

    @property
    def unique_extras(self) -> dict[str, list[str]]:
        unique_extras = {}
        for k, v in self.extras.items():
            unique_extras[k] = list(set(v))
        return unique_extras


setup_spec = SetupSpec()


def core_dependencies():
    setup_spec.extras["core"] = [
        "transformers>=4.41.2",
        "datasets>=2.14.6",
        "tiktoken>=0.7.0",
        "torch>=2.2.1",
        "peft>=0.4.0",
        "trl>=0.5.0",
        "prettytable",
        "func-timeout",
        "sqlparse",
        "jsonlines",
        "rouge-chinese>=1.0.3",
        "jieba>=0.42.1",
        "nltk>=3.8.1",
        "matplotlib>=3.8.1",
        "bitsandbytes>=0.39.0",
        "accelerate",
    ]


def init_install_requires():
    setup_spec.install_requires += setup_spec.extras["core"]
    print(f"Install requires: \n{','.join(setup_spec.install_requires)}")


core_dependencies()
init_install_requires()

excluded_packages = ["tests", "*.tests", "*.tests.*", "examples"]

setup(
    name="dbgpt-hub-gql",
    version="0.3.1",
    description="DB-GPT-Hub: Text-to-GQL parsing with LLMs",
    packages=find_packages(exclude=excluded_packages),
    install_requires=setup_spec.install_requires,
    extras_require=setup_spec.unique_extras,
    python_requires=">=3.10",
)
