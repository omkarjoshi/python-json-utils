from typing import Any

from converter.exceptions.exceptions import ObjectIsNoneException, ClassNotFoundException
from core import EncoderUtils, DecoderUtils
from core.reader import _readfile


def maptotypefromfile(filepath: str = None, type=None):
    if type is None:
        raise ClassNotFoundException()
    file = _readfile(filepath)
    if file is None:
        raise FileNotFoundError
    return DecoderUtils.GenericDecoder().decode(file)


def maptotypefromstring(jsonstring: str = None, type=None) -> Any:
    if jsonstring is None and type is None:
        raise ObjectIsNoneException()
    return DecoderUtils.GenericDecoder().decode(jsonstring)