** start of main.py **

def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = []
    second_line = []
    dashes = []
    results = []

    for problem in problems:
        parts = problem.split()
        num1, operator, num2 = parts

        if operator not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."

        if not num1.isdigit() or not num2.isdigit():
            return "Error: Numbers must only contain digits."

        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        width = max(len(num1), len(num2)) + 2

        first_line.append(num1.rjust(width))
        second_line.append(operator + ' ' + num2.rjust(width - 2))
        dashes.append('-' * width)

        if show_answers:
            result = str(int(num1) + int(num2)) if operator == '+' else str(int(num1) - int(num2))
            results.append(result.rjust(width))

    arranged_problems = '    '.join(first_line) + '\n'
    arranged_problems += '    '.join(second_line) + '\n'
    arranged_problems += '    '.join(dashes)

    if show_answers:
        arranged_problems += '\n' + '    '.join(results)

    return arranged_problems


** end of main.py **

