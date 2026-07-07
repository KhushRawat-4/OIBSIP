import threading
import tkinter as tk

from assistant import process_command
from speech import listen


class VoiceAssistantGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Voice Assistant")
        self.root.geometry("500x600")
        self.root.configure(bg="#1e1e1e")

        # Chat display
        self.chat_box = tk.Text(
            root,
            bg="#2b2b2b",
            fg="white",
            font=("Arial", 12),
            wrap="word"
        )
        self.chat_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Input
        self.entry = tk.Entry(root, font=("Arial", 12))
        self.entry.pack(padx=10, pady=5, fill=tk.X)
        self.entry.bind("<Return>", lambda event: self.send_command())

        # Buttons
        btn_frame = tk.Frame(root, bg="#1e1e1e")
        btn_frame.pack(pady=5)

        tk.Button(btn_frame, text="Send",
                  command=self.send_command).pack(side=tk.LEFT, padx=5)

        self.speak_button = tk.Button(
            btn_frame,
            text="Speak",
            command=self.voice_input
        )
        self.speak_button.pack(side=tk.LEFT, padx=5)

        tk.Button(btn_frame, text="Clear",
                  command=self.clear_chat).pack(side=tk.LEFT, padx=5)

        self.print_message("Assistant is ready. Type or speak a command.")

    def print_message(self, msg):
        self.chat_box.insert(tk.END, msg + "\n")
        self.chat_box.see(tk.END)

    def send_command(self):
        command = self.entry.get().strip()
        self.entry.delete(0, tk.END)

        if command:
            self.print_message(f"You: {command}")
            self.print_message("Assistant processing...")

            result = process_command(command)

            if result is False:
                self.print_message("Assistant stopped.")

    def voice_input(self):
        self.speak_button.config(state="disabled")
        self.print_message("Listening...")

        threading.Thread(
            target=self.listen_in_background,
            daemon=True
        ).start()

    def listen_in_background(self):
        command = listen()

        self.root.after(
            0,
            lambda: self.process_voice_command(command)
        )

    def process_voice_command(self, command):
        self.print_message(f"You (voice): {command}")
        self.print_message("Assistant processing...")

        result = process_command(command)

        self.speak_button.config(state="normal")

        if result is False:
            self.print_message("Assistant stopped.")

    def clear_chat(self):
        self.chat_box.delete("1.0", tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = VoiceAssistantGUI(root)
    root.mainloop()