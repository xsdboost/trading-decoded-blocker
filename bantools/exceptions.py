class BanningTools(Exception):
    ...


class BlockerToolsExceptions(BanningTools):
    ...


class RepositoryException(BanningTools):
    ...


class UtilException(BlockerToolsExceptions):
    ...


class NullArgumentsNotAllowed(BlockerToolsExceptions):
    ...


class EnvironmentVariableException(UtilException):
    ...


class EnvironmentVariableUnavaiable(EnvironmentVariableException):
    ...
