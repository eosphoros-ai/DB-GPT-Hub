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
    setup_spec.extras["core"] = ["transformers>=4.41.2", "accelerate", "scikit-learn", "torch>=2.2.1", "datasets"]



def init_install_requires():
    setup_spec.install_requires += setup_spec.extras["core"]
    print(f"Install requires: \n{','.join(setup_spec.install_requires)}")


core_dependencies()
init_install_requires()

excluded_packages = ["tests", "*.tests", "*.tests.*", "examples"]

setup(
    name="dbgpt-hub-nlu",
    version="0.1.0",
    description="Out-of-the-box text understanding model components, suitable for Chinese and English, capable of performing text understanding tasks such as information extraction and text classification under zero-shot conditions.",
    packages=find_packages(exclude=excluded_packages),
    install_requires=setup_spec.install_requires,
    extras_require=setup_spec.unique_extras,
    python_requires=">=3.10",
)
