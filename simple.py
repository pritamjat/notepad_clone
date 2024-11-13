import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

# Create the main application window
root = tk.Tk()
root.title("Simple Notepad")
root.geometry("600x400")


# Add a Text widget for the main text area
text_area = tk.Text(root, wrap='word')
text_area.pack(expand=1, fill='both')


def new_file():
    text_area.delete(1.0, tk.END)  # Clear the text area

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt"),
                                                        ("All files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text_area.get(1.0, tk.END))

def exit_app():
    if messagebox.askokcancel("Quit", "Do you really want to quit?"):
        root.destroy()

# Create a menu bar
menu_bar = tk.Menu(root)

# Add File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)
menu_bar.add_cascade(label="File", menu=file_menu)

root.config(menu=menu_bar)


root.mainloop()
