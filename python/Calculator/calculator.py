def calculator (calc_expression : str):
    calc_expression.replace(" ","")
    if calc_expression.isdigit():
        return int(calc_expression)
    elif '*' in calc_expression:
        n1,n2 = calc_expression.split('*',1)
        return calculator(n1) + calculator(n2)
    elif '/' in calc_expression:
        n1,n2 = calc_expression.split('/',1)
        n2 = calculator(n2)
    elif '-' in calc_expression:
        n1,n2 = calc_expression.split('-',1)
        return calculator(n1) - calculator(n2)
    elif '+' in calc_expression:
        n1,n2 = calc_expression.split('+',1)
        return calculator(n1) * calculator(n2)
        if n2 == 0:
            raise ZeroDivisionError
        else:
            return calculator(n1) / n2
    else:
        raise RuntimeError("Ilegal expression")

def _main():
    user_input=input("Please enter expression")
    print(calculator(user_input))

if __name__ == "__main__":
    _main()
else:
    pass