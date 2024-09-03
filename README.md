
# MathLib

MathLib is a Python library that provides basic mathematical operations such as absolute value, addition, subtraction, and multiplication. This library is designed to demonstrate object-oriented principles and interactive command-line interfaces.

## Features

- **Absolute Value**: Calculate the absolute value of a number.
- **Addition**: Add two numbers.
- **Subtraction**: Subtract one number from another.
- **Multiplication**: Multiply two numbers, supporting positive and negative multiplicands.

## Installation

To use this library, clone the repository and set up your environment:

1. **Clone the Repository**

```bash
git clone https://github.com/kelechiP/math_lib.git
cd math_lib
```

2. **Create a Virtual Environment (Recommended)**

```bash
python -m venv venv
```

3. **Activate the Virtual Environment**

- **On Windows:**

```bash
venv\Scripts\activate
```

- **On macOS/Linux:**

```bash
source venv/bin/activate
```

4. **Install Dependencies**

```bash
pip install -r requirements.txt
```

## Usage

To run the application interactively, use the following command:

```bash
python src/math_lib/math_lib.py
```

The application will display a menu with options to perform different operations. You can enter the values you want to calculate, and the results will be displayed.

## Example

Choose an operation:

1. Absolute Value
2. Addition
3. Subtraction
4. Multiplication
5. Exit
   Enter choice (1/2/3/4/5): 2
   Enter the first number: 10
   Enter the second number: 5
   Sum: 15.0

Choose an operation:

1. Absolute Value
2. Addition
3. Subtraction
4. Multiplication
5. Exit
   Enter choice (1/2/3/4/5): 1
   Enter a number: -20
   Absolute value: 20.0

Choose an operation:

1. Absolute Value
2. Addition
3. Subtraction
4. Multiplication
5. Exit
   Enter choice (1/2/3/4/5): 5
   Exiting the program.

## Running Tests

To run the tests for this library, use `pytest`:

```bash
pytest
```

This will execute all tests in the tests/ directory to ensure the correctness of the library functions.

## License
This project is licensed under the MIT License - see the `LICENSE` file for details.

## Contributing
If you'd like to contribute to the development of this library, please follow these steps:

   1. Fork the repository.
   2. Create a new branch for your feature or bug fix.
   3. Make your changes and commit them with clear messages.
   4. Push your branch and create a pull request

We appreciate any contributions and feedback!

## Contact
For any questions or feedback, please contact kelechi Uradu.
