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

button1 = ctk.CTkButton(window, text= 'a btton', fg_color='blue',
                        text_color='white',border_color= 'black',
                        border_width= 3, command = mode)

button2 = ctk.CTkButton(window, text= 'a btton 1', fg_color='blue',
                        text_color='white')

button3 = ctk.CTkButton(window, text= 'a btton', fg_color='blue',
                         text_color='white')

button4 = ctk.CTkButton(window, text= 'a btton', fg_color='blue',
                        text_color='white')

button5 = ctk.CTkButton(window, text= 'a btton', fg_color='blue',
                        text_color='white')

button6 = ctk.CTkButton(window, text= 'a btton', fg_color='blue',
                        text_color='white')

button7 = ctk.CTkButton(window, text= 'a btton', fg_color='blue',
                        text_color='white')

button8 = ctk.CTkButton(window, text= 'a btton', fg_color='blue',
                        text_color='white')

button9 = ctk.CTkButton(window, text= 'a btton', fg_color='blue',
                        text_color='white')

                        
window.columnconfigure(0, weight= 1)
window.columnconfigure(1, weight= 1)
window.columnconfigure(2, weight= 1)
window.columnconfigure(3, weight= 1)

window.rowconfigure(0, weight= 1)
window.rowconfigure(1, weight= 1)
window.rowconfigure(2, weight= 1)
window.rowconfigure(3, weight= 1)
window.rowconfigure(4, weight= 1)
window.rowconfigure(5, weight= 1)

opt_label.grid(row = 0)
button1.grid(row = 4, column = 0)
button2.grid(row = 4 , column = 1)
button3.grid(row = 4, column = 2)
button4.grid(row = 3, column = 0)
button5.grid(row = 3, column = 1 )


# run
window.mainloop()

