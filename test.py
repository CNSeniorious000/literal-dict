from literal_dict import DictBuilder


def test_self_reference():
    d = DictBuilder()

    assert d[d] == {"d": d}


def test_literals():
    d = DictBuilder()
    a = 1
    b = [a]
    c = "abc"
    assert d[a, b, c, c:4] == {"a": a, "b": b, "c": c, c: 4}
