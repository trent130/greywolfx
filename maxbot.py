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

# Create labels and entry fields with adjusted font sizes for larger screens using pack
label_font = ('Arial', 12)
entry_font = ('Arial', 12)

# Username
username_frame = tk.Frame(main_frame)
username_frame.pack(anchor='w')
username_label = tk.Label(username_frame, text="Username:", font=label_font)
username_label.pack(side='left')
username_entry = tk.Entry(username_frame, font=entry_font)
username_entry.pack(side='left')

# University Acronyms
acronym_frame = tk.Frame(main_frame)
acronym_frame.pack(anchor='w')
acronym_label = tk.Label(acronym_frame, text="Acronym:", font=label_font)
acronym_label.pack(side='left')
acronym_entry = tk.Entry(acronym_frame, font=entry_font)
acronym_entry.pack(side='left')

# Graduation Year
grad_year_frame = tk.Frame(main_frame)
grad_year_frame.pack(anchor='w')
grad_year_label = tk.Label(grad_year_frame, text="Graduation year:", font=label_font)
grad_year_label.pack(side='left')
grad_year_entry = tk.Entry(grad_year_frame, font=entry_font)
grad_year_entry.pack(side='left')

# Excluded Year
excluded_year_frame = tk.Frame(main_frame)
excluded_year_frame.pack(anchor='w')
excluded_year_label = tk.Label(excluded_year_frame, text="Excluded year:", font=label_font)
excluded_year_label.pack(side='left')
excluded_year_entry = tk.Entry(excluded_year_frame, font=entry_font)
excluded_year_entry.pack(side='left')

# Hashtags
hashtags_frame = tk.Frame(main_frame)
hashtags_frame.pack(anchor='w')
hashtags_label = tk.Label(hashtags_frame, text="Hashtag:", font=label_font)
hashtags_label.pack(side='left')
hashtags_entry = tk.Entry(hashtags_frame, font=entry_font)
hashtags_entry.pack(side='left')

# Maximum Follow Count
max_follow_frame = tk.Frame(main_frame)
max_follow_frame.pack(anchor='w')
max_follow_label = tk.Label(max_follow_frame, text="Maximum follow count:", font=label_font)
max_follow_label.pack(side='left')
max_follow_entry = tk.Entry(max_follow_frame, font=entry_font)
max_follow_entry.pack(side='left')

# Button for following accounts
follow_button = tk.Button(main_frame, text="Follow Accounts", command=follow_accounts, font=label_font, bg="blue", fg="white")
follow_button.pack(pady=20)

root.mainloop()
