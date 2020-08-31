from converter.exceptions.exceptions import ObjectIsNoneException
from core.EncoderUtils import GenericEncoder


def writetostring(obj=None) -> str:
    if obj is None:
        raise ObjectIsNoneException()
    return GenericEncoder().encode(obj)