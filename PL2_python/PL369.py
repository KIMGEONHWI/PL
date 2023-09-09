import re

def program():
    try:
        while pos < len(tokens):
            statement()
    except Exception as e:
        print(str(e))

def statement():
    global pos
    flag = False
    if tokens[pos] == 'print':
        match_token('print')
        result = aexpr()
        print(result)
        flag = True
    elif re.match(r'[a-z]', tokens[pos]):
        if len(tokens[pos]) > 1:
            syntax_error()
        var = tokens[pos]
        match_token(var)
        match_token('=')
        result = aexpr()
        variables[var] = result
        flag = True
    else:
        syntax_error()

    if not flag or (pos < len(tokens) and tokens[pos] != ';'):
        syntax_error()
    match_token(';')

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
    return result

def term():
    result = factor()
    while pos < len(tokens) and (tokens[pos] == '*' or tokens[pos] == '/'):
        operator = tokens[pos]
        match_token(operator)
        term_result = factor()
        if operator == '*':
            result *= term_result
        elif operator == '/':
            result /= term_result
    return result

def factor():
    if pos >= len(tokens):
        syntax_error()
    if re.match(r'[0-9]+', tokens[pos]):
        return number()
    elif re.match(r'[a-z]', tokens[pos]):
        if len(tokens[pos]) > 1:
            syntax_error()
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
    var = tokens[pos]
    if re.match(r'[a-z]', tokens[pos]):
        if len(tokens[pos]) > 1:
            syntax_error()
        match_token(var)
        if var in variables:
            return variables[var]
        else:
            return 0
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

blank_input_count = 0

while True:
        code = input()

        if code.strip() == '':
            blank_input_count += 1  # 빈 입력일 경우 카운터 증가
            if blank_input_count == 2:  # 빈 입력이 연속으로 2번 발생하면 프로그램 종료
                break
            continue
        else:
            blank_input_count = 0  # 빈 입력이 아닐 경우 카운터 초기화

        if code[-1] != ';':
            print("Syntax Error!!")
            continue

        tokens = re.findall(r'[a-z]+|[0-9]+|[+\-*/();=]', code)
        pos = 0
        variables = {}
        program()
