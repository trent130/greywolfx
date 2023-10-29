import tkinter as tk
from instabot import Bot
import time
import re

def follow_accounts():
    username = username_entry.get()
    password = password_entry.get()
    university_acronyms = acronyms_entry.get().split(',')
    grad_year = grad_year_entry.get()
    excluded_grad_year = excluded_grad_year_entry.get()
    hashtag_values = hashtags_entry.get().split(',')
    max_follow_accounts = int(max_follow_entry.get())

    bot = Bot()
    bot.login(username=username, password=password)

    # Rest of your follow_filtered_accounts function goes here...
    # Follow accounts based on provided user inputs

root = tk.Tk()
root.title("Instagram Bot")

# Create and configure the frame
main_frame = tk.Frame(root, padx=20, pady=20)
main_frame.pack()

# Create labels and entry fields
label_font = ('Arial', 10)
entry_font = ('Arial', 10)

username_label = tk.Label(main_frame, text="Username:", font=label_font)
username_label.grid(row=0, column=0, sticky='w')
username_entry = tk.Entry(main_frame, font=entry_font)
username_entry.grid(row=0, column=1)

# Create other entry fields and labels for Password, University Acronyms, Graduation Year, Excluded Year, Hashtags, and Max Follow Count

follow_button = tk.Button(main_frame, text="Follow Accounts", command=follow_accounts, font=label_font, bg="blue", fg="white")
follow_button.grid(row=7, columnspan=2, pady=10)

root.mainloop()
