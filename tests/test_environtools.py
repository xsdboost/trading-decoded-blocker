import os
from unittest import TestCase

import pytest

from bantools.exceptions import (EnvironmentVariableUnavaiable,
                                 NullArgumentsNotAllowed)
from bantools.utils.envtools import getenv_variable


class TestEnvironment(TestCase):
    def test_getenv_var(self) -> None:

        env_name = "test_var"
        os.environ[env_name] = "AHJ32g3j4"
        assert getenv_variable(env_name) == "AHJ32g3j4"

        del os.environ[env_name]

    def test_getenv_var_nullargs(self) -> None:

        with pytest.raises(NullArgumentsNotAllowed):
            getenv_variable(None)

    def test_getenv_var_environment_unavilable(self) -> None:

        env_name = "TeSt_VaR"
        os.environ[env_name] = "ANotherOne"
        with pytest.raises(EnvironmentVariableUnavaiable):
            getenv_variable(env_name)
