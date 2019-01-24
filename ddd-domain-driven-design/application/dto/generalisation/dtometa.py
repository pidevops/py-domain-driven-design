from . import type_checker
from .dtodescriptor import DTODescriptor

class DTOMeta(type):

    def __init__(cls, name, bases, namespace, partial: bool = False):
        super().__init__(name, bases, namespace)

    def __new__(cls, name, bases, class_dict, partial: bool = False):

        descriptors = {k: v for k, v in class_dict.items() if isinstance(v, tuple)}
        _ = [class_dict.pop(k, None) for k in descriptors]

        class_dict['__slots__'] = set(list(descriptors.keys()) + ['_dto_descriptors',
                                                                  '_initialized_dto_descriptors',
                                                                  '_dto_descriptors_values',
                                                                  '_field_validators',
                                                                  '_partial'])

        new_type = type.__new__(cls, name, bases, class_dict)
        new_type._dto_descriptors = descriptors
        new_type._field_validators = {}
        new_type._partial = partial
        for attr in new_type._dto_descriptors:
            attr_type = new_type._dto_descriptors[attr][0]
            descriptor_args = {}
            if len(new_type._dto_descriptors[attr]) > 1:
                descriptor_args = new_type._dto_descriptors[attr][1]
            setattr(new_type, attr, DTODescriptor(dto_class_name=name, field=attr, type_=attr_type, **descriptor_args))
        return new_type

    def __instancecheck__(self, inst):
        if type(inst) == type(self):
            return True
        if isinstance(inst, dict):
            # Comparing a dictionary and a DTO
            if not self._partial:
                if len(inst.keys()) != len(self._dto_descriptors.keys()):
                    return False
                for k, v in inst.items():
                    try:
                        type_checker._check_type(self._dto_descriptors[k][0], v)
                    except TypeError:
                        return False
            else:
                for k in self._dto_descriptors.keys():
                    try:
                        type_checker._check_type(self._dto_descriptors[k][0], inst[k])
                    except (TypeError, KeyError):
                        return False
            return True
        return False
