import pyperclip
import tkinter as tk
from tkinter import messagebox

from generator import generate_password
from utils import password_strength

import styles

from widgets import (
    create_title,
    create_subtitle,
    create_label,
    create_button
)


class PasswordGeneratorGUI:

    def __init__(self, root):

        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("520x650")
        self.root.configure(bg=styles.BACKGROUND)
        self.root.resizable(False, False)
        
        self.create_header()
        self.create_card()
        
        self.root.bind(
            "<Return>",
            lambda event: self.generate()
        )
    # ---------------- Header ---------------- #

    def create_header(self):

        create_title(
            self.root,
            "🔐 Password Generator"
        ).pack(pady=(20, 5))

        create_subtitle(
            self.root,
            "Generate strong and secure passwords"
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
            expand=True
        )

        self.create_length_selector()
        self.create_options()
        self.create_password_box()
        self.create_strength()
        self.create_buttons()
        self.create_footer()
    
        # ---------------- Length ---------------- #

    def create_length_selector(self):

        create_label(
            self.card,
            "Password Length"
        ).pack(anchor="w")

        self.length_value = tk.IntVar(value=16)

        self.length_label = tk.Label(
            self.card,
            text="16",
            bg=styles.CARD,
            fg=styles.TEXT
        )

        self.length_label.pack(anchor="e")

        self.slider = tk.Scale(
            self.card,
            from_=8,
            to=64,
            orient="horizontal",
            variable=self.length_value,
            bg=styles.CARD,
            fg=styles.TEXT,
            troughcolor=styles.SLIDER,
            highlightthickness=0,
            command=self.update_length
        )

        self.slider.pack(fill="x", pady=(5, 20))

    def update_length(self, value):
        self.length_label.config(text=value)



    # ---------------- Options ---------------- #

    def create_options(self):

        self.uppercase = tk.BooleanVar(value=True)
        self.lowercase = tk.BooleanVar(value=True)
        self.numbers = tk.BooleanVar(value=True)
        self.symbols = tk.BooleanVar(value=True)

        frame = tk.Frame(
            self.card,
            bg=styles.CARD
        )

        frame.pack(pady=10)

        tk.Checkbutton(
            frame,
            text="Uppercase",
            variable=self.uppercase,
            bg=styles.CARD,
            fg=styles.TEXT,
            selectcolor=styles.CARD
        ).grid(row=0, column=0, padx=20)

        tk.Checkbutton(
            frame,
            text="Lowercase",
            variable=self.lowercase,
            bg=styles.CARD,
            fg=styles.TEXT,
            selectcolor=styles.CARD
        ).grid(row=0, column=1, padx=20)

        tk.Checkbutton(
            frame,
            text="Numbers",
            variable=self.numbers,
            bg=styles.CARD,
            fg=styles.TEXT,
            selectcolor=styles.CARD
        ).grid(row=1, column=0, padx=20, pady=10)

        tk.Checkbutton(
            frame,
            text="Symbols",
            variable=self.symbols,
            bg=styles.CARD,
            fg=styles.TEXT,
            selectcolor=styles.CARD
        ).grid(row=1, column=1, padx=20, pady=10)

    # ---------------- Password Box ---------------- #

    def create_password_box(self):

        create_label(
            self.card,
            "Generated Password"
        ).pack(anchor="w", pady=(20, 5))

        self.password_var = tk.StringVar()

        self.password_entry = tk.Entry(
            self.card,
            textvariable=self.password_var,
            font=styles.ENTRY_FONT,
            justify="center",
            bg=styles.ENTRY_BG,
            fg=styles.ENTRY_FG,
            relief="flat",
            state="readonly"
        )

        self.password_entry.pack(
            fill="x",
            ipady=8
        )
    # ---------------- Strength ---------------- #

    def create_strength(self):

        self.strength_label = tk.Label(
            self.card,
            text="Strength: -",
            bg=styles.CARD,
            fg=styles.SUBTEXT,
            font=styles.LABEL_FONT
        )

        self.strength_label.pack(
            pady=(20, 10)
        )
        # ---------------- Buttons ---------------- #

    def create_buttons(self):

        frame = tk.Frame(
            self.card,
            bg=styles.CARD
        )

        frame.pack(pady=20)

        self.generate_btn = create_button(
            frame,
            "Generate",
            styles.BUTTON_GREEN,
            self.generate
        )

        self.generate_btn.pack(
            side="left",
            padx=8
        )

        self.copy_btn = create_button(
            frame,
            "Copy",
            styles.BUTTON_BLUE,
            self.copy_password
        )

        self.copy_btn.pack(
            side="left",
            padx=8
        )

        self.clear_btn = create_button(
            frame,
            "Clear",
                styles.BUTTON_RED,
            self.clear
        )

        self.clear_btn.pack(
            side="left",
            padx=8
        )
# ---------------- Footer ---------------- #

    def create_footer(self):

        tk.Label(
            self.card,
            text="Developed by Khush Rawat",
            bg=styles.CARD,
            fg=styles.SUBTEXT,
            font=styles.FOOTER_FONT
        ).pack(
            side="bottom",
        pady=(20, 0)
        )   

# ---------------- Generate ---------------- #

    def generate(self):

        try:

            password = generate_password(
                length=self.length_value.get(),
                uppercase=self.uppercase.get(),
                lowercase=self.lowercase.get(),
                numbers=self.numbers.get(),
                symbols=self.symbols.get()
            )

        except ValueError as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

            return

        self.password_entry.config(state="normal")
        self.password_var.set(password)
        self.password_entry.config(state="readonly")

        strength = password_strength(password)

        colors = {
            "Weak": styles.WEAK,
            "Medium": styles.MEDIUM,
            "Strong": styles.STRONG
        }

        self.strength_label.config(
            text=f"Strength: {strength}",
            fg=colors[strength]
        )

# ---------------- Copy ---------------- #

    def copy_password(self):

        password = self.password_var.get()

        if not password:
            return

        pyperclip.copy(password)

        self.copy_btn.config(text="✓ Copied")

        self.copy_btn.config(
        text="✓ Copied",
        state="disabled"
        )

        self.root.after(
            2000,
            lambda: self.copy_btn.config(
                text="Copy",
                state="normal"
            )
        )

# ---------------- Clear ---------------- #

    def clear(self):

        self.password_entry.config(state="normal")
        self.password_var.set("")
        self.password_entry.config(state="readonly")

        self.strength_label.config(
            text="Strength: -",
            fg=styles.SUBTEXT
        )
