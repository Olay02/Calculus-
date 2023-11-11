import customtkinter as ctk



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
                        text_color='white', command = lambda: ctk.set_appearance_mode('dark') )
button.pack()

# run
window.mainloop()

