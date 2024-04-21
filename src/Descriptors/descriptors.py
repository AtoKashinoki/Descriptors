"""
    Descriptors.descriptors

This file contains the descriptor classes used by the Descriptors module.
"""

# import modules
from abc import ABC
from copy import copy


""" Skeleton class of descriptors """


class Skeleton(ABC):
    """
        Skeleton class of descriptors

    This class is an inherited class.
    This class be used to create descriptor classes.
    """

    # variables
    __get_mode: str = None
    __owner: any = None
    __name: str = None

    def __init__(self, get_mode: str = ""):
        """
            Initialize descriptor settings
        :param get_mode: return mode of __get__ function.
        """
        self.__get_mode = get_mode
        return

    def __set_name__(self, owner, name):
        """ Initialize variable in owner """
        self.__owner = owner
        self.__name = name
        return

    def __set__(self, instance, value):
        """ Set value in instance.name """
        instance.__dict__[self.__name] = value
        return

    def __get__(self, instance, owner):
        """ Get value in instance.name """
        try:
            value = instance.__dict__[self.__name]
            if "c" in self.__get_mode:
                value = copy(value)
            return value
        except KeyError as e:
            return KeyError(F"KeyError: instance.__dict__[{e}]")

    @property
    def get_mode(self):
        """ return get_mode """
        return self.__get_mode

    @property
    def owner(self):
        """ return owner """
        return self.__owner

    @property
    def name(self) -> str:
        """ return name """
        return self.__name


""" Validate data type function"""


def validate_dtype(data, dtypes: tuple[type | None, ...]) -> str:
    """
        Validate data type of data.
    :param data: data to validate data type.
    :param dtypes: data types to validate.
    :return: return "dtype"
    """
    if any in dtypes:
        return "any"
    if data is None and None in dtypes:
        return "None"
    if type(data) in dtypes:
        return "type[data] in dtypes"

    raise TypeError(
        f"Unexpected data type assignment: "
        f"{data}('{type(data)}')\n"
        f"  Allowed data types -> {dtypes}"
    )


""" Data types validator """


class DataType(Skeleton):
    """
        DataType validator class

    This class validates the data type of the assigned value.
    """

    # variables
    __dtypes_type = tuple[type | None, ...]
    __dtypes: __dtypes_type = None

    def __init__(self, *dtypes: type | None, get_mode: str = ""):
        """
            Initialize dtypes and settings.
        :param dtypes: dtypes to validate.
        :param get_mode: return mode of __get__ function.
        """
        super().__init__(get_mode=get_mode)
        if len(dtypes) == 0:
            dtypes = (any, None)
        self.__dtypes = dtypes
        return

    def __set__(self, instance, value):
        """ Validate dtypes and set value """
        validate_dtype(value, self.__dtypes)
        Skeleton.__set__(self, instance, value)
        return

    @property
    def allowed_dtypes(self) -> __dtypes_type:
        """ return dtypes to allowed assignment """
        return self.__dtypes


""" Validate attribute function """


def validate_attribute(
        data, attributes: tuple[str | None, ...]
) -> str:
    """
        Validate value.attribute.
    :param data: value to validate attribute.
    :param attributes: attributes to validate.
    :return: return "attribute"
    """
    try:
        data_attributes = data.attribute
    except AttributeError:
        data_attributes = ()

    if any in attributes:
        return "any attribute"
    validate_result = {
        data_attribute: data_attribute in attributes
        for data_attribute in data_attributes
    }
    if sum(validate_result.values()) > 0:
        return f"{validate_result}"

    raise TypeError(
        f"Unexpected attribute assignment: "
        f"{data}('{data_attributes}')\n"
        f"  Allowed attribute -> {attributes}"
    )


""" Attribute validator """


class Attribute(DataType):
    """
        Attribute validator class.

    This class validates tha attribute of assigned value.
    """
    __attributes_type = tuple[str, ...]
    attributes: __attributes_type = \
        DataType(tuple, get_mode="c")

    def __init__(
            self, *attributes: str,
            dtypes: tuple[type | None, ...] = (),
            get_mode: str = "c"
    ):
        """
            Initialize attributes and setting.
        :param attributes: attributes to validate.
        :param dtypes: dtypes to validate.
        :param get_mode: return mode of __get__ function.
        """
        super().__init__(*dtypes, get_mode=get_mode)
        if len(attributes) == 0:
            attributes = (any, )
        self.attributes = attributes
        return

    def __set__(self, instance, value):
        """ Validate attribute and set value """
        validate_attribute(value, self.attributes)
        DataType.__set__(self, instance, value)
        return
