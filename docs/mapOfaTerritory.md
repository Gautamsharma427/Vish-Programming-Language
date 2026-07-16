Flow goes like this:
1. Scanner - Converting language to tokens
2. Parser - Converts tokens to AST also known as abstract syntax tree.
3. Static Analysis 
    - Binding : Finding out where a particular variable or a name is defined.
    - if the language is statically typed, this is where we check type
    - if the two types don't support operations with each other then we report type error.
    - Now this insight gets stored:
        - In abstract syntax tree itself in form of *attributes*
        - In form of a Lookup Table whose keys are the names of the variables or declarations(also called Identifiers). This table is then called Symbol Table.
Everything up until here is called **FRONT END**
-----
**MIDDLE END** starts after this:
- if the **FRONT END** is concerned with the source language and **backend** is concerned with the architecture in which the program runs then the middle end is stored as a immediate representation that isn't tied to either the backend or the frontend instead it acts as a connector between the frontend and the backend.
- The middle end makes supporting multiple frontends and backends easier.
- Optimization : swapping out code from the program to make the same program run in lesser time (more effeciently)
- Code generation : the last step is generating code which the computer can understand.
------
**BACKEND** finally starts:

- Runtime:
    - Two ways:
    1. Intpreted Language - Running the machine code through virtual machine (Slow but portable)
    2. Compiled Language - Running the machine code directly into the CPU (Fast but you'll need to write a different logic for a different architecture making it a hassle. hence it isn't that portable)
    