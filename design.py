import customtkinter as ctk
from PIL import Image
from calculations import Calc

# True for light mode
appearence = True

WHITE = "#FFFFFF"
BLACK = "#111111"
DIGITS_FONT = ("Arial", 24, "bold")
HOVER_BUTTON = "#333333"
FG_COLOR = "#6d6acb"

# func to change modes
"""def  mode():
    global appearence
    if appearence:
        ctk.set_appearance_mode('dark')
        appearence = False
    else:
        ctk.set_appearance_mode('light')
        appearence = True

def on_button_click(value):
    current_text = entry_var.get()
    entry_var.set(current_text + str(value))"""

class Calculator:

    def __init__(self) -> None:
        self.window = ctk.CTk()
        self.window.title("Calculator")
        self.window.geometry('400x700')
        self.window.resizable(False, False)

        self.obj = Calc(calculator=self)

        self.total = ""
        self.current_exp = "0"
        self.display_frame = self.create_display_frame()
        self.total_label, self.curr_label = self.create_display_labels()

        
        self.butt_frame  = self.create_button_frame()

        for x in range(0,5):
            self.butt_frame.rowconfigure(x, weight = 1)
            self.butt_frame.columnconfigure(x, weight = 1)

        self.digits = {
            7:(1,1), 8:(1,2), 9:(1,3),
            4:(2,1), 5:(2,2), 6:(2,3),
            1:(3,1), 2:(3,2), 3:(3,3),
            0:(4,1), ".":(4,3), "%":(0,3)
        }
    
        self.create_clear_button()
        self.create_operations_buttons()
        self.create_digit_buttons()



    def run(self):
        self.window.mainloop()


    def create_display_labels(self):
        total_lable = ctk.CTkLabel(self.display_frame, text = self.total, font = DIGITS_FONT, fg_color="#d4d4d4", anchor = "e", padx =24)
        total_lable.pack(expand = True, fill = "both")

        current_label = ctk.CTkLabel(self.display_frame, text = self.current_exp,font = DIGITS_FONT, fg_color="#d4d4d4", anchor ="e", padx= 24)
        current_label.pack(expand = True, fill = "both")

        return total_lable, current_label 
    

    def create_display_frame(self):
        display_frame = ctk.CTkFrame(self.window, fg_color = "#7c7675", border_color= "#FFCC70", border_width= 2, corner_radius= 70)
        display_frame.pack(expand = True, fill = "both")
        return display_frame
    

    def create_button_frame(self):
        button_frame = ctk.CTkFrame(self.window, fg_color = "#5d7d9a", border_color= "#8f9e8a", border_width= 2)
        button_frame.pack(expand = True, fill = "both")
        return button_frame
    
    
    def create_digit_buttons(self):

        for digit,grid_values in self.digits.items():
            button = ctk.CTkButton(self.butt_frame, text=str(digit), bg_color=BLACK, font = DIGITS_FONT, fg_color=FG_COLOR,
                                    hover_color= HOVER_BUTTON, border_width=0, command = lambda x = digit: self.obj.add_to_label(x))
            
            
            if digit == 0:
                button.grid(row = 4, column = 1, columnspan = 2, sticky = ctk.NSEW)
            else:
                button.grid(row = grid_values[0], column = grid_values[1], sticky = ctk.NSEW)
        
        


    

    def create_clear_button(self):

        clear_button = ctk.CTkButton(self.butt_frame, text="AC", bg_color=BLACK, font = DIGITS_FONT, fg_color=FG_COLOR,
                                    hover_color= HOVER_BUTTON, border_width=0, command = lambda: self.obj.clear())
        
        clear_button.grid(row = 0, column = 1, sticky = ctk.NSEW)


    def create_operations_buttons(self):
        
        # Import Images from Imgs folder
        add_img = ctk.CTkImage(light_image=Image.open("imgs/add_symbol.png"), dark_image=Image.open("imgs/add_symbol.png"))
        sub_img = ctk.CTkImage(light_image=Image.open("imgs/sub_symbol.png"), dark_image=Image.open("imgs/sub_symbol.png"))
        divi_img = ctk.CTkImage(light_image =Image.open("imgs/division_symbol.png"), dark_image=Image.open("imgs/division_symbol.png"))
        mult_img = ctk.CTkImage(light_image=Image.open("imgs/mult_symbol.png"), dark_image=Image.open("imgs/mult_symbol.png"))
        plsmin_img = ctk.CTkImage(light_image=Image.open("imgs/plus-minus.png"), dark_image=Image.open("imgs/plus-minus.png"))
        equal_img = ctk.CTkImage(light_image=Image.open("imgs/equal_symbol.png"), dark_image=Image.open("imgs/equal_symbol.png"))

        
        # defined operators button and their fuctions
        add_button = ctk.CTkButton(self.butt_frame, text="", image = add_img, border_width=0, hover_color= HOVER_BUTTON, fg_color=FG_COLOR,  bg_color=BLACK, command = lambda: self.obj.append_operator("+"))
        sub_button = ctk.CTkButton(self.butt_frame, text="", image = sub_img, border_width=0, hover_color=HOVER_BUTTON, fg_color=FG_COLOR, bg_color=BLACK, command = lambda: self.obj.append_operator("-"))
        divi_button = ctk.CTkButton(self.butt_frame, text="", image = divi_img, border_width=0, hover_color= HOVER_BUTTON, fg_color=FG_COLOR, bg_color=BLACK, command = lambda: self.obj.append_operator("/"))
        mult_button = ctk.CTkButton(self.butt_frame, text="", image = mult_img, border_width=0, hover_color= HOVER_BUTTON, fg_color=FG_COLOR, bg_color=BLACK, command = lambda: self.obj.append_operator("*"))
        plsmin_button = ctk.CTkButton(self.butt_frame, text="+/-", image = plsmin_img, border_width=0, hover_color= HOVER_BUTTON, fg_color=FG_COLOR, bg_color=BLACK )
        equal_button = ctk.CTkButton(self.butt_frame, text="", image = equal_img, border_width=0, hover_color= HOVER_BUTTON, fg_color=FG_COLOR, bg_color=BLACK, command = lambda: self.obj.evaulate())


        # Map buttons onto Button Frame
        plsmin_button.grid(row = 0, column = 2, sticky = ctk.NSEW)
        divi_button.grid(row= 0, column = 4, sticky = ctk.NSEW)
        mult_button.grid(row= 1, column = 4, sticky = ctk.NSEW)
        sub_button.grid(row= 2, column = 4, sticky = ctk.NSEW)
        add_button.grid(row= 3, column = 4, sticky = ctk.NSEW)
        equal_button.grid(row= 4, column = 4, sticky = ctk.NSEW)




if __name__ == "__main__":
    obj = Calculator()
    obj.run()


