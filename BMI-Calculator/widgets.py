import tkinter as tk
import styles


def create_button(parent, text, color, command):
    """
    Create a styled button with hover effect.
    """

    button = tk.Button(
        parent,
        text=text,
        command=command,
        font=styles.BUTTON_FONT,
        bg=color,
        fg="white",
        activeforeground="white",
        relief="flat",
        bd=0,
        cursor="hand2",
        width=15,
        pady=8
    )

    hover_color = {
        styles.BUTTON_GREEN: styles.BUTTON_GREEN_HOVER,
        styles.BUTTON_GRAY: styles.BUTTON_GRAY_HOVER,
    }.get(color, color)

    button.bind(
        "<Enter>",
        lambda e: button.config(bg=hover_color)
    )

    button.bind(
        "<Leave>",
        lambda e: button.config(bg=color)
    )

    return button


def create_title(parent, text):
    return tk.Label(
        parent,
        text=text,
        bg=styles.BACKGROUND,
        fg=styles.TEXT,
        font=styles.TITLE_FONT
    )


def create_subtitle(parent, text):
    return tk.Label(
        parent,
        text=text,
        bg=styles.BACKGROUND,
        fg=styles.SUBTEXT,
        font=styles.SUBTITLE_FONT
    )


def create_label(parent, text):
    return tk.Label(
        parent,
        text=text,
        bg=styles.CARD,
        fg=styles.TEXT,
        font=styles.LABEL_FONT
    )


def create_entry(parent):
    return tk.Entry(
        parent,
        font=styles.ENTRY_FONT,
        justify="center",
        bg=styles.ENTRY_BG,
        fg=styles.ENTRY_FG,
        insertbackground="white",
        relief="flat",
        bd=0
    )