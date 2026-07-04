from calculator import calculate_bmi, bmi_category
from utils import validate_input
from tkinter import messagebox
import tkinter as tk
import styles

from widgets import (
    create_button,
    create_entry,
    create_label,
    create_title,
    create_subtitle,
)


class BMICalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI Calculator")
        self.root.geometry("520x780")
        self.root.configure(bg=styles.BACKGROUND)
        self.root.resizable(False, False)

        self.create_header()
        self.create_card()
        self.bind_keys()

        # Cursor starts in Height field
        self.height_entry.focus_set()

    # ---------------- Header ---------------- #

    def create_header(self):
        create_title(
            self.root,
            "BMI Calculator"
        ).pack(pady=(20, 5))

        create_subtitle(
            self.root,
            "Calculate your Body Mass Index"
        ).pack()

    # ---------------- Main Card ---------------- #

    def create_card(self):

        self.card = tk.Frame(
            self.root,
            bg=styles.CARD,
            padx=25,
            pady=25
        )

        self.card.pack(
            padx=20,
            pady=20,
            fill="both",

        )

        self.create_unit_selector()
        self.create_inputs()
        self.create_buttons()
        self.create_result()
        self.create_footer()

    # ---------------- Unit Selector ---------------- #

    def create_unit_selector(self):

        self.unit = tk.StringVar(value="metric")

        frame = tk.Frame(self.card, bg=styles.CARD)
        frame.pack(pady=(0, 20))

        tk.Radiobutton(
            frame,
            text="Metric (cm / kg)",
            variable=self.unit,
            value="metric",
            bg=styles.CARD,
            fg=styles.TEXT,
            selectcolor=styles.CARD,
            activebackground=styles.CARD,
            activeforeground=styles.TEXT
        ).pack(side="left", padx=10)

        tk.Radiobutton(
            frame,
            text="Imperial (ft / lb)",
            variable=self.unit,
            value="imperial",
            bg=styles.CARD,
            fg=styles.TEXT,
            selectcolor=styles.CARD,
            activebackground=styles.CARD,
            activeforeground=styles.TEXT
        ).pack(side="left", padx=10)

    # ---------------- Inputs ---------------- #

    def create_inputs(self):

        # Height
        create_label(
            self.card,
            "Height (cm)"
        ).pack(anchor="w")

        self.height_entry = create_entry(self.card)
        self.height_entry.pack(
            fill="x",
            pady=(5, 20),
            ipady=8
        )

        # Weight
        create_label(
            self.card,
            "Weight (kg)"
        ).pack(anchor="w")

        self.weight_entry = create_entry(self.card)
        self.weight_entry.pack(
            fill="x",
            pady=(5, 25),
            ipady=8
        )

    

    # ---------------- Buttons ---------------- #

    def create_buttons(self):

        frame = tk.Frame(
        self.card,
        bg=styles.CARD
        )

        frame.pack(pady=10)

        self.calculate_btn = create_button(
            frame,
            "Calculate BMI",
            styles.BUTTON_GREEN,
            self.calculate
        )

        self.calculate_btn.pack(
            side="left",
            padx=10
        )

        self.reset_btn = create_button(
            frame,
            "Reset",
            styles.BUTTON_GRAY,
            self.reset
        )

        self.reset_btn.pack(
            side="left",
            padx=10
        )

    # ---------------- Result ---------------- #

    def create_result(self):

        result_frame = tk.Frame(
            self.card,
            bg="#2F3136",
            padx=15,
            pady=20
    )

        result_frame.pack(fill="x", pady=25)

        self.result_label = tk.Label(
        result_frame,
        text="--",
        bg="#2F3136",
        fg=styles.TEXT,
        font=styles.RESULT_FONT
    )
        self.result_label.pack()

        self.category_label = tk.Label(
            result_frame,
            text="Enter your height and weight",
            bg="#2F3136",
            fg=styles.SUBTEXT,
            font=styles.CATEGORY_FONT
    )
        self.category_label.pack(pady=(10, 5))

        self.advice_label = tk.Label(
        result_frame,
        text="",
        bg="#2F3136",
        fg=styles.SUBTEXT,
        font=styles.ADVICE_FONT,
        wraplength=380,
        justify="center"
    )
        self.advice_label.pack()

    # ---------------- Footer ---------------- #

    def create_footer(self):

        tk.Label(
            self.card,
            text="Developed by Khush Rawat",
            bg=styles.CARD,
            fg=styles.SUBTEXT,
            font=styles.FOOTER_FONT
        ).pack(side="bottom", pady=(25, 0))


    # ---------------- Shortcuts ---------------- #

    def bind_keys(self):

        self.root.bind("<Return>", lambda e: self.calculate())
        self.root.bind("<Escape>", lambda e: self.reset())

    # ---------------- Temporary Methods ---------------- #

    # ---------------- Calculate ---------------- #

    def calculate(self):

        height = self.height_entry.get().strip()
        weight = self.weight_entry.get().strip()

        valid, message = validate_input(height, weight)

        if not valid:
            messagebox.showerror("Invalid Input", message)
            return

        height = float(height)
        weight = float(weight)

        bmi = calculate_bmi(height, weight)

        category, advice = bmi_category(bmi)

        colors = {
            "Underweight": styles.UNDERWEIGHT,
            "Normal Weight": styles.NORMAL,
            "Overweight": styles.OVERWEIGHT,
            "Obese": styles.OBESE
            }

        self.result_label.config(
        text=f"{bmi:.2f}"
        )

        self.category_label.config(
            text=category,
            fg=colors.get(category, styles.TEXT)
        )

        self.advice_label.config(
        text=advice
        )

    # ---------------- Reset ---------------- #

    def reset(self):

        self.height_entry.delete(0, tk.END)
        self.weight_entry.delete(0, tk.END)

        self.result_label.config(
            text="--",
            fg=styles.TEXT
        )

        self.category_label.config(
            text="Enter your height and weight",
            fg=styles.SUBTEXT
        )

        self.advice_label.config(
            text=""
        )

        self.height_entry.focus_set()

