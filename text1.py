
def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems"

    arranged_problems = ""
    for problem in problems:
        first_operand, operator, second_operand = problem.split()

        if operator not in ("+", "-"):
            return "Error: Operator must be '+' or '-'"

        if not first_operand.isdigit() or not second_operand.isdigit():
            return "Error: Numbers must only contain digits"

        if len(first_operand) > 4 or len(second_operand) > 4:
            return "Error: Numbers cannot be more than four digits"

        max_operand_length = max(len(first_operand), len(second_operand))
        spaces_between = 2 + max_operand_length - len(second_operand)

        arranged_problems += " " * spaces_between + first_operand + "\n"
        arranged_problems += operator + " " + " " * (max_operand_length - len(second_operand)) + second_operand + "\n"
        arranged_problems += "-" * (max_operand_length + 2) + "\n"

        if show_answers:
            if operator == "+":
                answer = str(int(first_operand) + int(second_operand))
            else:
                answer = str(int(first_operand) - int(second_operand))
            arranged_problems += " " * spaces_between + answer + "\n"

    return arranged_problems.rstrip()


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))