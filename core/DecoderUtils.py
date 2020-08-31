import json
from json import JSONDecoder


class GenericDecoder(JSONDecoder):

    def default(self, object):

        if isinstance(object, type(object)):

            return object.__dict__

        else:
            return json.JSONDecoder.default(self, object)
