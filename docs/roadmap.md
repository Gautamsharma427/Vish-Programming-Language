1. I'm gonna make a lexer:
 - Converts Program to Tokens 
 - Point to a character 
    - Letter?
        - Make a word until you're getting characters and Check:
            - is it a Keyword?
                - Add it to the type Keywords
            - is it not a Keyword?
                - Check if it follows the rules to be a identifier
                    - If yes, Add it to the identifier class
                    - If no, Raise the error of Invalid Identifier
    - Number?
        - Keep reading until no more numbers
        - Add the final output in a template token of type number
        - Add it to the Number Template
    - Whitespaces? Tabs? Spaces?
        - Skip them instantly
    - Operators?
        - Listen until no more special symbols
        - Check for which operator it matches from a list of operators
        - Add it to the tokenlist with that type only
1.1. When to mark the End of a token?
- Two Ways:
    1. Use a SET of enders and whenever a ender is detected just switch the word right away(This'll create a strict language which will be better and faster for the system)
    2. Keep checking for alpha numeric characters and when a non alpha numeric character is detected just Switch the word.
1.2 How do you make a arrangement for the final output token?
    - Just pack all of them in a python list and add dictionaries inside the list.
-------------------------


==========================================================
                 LEXER DESIGN (Version 1.0)
==========================================================

Goal
-----
Convert source code into an ordered list of tokens that the parser can understand.


==========================================================
MAIN ALGORITHM
==========================================================

Read Source Code
        │
        ▼
pointer = 0
line = 1
column = 1

While pointer < source length

    current = source[pointer]

    Determine what token begins here.

    Read the complete token.

    Create Token.

    Store Token.

End While

Append EOF Token.


==========================================================
CHARACTER CLASSIFICATION
==========================================================

For every character, determine which category it belongs to.

• Letter / _
• Digit
• Whitespace
• Operator
• Delimiter
• Quote
• Comment
• Unknown Character


==========================================================
IDENTIFIER / KEYWORD
==========================================================

If current character is Letter or '_'

    Read while character is

        Letter
        Digit
        '_'

    word = collected characters

    If word exists in KEYWORD_TABLE

        Emit KEYWORD Token

    Else

        Emit IDENTIFIER Token




let counter

↓

KEYWORD(let)
IDENTIFIER(counter)


==========================================================
NUMBER
==========================================================

If current character is Digit

    Read while Digit

    Emit NUMBER Token

(Currently supports integers.)

Future extensions

• Floating Point
• Binary
• Hexadecimal
• Scientific Notation
• Digit Separators


==========================================================
STRING
==========================================================

If current == '"'

    Skip opening quote

    Read until another '"'

    If EOF occurs first

        Raise
        Unterminated String Error

    Emit STRING Token


==========================================================
CHARACTER LITERAL
==========================================================

If current == '\''

    Read exactly one character

    Expect '\''

    Emit CHAR Token


==========================================================
WHITESPACE
==========================================================

If current is

    Space
    Tab
    Carriage Return

Skip it.

If current is Newline

    line += 1
    column = 1


==========================================================
OPERATORS
==========================================================

Always match the LONGEST VALID OPERATOR.

Examples

==
!=
<=
>=
&&
||
++
--
+=
-=
=
+
-
*
/
%

Example

Input

==

Correct Output

OPERATOR(==)

NOT

OPERATOR(=)
OPERATOR(=)


==========================================================
DELIMITERS
==========================================================

Single-character tokens.

(
)
{
}
[
]
;
,
.
:


==========================================================
COMMENTS
==========================================================

Single Line

//

Read until newline.

Ignore.

-----------------------------------------

Multi Line

/*

Read until

*/

If EOF occurs first

Raise
Unterminated Comment Error


==========================================================
UNKNOWN CHARACTER
==========================================================

If none of the lexer rules match

Raise

Invalid Character Error


==========================================================
TOKEN BOUNDARY RULE
==========================================================

A token ends when its reading rule fails.

Identifier

while Letter Digit _

Number

while Digit

Operator

Longest Valid Match

String

Until closing quote

Delimiter

Immediately

No need for a large set of "ending characters."


==========================================================
TOKEN STRUCTURE
==========================================================

Each token contains

Type
Value
Line
Column

Example

{
    "type": "IDENTIFIER",
    "value": "counter",
    "line": 10,
    "column": 15
}


==========================================================
TOKEN OUTPUT
==========================================================

Input

let age = 18;

Output

[
    {
        "type": "KEYWORD",
        "value": "let"
    },
    {
        "type": "IDENTIFIER",
        "value": "age"
    },
    {
        "type": "OPERATOR",
        "value": "="
    },
    {
        "type": "NUMBER",
        "value": "18"
    },
    {
        "type": "DELIMITER",
        "value": ";"
    },
    {
        "type": "EOF",
        "value": ""
    }
]


==========================================================
DATA TABLES
==========================================================

KEYWORDS

{
    let,
    if,
    else,
    while,
    for,
    break,
    continue,
    return,
    function,
    class,
    ...
}

OPERATORS

{
    +  -  *  /  %
    =
    ==
    !=
    <
    >
    <=
    >=
    &&
    ||
    !
    ++
    --
    +=
    -=
    *=
    /=
    ...
}

DELIMITERS

{
    ( ) { } [ ]
    ;
    ,
    .
    :
}


==========================================================
TIME COMPLEXITY
==========================================================

Time Complexity

O(n)

Each character is processed approximately once.

Space Complexity

O(t)

t = Number of Tokens


==========================================================
FINAL LEXER PIPELINE
==========================================================

Source Code
      │
      ▼
Character Scanner
      │
      ▼
Character Classification
      │
      ├── Identifier / Keyword
      ├── Number
      ├── String
      ├── Character Literal
      ├── Operator
      ├── Delimiter
      ├── Comment
      ├── Whitespace
      └── Error
             │
             ▼
Create Token
      │
      ▼
Append to Token List
      │
      ▼
Repeat until EOF
      │
      ▼
Return Token List