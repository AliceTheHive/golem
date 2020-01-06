import time
from tkinter import *
from tkinter import scrolledtext
from tkinter import filedialog
from utils import *
from sys import exit

window = Tk()
# We set our title
window.title("Golem 0.1")

frame = Frame(window)
frame.pack()

# We can set the size of the window
window.geometry('600x400')

# We can add a scrolledTextWidget
stxt = scrolledtext.ScrolledText(window, width=150, height=20, bg='black', fg='white')
# To empty all the content of the scrolled text, we can use :
stxt.delete(1.0, END)
stxt.pack(side=BOTTOM)


def choose_project():
    # this is a sample for a file chooser
    dir = filedialog.askdirectory()
    stxt.insert(INSERT, '\n[+] Path selectionned: ' + dir)

    stxt.insert(INSERT, '\n[+] Start generating the application')
    # Then generate the application
    generate_app(dir, "py", stxt, INSERT)


btn = Button(window, text="Choose your project", bg="blue", fg="white", command=choose_project)
# We we specify the position of the widget
btn.pack(side=TOP, pady=50)

# To insert content, we can use INSERT
stxt.insert(INSERT, '[+] ---------------')
stxt.insert(INSERT, '\n[+] Collecting datas...')
stxt.insert(INSERT, '\n[+] Golem started successfully !')

window.mainloop()
