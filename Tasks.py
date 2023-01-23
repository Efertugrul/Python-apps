import tkinter as tk
from tkinter import messagebox
import os

class ShoppingListApp:
    def __init__(self, master):
        self.master = master
        master.title("Shopping List")

        # Create a listbox to display the items
        self.listbox = tk.Listbox(master, height=10, width=30)
        self.listbox.pack()

        # Create a textbox for the user to input items
        self.textbox = tk.Entry(master, width=30)
        self.textbox.pack()

        # Create a button to add items to the list
        self.add_button = tk.Button(master, text="Add", command=self.add_item, foreground= "blue")
        self.add_button.pack()

        # Create a button to remove items from the list
        self.remove_button = tk.Button(master, text="Remove", command=self.remove_item, foreground= "red")
        self.remove_button.pack()

        # Create a button to clear the list
        self.clear_button = tk.Button(master, text="Clear", command=self.clear_list)
        self.clear_button.pack()

        # Create a button to save the list to a file
        self.save_button = tk.Button(master, text="Save", command=self.save_list)
        self.save_button.pack()

        # Create a button to load the list from a file
        self.load_button = tk.Button(master, text="Load", command=self.load_list)
        self.load_button.pack()

        # Try to load the list from a file
        self.load_list()

    def add_item(self):
        item = self.textbox.get()
        if item:
            self.listbox.insert(tk.END, item)
            self.textbox.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter an item to add.")

    def remove_item(self):
        selected_item = self.listbox.get(self.listbox.curselection())
        if selected_item:
            self.listbox.delete(self.listbox.curselection())
        else:
            messagebox.showerror("Error", "Please select an item to remove.")

    def clear_list(self):
        self.listbox.delete(0, tk.END)

    def save_list(self):
        with open("shopping_list.txt", "w") as file:
            for item in self.listbox.get(0, tk.END):
                file.write(item + "\n")
        messagebox.showinfo("Success", "Shopping list saved to shopping_list.txt.")

    def load_list(self):
        if os.path.exists("shopping_list.txt"):
            with open("shopping_list.txt", "r") as file:
                for line in file:
                    self.listbox.insert(tk.END, line.strip())
           
        else:
            messagebox.showinfo("Info", "Previous shopping list does not exist.")



root = tk.Tk()
app = ShoppingListApp(root)
root.mainloop()
