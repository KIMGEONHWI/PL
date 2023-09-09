def program():
    while True:
        statement()
        if input_str == '':
            break

def statement():
    global input_str
    if input_str.startswith('print'):
        input_str = input_str[6:]
        aexpr()
        if input_str.startswith(';'):
            input_str = input_str[1:]
            print(result)
        else:
            print("Syntax Error!")
    elif var() == True:
        if input_str.startswith('='):
            input_str = input_str[1:]
            aexpr()
            if input_str.startswith(';'):
                input_str = input_str[1:]
            else:
                print("Syntax Error!")
        else:
            print("Syntax Error!")
    else:
        print("Syntax Error!")

def aexpr():
    global input_str
    term()
    while input_str.startswith('+') or input_str.startswith('-'):
        op = input_str[0]
        input_str = input_str[1:]
        term()
        if op == '+':
            result += temp_result
        else:
            result -= temp_result

def term():
    global input_str, result, temp_result
    if var() == True:
        temp_result = variables[input_str]
        input_str = input_str[1:]
    elif number() == True:
        temp_result = int(input_str[0])
        input_str = input_str[1:]
    else:
        print("Syntax Error!")

def number():
    global input_str
    if input_str.startswith('0') or input_str.startswith('1') or input_str.startswith('2') or input_str.startswith('3') or input_str.startswith('4') or input_str.startswith('5') or input_str.startswith('6') or input_str.startswith('7') or input_str.startswith('8') or input_str.startswith('9'):
        return True
    else:
        return False

def var():
    global input_str, variables
    if input_str.startswith('a') or input_str.startswith('b') or input_str.startswith('c') or input_str.startswith('d') or input_str.startswith('e') or input_str.startswith('f') or input_str.startswith('g') or input_str.startswith('h') or input_str.startswith('i') or input_str.startswith('j') or input_str.startswith('k') or input_str.startswith('l') or input_str.startswith('m') or input_str.startswith('n') or input_str.startswith('o') or input_str.startswith('p') or input_str.startswith('q') or input_str.startswith('r') or input_str.startswith('s') or input_str.startswith('t') or input_str.startswith('u') or input_str.startswith('v') or input_str.startswith('w') or input_str.startswith('x') or input_str.startswith('y') or input_str.startswith('z'):
        variables[input_str[0]] = 0
        return True
    else:
        return False

# 변수 저장을 위한 딕셔너리
variables = {}

# 사용자로부터 코드 입력 받기
input_str = input()

# 결과 변수 초기화
result = 0
temp_result = 0

# 프로그램 실행
program()
