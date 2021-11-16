from main import probe_movement


def test_probe_movement_1():
    result = probe_movement(x=1, y=2, direction="N", command="LMLMLMLMM")
    expected = "1 3 N"
    assert result == expected


def test_probe_movement_2():
    result = probe_movement(x=3, y=3, direction="E", command="MMRMMRMRRM")
    expected = "5 1 E"
    assert result == expected


def test_probe_movement_3():
    result = probe_movement(x=2, y=3, direction="S", command="RMLMLLMRML")
    expected = "2 3 N"
    assert result == expected
