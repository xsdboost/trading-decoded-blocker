import yaml
from typing import Any, Dict
from yaml.loader import SafeLoader
from bantools.exceptions import ConfigFileMissingOrMalformed


class Config:
    def __init__(self, file_path: str) -> None:
        self.__get_config(file_path)

    @staticmethod
    def __load_file(file_path: str) -> Dict[Any, Any]:
        """

        Parameters
        ----------
        file_path: str
            yaml config file path

        Returns
        -------
            Config file returned as dictionary

        Exceptions
        ----------
            ConfigFileMissingOrMalformed
                thrown if file could not be found or it is malformed in some way
        """
        with open(file_path) as file_pointer:
            try:
                config: Dict[Any, Any] = yaml.load(file_pointer, Loader=SafeLoader)
            except Exception as e:
                raise ConfigFileMissingOrMalformed(
                    f"Config file malformed or missing value, file at {file_path}", e
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

    def __get_config(self, file_path: str):
        """

        Parameters
        ----------
        file_path: str
            functional calls helper objects to set member variables

        Returns
        -------
        None

        """
        config: Dict[Any, Any] = self.__load_file(file_path)
        self.__set_attrib(config)
