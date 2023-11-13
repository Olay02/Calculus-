import customtkinter as ctk

# True for light mode
appearence = True

# func to change modes
def  mode():
    global appearence
    if appearence:
        ctk.set_appearance_mode('dark')
        appearence = False
    else:
        ctk.set_appearance_mode('light')
        appearence = True



#create window
window = ctk.CTk()
window.title("Calculator")
window.geometry('400x700')
window.resizable(False, False)

# widgets
opt_label = ctk.CTkLabel(window, text = 'a ctk label jit', 
                         fg_color=('white', 'black'), text_color= ('black', 'white'),
                         corner_radius= 10,)
#opt_label.pack()

button1 = ctk.CTkButton(window, text= 'a btton', fg_color='blue',
                        text_color='white', command = mode)
button1.grid(row=1, column =1)

button2 = ctk.CTkButton(window, text= 'a btton 1', fg_color='blue',
                        text_color='white')
button2.grid(row=1, column =2)


button3 = ctk.CTkButton(window, text= 'a btton', fg_color='blue',
                        text_color='white')
button3.grid(row=1, column =3)


button4 = ctk.CTkButton(window, text= 'a btton', fg_color='blue',
                        text_color='white')
button4.grid(row=1, column =4)


# run
window.mainloop()

