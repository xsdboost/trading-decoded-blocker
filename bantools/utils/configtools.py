import yaml
from typing import Any, Dict

from pkg_resources import resource_stream
from yaml.loader import SafeLoader
from bantools.exceptions import ConfigFileMissingOrMalformed


class Config:
    def __init__(self, project_name: str,  config_resource: str) -> None:
        self.__get_config(project_name, config_resource)

    @staticmethod
    def __load_file(project_name: str, config_resource: str) -> Dict[Any, Any]:
        """

        Parameters
        ----------
        config_resource: str
            yaml config file path

        Returns
        -------
            Config file returned as dictionary

        Exceptions
        ----------
            ConfigFileMissingOrMalformed
                thrown if file could not be found or it is malformed in some way
        """
        with resource_stream(project_name, config_resource) as file_pointer:
            try:
                config: Dict[Any, Any] = yaml.load(file_pointer, Loader=SafeLoader)
            except Exception as e:
                raise ConfigFileMissingOrMalformed(
                    f"Config resource file malformed or missing values, resource at {config_resource}", e
                )

            return config

    def __set_attrib(self, config: Dict[Any, Any]) -> None:
        """

        Function creates class members based off config file

        Parameters
        ----------
        config: Dict[Any, Any]
            config yaml file loaded into dictionary

        Returns
        -------
        None

        Exception
        ---------
            ConfigFileMissingOrMalformed
                as we are setting attributes if file format is unrecognize this exception is thrown

        """
        for attrib_name, attrib_value in config.items():
            if not isinstance(attrib_value, str):
                raise ConfigFileMissingOrMalformed(
                    "Config file does not  match expected format, please fix file"
                )
            setattr(self, attrib_name, attrib_value)

    def __get_config(self, project_name: str,  config_resource: str):
        """

        Parameters
        ----------
        config_resource: str
            functional calls helper objects to set member variables

        Returns
        -------
        None

        """
        config: Dict[Any, Any] = self.__load_file(project_name, config_resource)
        self.__set_attrib(config)
