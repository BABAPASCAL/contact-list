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