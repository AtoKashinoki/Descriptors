"""
    Descriptors module

We will add a class that facilitates the use of descriptors
to support development.

"""

# import
import sys


if __name__ == '__main__':
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


print("**Initialize descriptors**")
