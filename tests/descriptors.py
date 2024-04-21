from Descriptors.descriptors import (
    DataType, Attribute
)


class AttrTest:
    attribute = ("test1", "test3")


class Test:
    data_type = DataType(
        list, get_mode="c"
    )
    attribute = Attribute(
        "test1", "test2",
        dtypes=(AttrTest, ),
        get_mode=""
    )

    def __init__(self, data_type, attribute):
        self.data_type = data_type
        self.attribute = attribute
        return


if __name__ == '__main__':
    ins = Test(
        ["test"],
        AttrTest()
    )
    print(
        ins.data_type, ins.attribute
    )
