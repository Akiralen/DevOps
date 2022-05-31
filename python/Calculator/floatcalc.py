__operands_list = ['*','/','+','-']

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
    
def minimal_expression(string : str, operand : str):
    i_middle = string.find(operand)
    if len(string) > i_middle + 1:
        if string[i_middle+1] == '-':
            i_right = i_middle + 2
        else:
            i_right = i_middle + 1
    operand_dict = {}
    for _operand in __operands_list:
        operand_dict.update(_operand,string[i_right:].find(_operand))       
    operand_dict = {k:v for k,v in operand_dict.item() if v!=-1}    
    if operand_dict > 0:
        r_index = max(operand_dict, key = operand_dict.get)
    else:
        pass
def calculator (calc_expression : str):
    # this calculator works on expresions using unsigned int using '+','-','/','*' operands and '()'
    if '(' in calc_expression:
       start,middle,end = get_inner_expression(calc_expression)
       return calculator(start + str(calculator(middle)) + end)
        
    try:
        result = float(calc_expression)
        return result
    except:
        if not(('+' in calc_expression)or('-' in calc_expression)or('*' in calc_expression)or('/'in calc_expression)):
            raise RuntimeError('Ileagal expression')
    if '-' in calc_expression:
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