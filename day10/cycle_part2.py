import re

addx_pattern = re.compile(r"addx (-?\d*)")
drawn_out = ["", "", "", "", "", ""]

with open("input.txt", "r") as f:
    cycle_counter = 0
    current_value = 1
    drawn_out_idx = 0
    for line in f:
        addx_match = re.match(addx_pattern, line.strip())
        if addx_match:
            for i in range(2):
                cycle_counter += 1
                if cycle_counter in [41, 81, 121, 161, 201]:
                    drawn_out_idx += 1
                pixel = len(drawn_out[drawn_out_idx])
                if drawn_out_idx == 1 and len(drawn_out[drawn_out_idx]) == 12:
                    print(current_value)

                if current_value == pixel or current_value - 1 == pixel or current_value + 1 == pixel:
                    drawn_out[drawn_out_idx] += "#"
                else:
                    drawn_out[drawn_out_idx] += "."
                if i == 1:
                    current_value += int(addx_match.group(1))
        elif line.strip() == "noop":
            cycle_counter += 1
            if cycle_counter in [41, 81, 121, 161, 201]:
                drawn_out_idx += 1
            pixel = len(drawn_out[drawn_out_idx])
            if current_value == pixel or current_value - 1 == pixel or current_value + 1 == pixel:
                drawn_out[drawn_out_idx] += "#"
            else:
                drawn_out[drawn_out_idx] += "."

for row in drawn_out:
    print(row)