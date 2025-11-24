📘 Arithmetic Formatter – Python Solution

This project contains a Python function that formats multiple arithmetic problems (addition and subtraction) in a clean, vertically arranged layout.
It follows the specifications of the FreeCodeCamp Arithmetic Formatter challenge.


---

🚀 Features

Supports addition (+) and subtraction (-)

Ensures:

No more than 5 problems

Numbers contain digits only

Operands are maximum 4 digits


Returns neatly formatted output with:

Right-aligned operands

Dashes under each equation

Optional results




---

📂 File Included

arithmetic_formatter.py – Contains the implementation and a sample print call.



---

🧠 Example Output

Input:

arithmetic_arranger(
    ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"],
    True
)

Output:

32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
  730      3799      88      172


---

🛠️ How to Use

1. Clone the repository:



git clone https://github.com/natnaeltassew/arithmetic_formatter.git

2. Run the Python file:



python arithmetic_formatter.py

3. Modify the problems list inside the file to test more inputs.




---

📜 Function Description

arithmetic_arranger(problems, show_answers=False)

Parameters:

Parameter	Type	Description

problems	list of strings	Arithmetic problems like "32 + 8"
show_answers	bool	If True, results are displayed


Returns:

A formatted multi-line string containing the arranged problems.


---

📘 Requirements

Python 3.6 or above



---

🤝 Contributing

Pull requests are welcome.
For major changes, please open an issue first to discuss what you would like to change.


---

📄 License

This project is open-source and free to use.
