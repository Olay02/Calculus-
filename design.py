import customtkinter as ctk

appearence = True

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

# widgets
opt_label = ctk.CTkLabel(window, text = 'a ctk label jit', 
                         fg_color=('white', 'black'), text_color= ('black', 'white'),
                         corner_radius= 10,)
opt_label.pack()

button = ctk.CTkButton(window, text= 'a btton', fg_color='blue',
                        text_color='white', command = mode)
button.pack()

# run
window.mainloop()

