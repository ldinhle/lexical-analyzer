import sys
import re


def read_file(filename: str) -> str:
    with open(filename, 'r') as file:
        return file.read()


def write_output(tokens: list, output_filename: str):
    with open(output_filename, 'w') as file:
        for token, lexeme in tokens:
            file.write(f"{token}\t{lexeme}\n")


def tokenize(content: str) -> list:
    # regex main
    anyChar = r'[ -~]'
    letter = r'[a-zA-Z]'
    digit = r'[0-9]'
    whitespace = r'[ \t\n]'

    token_dict = {
        'type': r'(bool|char|float|int)',
        'main': r'main',
        'if': r'if',
        'else': r'else',
        'while': r'while',
        'return': r'return',
        'print': r'print',
        'boolLiteral': r'(true|false)',
        'equOp': r'==|!=',
        'relOp': r'>=|<=|>|<',
        'assignOp': r'=',
        'addOp': r'\+|-',
        'multOp': r'\*|/',
        ',': r',',
        ';': r';',
        '(': r'\(',
        ')': r'\)',
        '{': r'{',
        '}': r'}',
        '[': r'\[',
        ']': r'\]',
        'comment': rf'\/\/({anyChar}|{whitespace})*',
        'id': rf'{letter}({letter}|{digit})*',
        'intLiteral': rf'{digit}+',
        'floatLiteral': rf'{digit}+\.{digit}+',
        'charLiteral': fr"'{anyChar}'"
    }

    lexemes = re.split("(\d+|\W)", content)
    # Get rid of new line, empty string, space,

    # Create a list of filtered lexemes by iterating over each lexeme in the original lexemes list

    # Initialize an empty list to store the filtered lexemes
    filtered_lexemes = []

    # Iterate over each lexeme in the original lexemes list
    for lexeme in lexemes:
        # Check if the lexeme, when stripped of leading and trailing whitespaces, is non-empty
        if lexeme.strip():
            # If the lexeme is non-empty after stripping, add it to the filtered list
            filtered_lexemes.append(lexeme)

    position = 0
    tokens = []

    for lexeme in filtered_lexemes:  # position < len(content):
        # Initialize match to None for each iteration
        match = None

        if lexeme == '>=' or lexeme == '<=':
            tokens.append(('relOp', lexeme))
            continue

        # Iterate over each token and its corresponding pattern in the token dictionary
        for token, pattern in token_dict.items():
            # Compile the current pattern into a regex object
            # regex = re.compile(pattern)

            # Try to match the pattern starting from the current position in the content
            match = re.match(pattern, lexeme)

            # Python re checking for full match
            # How far has it gone for matching

            if match:
                # Retrieve the matched lexeme (the actual string that matched the pattern)

                tokens.append((token, lexeme))  # Add the token and its corresponding lexeme to the tokens list
                position = match.end()  # Update the position to the end of the matched lexeme
                break

        if not match:
            if re.match(whitespace, content[position]):
                position += 1  # Skip whitespace
            else:
                # print(f"Error: Unrecognized character '{content[position]}' at position {position}")
                position += 1

    return tokens


def main(input_file_name: str):
    # Reading in file
    content = read_file(input_file_name)
    tokens = tokenize(content)

    # for token, lexeme in tokens:
    #     print(f"{token}\t{lexeme}")

    test_string = "x >= 5"
    tokens = tokenize(test_string)
    for token, lexeme in tokens:
        print(f"{token}\t{lexeme}")

    # Get the output filename from the input filename
    base_name = input_file_name.split('.')[0]  # Get the filename without .c
    output_filename = f"{base_name}_output.txt"
    write_output(tokens, output_filename)


if __name__ == "__main__":
    main(sys.argv[1])

