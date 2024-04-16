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


def test_global_reference():
    d = DictBuilder()

    def f():
        assert d[DictBuilder] == {"DictBuilder": DictBuilder}

    f()


def test_builtin_reference():
    d = DictBuilder()

    def f():
        assert d[print] == {"print": print}

    f()


def test_same_value_different_name():
    d = DictBuilder()
    a = b = 1
    assert d[a, b] == {"a": 1, "b": 1}
