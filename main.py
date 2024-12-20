import tkinter as tk
import calendar
from tkinter import messagebox

class CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calendar App")
        
        self.year_var = tk.IntVar()
        self.month_var = tk.IntVar()
        
        self.create_widgets()
        self.show_calendar()

    def create_widgets(self):
        # Dropdown for selecting the year
        tk.Label(self.root, text="Select Year:").grid(row=0, column=0, padx=10, pady=10)
        year_dropdown = tk.Spinbox(self.root, from_=1900, to=2100, textvariable=self.year_var)
        year_dropdown.grid(row=0, column=1, padx=10, pady=10)
        
        # Dropdown for selecting the month
        tk.Label(self.root, text="Select Month:").grid(row=1, column=0, padx=10, pady=10)
        month_dropdown = tk.Spinbox(self.root, from_=1, to=12, textvariable=self.month_var)
        month_dropdown.grid(row=1, column=1, padx=10, pady=10)

        # Button to show the calendar
        show_button = tk.Button(self.root, text="Show Calendar", command=self.show_calendar)
        show_button.grid(row=2, column=0, columnspan=2, pady=10)
        
        # Frame for displaying the calendar
        self.calendar_frame = tk.Frame(self.root)
        self.calendar_frame.grid(row=3, column=0, columnspan=2)

    def show_calendar(self):
        # Clear the previous calendar
        for widget in self.calendar_frame.winfo_children():
            widget.destroy()

        year = self.year_var.get() if self.year_var.get() != 0 else 2024
        month = self.month_var.get() if self.month_var.get() != 0 else 1

        try:
            month_name = calendar.month_name[month]
            self.root.title(f"Calendar - {month_name} {year}")
            cal = calendar.monthcalendar(year, month)

            # Display the days of the week (Header)
            for col, day in enumerate(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']):
                tk.Label(self.calendar_frame, text=day, width=10, relief="solid").grid(row=0, column=col)

            # Display the calendar days
            for row, week in enumerate(cal, start=1):
                for col, day in enumerate(week):
                    if day != 0:
                        tk.Button(self.calendar_frame, text=str(day), width=10, height=2,
                                  command=lambda day=day: self.on_day_click(day)).grid(row=row, column=col)

        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate calendar: {e}")

    def on_day_click(self, day):
        messagebox.showinfo("Selected Day", f"You selected {day}")
root = tk.Tk()

# Create the CalendarApp
app = CalendarApp(root)

# Start the GUI event loop
root.mainloop()
