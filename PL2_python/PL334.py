import re

def program():
    try:
        statement()
    except:
        print("Syntax Error!!")

def statement():
    global pos
    flag = False
    while pos < len(tokens) and tokens[pos] != '':
        if tokens[pos] == 'print':
            match_token('print')
            var = tokens[pos]
            if len(var) > 1:
                syntax_error()
            match_token(var)
            flag = True
            if var in variables:
                result = variables[var]
            else:
                result = 0  # Set result to 0 if variable is not assigned
            print(result)
        elif re.match(r'[a-z]', tokens[pos]):
            var = tokens[pos]
            if len(var) > 1:
                syntax_error()
            match_token(var)
            match_token('=')
            result = aexpr()
            variables[var] = result
            flag = True
        else:
            syntax_error()
        if not flag or (pos < len(tokens) and tokens[pos] != ';'):
            syntax_error()  # Check if statement ends with semicolon
        match_token(';')  # Consume the semicolon at the end of the statement

def aexpr():
    result = term()
    while pos < len(tokens) and (tokens[pos] == '+' or tokens[pos] == '-'):
        operator = tokens[pos]
        match_token(operator)
        term_result = term()
        if operator == '+':
            result += term_result
        elif operator == '-':
            result -= term_result
        else:
            syntax_error()
    return result

def term():
    result = factor()
    while pos < len(tokens) and (tokens[pos] == '*' or tokens[pos] == '/'):
        syntax_error()
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
            return 0  # Return 0 if variable is not assigned
    else:
        syntax_error()

def match_token(expected_token):
    global pos
    if pos < len(tokens) and tokens[pos] == expected_token:
        pos += 1
    else:
        syntax_error()

def syntax_error():
    raise Exception("Syntax Error!!")

consecutive_empty_inputs = 0

while True:
    try:
        code = input()
        if code.strip() == '':
            consecutive_empty_inputs += 1
            if consecutive_empty_inputs >= 2:
                break
            else:
                continue
        else:
            consecutive_empty_inputs = 0

        if code[-1] != ';':  # Check if the last character of the code is semicolon
            print("Syntax Error!!")
            continue

        tokens = re.findall(r'[a-z]+|[0-9]+|[+\-*/();=]', code)
        pos = 0
        variables = {}
        program()

    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")
        break
