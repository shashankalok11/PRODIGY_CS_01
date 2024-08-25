import tkinter as tk
from tkinter import messagebox

def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            ascii_offset = 65 if char.isupper() else 97
            new_char = chr(((ord(char) - ascii_offset + shift_amount) % 26) + ascii_offset)
            encrypted_text += new_char
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

def perform_encryption():
    message = entry_message.get()
    try:
        shift = int(entry_shift.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift value must be an integer.")
        return
    
    encrypted_message = caesar_cipher_encrypt(message, shift)
    output_text.set(encrypted_message)

def perform_decryption():
    message = entry_message.get()
    try:
        shift = int(entry_shift.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift value must be an integer.")
        return
    
    decrypted_message = caesar_cipher_decrypt(message, shift)
    output_text.set(decrypted_message)

# GUI setup
root = tk.Tk()
root.title("Caesar Cipher")

# Labels
label_message = tk.Label(root, text="Enter your message:")
label_message.grid(row=0, column=0, padx=10, pady=10)

label_shift = tk.Label(root, text="Enter shift value:")
label_shift.grid(row=1, column=0, padx=10, pady=10)

label_output = tk.Label(root, text="Output:")
label_output.grid(row=3, column=0, padx=10, pady=10)

# Entry fields
entry_message = tk.Entry(root, width=40)
entry_message.grid(row=0, column=1, padx=10, pady=10)

entry_shift = tk.Entry(root, width=10)
entry_shift.grid(row=1, column=1, padx=10, pady=10)

output_text = tk.StringVar()
label_result = tk.Label(root, textvariable=output_text, wraplength=300, bg="lightgrey", width=40, height=5)
label_result.grid(row=3, column=1, padx=10, pady=10)

# Buttons
button_encrypt = tk.Button(root, text="Encrypt", command=perform_encryption)
button_encrypt.grid(row=2, column=0, padx=10, pady=10)

button_decrypt = tk.Button(root, text="Decrypt", command=perform_decryption)
button_decrypt.grid(row=2, column=1, padx=10, pady=10)

# Start the GUI loop
root.mainloop()
