from enum import Enum, auto
from yaml.loader import SafeLoader
import yaml


class ConfigType(Enum):
    BAN = 1


class Config:
    pass


def get_config(config_type: ConfigType, file_path: str, environ: str = None):
    conf = Config()
    if config_type == ConfigType.BAN:

        with open(file_path) as f:
            config = yaml.load(f, Loader=SafeLoader)

            if environ is not None:
                config = config[environ]

            for attrib_name, attrib_value in config.items():
                setattr(conf, attrib_name, attrib_value)
    else:
        raise NotImplementedError("Config type not supported")

    return conf
