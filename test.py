from collections import UserDict

from src.literal_dict import DictBuilder


def test_self_reference():
    d = DictBuilder()

    assert d[d] == {"d": d}


def test_literals():
    d = DictBuilder()
    a = 1
    b = [a]
    c = "abc"
    assert d[a, b, c, c:4] == {"a": a, "b": b, "c": c, c: 4}


def test_custom_dict_class():
    class DotDict(UserDict):
        def __getattr__(self, key):
            return self[key]

    d = DictBuilder(DotDict)
    a = 1
    assert d[a].a == a
