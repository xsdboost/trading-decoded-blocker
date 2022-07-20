from enum import Enum, auto
from typing import Dict
from yaml.loader import SafeLoader
import yaml


class ConfigType(Enum):
    BAN = auto()

def get_config(config_type: ConfigType, file_path: str, environ: str):

    if config_type == ConfigType.BAN:

        with open(file_path) as f:
            config = yaml.load(f, Loader=SafeLoader)
            conf = BanningtoolConfig(config[environ])
    else:
        raise NotImplementedError("Config type not supported")

    return conf

class BanningtoolConfig:
    def __init__(self, attribs: Dict[str, str]):
        for attrib_name, attrib_values in attribs:
            setattr(self, attrib_name, attrib_values)
