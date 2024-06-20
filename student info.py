import mytkinter as tk

def submit():
    name = name_entry.get()
    roll_no = roll_entry.get()
    units_selected = [unit1_var.get(), unit2_var.get(), unit3_var.get(), unit4_var.get(), unit5_var.get()]
    print("Name:", name)
    print("Roll No:", roll_no)
    print("Units selected:", units_selected)

# Create the main Tkinter window
window = tk.Tk()
window.title("Student Information System")


# Create labels and entry widgets for Name and Roll No
name_label = tk.Label(window, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=5)

name_entry = tk.Entry(window)
name_entry.grid(row=0, column=1, padx=10, pady=5)

roll_label = tk.Label(window, text="Roll No:")
roll_label.grid(row=1, column=0, padx=10, pady=5)

roll_entry = tk.Entry(window)
roll_entry.grid(row=1, column=1, padx=10, pady=5)

# Create checkboxes for units 1 to 5
unit1_var = tk.BooleanVar()
unit1_checkbox = tk.Checkbutton(window, text="Unit 1", variable=unit1_var)
unit1_checkbox.grid(row=2, column=0, padx=10, pady=5)

unit2_var = tk.BooleanVar()
unit2_checkbox = tk.Checkbutton(window, text="Unit 2", variable=unit2_var)
unit2_checkbox.grid(row=3, column=0, padx=10, pady=5)

unit3_var = tk.BooleanVar()
unit3_checkbox = tk.Checkbutton(window, text="Unit 3", variable=unit3_var)
unit3_checkbox.grid(row=4, column=0, padx=10, pady=5)

unit4_var = tk.BooleanVar()
unit4_checkbox = tk.Checkbutton(window, text="Unit 4", variable=unit4_var)
unit4_checkbox.grid(row=5, column=0, padx=10, pady=5)

unit5_var = tk.BooleanVar()
unit5_checkbox = tk.Checkbutton(window, text="Unit 5", variable=unit5_var)
unit5_checkbox.grid(row=6, column=0, padx=10, pady=5)

# Create a button to submit the data
submit_button = tk.Button(window, text="Submit", command=submit)
submit_button.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

# Run the Tkinter event loop
window.mainloop()