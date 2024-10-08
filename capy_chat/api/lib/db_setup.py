import json
from pathlib import Path

from .logger import get_customized_logger

logger = get_customized_logger(__name__)


def get_config(config_path_override: str = "config.json") -> dict | None:
    config_path = Path(config_path_override)
    try:
        config_text = config_path.read_text()
        return json.loads(config_text)
    except FileNotFoundError:
        logger.error(f"get_config: Error opening config at {config_path}")
    except Exception as err:
        logger.error(f"Unexpected exception: {err}")
