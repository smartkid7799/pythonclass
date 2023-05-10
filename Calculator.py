import customtkinter as ctk

currentText="0"
num=0
op=""

def updateText():
    global currentText
    if len(currentText) ==0:
        currentText = "0"


    if len(currentText) > 12:
        currentText = currentText[:12]


    calcLabel.configure(text=currentText)
def addText(str):
    global currentText
    if float(currentText) ==0 and str != "." and "." not in currentText:
        currentText=""



    if '.' in currentText and str == '.':
        return



    currentText = currentText + str
    updateText()

def CE():
    global currentText
    global num
    global op
    currentText = "0"
    num = 0
    op = ""

    updateText()

def Back():
    global currentText
    currentText = currentText[0:len(currentText)-1]


    updateText()

def plus_minus():
    global currentText
    if '-' in currentText:
        currentText = currentText.replace('-', '')
    else:
        currentText = '-' + currentText
    updateText()

app=ctk.CTk()
app.geometry("350x500")
app.title("Calculator")
app.configure(bg_color="white", fg_color="white")

calcFrame=ctk.CTkFrame(app, width=340, height=70, bg_color="white", fg_color="white")
calcFrame.grid(row=0, column=0, padx=5, pady=5)

btnFrame=ctk.CTkFrame(app, width=340, height=400,  bg_color="white", fg_color="white")
btnFrame.grid(row=1, column=0, padx=5, pady=5)

calcLabel=ctk.CTkLabel(calcFrame, text="0", anchor="e", font=ctk.CTkFont(size=50), width=340, height=0)
calcLabel.grid(row=0, column=0)

CEbtn=ctk.CTkButton(btnFrame, text="CE", anchor="nw", width=75, height=65,text_color="black",fg_color="#37b8b4",  font=ctk.CTkFont(size=40), command = CE)
CEbtn.grid(row=0, column=0, padx=5, pady=5)

backbtn=ctk.CTkButton(btnFrame, text=" <-", anchor="nw", width=75, height=65,text_color="black",fg_color="#37b8b4", font=ctk.CTkFont(size=40), command=Back)
backbtn.grid(row=0, column=1, padx=5, pady=5)

squarebtn=ctk.CTkButton(btnFrame, text=" x^2", anchor="nw", width=75, height=65,text_color="black",fg_color="#37b8b4", font=ctk.CTkFont(size=40))
squarebtn.grid(row=0, column=2, padx=5, pady=5)

dividebtn=ctk.CTkButton(btnFrame, text="  /", anchor="nw", width=75, height=65,text_color="black",fg_color="#37b8b4", font=ctk.CTkFont(size=40))
dividebtn.grid(row=0, column=3, padx=5, pady=5)

btn7=ctk.CTkButton(btnFrame, text=" 7", anchor="nw", width=75, height=65,text_color="black",fg_color="light blue",  command=lambda : addText("7"),  font=ctk.CTkFont(size=40))
btn7.grid(row=1, column=0, padx=0, pady=5)

btn8=ctk.CTkButton(btnFrame, text=" 8", anchor="nw", width=75, height=65,text_color="black",fg_color="light blue",command=lambda : addText("8"), font=ctk.CTkFont(size=40))
btn8.grid(row=1, column=1, padx=5, pady=5)

btn9=ctk.CTkButton(btnFrame, text=" 9", anchor="nw", width=75, height=65,text_color="black",fg_color="light blue",command=lambda : addText("9"), font=ctk.CTkFont(size=40))
btn9.grid(row=1, column=2, padx=5, pady=5)

multiplybtn=ctk.CTkButton(btnFrame, text="  x", anchor="nw", width=75, height=65,text_color="black",fg_color="#37b8b4", font=ctk.CTkFont(size=40))
multiplybtn.grid(row=1, column=3, padx=5, pady=5)

btn4=ctk.CTkButton(btnFrame, text=" 4", anchor="nw", width=75, height=65,text_color="black",fg_color="light blue",command=lambda : addText("4"), font=ctk.CTkFont(size=40))
btn4.grid(row=2, column=0, padx=5, pady=5)

btn5=ctk.CTkButton(btnFrame, text=" 5", anchor="nw", width=75, height=65,text_color="black",fg_color="light blue",command=lambda : addText("5"), font=ctk.CTkFont(size=40))
btn5.grid(row=2, column=1, padx=5, pady=5)

btn6=ctk.CTkButton(btnFrame, text=" 6", anchor="nw", width=75, height=65,text_color="black",fg_color="light blue",command=lambda : addText("6"), font=ctk.CTkFont(size=40))
btn6.grid(row=2, column=2, padx=5, pady=5)

subtractbtn=ctk.CTkButton(btnFrame, text="  -", anchor="nw", width=75, height=65,text_color="black",fg_color="#37b8b4", font=ctk.CTkFont(size=40))
subtractbtn.grid(row=2, column=3, padx=5, pady=5)

btn1=ctk.CTkButton(btnFrame, text=" 1", anchor="nw", width=75, height=65,text_color="black",fg_color="light blue",command=lambda : addText("1"), font=ctk.CTkFont(size=40))
btn1.grid(row=3, column=0, padx=5, pady=5)

btn2=ctk.CTkButton(btnFrame, text=" 2", anchor="nw", width=75, height=65,text_color="black",fg_color="light blue",command=lambda : addText("2"), font=ctk.CTkFont(size=40))
btn2.grid(row=3, column=1, padx=5, pady=5)

btn3=ctk.CTkButton(btnFrame, text=" 3", anchor="nw", width=75, height=65,text_color="black",fg_color="light blue",command=lambda : addText("3"), font=ctk.CTkFont(size=40))
btn3.grid(row=3, column=2, padx=5, pady=5)

addbtn=ctk.CTkButton(btnFrame, text=" +", anchor="nw", width=75, height=65,text_color="black",fg_color="#37b8b4", font=ctk.CTkFont(size=40))
addbtn.grid(row=3, column=3, padx=5, pady=5)

changesignbtn=ctk.CTkButton(btnFrame, text="+/-", anchor="nw", width=75, height=65,text_color="black",fg_color="light blue", font=ctk.CTkFont(size=40), command=plus_minus)
changesignbtn.grid(row=4, column=0, padx=5, pady=5)

btn0=ctk.CTkButton(btnFrame, text=" 0", anchor="nw", width=75, height=65,text_color="black",fg_color="light blue",command=lambda : addText("0"), font=ctk.CTkFont(size=40))
btn0.grid(row=4, column=1, padx=5, pady=5)

pointbtn=ctk.CTkButton(btnFrame, text="  .", anchor="nw", width=75, height=65,text_color="black",fg_color="light blue",command=lambda : addText("."), font=ctk.CTkFont(size=40))
pointbtn.grid(row=4, column=2, padx=5, pady=5)

equalbtn=ctk.CTkButton(btnFrame, text=" =", anchor="nw", width=75, height=65,text_color="black", fg_color="#37b8b4", font=ctk.CTkFont(size=40))
equalbtn.grid(row=4, column=3, padx=5, pady=5)
app.mainloop()