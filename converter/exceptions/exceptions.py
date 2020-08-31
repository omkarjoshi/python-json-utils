
class ObjectIsNoneException(BaseException):
    objectname: str = __name__

    __doc__ = "This method is "


class ClassNotFoundException(BaseException):
    pass
