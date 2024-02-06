import tkinter as tk

class ContactsExploreAppCover(tk.Tk):
    def __init__(self, on_start_callback):
        super().__init__()

        self.title("Contacts Explore App")
        self.geometry("1920x1080")
        self.configure(bg="black")  # Set background color to black

        self.label = tk.Label(self, text="Contacts Explore App", font=("Forte", 20), bg="black", fg="white")
        self.label.pack(pady=20)

        self.description = tk.Label(self, text="A simple app to manage your contacts :).", bg="black", fg="white")
        self.description.pack(pady=10)

        self.start_button = tk.Button(self, text="Start App", command=on_start_callback, bg="blue", fg="black")
        self.start_button.pack(pady=20)

class ContactsExploreApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Contacts Explore App")
        self.geometry("1920x1080")
        self.configure(bg="black")  # Set background color to black

        self.label = tk.Label(self, text="Welcome to the Contacts Explore App!", font=("Forte", 20), bg="black", fg="white")
        self.label.pack(pady=10)

        self.contacts = {}

        self.add_contact_frame = tk.Frame(self, bg="blue")
        self.add_contact_frame.pack(pady=10)

        self.search_contact_frame = tk.Frame(self, bg="blue")
        self.search_contact_frame.pack(pady=10)

        self.display_contact_frame = tk.Frame(self, bg="blue")
        self.display_contact_frame.pack(pady=10)

        self.edit_contact_frame = tk.Frame(self, bg="blue")
        self.edit_contact_frame.pack(pady=10)

        self.delete_contact_frame = tk.Frame(self, bg="blue")
        self.delete_contact_frame.pack(pady=10)

        self.add_contact_button = tk.Button(self.add_contact_frame, text="Add Contact", command=self.add_contact, bg="black", fg="white")
        self.add_contact_button.pack(pady=5)

        self.search_contact_button = tk.Button(self.search_contact_frame, text="Search Contact", command=self.search_contact, bg="black", fg="white")
        self.search_contact_button.pack(pady=5)

        self.display_contact_button = tk.Button(self.display_contact_frame, text="Display Contacts", command=self.display_contacts, bg="black", fg="white")
        self.display_contact_button.pack(pady=5)

        self.edit_contact_button = tk.Button(self.edit_contact_frame, text="Edit Contact", command=self.edit_contact, bg="black", fg="white")
        self.edit_contact_button.pack(pady=5)

        self.delete_contact_button = tk.Button(self.delete_contact_frame, text="Delete Contact", command=self.delete_contact, bg="black", fg="white")
        self.delete_contact_button.pack(pady=5)

def add_contact(self):
    add_contact_window = tk.Toplevel(self)
    add_contact_window.title("Add Contact")
    add_contact_window.geometry("300x150")
    add_contact_window.configure(bg="black")

    name_label = tk.Label(add_contact_window, text="Name:", bg="black", fg="white")


name_label.pack(pady=5)
name_entry = tk.Entry(add_contact_window)
name_entry.pack(pady=5)

phone_label = tk.Label(add_contact_window, text="Phone:", bg="black", fg="white")
phone_label.pack(pady=5)
phone_entry = tk.Entry(add_contact_window)
phone_entry.pack(pady=5)

save_button = tk.Button(add_contact_window, text="Save",
                        command=lambda: self.save_contact(name_entry.get(), phone_entry.get(), add_contact_window),
                        bg="black", fg="white")
save_button.pack(pady=5)


def save_contact(self, name, phone, window):
    self.contacts[name] = phone
    window.destroy()


def search_contact(self):
    search_contact_window = tk.Toplevel(self)
    search_contact_window.title("Search Contact")
    search_contact_window.geometry("300x100")
    search_contact_window.configure(bg="black")

    search_label = tk.Label(search_contact_window, text="Search Name:", bg="black", fg="white")
    search_label.pack(pady=5)
    search_entry = tk.Entry(search_contact_window)
    search_entry.pack(pady=5)

    search_button = tk.Button(search_contact_window, text="Search",
                              command=lambda: self.display_search_result(search_entry.get()), bg="black", fg="white")
    search_button.pack(pady=5)

    def display_search_result(self, search_name):
        if name in self.contacts:
            self.contacts[name] = phone
            window.destroy()
            self.display_contacts()
        else:
            not_found_window = tk.Toplevel(self)
            not_found_window.title("Update Result")
            not_found_window.geometry("200x100")
            not_found_window.configure(bg="black")

            not_found_label = tk.Label(not_found_window, text="Name is not found in the contact book", bg="black", fg="white")
            not_found_label.pack(pady=20)

    def delete_contact(self):
        delete_contact_window = tk.Toplevel(self)
        delete_contact_window.title("Delete Contact")
        delete_contact_window.geometry("300x100")
        delete_contact_window.configure(bg="black")

        delete_label = tk.Label(delete_contact_window, text="Name:", bg="black", fg="white")
        delete_label.pack(pady=5)
        delete_entry = tk.Entry(delete_contact_window)
        delete_entry.pack(pady=5)

        delete_button = tk.Button(delete_contact_window, text="Delete", command=lambda: self.remove_contact(delete_entry.get(), delete_contact_window), bg="black", fg="white")
        delete_button.pack(pady=5)

    def remove_contact(self, name, window):
        if name in self.contacts:
            del self.contacts[name]
            window.destroy()
            self.display_contacts()
        else:
            not_found_window = tk.Toplevel(self)
            not_found_window.title("Delete Result")
            not_found_window.geometry("200x100")
            not_found_window.configure(bg="black")

            not_found_label = tk.Label(not_found_window, text="Name is not found in the contact book", bg="black", fg="white")
            not_found_label.pack(pady=20)


if __name__ == "__main__":
    def start_app():
        app_cover.destroy()
        contacts_explore_app = ContactsExploreApp()
        contacts_explore_app.mainloop()

    app_cover = ContactsExploreAppCover(on_start_callback=start_app)
    app_cover.mainloop()
