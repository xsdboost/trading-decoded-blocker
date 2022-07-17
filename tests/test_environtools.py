import os
import pytest
from bantools import getenv_var
from unittest import TestCase
from bantools import NullArgumentsNotAllowed, EnvironmentVariableUnavaiable


class TestEnvironment(TestCase):
    def test_getenv_var(self) -> None:

        env_name = "test_var"
        os.environ[env_name] = "AHJ32g3j4"
        assert getenv_var(env_name) == "AHJ32g3j4"

        del os.environ[env_name]

    def test_getenv_var_nullargs(self) -> None:

        with pytest.raises(NullArgumentsNotAllowed):
            getenv_var(None)

    def test_getenv_var_environment_unavilable(self) -> None:

        env_name = "TeSt_VaR"
        os.environ[env_name] = "ANotherOne"
        with pytest.raises(EnvironmentVariableUnavaiable):
            getenv_var(env_name)
