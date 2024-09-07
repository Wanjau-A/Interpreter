# Prompt user for an arithmetic expression
def main():
    expression = input("Enter an arithmetic expression (e.g., 1 + 1): ").strip()
    result = compute_result(expression)
    print(result)


def compute_result(expression):
    my_list = expression.split(" ")
    left_operand = float(my_list[0])
    operator = my_list[1]
    right_operand =float(my_list[2])
 
    if operator == "+":
        result = left_operand + right_operand
        return result

    if operator == "-":
        result = left_operand - right_operand
        return result
     
    if operator == "/":
        result = left_operand / right_operand
        return result
     
    if operator == "*":
        result = left_operand * right_operand
        return result


if __name__ == "__main__":
    main()