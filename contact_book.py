import tkinter as tk
from tkinter import messagebox

contacts = {}

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()

    if not name or not phone or not email:
        messagebox.showwarning("Input Error", "Please fill out all fields")
        return

    if name in contacts:
        messagebox.showwarning("Contact Exists", "Contact with this name already exists")
        return

    contacts[name] = {'phone': phone, 'email': email}
    messagebox.showinfo("Success", "Contact added successfully")
    clear_entries()

def view_contacts():
    output = ""
    for name, info in contacts.items():
        output += f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}\n"
    if not output:
        output = "No contacts to display"
    messagebox.showinfo("Contacts", output)

def search_contact():
    name = name_entry.get()
    if name in contacts:
        info = contacts[name]
        result = f"Name: {name}\nPhone: {info['phone']}\nEmail: {info['email']}"
    else:
        result = "Contact not found"
    messagebox.showinfo("Search Result", result)
    clear_entries()

def update_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()

    if not name:
        messagebox.showwarning("Input Error", "Please enter the contact name to update")
        return

    if name not in contacts:
        messagebox.showwarning("Contact Not Found", "Contact does not exist")
        return

    if phone:
        contacts[name]['phone'] = phone
    if email:
        contacts[name]['email'] = email
    
    messagebox.showinfo("Success", "Contact updated successfully")
    clear_entries()

def delete_contact():
    name = name_entry.get()
    if name in contacts:
        del contacts[name]
        messagebox.showinfo("Success", "Contact deleted successfully")
    else:
        messagebox.showwarning("Contact Not Found", "Contact does not exist")
    clear_entries()

def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Contact Book")

tk.Label(root, text="Name").grid(row=0, column=0, padx=10, pady=5)
tk.Label(root, text="Phone").grid(row=1, column=0, padx=10, pady=5)
tk.Label(root, text="Email").grid(row=2, column=0, padx=10, pady=5)

name_entry = tk.Entry(root)
phone_entry = tk.Entry(root)
email_entry = tk.Entry(root)

name_entry.grid(row=0, column=1, padx=10, pady=5)
phone_entry.grid(row=1, column=1, padx=10, pady=5)
email_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Button(root, text="Add Contact", command=add_contact).grid(row=3, column=0, padx=10, pady=5)
tk.Button(root, text="View Contacts", command=view_contacts).grid(row=3, column=1, padx=10, pady=5)
tk.Button(root, text="Search Contact", command=search_contact).grid(row=4, column=0, padx=10, pady=5)
tk.Button(root, text="Update Contact", command=update_contact).grid(row=4, column=1, padx=10, pady=5)
tk.Button(root, text="Delete Contact", command=delete_contact).grid(row=5, column=0, padx=10, pady=5)

root.mainloop()
