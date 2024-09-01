import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("BMI Calculator")
        self.geometry("500x500")

app = App()
app.mainloop()