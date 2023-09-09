import re

def program():
    try:
        statement()
    except:
        print("Syntax Error!")

def statement():
    global pos
    flag = False
    while pos < len(tokens) and tokens[pos] != '':
        if tokens[pos] == 'print':
            match_token('print')
            result = aexpr()
            match_token(';')
            flag = True
            print(result)
            if pos >= len(tokens) or tokens[pos] == '':
                return
        elif re.match(r'[a-z]', tokens[pos]):
            var = tokens[pos]
            match_token(var)
            match_token('=')
            result = aexpr()
            variables[var] = result
            match_token(';')
            flag = True
            if pos >= len(tokens) or tokens[pos] == '':
                return  # Exit the statement if no more code is available
        else:
            syntax_error()
        if not flag:
            syntax_error()

def aexpr():
    result = term()
    while pos < len(tokens) and (tokens[pos] == '+' or tokens[pos] == '-'):
        operator = tokens[pos]
        match_token(operator)
        term_result = term()
        if operator == '+':
            result += term_result
        else:
            result -= term_result
    return result

def term():
    result = factor()
    while pos < len(tokens) and (tokens[pos] == '*' or tokens[pos] == '/'):
        operator = tokens[pos]
        match_token(operator)
        factor_result = factor()
        if operator == '*':
            result *= factor_result
        else:
            result /= factor_result
    return result

def factor():
    if pos >= len(tokens):
        syntax_error()
    if re.match(r'[0-9]+', tokens[pos]):
        return number()
    elif re.match(r'[a-z]', tokens[pos]):
        return variable()
    elif tokens[pos] == '(':
        match_token('(')
        result = aexpr()
        match_token(')')
        return result
    else:
        syntax_error()

def number():
    result = 0
    if re.match(r'[0-9]+', tokens[pos]):
        result = int(tokens[pos])
        match_token(tokens[pos])
    else:
        syntax_error()
    return result

def variable():
    if re.match(r'[a-z]+', tokens[pos]):
        var = tokens[pos]
        if len(var) > 1:
            syntax_error()
        match_token(var)
        if var in variables:
            return variables[var]
        else:
            syntax_error()
    else:
        syntax_error()

def match_token(expected_token):
    global pos
    if pos < len(tokens) and tokens[pos] == expected_token:
        pos += 1
    else:
        syntax_error()

def syntax_error():
    raise Exception("Syntax Error!")

consecutive_empty_inputs = 0

while True:
    try:
        code = input("Enter the code: ")
        if code.strip() == '':
            consecutive_empty_inputs += 1
            if consecutive_empty_inputs >= 2:
                break
            else:
                continue
        else:
            consecutive_empty_inputs = 0

        tokens = re.findall(r'[a-z]+|[0-9]+|[+\-*/();=]', code)
        pos = 0
        variables = {}
        program()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")
        break
