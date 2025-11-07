import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def organize_files():
    directory = folder_path.get()
    split = split_char_var.get().strip()

    if not directory:
        messagebox.showwarning("No Folder Selected", "Please select a folder first.")
        return

    if not split:
        messagebox.showwarning("No Split Character", "Please enter a character or string to split filenames by.")
        return

    try:
        organize_count = 0
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            if not os.path.isfile(file_path):
                continue

            #Create a split based off of a user defined character, such as -, _, or (.
            if split in filename:
                folder_name = filename.split(split, 1)[0]
            else:
                folder_name = "misc"

            target = os.path.join(directory, folder_name)
            os.makedirs(target, exist_ok=True)

            destination = os.path.join(target, filename)
            if os.path.exists(destination):
                print(f"Skipped: {filename} already exists")
                continue

            shutil.move(file_path, destination)
            organize_count += 1

        messagebox.showinfo("Done", f"Organized {organize_count} files successfully!")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred:\n{e}")

def browse_folder():
    folder = filedialog.askdirectory()
    if folder:
        folder_path.set(folder)

#GUI
root = tk.Tk()
root.title("Flexible File Organizer")
root.geometry("420x260")
root.resizable(False, False)

folder_path = tk.StringVar()
split_char_var = tk.StringVar(value="-")

#Labels
tk.Label(root, text="Select Folder to Organize:", font=("Segoe UI", 11)).pack(pady=8)
tk.Entry(root, textvariable=folder_path, width=50).pack(pady=3)
tk.Button(root, text="Browse", command=browse_folder).pack(pady=3)

tk.Label(root, text="Split filenames at (e.g. '-', '_', or '.'):", font=("Segoe UI", 11)).pack(pady=10)
tk.Entry(root, textvariable=split_char_var, width=10, justify='center').pack(pady=3)

#Button 1
tk.Button(
    root,
    text="Organize Files",
    command=organize_files,
    bg="#4CAF50",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    width=20,
    height=2
).pack(pady=15)

tk.Label(root, text="No files will ever be deleted or overwritten.", fg="gray").pack(pady=5)

root.mainloop()

