def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = []
    second_line = []
    dash_line = []
    result_line = []

    for problem in problems:
        first, operator, second = problem.split()

        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        if not first.isdigit() or not second.isdigit():
            return "Error: Numbers must only contain digits."

        if len(first) > 4 or len(second) > 4:
            return "Error: Numbers cannot be more than four digits."

        width = max(len(first), len(second)) + 2
        first_line.append(first.rjust(width))
        second_line.append(operator + second.rjust(width - 1))
        dash_line.append('-' * width)

        if show_answers:
            if operator == "+":
                result = str(int(first) + int(second))
            else:
                result = str(int(first) - int(second))
            result_line.append(result.rjust(width))

    arranged_problems = (
        "    ".join(first_line) + "\n" +
        "    ".join(second_line) + "\n" +
        "    ".join(dash_line)
    )

    if show_answers:
        arranged_problems += "\n" + "    ".join(result_line)

    return arranged_problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)}')
