def get_inner_expression(string : str):
    # divides string in three parts where midle is first encased in '()'
    inner_string = ""
    for i, char in enumerate(string):
        if char == "(" :
            inner_string = '('
        elif char == ")":
            inner_string += ')'
            break
        else:
            inner_string += char
    string_list = list(string.partition(inner_string))
    string_list[1] = string_list[1][1:-1]
    return string_list
    


def calculator (calc_expression : str):
    # this calculator works on expresions using unsigned int using '+','-','/','*' operands and '()'
    if '(' in calc_expression:
       start,middle,end = get_inner_expression(calc_expression)
       return calculator(start + str(calculator(middle)) + end)
        
    if calc_expression.isdigit():
        return int(calc_expression)
    elif '-' in calc_expression:
        n1,n2 = calc_expression.split('-',1)
        return calculator(n1) - calculator(n2)
    elif '+' in calc_expression:
        n1,n2 = calc_expression.split('+',1)
        return (calculator(n1) + calculator(n2))
    elif '*' in calc_expression:
        n1,n2 = calc_expression.split('*',1)
        return calculator(n1) * calculator(n2)
    elif '/' in calc_expression:
        n1,n2 = calc_expression.split('/',1)
        n2 = calculator(n2)
        if n2 == 0:
            raise ZeroDivisionError
        else:
            return calculator(n1) / n2
    else:
        raise RuntimeError("Ilegal expression")

def _main():
    user_input=input("Please enter expression: ")
    user_input.replace(" ","")
    print(calculator(user_input))
if __name__ == "__main__":
    _main()
else:
    pass