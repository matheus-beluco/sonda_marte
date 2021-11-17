def next_direction(letter: str, direction: str) -> str:
    direction_left = {"N": "W", "S": "E", "E": "N", "W": "S"}
    direction_right = {"E": "S", "S": "W", "W": "N", "N": "E"}

    if letter == "L":
        return direction_left[direction]

    return direction_right[direction]


def probe_movement(x: int, y: int, direction: str, command: str) -> str:
    direction_values = {"N": 1, "S": -1, "E": 1, "W": -1}

    for letter in command:
        if letter == "L" or letter == "R":
            direction = next_direction(letter, direction)
            continue

        if direction == "E" or direction == "W":
            x += direction_values[direction]

        if direction == "N" or direction == "S":
            y += direction_values[direction]

    return f"{x} {y} {direction}"
