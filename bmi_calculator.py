
def calculate_bmi(height_entry, weight_entry, bmi_label):
    height_entry = float(height_entry.get())
    weight_entry = float(weight_entry.get())

    height_meters = height_entry / 100
    bmi_value = (weight_entry / (height_meters ** height_meters))

    bmi_label.configure(text=f"{bmi_value:.1f}")