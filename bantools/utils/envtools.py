import os
from bantools.exceptions import EnvironmentVariableUnavaiable, NullArgumentsNotAllowed


def getenv_variable(variable_name: str) -> str:
    """
    Parameters
    ----------
    variable_name : str
        The environment variable we want to retrieve

    Returns
    -------
    str
        Returns the value of envrionment named by variable_name.

    Raises
    ------
    NullArgumentsNotAllowed
        If user passes None for variable name argument this exception will be raised

    EnvironmentVariableUnavaiable
        if environment variable does not exist then throw this exception


    """

    if variable_name is None:
        raise NullArgumentsNotAllowed("A None arguement was passed to variable_name")

    environ_var = os.environ.get(variable_name.lower())

    if environ_var is None:
        environ_var = os.environ.get(variable_name.upper())

    if environ_var is None:
        raise EnvironmentVariableUnavaiable(
            "Environment variable defined on system must be all uppercase or all lowercase"
        )

    return environ_var
