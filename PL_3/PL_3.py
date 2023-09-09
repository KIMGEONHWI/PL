import re

def parse(program):
    tokens = re.findall(r'\bprint|\w+|\S\b', program)
    num_tokens = len(tokens)
    token_index = 0

    def next_token():
        nonlocal token_index
        token_index += 1
        if token_index < num_tokens:
            return tokens[token_index]
        return None

    def parse_program():
        statements = parse_statements()
        if statements is None:
            return None
        return {'type': 'Program', 'statements': statements}

    def parse_statements():
        statements = []
        statement = parse_statement()
        if statement is None:
            return None
        statements.append(statement)
        while tokens[token_index] == ';':
            token = next_token()
            statement = parse_statement()
            if statement is None:
                return None
            statements.append(statement)
        return statements

    def parse_statement():
        var = parse_var()
        if var is not None:
            token = next_token()
            if token == '=':
                aexpr = parse_aexpr()
                if aexpr is not None:
                    token = next_token()
                    if token == ';':
                        return {'type': 'Assignment', 'var': var, 'aexpr': aexpr}
        elif tokens[token_index] == 'print':
            token = next_token()
            if token == 'print':
                aexpr = parse_aexpr()
                if aexpr is not None:
                    token = next_token()
                    if token == ';':
                        return {'type': 'Print', 'aexpr': aexpr}
        return None

    def parse_aexpr():
        term = parse_term()
        if term is None:
            return None
        aexpr = {'type': 'AExpression', 'term': term}
        token = next_token()
        while token in ['+', '-']:
            term = parse_term()
            if term is None:
                return None
            aexpr = {'type': 'AExpression', 'operator': token, 'left': aexpr, 'right': term}
            token = next_token()
        return aexpr

    def parse_term():
        token = next_token()
        if re.match(r'\d+', token):
            return {'type': 'Number', 'value': int(token)}
        elif re.match(r'[a-z]', token):
            return {'type': 'Variable', 'name': token}
        return None

    def parse_var():
        token = next_token()
        if re.match(r'[a-z]+$', token):
            return token
        return None

    return parse_program()

while True:
    program = input("Enter a program: ")
    result = parse(program)
    if result is None:
        print("Syntax Error!")
    else:
        print(result)
