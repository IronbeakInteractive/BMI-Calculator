import customtkinter
from bmi_calculator import calculate_bmi

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("BMI Calculator")
        self.geometry("500x500")
        
        self.height_label = customtkinter.CTkLabel(self, text="Enter your height (cm):")
        self.height_label.pack(pady=(20, 5))

        self.height_entry = customtkinter.CTkEntry(self, placeholder_text="Height", width=350)
        self.height_entry.pack(pady=(0, 20))

        self.weight_label = customtkinter.CTkLabel(self, text="Enter your weight (kg):")
        self.weight_label.pack(pady=(0, 5))

        self.weight_entry = customtkinter.CTkEntry(self, placeholder_text="Weight", width=350)
        self.weight_entry.pack(pady=(0, 20))

        self.calc_button = customtkinter.CTkButton(self, text="Calculate Your BMI",  command=lambda: calculate_bmi(self.height_entry, self.weight_entry, self.bmi_label))
        self.calc_button.pack(pady=(0, 20))

        self.bmi_label = customtkinter.CTkLabel(self, text=" ")
        self.bmi_label.pack(pady=(20, 10))

if __name__ == "__main__":
    app = App()
    app.mainloop()
