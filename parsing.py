
# Term -> Factor {(*|/) Factor
def term():
    global token_pointer
    factor()
    while token_pointer < len(tokens) and (tokens[token_pointer] == "*" or tokens[token_pointer] == "/"):
        token_pointer += 1
        factor()

# Factor -> intLiteral
def factor():
    global token_pointer

# Expr -> Term {(+|-) Term}
def expr():
    global token_pointer
    term()
    while token_pointer < len(tokens) and (tokens[token_pointer]=="+" or tokens[token_pointer]=='-'):
        token_pointer += 1
        term()

def main():
    expr() #start