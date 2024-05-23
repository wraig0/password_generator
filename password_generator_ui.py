import tkinter as tk
from tkinter import messagebox
from password_generator import generate
  
def copy_password(root, password_text):
  root.clipboard_clear()
  root.clipboard_append(password_text.get())
  messagebox.showinfo("Password Copied", "Password has been copied to the clipboard.")

def main():

  root = tk.Tk()
  root.title("Password Generator")
  root.wm_minsize(300, 100)

  password_text = tk.StringVar()

  generate_button = tk.Button(root, text="Generate Password", command=lambda: password_text.set(generate()))
  generate_button.pack(pady=10)

  password_label = tk.Label(root, textvariable=password_text, font=("Segoe UI", 12), relief="solid")
  password_label.pack(pady=10)
  password_label.config(width=20)

  copy_button = tk.Button(root, text="Copy Password", command=lambda: copy_password(root, password_text))
  copy_button.pack(pady=10)

  root.mainloop()
  
if __name__ == "__main__":
  main()