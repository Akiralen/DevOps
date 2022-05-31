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
    
def simplify_expression(string : str, operand : str):
    # simplifies expresion by solving operand
    right_negative = 0
    m_index = string.find(operand)
    if len(string) > m_index + 1:
        if string[m_index+1] == '-':
            right_negative = 1
    else:
        # missing right value
        raise RuntimeError(f"No right side to the expression <{string}>")
    if m_index > 0:
        l_index = m_index - 1
    else:
        # missing left value
        raise RuntimeError(f"No left side to the expression <{string}>")
    
    r_index = m_index + right_negative + 1
    operand_dict = {}
    
    # find next operand right
    for _operand in __operands_list:
        operand_dict.update({_operand:string[r_index:].find(_operand)})       
    operand_dict = {k:v for k,v in operand_dict.items() if v!=-1}    
    if len(operand_dict) > 0:
        r_index = operand_dict.get(min(operand_dict, key = operand_dict.get)) + right_negative
    else:
        r_index = len(string[m_index+1:])
    
    #find next operand left    
    for _operand in __operands_list:
        operand_dict.update({_operand :string[:l_index].rfind(_operand)})       
    operand_dict = {k:v for k,v in operand_dict.items() if v!=-1}    
    if len(operand_dict) > 0:
        l_index = operand_dict.get(min(operand_dict, key = operand_dict.get)) + 1
    else:
        l_index = 0     
    r_index += m_index
    new_string = ""
    new_string += string[:l_index]
    try:
        num1 = float(string[l_index:m_index])
    except:
        raise RuntimeError(f'Syntax error in <{string}>')
    try:
        num2 = float(string[m_index+1:r_index+1])
    except:
        raise RuntimeError(f'Syntax error in <{string}>')
    new_string += str(calculate(num1,num2,string[m_index]))
    new_string += string[r_index+1:]

    return new_string
        
def calculate (num1 : float,num2 : float, operand):
    if operand == '*':
        return num1 + num2
    elif operand == '/':
        if num2 == 0:
            raise ZeroDivisionError
        else:
            return num1 / num2
    elif operand == '+':
        return num1 + num2
    elif operand == '-':
        return num1 - num2
    
def calculator (calc_expression : str):
    # this calculator works on expresions using unsigned int using '+','-','/','*' operands and '()'
    negative_multiplier = 1
    if '(' in calc_expression:
       start,middle,end = get_inner_expression(calc_expression)
       return calculator(start + str(calculator(middle)) + end)
    if calc_expression[0] == '-':
        negative_multiplier = -1
        calc_expression = calc_expression[1:]
    calc_expression = calc_expression.replace('--','+')
    calc_expression = calc_expression.replace('+-','-')    
    for _operand in __operands_list:
        while calc_expression.find(_operand) > 0:
            print(calc_expression)
            calc_expression = simplify_expression(calc_expression,_operand)

            
    try:
        result = float(calc_expression)
        return result * negative_multiplier
    except:
        raise RuntimeError('Ileagal expression')

def _main():
    user_input=input("Please enter expression: ")
    user_input.replace(" ","")
    print(calculator(user_input))
if __name__ == "__main__":
    _main()
else:
    pass