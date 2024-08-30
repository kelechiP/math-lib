"""MathLib class for basic mathematical operations."""

class MathLib:
    @staticmethod
    def abs(number: float) -> float:
        """Absolute function.

        Args:
            number (float): Real number.

        Returns:
            float: Absolute value of number.
        """
        if number < 0:
            number = -1 * number
        return number

    @staticmethod
    def add(augend: float, addend: float) -> float:
        """Addition function.

        Args:
            augend (float): The augend of the addition.
            addend (float): The addend of the addition.

        Returns:
            float: The sum of augend and addend.
        """
        return augend + addend

    @staticmethod
    def sub(minuend: float, subtrahend: float) -> float:
        """Subtraction function.

        Args:
            minuend (float): The number being subtracted from.
            subtrahend (float): The number being subtracted from another.

        Returns:
            float: The difference of minuend and subtrahend.
        """
        return minuend - subtrahend

    @classmethod
    def mult(cls, multiplier: float, multiplicand: float) -> float:
        """Multiplication function.

        Args:
            multiplier (float): Multiplier.
            multiplicand (float): Multiplicand.

        Returns:
            float: Product of multiplier and multiplicand.
        """
        value = range(multiplicand)
        func = cls.add
        if multiplicand < 0:
            value = range(0, multiplicand, -1)
            func = cls.sub

        sum = 0
        for _ in value:
            sum = func(sum, multiplier)
        return sum

if __name__ == "__main__":
    math_lib = MathLib()

    while True:
        print("\nChoose an operation:")
        print("1. Absolute Value")
        print("2. Addition")
        print("3. Subtraction")
        print("4. Multiplication")
        print("5. Exit")

        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '1':
            num = float(input("Enter a number: "))
            print(f"Absolute value: {math_lib.abs(num)}")
        elif choice == '2':
            augend = float(input("Enter the first number: "))
            addend = float(input("Enter the second number: "))
            print(f"Sum: {math_lib.add(augend, addend)}")
        elif choice == '3':
            minuend = float(input("Enter the number to subtract from: "))
            subtrahend = float(input("Enter the number to subtract: "))
            print(f"Difference: {math_lib.sub(minuend, subtrahend)}")
        elif choice == '4':
            multiplier = float(input("Enter the multiplier: "))
            multiplicand = int(input("Enter the multiplicand: "))
            print(f"Product: {math_lib.mult(multiplier, multiplicand)}")
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")
