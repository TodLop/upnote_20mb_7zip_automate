import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox

def get_all_files(folder_path):
    files = []
    for root, _, filenames in os.walk(folder_path):
        for filename in filenames:
            files.append(os.path.join(root, filename))
    return files

def compress_file(file_path, output_folder, chunk_size=20):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Full path to 7z.exe
    seven_zip_path = "C:\\Program Files\\7-Zip\\7z.exe"
    
    # Ensure chunk_size is correctly formatted
    volume_size = f"-v{chunk_size}m"
    
    command = [
        seven_zip_path, "a",
        os.path.join(output_folder, os.path.basename(file_path) + ".7z"),
        file_path,
        volume_size,
        "-mx=9",  # Maximum compression level
        "-m0=LZMA2"  # Use LZMA2 compression method
    ]
    
    subprocess.run(command, check=True)

def start_compression(folder_path):
    output_folder = os.path.join(folder_path, "compressed")
    files = get_all_files(folder_path)
    
    for file in files:
        compress_file(file, output_folder)
        print(f"Compressed {file} into {output_folder}")
    
    messagebox.showinfo("Success", "All files have been compressed successfully!")

def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        folder_path_var.set(folder_path)

def on_compress_button_click():
    folder_path = folder_path_var.get()
    if folder_path and os.path.isdir(folder_path):
        start_compression(folder_path)
    else:
        messagebox.showerror("Error", "Please select a valid folder.")

app = tk.Tk()
app.title("7-Zip Compression Tool")

folder_path_var = tk.StringVar()

frame = tk.Frame(app)
frame.pack(padx=10, pady=10)

select_button = tk.Button(frame, text="Select Folder", command=select_folder)
select_button.pack(side=tk.LEFT, padx=(0, 10))

folder_entry = tk.Entry(frame, textvariable=folder_path_var, width=50)
folder_entry.pack(side=tk.LEFT)

compress_button = tk.Button(app, text="Compress Files", command=on_compress_button_click)
compress_button.pack(pady=(10, 0))

app.mainloop()
