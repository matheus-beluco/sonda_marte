from main import probe_movement


def test_invalid_command():
    result = probe_movement(x=1, y=2, direction="N", command="KKKKK")
    expected = "Invalid letter in command."
    assert result == expected


def test_invalid_direction():
    result = probe_movement(x=3, y=3, direction="K", command="MMRMMRMRRM")
    expected = "Invalid direction."
    assert result == expected


def test_invalid_coordinates():
    result = probe_movement(x="2", y="3", direction="S", command="RMLMLLMRML")
    expected = "Invalid types."
    assert result == expected


def test_upper_command():
    result = probe_movement(x=3, y=3, direction="E", command="mmrMMRMRRM")
    expected = "5 1 E"
    assert result == expected


def test_upper_direction():
    result = probe_movement(x=2, y=3, direction="s", command="RMLMLLMRML")
    expected = "2 3 N"
    assert result == expected