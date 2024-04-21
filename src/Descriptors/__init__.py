"""
    Descriptors module

We will add a class that facilitates the use of descriptors
to support development.

"""

# import
import sys


__self_name__ = "Descriptors"


if not __name__ == __self_name__:
    print("Execution failed -> This file is module.")
    sys.exit()


try:
    import Descriptors.descriptors
except ImportError as message:
    descriptors = ImportError(message)


from Descriptors.descriptors import (
    Skeleton,
    DataType,
    Attribute,
)


print(f"**Initialize {__self_name__}**")
