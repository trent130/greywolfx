import tkinter as tk
from instabot import Bot
import time
import re

def follow_accounts():
    # The function to handle following accounts
    pass

root = tk.Tk()
root.title("Instagram Bot")

# Create and configure the frame with increased padding for larger screens
main_frame = tk.Frame(root, padx=40, pady=40)
main_frame.pack(fill='both', expand=True)  # Adjusting to fill and expand

# Create a title label to use additional space
title_label = tk.Label(main_frame, text="Instagram Bot", font=('Arial', 18, 'bold'))
title_label.pack()

# Create labels and entry fields with adjusted font sizes for larger screens
label_font = ('Arial', 12)
entry_font = ('Arial', 12)

# Username
username_label = tk.Label(main_frame, text="Username:", font=label_font)
username_label.pack(anchor='w')
username_entry = tk.Entry(main_frame, font=entry_font)
username_entry.pack()

# University Acronyms
university_acronym_label = tk.Label(main_frame, text="Acronym:", font=label_font)
university_acronym_label.grid(row=1, column=0, sticky='w')
university_acronym_entry = tk.Entry(main_frame, font=entry_font)
university_acronym_entry.grid(row=1, column=1)

# Graduation Year
grad_year_label = tk.Label(main_frame, text="Graduation year:", font=label_font)
grad_year_label.grid(row=2, column=0, sticky='w')
grad_year_entry = tk.Entry(main_frame, font=entry_font)
grad_year_entry.grid(row=2, column=1)

# Excluded Year
excluded_year_label = tk.Label(main_frame, text="Excluded year:", font=label_font)
excluded_year_label.grid(row=3, column=0, sticky='w')
excluded_year_entry = tk.Entry(main_frame, font=entry_font)
excluded_year_entry.grid(row=3, column=1)

# Hashtags
hashtags_label = tk.Label(main_frame, text="Hashtag:", font=label_font)
hashtags_label.grid(row=4, column=0, sticky='w')
hashtags_entry = tk.Entry(main_frame, font=entry_font)
hashtags_entry.grid(row=4, column=1)

# Maximum Follow Count
max_follow_label = tk.Label(main_frame, text="Maximum follow count:", font=label_font)
max_follow_label.grid(row=5, column=0, sticky='w')
max_follow_entry = tk.Entry(main_frame, font=entry_font)
max_follow_entry.grid(row=5, column=1)

# Button for following accounts
follow_button = tk.Button(main_frame, text="Follow Accounts", command=follow_accounts, font=label_font, bg="blue", fg="white")
follow_button.pack(pady=20)

root.mainloop()
