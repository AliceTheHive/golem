import time
from tkinter import *
from tkinter import scrolledtext
from tkinter import filedialog
# For messageBox
from tkinter import messagebox
from utils import *

window = Tk()
# We set our title
window.title("Golem 0.1")

frame = Frame(window)
frame.pack()

# We can set the size of the window
window.geometry('500x550')

# We can add a scrolledTextWidget
stxt = scrolledtext.ScrolledText(window, width=150, height=50, bg='black', fg='white', font=("Arial Bold", 7))
# To empty all the content of the scrolled text, we can use :
stxt.delete(1.0, END)
stxt.pack(side=BOTTOM)


def choose_project():
    # this is a sample for a file chooser
    dir = filedialog.askdirectory()
    stxt.insert(INSERT, '\n[+] Path selectionned: ' + ''.join(dir))

    stxt.insert(INSERT, '\n[+] Start generating the application')
    try:
        # Then generate the application
        generate_app(dir, "py", dir.split("/")[-1], stxt, INSERT)
        # We print the message box to the screen
        messagebox.showinfo('Golem status', 'Your application have been generated successfully here : \
                                           ' + dir + '/dist/' + dir.split("/")[-1])
    except: pass


#
# background_image = PhotoImage("./images/bg.jpg")
# background_label = Label(window, image=background_image)
# background_label.place(x=0, y=0, relwidth=1, relheight=1)
#

btn = Button(window, text="Choose your project", bg="blue", fg="white", command=choose_project)
# We we specify the position of the widget
btn.pack(side=TOP, pady=30)

# To insert content, we can use INSERT
stxt.insert(INSERT, '[+] ---------------')
stxt.insert(INSERT, '\n[+] Collecting datas...')
stxt.insert(INSERT, '\n[+] Golem started successfully !')

window.mainloop()
