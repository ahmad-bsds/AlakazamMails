import tkinter as tk
from tkinter import ttk
from sendBirthdayWishes import send_wish
from mailSendSystem import send_mail

# -------- User credentials.---------
# user email.
EMAIL = 'Your_email_here'
PASSWORD = 'Your_password_here'

# create the main window.
window = tk.Tk()
# Title.
window.title('Alakazam Messages')
# window icon.
icon = tk.PhotoImage(file='sendWishesButton.png')
window.iconphoto(False, icon)
# create a Notebook widget
notebook = ttk.Notebook(window, height=400, width=760)

# create the tabs
birthday = ttk.Frame(notebook, borderwidth=0)
message = ttk.Frame(notebook, borderwidth=0)

# add tabs to the notebook
notebook.add(birthday, text='Birthday')
notebook.add(message, text='Message')

# create a new style for the notebook tabs
style = ttk.Style()
style.theme_use('default')
style.configure('TNotebook.Tab', background="#F7DB6A")  # other tab color.
style.configure('TFrame', background="#7AA874")  # color of all frame.
style.map("TNotebook.Tab", background=[("selected", "#7AA874")])  # selected tab color.

# add content to the tabs

# Section 1: Birthday:
# Image:
birthday_image = tk.PhotoImage(file='birthdayPic.png')
birthday_image1 = tk.PhotoImage(file='birthdayPic1.png')
birthday_image2 = tk.PhotoImage(file='birthdayPic2.png')
birthday_image3 = tk.PhotoImage(file='birthdayPic3.png')
button_image = tk.PhotoImage(file='sendWishesButton.png')

# left pic.
birthday_canvas = tk.Canvas(birthday, height=350, width=200, bg='#7AA874', highlightthickness=0)
birthday_canvas.create_image(180, 180, image=birthday_image)
birthday_canvas.grid(row=0, rowspan=4)
# right pic.
birthday_canvas1 = tk.Canvas(birthday, height=350, width=200, bg='#7AA874', highlightthickness=0)
birthday_canvas1.create_image(30, 165, image=birthday_image1)
birthday_canvas1.grid(row=0, column=9, rowspan=4, columnspan=8)
# birthday logo at center.
birthday_canvas2 = tk.Canvas(birthday, height=280, width=360, bg='#7AA874', highlightthickness=0)
birthday_canvas2.create_image(180, 145, image=birthday_image2)
birthday_canvas2.grid(row=1, column=1)
# top pic.
birthday_canvas3 = tk.Canvas(birthday, height=50, width=350, bg='#7AA874', highlightthickness=0)
birthday_canvas3.create_image(180, 25, image=birthday_image3)
birthday_canvas3.grid(row=0, column=1)

# Button for send wishes.:

wish_button = ttk.Button(birthday, text='Send Wishes!!', command=lambda: send_wish(EMAIL, PASSWORD))
wish_button.configure(image=button_image)
wish_button.grid(row=3, column=1)

# Section 2: Message
# image:
send_button_image = tk.PhotoImage(file='msgSendButton.png')
msgImage = tk.PhotoImage(file='messageImage.png')
# message body.
message_box = tk.Text(message, width=60, height=10)
message_box.config(bg='#EBB02D', borderwidth='0', font=('Ariel', 10))
message_box.insert('end', 'Type type message here!!')
message_box.grid(row=0, column=1, columnspan=4, padx=(200, 0), pady=(60, 30))
# message subject.
subject_box = tk.Text(message, width=40, height=1)
subject_box.config(bg='#EBB02D', borderwidth='0', font=('Ariel', 10))
subject_box.insert('end', 'Type your subject here!!')
subject_box.grid(row=2, column=1, columnspan=2, pady=(0, 30), padx=(200, 0))
# Receiver mail.
receiver_mail = tk.Text(message, width=40, height=1)
receiver_mail.config(bg='#EBB02D', borderwidth='0', font=('Ariel', 10), )
receiver_mail.insert('end', 'Type receiver mail here!!')
receiver_mail.tk_focusFollowsMouse()
receiver_mail.grid(row=3, column=0, columnspan=3, pady=(0, 30), padx=(200, 0))


# Send button
send_button = ttk.Button(message, text='Send Wishes!!',
                         command=lambda: send_mail(EMAIL, PASSWORD, subject_box.get('1.0', 'end'), message_box.get('1.0', 'end'), receiver_mail.get('1.0', 'end')))
send_button.configure(image=send_button_image)
send_button.grid(row=3, column=4, columnspan=3, rowspan=3)
# pack the notebook widget
notebook.grid(row=1, column=1, columnspan=10, rowspan=10)
# start the event loop
window.mainloop()
