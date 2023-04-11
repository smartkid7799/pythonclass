import customtkinter as ctk

def enter_clicked():
    print("enter clicked")

app = ctk.CTk()
app.geometry("500x300")
app.title("My First App")

nameLabel = ctk.CTkLabel(app, text="Name: ")
nameLabel.grid(row=0, column=0)

nameEntry= ctk.CTkEntry(app, placeholder_text="Enter your name")
nameEntry.grid(row=0, column=1)

AddressLabel = ctk.CTkLabel(app, text="Address")
AddressLabel.grid(row=1, column=0)

AddressEntry= ctk.CTkEntry(app, placeholder_text=" Enter your Address")
AddressEntry.grid(row=1, column=1)

enterButton = ctk.CTkButton(app, text="Enter", command=enter_clicked, border_width=1)
enterButton.grid(row=2, column=1)

app.mainloop()