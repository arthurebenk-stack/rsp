from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Reading Schedule Planner")
root.geometry("500x450")
root.config(bg="lightgreen")

def calculate_schedule():
    try:
        total_pages = int(page_entry.get())
        pages_per_day = int(daily_entry.get())

        if pages_per_day <= 0:
            messagebox.showerror("Error", "Daily pages must be greater than 0!")
            return

        total_days = total_pages // pages_per_day
        leftover_pages = total_pages % pages_per_day

        if leftover_pages > 0:
            actual_days = total_days + 1
        else:
            actual_days = total_days

        weeks = actual_days // 7
        remaining_days = actual_days % 7

        result.config(
            text = f"Total Time Needed:\n\n"
                   f"📅 Weeks: {weeks}\n"
                   f"📆 Extra Days: {remaining_days}\n"
                   f"📖 Total Days: {actual_days}\n\n"
                   f"💡 Note: On the very last day,\n"
                   f"you only need to read {leftover_pages if leftover_pages > 0 else pages_per_day} pages!"
        )
    except ValueError:
        messagebox.showerror("Error", "Please enter valid whole numbers!")

Label(root, text="Reading Schedule Planner",
      font=("Arial", 20, "bold"), bg="darkgreen", fg="white").pack(fill=X, pady=10)

Label(root, text="Total Pages in Book:", bg="lightgreen", font=("Arial", 12)).pack(pady=5)
page_entry = Entry(root, font=("Arial", 12))
page_entry.pack()

Label(root, text="Pages to Read Per Day:", bg="lightgreen", font=("Arial", 12)).pack(pady=5)
daily_entry = Entry(root, font=("Arial", 12))
daily_entry.pack()

Button(root, text="Generate Schedule", command=calculate_schedule,
       bg="forestgreen", fg="white", font=("Arial", 12, "bold")).pack(pady=15)

result = Label(root, text="Enter details and click generate!",
                bg="lightgreen", font=("Arial", 13), justify=LEFT)
result.pack(pady=10)

root.mainloop()
