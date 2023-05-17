"""Install """
import subprocess
from typing import Dict, Any

__all__ = ("build",)


def build_detectron2(setup_kwargs: Dict[str, Any]) -> None:
    subprocess.call(["pip3", "install", "git+https://github.com/facebookresearch/detectron2.git@v0.6"])

def build_centernet2(setup_kwargs: Dict[str, Any]) -> None:
    subprocess.call(["pip3", "install", "git+https://github.com/xingyizhou/CenterNet2.git@v0.4"])

if __name__ == "__main__":
    build_centernet2({})
    build_detectron2({})
