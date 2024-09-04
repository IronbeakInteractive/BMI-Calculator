
def calculate_bmi(height_entry, weight_entry, bmi_label):
    try:
        height_entry = float(height_entry.get())
        weight_entry = float(weight_entry.get())

        height_meters = height_entry / 100
        bmi_value = (weight_entry / (height_meters ** 2))

        bmi_label.configure(text=f"Your BMI is: {bmi_value:.1f}")
    except ValueError:
        bmi_label.configure(text="Please enter valid values!")