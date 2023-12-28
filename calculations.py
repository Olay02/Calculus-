

class Calc():

    def __init__(self, calculator = None) -> None:
        from design import Calculator
        self.calc = calculator if calculator else Calculator()

    def update_total_label(self):
        self.calc.total_label.configure(text = self.calc.total)
        

    def update_curr_label(self):
        self.calc.curr_label.configure(text = self.calc.current_exp)

    def clear(self):
        self.calc.current_exp = ""
        self.calc.total = ""
        self.update_curr_label()
        self.update_total_label()


    def add_to_label(self, value):

        if self.calc.current_exp == "0":
            self.calc.current_exp = str(value)
            self.calc.total += str(value)


        else:

            self.calc.current_exp += str(value)
            self.calc.total += str(value)
        self.update_curr_label()
        self.update_total_label()


    def append_operator(self, operator):
        #self.current_exp += operator
        try:
            last_character = str(self.calc.total[-1])
            if last_character.isdigit():
                self.calc.total += operator
                self.calc.current_exp = ""
                self.update_curr_label()
                self.update_total_label()
        except:
            pass

    def evaulate(self):
        try:

            self.calc.current_exp = str(eval(self.calc.total))
            self.calc.total = ""

            self.update_curr_label()
            self.update_total_label()
        except:
            pass


if __name__ == "__main__":
    obj = Calc()