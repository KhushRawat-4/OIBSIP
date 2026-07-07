import tkinter as tk
import styles


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
        relief="flat"
    )


def create_button(parent, text, color, command):
    return tk.Button(
        parent,
        text=text,
        command=command,
        bg=color,
        fg="white",
        relief="flat",
        font=styles.BUTTON_FONT,
        width=12,
        cursor="hand2",
        activebackground=color,
        activeforeground="white"
    )