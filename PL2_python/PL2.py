from queue import Queue
from typing import List
from sys import stdin

token: Queue[str] = Queue()
zerodivide: bool = True

def aexpr() -> int:
    left: int = term()

    while True:
        if not token.empty() and (token.queue[0] == '*' or token.queue[0] == '/'):
            op: str = token.get()

            right: int = term()

            if op == '*':
                left = left * right
            else:
                if right == 0:
                    global zerodivide
                    zerodivide = False
                else:
                    left = int(left / right)
        else:
            break

    return left

def term() -> int:
    left: int = factor()

    while True:
        if not token.empty() and (token.queue[0] == '+' or token.queue[0] == '-'):
            op: str = token.get()

            right: int = factor()

            if op == '+':
                left = left + right
            else:
                left = left - right
        else:
            break
    return left

def factor() -> int:
    num: int = 0

    if not token.empty() and '0' <= token.queue[0] <= '9':
        return number()
    else:
        token.get()
        num = aexpr()

        token.get()
        return num

def number() -> int:
    num: int = 0

    while True:
        if not token.empty() and '0' <= token.queue[0] <= '9':
            if num == 0:
                num = num + dec()
            else:
                num = num * 10
                num = num + dec()
        else:
            break

    return num

def dec() -> int:
    num: int = ord(token.get()) - ord('0')

    return num

while True:
    syntax: str = stdin.readline().rstrip('\n')

    if not syntax:
        break

    b: bool = True
    stack: List[int] = []
    token = Queue()
    zerodivide = True

    # Tokenization and Syntax Error checking
    for i in range(len(syntax)):
        if ('(' <= syntax[i] <= '+') or (syntax[i] == '-') or ('/' <= syntax[i] <= '9'):
            if syntax[i] in ['+', '-', '*', '/']:
                if token.empty() or (token.queue[-1] in ['+', '-', '*', '/']):
                    b = False
                    break
            elif syntax[i] == '(':
                stack.append(0)

                if (not token.empty()) and ('0' <= token.queue[-1] <= '9'):
                    b = False
                    break
            elif syntax[i] == ')':
                if not stack:
                    b = False
                    break
                else:
                    stack.pop()

                if (not token.empty()) and token.queue[-1] == '(':
                    b = False
                    break
            else:
                if (not token.empty()) and token.queue[-1] == ')':
                    b = False
                    break

            token.put(syntax[i])
        elif syntax[i] == ' ':
            continue
        else:
            b = False
            break

    if stack or (not token.empty() and (token.queue[-1] in ['+', '-', '*', '/'])):
        b = False

    if b:
        res = aexpr()

        if zerodivide:
            print(res)
        else:
            print("can't divide 0")
    else:
        print("syntax error!")