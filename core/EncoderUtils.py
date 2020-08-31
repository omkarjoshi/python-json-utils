import json
from json import JSONEncoder


class GenericEncoder(JSONEncoder):

    def default(self, object):

        if isinstance(object, type(object)):

            return object.__dict__

        else:
            return json.JSONEncoder.default(self, object)
