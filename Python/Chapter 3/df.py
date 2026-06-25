from tkinter import *
from tkinter import messagebox

def save_data():
    name = t1.get()
    address = t2.get()
    
    if name and address:
        # Save data to file
        with open("user_data.txt", "a", encoding="utf-8") as file:
            file.write(f"Name: {name}, Address: {address}\n")
        
        messagebox.showinfo("Success", f"Data Saved to file!\nName: {name}\nAddress: {address}")
        # Clear fields after saving
        t1.delete(0, END)
        t2.delete(0, END)
    else:
        messagebox.showwarning("Warning", "Please fill all fields!")

# Create main window
top = Tk()
top.title("User Information Form")
top.geometry('400x200')
top.resizable(False, False)

# Add padding to make it look better
top.config(padx=20, pady=20)

# Name field
n1 = Label(top, text="Name:", font=("Arial", 12))
n1.grid(row=0, column=0, sticky="w", pady=10)
t1 = Entry(top, width=30, font=("Arial", 11))
t1.grid(row=0, column=1, pady=10, padx=10)

# Address field
n2 = Label(top, text="Address:", font=("Arial", 12))
n2.grid(row=1, column=0, sticky="w", pady=10)
t2 = Entry(top, width=30, font=("Arial", 11))
t2.grid(row=1, column=1, pady=10, padx=10)

# Save button with functionality
btn = Button(top, text="Save", command=save_data, bg="#4CAF50", fg="white", 
             font=("Arial", 11, "bold"), width=15, cursor="hand2")
btn.grid(row=2, column=0, columnspan=2, pady=20)

# Start the GUI
top.mainloop()