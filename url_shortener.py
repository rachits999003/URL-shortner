import tkinter as tk
from tkinter import messagebox
import pyshorteners
import pyperclip

def shorten_url():
    long_url = url_entry.get()
    if not long_url:
        messagebox.showerror("Error", "Enter a URL first!")
        return
    
    try:
        s = pyshorteners.Shortener()
        short_url = s.tinyurl.short(long_url)
        result_entry.delete(0, tk.END)
        result_entry.insert(0, short_url)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to shorten URL: {e}")

def copy_to_clipboard():
    short_url = result_entry.get()
    if short_url:
        pyperclip.copy(short_url)
        messagebox.showinfo("Copied", "Short URL copied to clipboard!")

# GUI Setup
root = tk.Tk()
root.title("URL Shortener")
root.geometry("400x200")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack(pady=10)

tk.Label(frame, text="Enter URL:", font=("Arial", 12)).pack()
url_entry = tk.Entry(frame, width=40)
url_entry.pack(pady=5)

tk.Button(frame, text="Shorten URL", command=shorten_url, font=("Arial", 12)).pack(pady=5)

tk.Label(frame, text="Shortened URL:", font=("Arial", 12)).pack()
result_entry = tk.Entry(frame, width=40)
result_entry.pack(pady=5)

tk.Button(frame, text="Copy", command=copy_to_clipboard, font=("Arial", 12)).pack(pady=5)

root.mainloop()