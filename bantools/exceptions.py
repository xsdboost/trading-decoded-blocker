"""

Core exception

"""


class BanningTools(Exception):
    ...


"""
    
Base level exception dependencies 
    
"""


class BlockerToolsExceptions(BanningTools):
    ...


class RepositoryException(BanningTools):
    ...


"""

Second level exception dependencies

"""


class UtilException(BlockerToolsExceptions):
    ...


class NullArgumentsNotAllowed(BlockerToolsExceptions):
    ...


"""
    
Third level exception dependencies

"""


class EnvironmentVariableException(UtilException):
    ...


class EnvironmentVariableUnavaiable(EnvironmentVariableException):
    ...
