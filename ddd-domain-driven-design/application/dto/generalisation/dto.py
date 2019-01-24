import json
from .dtometa import DTOMeta


class DTO(metaclass=DTOMeta):

    def __new__(cls, *args, **kwargs):
        obj = super(DTO, cls).__new__(cls)
        obj._initialized_dto_descriptors = dict()
        obj._dto_descriptors_values = dict()
        for attr in obj._dto_descriptors:
            obj._initialized_dto_descriptors[attr] = False
        return obj

    @classmethod
    def from_dict(cls, dictionary: dict):
        return cls(dictionary)

    @classmethod
    def from_json(cls, json_string: str):
        dict_ = json.loads(json_string)
        return cls.from_dict(dict_)

    def __setattr__(self, attr, val):
        try:
            obj = object.__getattribute__(self, attr)
        except AttributeError:
            object.__setattr__(self, attr, val)
        else:
            if hasattr(obj, '__set__'):
                obj.__set__(self, val)
            else:
                object.__setattr__(self, attr, val)

    def __getattribute__(self, attr):
        obj = object.__getattribute__(self, attr)
        if hasattr(obj, '__get__'):
            return obj.__get__(self, type(self))
        return obj

    def __init__(self, dto_dict: dict):
        if not self._partial:
            assert set(dto_dict.keys()) == set(self._dto_descriptors.keys()), \
                "DTO {} fields {} mismatch the dictionary keys {}".format(self.__class__.__qualname__,
                                                                          list(self._dto_descriptors.keys()),
                                                                          list(dto_dict.keys()))
        else:
            assert set(self._dto_descriptors.keys()) < set(dto_dict.keys()), \
                "Partial DTO {} fields {} are missing in the dictionary keys".format(self.__class__.__qualname__,
                                                                                     set(self._dto_descriptors.keys())
                                                                                     > set(dto_dict.keys()))

        for k in self._dto_descriptors.keys():
            setattr(self, k, dto_dict[k])

    def to_dict(self):
        dto_dict = {}
        for k, v in self._dto_descriptors_values.items():
            if issubclass(v.__class__, DTO):
                dto_dict[k] = v.to_dict()
            else:
                dto_dict[k] = v
        return dto_dict

    def __str__(self):
        return '{}({})'.format(self.__class__.__qualname__, str(self._dto_descriptors_values))

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if type(self) != type(other):
            return False

        if set(self._dto_descriptors.keys()) != set(other._dto_descriptors.keys()):
            return False

        for k in self._dto_descriptors:
            if getattr(self, k) != getattr(other, k):
                return False

        return True
