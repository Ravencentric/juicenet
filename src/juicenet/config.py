import json
from pathlib import Path
from typing import Any, Union

import yaml

from .model import JuicenetConfig
from .types import JuicenetException


def read_config(config: Union[Path, dict[str, Any]]) -> JuicenetConfig:
    """
    Reads the yaml config file

    Returns a JuicenetConfig object with the data validated and type casted
    """
    if isinstance(config, Path):
        data = yaml.safe_load(config.read_text()) or {}
    elif isinstance(config, dict):
        data = config
    else:
        raise JuicenetException("Config must be a pathlib.Path or dict")

    return JuicenetConfig.model_validate(data)


def get_dump_failed_posts(config: Path) -> Path:
    """
    Get the value of `dump-failed-posts` from Nyuu config
    """
    data = json.loads(config.read_text())
    return Path(data["dump-failed-posts"]).resolve()
