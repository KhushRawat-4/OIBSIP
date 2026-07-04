import tkinter as tk
from gui import BMICalculatorGUI


def main():
    root = tk.Tk()

    app = BMICalculatorGUI(root)

    root.mainloop()


if __name__ == "__main__":
    main()