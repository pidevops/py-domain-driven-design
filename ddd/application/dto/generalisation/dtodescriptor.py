from ddd.application.dto.generalisation import type_checker


class DTODescriptor:
    __slots__ = "_immutable", "_type", "_field", "_validator", "_dto_class_name", "_coerce"

    def __init__(self, dto_class_name: str, field: str, type_: type, immutable: bool = True,
                 validator: callable = None, coerce: callable = None):
        self._dto_class_name = dto_class_name
        self._field = field
        self._type = type_
        self._immutable = immutable
        if validator and not callable(validator):
            raise TypeError("Validator for field '{}' of DTO class '{}' is not callable".format(field,
                                                                                                self._dto_class_name))
        self._validator = validator

        if coerce and not callable(coerce):
            raise TypeError("Coerce for field '{}' of DTO class '{}' is not callable".format(field,
                                                                                             self._dto_class_name))
        self._coerce = coerce

    def __get__(self, instance, type):
        if not instance._initialized_dto_descriptors[self._field]:
            raise AttributeError("Field '{}' of DTO class '{} is not Initialized".format(self._field,
                                                                                         self._dto_class_name))
        return instance._dto_descriptors_values.get(self._field)

    def _check_value(self, value):
        if self._validator is not None and not self._validator(value):
            raise ValueError(
                "{} is not a valid value for the field '{}' or DTO class {} using its validator".format(
                    value, self._field, self._dto_class_name))

    def __set__(self, instance, value):
        if self._coerce:
            value = self._coerce(value)

        if self._immutable and instance._initialized_dto_descriptors[self._field]:
            raise AttributeError("Immutable attribute '{}' of DTO class '{}' cannot be changed".format(self._field,
                                                                                                       instance.__class__.__name__))
        _type = type_checker._check_type_dto_descriptor(self, value)

        if _type is type(None):
            instance._dto_descriptors_values[self._field] = None

        else:
            self._check_value(value)
            instance._dto_descriptors_values[self._field] = value

        instance._initialized_dto_descriptors[self._field] = True
