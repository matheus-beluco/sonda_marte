from exc import CommandError, CoordinatesError, DirectionError


def verify_command(command: str):
    command = command.upper()
    valid_letters = ["R", "L", "M"]

    for letter in command:
        if letter not in valid_letters:
            raise CommandError("Invalid letter in command.")

    return command


def verify_direction(direction: str):
    direction = direction.upper()
    valid_directions = ["E", "W", "N", "S"]

    if direction not in valid_directions:
        raise DirectionError("Invalid direction.")

    return direction


def verify_coordinates(x, y):
    if type(x) != int or type(y) != int:
        raise CoordinatesError("Invalid types.")


def next_direction(letter: str, direction: str) -> str:
    direction_left = {"N": "W", "S": "E", "E": "N", "W": "S"}
    direction_right = {"E": "S", "S": "W", "W": "N", "N": "E"}

    if letter == "L":
        return direction_left[direction]

    return direction_right[direction]


def probe_movement(x: int, y: int, direction: str, command: str) -> str:
    try:

        """
        This part checks the function entries.
        """
        command = verify_command(command)
        direction = verify_direction(direction)
        verify_coordinates(x, y)

        """
            This part moves the probe.
        """
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

    except CommandError as e:
        return e.args[0]

    except DirectionError as e:
        return e.args[0]

    except CoordinatesError as e:
        return e.args[0]
