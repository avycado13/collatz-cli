from helpers import collatz


def write_collatz_to_file(starting_number, filename):
    with open(filename, "w+") as file:
        sequence = collatz(starting_number)
        for num in sequence:
            calculation = f"{num} -> "
            if num != 1:
                if num % 2 == 0:
                    next_num = num // 2
                    calculation += f"{num} ÷ 2 = {next_num}"
                else:
                    next_num = 3 * num + 1
                    calculation += f"{num} × 3 + 1 = {next_num}"
            file.write(calculation + "\n")
