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
        "datasets>=2.14.7",
        "tiktoken>=0.7.0",
        "torch>=2.0.0",
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
        "bitsandbytes==0.41.3.post2",
        "accelerate",
        "sentencepiece==0.1.99",
        "einops==0.6.1",
        "evaluate==0.4.0",
        "scikit-learn==1.2.2",
        "wandb==0.15.3",
        "pydantic==1.10.11",
        "gradio>=3.36.0",
        "uvicorn-http2>=0.0.0",
        "uvicorn>=0.24.0.post1",
        "fastapi==0.95.1",
        "transformers-stream-generator>=0.0.4",
        "sse-starlette>=1.6.5",
        "rapidfuzz>=3.5.2",
        "scipy>=1.11.3",
        "nltk>=3.8.1",
        "pymysql>=1.1.0",
        "pyyaml==6.0.1",
        "black>=23.11.0",
        "pyright>=1.1.335",
        "pylint>=3.0.2",
        "markupsafe==2.1.3",
        "nvidia-cuda-nvrtc-cu12==12.1.105",
        "nvidia-cuda-runtime-cu12==12.1.105",
        "nvidia-cuda-cupti-cu12==12.1.105",
        "nvidia-cudnn-cu12==8.9.2.26",
        "nvidia-cublas-cu12==12.1.3.1",
        "nvidia-cufft-cu12==11.0.2.54",
        "nvidia-curand-cu12==10.3.2.106",
        "nvidia-cusolver-cu12==11.4.5.107",
        "nvidia-cusparse-cu12==12.1.0.106",
        "nvidia-nccl-cu12==2.18.1",
        "nvidia-nvtx-cu12==12.1.105",
        "triton==2.1.0",
        "nvidia-nvjitlink-cu12>=12.3.52",
        "docopt>=0.6.2",
        "openai>=1.6.1",
        "jaro-winkler==2.0.3",
        "antlr4-python3-runtime==4.13.2",
        "JPype1==1.5.0",
        "neo4j>=5.26.0",
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
