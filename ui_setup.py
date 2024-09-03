import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("BMI Calculator")
        self.geometry("500x500")
        
        # Create and pack a CTkLabel and CTkEntry for height
        self.height_label = customtkinter.CTkLabel(self, text="Enter your height (cm):")
        self.height_label.pack(pady=(20, 5))  # Add some padding

        self.height_entry = customtkinter.CTkEntry(self, placeholder_text="Height", width=350)
        self.height_entry.pack(pady=(0, 20))  # Add some padding

        # Create and pack a CTkLabel and CTkEntry for weight
        self.weight_label = customtkinter.CTkLabel(self, text="Enter your weight (kg):")
        self.weight_label.pack(pady=(0, 5))  # Add some padding

        self.weight_entry = customtkinter.CTkEntry(self, placeholder_text="Weight", width=350)
        self.weight_entry.pack(pady=(0, 20))  # Add some padding

        def calculate_bmi():
            print("Your BMI is:")

        self.calc_button = customtkinter.CTkButton(self, text="Calculate Your BMI", command=calculate_bmi())
        self.calc_button.pack(pady=(0, 20))

app = App()
app.mainloop()
