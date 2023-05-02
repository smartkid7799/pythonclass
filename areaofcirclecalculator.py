import customtkinter as ctk
import math

def enter_clicked():
    radius=float(radiusEntry.get())
    area=radius*radius
    answerLabel.configure(text=str(area)+"π")
    print(area)


app=ctk.CTk()
app.geometry("350x500")
app.title("area of circle calculator")

titleLabel=ctk.CTkLabel(app, text="Enter the radius", anchor="e", font=ctk.CTkFont(size=30), width=150, height=0)
titleLabel.grid(row=0, column=0)

radiusEntry= ctk.CTkEntry(app, placeholder_text="Enter radius of the circle", width=300, height=50)
radiusEntry.grid(row=1, column=0)

enterButton = ctk.CTkButton(app, text="Find the Area", border_width=1, height=40, width=250, command=enter_clicked)
enterButton.grid(row=2, column=0)

answerLabel=ctk.CTkLabel(app, text=" ", anchor="e", font=ctk.CTkFont(size=30), width=150, height=0)
answerLabel.grid(row=3, column=0)

app.mainloop()