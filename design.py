import customtkinter as ctk
import tkinter as tk
# True for light mode
appearence = True

WHITE = "#FFFFFF"
DIGITS_FONT = ("Arial", 24, "bold")

# func to change modes
def  mode():
    global appearence
    if appearence:
        ctk.set_appearance_mode('dark')
        appearence = False
    else:
        ctk.set_appearance_mode('light')
        appearence = True

def on_button_click(value):
    current_text = entry_var.get()
    entry_var.set(current_text + str(value))

class Calculator:

    def __init__(self) -> None:
        self.window = ctk.CTk()
        self.window.title("Calculator")
        self.window.geometry('400x700')
        self.window.resizable(False, False)

        self.total = "0"
        self.current_exp = "0"
        self.display_frame = self.create_display_frame()
        self.total_label, self.curr_label = self.create_display_labels()

        
        self.butt_frame  = self.create_button_frame()
        self.digits = {
            7:(1,1), 8:(1,2), 9:(1,3),
            4:(2,1), 5:(2,2), 6:(2,3),
            1:(3,1), 2:(3,2), 3:(3,3),
            0:(4,2), ".":(4,3) 
        }

        self.create_digit_buttons()


    def run(self):
        self.window.mainloop()


    def create_display_labels(self):
        total_lable = ctk.CTkLabel(self.display_frame, text = self.total, fg_color="#fcfdfb", anchor = "e", padx =24)
        total_lable.pack(expand = True, fill = "both")

        current_label = ctk.CTkLabel(self.display_frame, text = self.current_exp, fg_color="#fcfdfb", anchor ="e", padx= 24)
        current_label.pack(expand = True, fill = "both")

        return total_lable, current_label
    

    def create_display_frame(self):
        display_frame = ctk.CTkFrame(self.window, fg_color = "#8D6F3A", border_color= "#FFCC70", border_width= 2, corner_radius= 70)
        display_frame.pack(expand = True, fill = "both")
        return display_frame
    

    def create_button_frame(self):
        button_frame = ctk.CTkFrame(self.window, fg_color = "#5d7d9a", border_color= "#8f9e8a", border_width= 2)
        button_frame.pack(expand = True, fill = "both")
        return button_frame
    
    
    def create_digit_buttons(self):

        for digit,grid_values in self.digits.items():
            button = ctk.CTkButton(self.butt_frame, text=str(digit), bg_color=WHITE, font = DIGITS_FONT, fg_color="#555555", hover_color= "#333333")
            button.grid(row = grid_values[0], column = grid_values[1])


if __name__ == "__main__":
    calc = Calculator()
    calc.run()