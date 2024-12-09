def Basic_caluculator_and_conditional_flow (): 
    print("Welcome")
    
    first_number = int(input('Please input any number of your choice: '))
    print("Thank you, you inputted", first_number)
    second_number = int(input('Please input any number of your choice: '))
    print("Thank you, you inputted", first_number, 'and' , second_number)

    operator = input("choose an operator, +, -, *, /: ")

    if operator == "+": 
        calculate = first_number + second_number
    
    elif operator == "-":
        calculate = first_number - second_number
    elif operator == "*":
        calculate = first_number * second_number
    elif operator == "/":
        if second_number == 0: 
            print("Not divisible by zero")
        else: 
            calculate = first_number / second_number

    else: 
        print("Invalid Operator")

    print(calculate)


def Basic_calculator_and_conditional_flow_sample2 ():
    first_number = float (input('input the first number you want to calculate: '))
    second_number = float (input('input the second number you want to calculate: '))
    symbol = input ('input the arithemetic symbol of the operation you wish to perform:')

    if symbol == "+":
        added_value = first_number + second_number
        return added_value
    elif symbol == "-":
        substracted_value = first_number - second_number
        return substracted_value
    elif symbol == "*":
        multiplied_value = first_number * second_number
        return multiplied_value
    elif symbol == "/":
        divided_value = first_number + second_number
        if second_number == 0:
            return "Division error! Indivisible by zero"
        divided_value = first_number /second_number
        return divided_value
    else:
        return "Error! there is a problem, check your selection and symbol again"
    
