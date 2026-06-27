# 🛠️ Compiler Construction in Python

A custom programming language compiler built from scratch in Python as a university course project.  
The compiler processes source code written in a **custom-defined language** through three core phases:

> **Lexical Analysis → Syntax Analysis → Semantic Analysis**

---

## 📁 Project Structure

```
compiler-construction-python/
│
├── lexical_analyzer.py           # Phase 1: Tokenizes source code into lexemes
├── syntax_semantic_analyzer.py   # Phase 2 & 3: Parses tokens and validates semantics
├── work.txt                      # Sample input source code (custom language)
├── lexical.txt                   # Output of lexical analyzer (token stream)
└── README.md
```

---

## ⚙️ How It Works

### 🔵 Phase 1 — Lexical Analyzer (`lexical_analyzer.py`)

Reads source code from `work.txt` and breaks it into a stream of **tokens**.  
Each token is classified into a category:

| Token Type       | Token Tag      | Examples                            |
|------------------|----------------|-------------------------------------|
| Keywords         | `kw`           | `int`, `float`, `Class`, `function` |
| Identifier       | `ID`           | Variable names, class names         |
| Data Type        | `dt`           | `int`, `float`, `char`, `string`    |
| Assignment Op    | `AS`           | `=`                                 |
| Compound Assign  | `CA`           | `+=`, `-=`, `*=`, `/=`, `%=`        |
| Arithmetic Op    | `PM`, `MDM`    | `+`, `-`, `*`, `/`, `%`             |
| Relational Op    | `RO`           | `<`, `>`, `<=`, `>=`, `!=`          |
| Comparison Op    | `CO`           | `==`                                |
| Logical Op       | `AND`, `OR`    | `&&`, `\|\|`                        |
| Increment/Dec    | `incdec`       | `++`, `--`                          |
| Integer Constant | `int_const`    | `0`, `42`, `100`                    |
| Float Constant   | `float_const`  | `3.14`, `0.5`                       |
| Char Constant    | `chr_const`    | `'a'`, `'\n'`                       |
| String Constant  | `str_const`    | `"hello"`                           |
| Punctuators      | `(`, `)`, etc. | `{`, `}`, `(`, `)`, `;`, `,`        |
| End of File      | `$`            | `$`                                 |

Output is written to `lexical.txt` in the format:
```
TOKEN_TYPE  TOKEN_VALUE  LINE_NUMBER
```

**Example output (`lexical.txt`):**
```
abstract  abstract  1
Class     Class     1
ID        Viraad    1
{         {         1
dt        int       3
ID        x         3
;         ;         3
```

---

### 🟡 Phase 2 — Syntax Analyzer (`syntax_semantic_analyzer.py`)

Reads the token stream from `lexical.txt` and validates code structure using **recursive descent parsing**.

Grammar rules supported:
- Class declarations (`abstract`, `final`, `extends`)
- Function and constructor definitions
- Variable declarations and assignments
- `if`, `elif`, `else` blocks
- `till` loop (custom loop construct)
- Object creation with `new`
- `return`, `this`, `super` statements
- Arithmetic, relational, and logical expressions

---

### 🔴 Phase 3 — Semantic Analyzer (`syntax_semantic_analyzer.py`)

Performs deeper validation beyond syntax:

| Check | Description |
|---|---|
| **Scope Tracking** | Manages a scope stack to track variable visibility |
| **Redeclaration Detection** | Catches duplicate variable or function names in the same scope |
| **Undeclared Identifiers** | Reports use of variables/classes not yet declared |
| **Inheritance Validation** | Enforces `abstract`, `final`, and `extends` rules |
| **Type Recording** | Records data types in the symbol table for reference |

### Symbol Tables Used

| Table | Class | Purpose |
|---|---|---|
| Data Table | `DT` | Stores variable declarations per class scope |
| Main Data Table | `MDT` | Stores class metadata (name, type, modifier, parent) |
| Function Table | `FT` | Stores function signatures and return types |

---

## 📝 Custom Language Reference

### Supported Keywords

```
int     float    char     string   Class
if      elif     else     till     return
function  start  abstract  final   extends
new     this     super    try      catch
```

### Supported Data Types

| Type | Description |
|---|---|
| `int` | Integer values |
| `float` | Floating point values |
| `char` | Single character |
| `string` | String of characters |

### Class Declaration Syntax

```
abstract Class ClassName extends ParentClass {
    // constructor
    ClassName() {
        int x;
    }

    // member variables
    int a;
    string name = "hello";

    // abstract method
    abstract int function myFunc(int x) {
        x++;
    }
}
```

### Function Entry Point

```
function start() {
    ClassName obj = new ClassName();
}
```

### Control Flow

```
// if-elif-else
if (x > 0) {
    y = 1;
} elif (x == 0) {
    y = 0;
} else {
    y = -1;
}

// till loop (like while)
till (x < 10) {
    x++;
}
```

### Comments

```
# This is a single-line comment
```

---

## 🚀 How to Run

**Requirements:** Python 3.x — No external libraries required.

### Step 1 — Write your source code

Edit `work.txt` with your custom language code. A sample is already provided.

### Step 2 — Run the Lexical Analyzer

```bash
python lexical_analyzer.py
```

This reads `work.txt` and generates `lexical.txt` containing the full token stream.

### Step 3 — Run the Syntax & Semantic Analyzer

```bash
python syntax_semantic_analyzer.py
```

This reads `lexical.txt` and prints analysis results to the console.

---

## 📊 Sample Input & Output

**Input (`work.txt`):**
```
abstract Class Viraad {
    Sameer(){
        int x;
    }
    int a;
    int b;
    int c;
    string y = a+b*c;
    abstract int function myfunc(int x){
        y++;
        z++;
    }
    abstract int function myfunc(int x){
        u++;
    }
}
function start(){
    Sameer obj = new Sameer();
}
```

**Console Output:**
```
SCOPE STACK [1]
[['x', ' ->', '', 'Viraad'], ['a', 'int', '', 'Viraad'], ...]  data table
Redeclaration Error of function myfunc
no syntax error
[['Viraad', 'Class', 'abstract', '', ...]]  main table
[['myfunc', 'int -> int', 'abstract', ...]] function table
```

---

## 🧠 Concepts Demonstrated

- **Compiler Design** — Full pipeline from source code to semantic validation
- **Lexical Analysis** — Regex-based tokenization and classification
- **Recursive Descent Parsing** — Manual implementation without parser generators
- **Symbol Table Management** — Scope-aware storage and lookup
- **OOP in Python** — Classes for Tokens, DT, MDT, FT
- **Error Detection** — Redeclaration, undeclared identifiers, inheritance violations

---

## 👥 Team

Group project — Compiler Construction Course  
**University of Karachi** — BS Computer Science

---

## 📄 License

This project was developed for academic purposes.
