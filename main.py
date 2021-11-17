def probe_movement(x, y, direction, command):
    direction_values = {"N": 1, "S": -1, "E": 1, "W": -1}
    direction_l = {"N": "W", "S": "E", "E": "N", "W": "S"}
    direction_r = {"E": "S", "S": "W", "W": "N", "N": "E"}
    for letter in command:
        if letter == "L":
            direction = direction_l[direction]
            continue
        if letter == "R":
            direction = direction_r[direction]
            continue
        if letter == "M":
            if direction == "E" or direction == "W":
                x += direction_values[direction]
            if direction == "N" or direction == "S":
                y += direction_values[direction]
    return f"{x} {y} {direction}"