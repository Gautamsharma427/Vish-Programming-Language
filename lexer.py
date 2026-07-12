def lexer(SOURCE):
    TOKENS = []
    KEYWORDS = {
        # Package / Module
        "lao",
        # Data Types
        "akshar",
        "sankhya",
        "dashamlab",
        "satya",
        "shabd",
        # Boolean Literals
        "Haan",
        "Nahi",
        # Conditionals
        "agar",
        "yaFir",
        "nahiToh",
        # Exception Handling
        "koshish",
        "galti",
        "aakhiri",
        # Loops
        "jabtak",
        "kro",
        "check",
        "keLiye",
        # Functions
        "kaam",
        "vaapas",
        "shunya",
        # Input / Output
        "dikhao",
        "pucho",
        # Loop Control
        "ruko",
        "chalo",
    }
    OPERATORS = {
        "=",
        "+",
        "-",
        "*",
        "/",
        "<=",
        ">=",
        "!=",
        "==",
        "+=",
        "||",
        "&&",
        "<",
        ">",
        "-=", 
        "*=", 
        "/=",
    }
    DELIMITERS = {"(", ")", "{", "}", "[", "]", ";", ",", ".", ":"}
    DIGITS = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0"}
    file = open(SOURCE, "r")
    data = file.read()
    cursor = 0
    word = ""

    while cursor < len(data):
        # current character at current point in the program.
        current_char = data[cursor]
        # ignoring if the current character is a white space
        if current_char.isspace():
            cursor += 1
            continue
        # checking if the current character is alpha numeric or is a underscore
        while current_char.isalnum() or current_char == "_":
            # adding the current character to the word (as it is still receiving alpha numeric characters.)
            word += current_char
            # adding 1 to cursor for the outer loop
            cursor += 1
            # updating current character while avoiding Indexerror for the inner loop
            if cursor < len(data):
                current_char = data[cursor]
        # checking if the word upon completion is a keyword
        if word in KEYWORDS:
            TOKENS.append({"type": "keyword", "value": word})
            # emptying the word after a condition is matched
            word = ""
        # checking if the word upon completion is a number
        elif word.isnumeric():
            TOKENS.append({"type": "Number", "value": word})
            # emptying the word after a condition is matched
            word = ""
        # do nothing if the word itself is recorded empty
        elif word == "":
            pass
        # if nothing else matches, the word must be a identifier
        else:
            TOKENS.append({"type": "Identifier", "value": word})
            # emptying the word after a condition is matched
            word = ""
        if cursor + 1 < len(data):
            two_char = current_char + data[cursor + 1]

            if two_char in OPERATORS:
                TOKENS.append({"type": "operator", "value": two_char})
                cursor += 1

            elif current_char in OPERATORS:
                TOKENS.append({"type": "operator", "value": current_char})

        elif current_char in OPERATORS:
            TOKENS.append({"type": "operator", "value": current_char})
        if current_char in DELIMITERS:
            TOKENS.append({"type": "delimiter", "value": current_char})
        cursor += 1


    # appending the EOF token at the end of the program.
    TOKENS.append({"type": "EOF", "value": ""})
    file.close()
    return TOKENS