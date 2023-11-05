import tkinter as tk
from tkinter import messagebox

# Contact list stored as a list of dictionaries
contacts = []

# Function to add a new contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name and phone:
        contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
        contacts.append(contact)
        update_contact_list()
        clear_entries()
    else:
        messagebox.showerror("Error", "Name and Phone fields are required!")

# Function to view the contact list
def update_contact_list():
    contact_list.delete(0, tk.END)  # Clear the current list

    for contact in contacts:
        name = contact["Name"]
        phone = contact["Phone"]
        contact_list.insert(tk.END, f"{name}: {phone}")

# Function to search for a contact
def search_contact():
    search_term = search_entry.get().lower()

    for contact in contacts:
        if (
            search_term in contact["Name"].lower()
            or search_term in contact["Phone"].lower()
        ):
            messagebox.showinfo("Contact Found", f"Name: {contact['Name']}\nPhone: {contact['Phone']}\nEmail: {contact['Email']}\nAddress: {contact['Address']}")
            return
    messagebox.showinfo("Contact Not Found", "No contact found with the given search term.")

# Function to update a contact
def update_contact():
    selected_contact = contact_list.curselection()
    if selected_contact:
        selected_contact_index = selected_contact[0]
        name = name_entry.get()
        phone = phone_entry.get()
        email = email_entry.get()
        address = address_entry.get()

        if name and phone:
            contacts[selected_contact_index] = {
                "Name": name,
                "Phone": phone,
                "Email": email,
                "Address": address,
            }
            update_contact_list()
            clear_entries()
        else:
            messagebox.showerror("Error", "Name and Phone fields are required!")

# Function to delete a contact
def delete_contact():
    selected_contact = contact_list.curselection()
    if selected_contact:
        selected_contact_index = selected_contact[0]
        contacts.pop(selected_contact_index)
        update_contact_list()
        clear_entries()

# Function to clear entry fields
def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Contact Management System")

# Create and set up GUI elements
name_label = tk.Label(root, text="Name:")
phone_label = tk.Label(root, text="Phone:")
email_label = tk.Label(root, text="Email:")
address_label = tk.Label(root, text="Address:")
name_entry = tk.Entry(root)
phone_entry = tk.Entry(root)
email_entry = tk.Entry(root)
address_entry = tk.Entry(root)
add_button = tk.Button(root, text="Add Contact", command=add_contact)
view_button = tk.Button(root, text="View Contacts", command=update_contact_list)
search_label = tk.Label(root, text="Search:")
search_entry = tk.Entry(root)
search_button = tk.Button(root, text="Search Contact", command=search_contact)
update_button = tk.Button(root, text="Update Contact", command=update_contact)
delete_button = tk.Button(root, text="Delete Contact", command=delete_contact)
contact_list = tk.Listbox(root)

# Arrange GUI elements in the window
name_label.grid(row=0, column=0)
phone_label.grid(row=1, column=0)
email_label.grid(row=2, column=0)
address_label.grid(row=3, column=0)
name_entry.grid(row=0, column=1)
phone_entry.grid(row=1, column=1)
email_entry.grid(row=2, column=1)
address_entry.grid(row=3, column=1)
add_button.grid(row=4, column=0)
view_button.grid(row=4, column=1)
search_label.grid(row=5, column=0)
search_entry.grid(row=5, column=1)
search_button.grid(row=6, column=0)
update_button.grid(row=6, column=1)
delete_button.grid(row=7, column=0)
contact_list.grid(row=8, columnspan=2)

root.mainloop()
