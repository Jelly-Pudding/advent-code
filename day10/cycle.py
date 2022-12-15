import re

addx_pattern = re.compile(r"addx (-?\d*)")
with open("input.txt", "r") as f:
    cycle_counter = 0
    current_value = 1
    sum_signal_strength = 0
    for line in f:
        addx_match = re.match(addx_pattern, line.strip())
        if addx_match:
            for i in range(2):
                cycle_counter += 1
                if cycle_counter in [20, 60, 100, 140, 180, 220]:
                    signal_strength = cycle_counter * current_value
                    sum_signal_strength += signal_strength
                if i == 1:
                    current_value += int(addx_match.group(1))
        elif line.strip() == "noop":
            cycle_counter += 1
            if cycle_counter in [20, 60, 100, 140, 180, 220]:
                signal_strength = cycle_counter * current_value
                sum_signal_strength += signal_strength
print(sum_signal_strength)