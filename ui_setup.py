import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("BMI Calculator")
        self.geometry("500x500")

        self.calculate_button = customtkinter.CTkButton(
            self, text="Calculate BMI", command=self.calculate_bmi
        )

        self.calculate_button2 = customtkinter.CTkButton(
            self, text="Calculate BMI2", command=self.calculate_bmi
        )

app = App()
app.mainloop()
