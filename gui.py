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
stxt = scrolledtext.ScrolledText(window, width=150, height=47, bg='black', fg='white', font=("Arial Bold", 7))
# To empty all the content of the scrolled text, we can use :
stxt.delete(1.0, END)
stxt.pack(side=BOTTOM)

# We can add a textBox
txt = Entry(window, width=70)  # can also add the disable attribute here , state='disabled'
txt.pack(side=TOP, pady=10)
# We can set the focus on the textBox automatically !
txt.focus()


def set_text(text):
    txt.delete(0, END)
    txt.insert(0, text)
    return


def choose_project():
    # this is a sample for a file chooser
    dir = filedialog.askdirectory()
    stxt.insert(INSERT, '\n[+] Path selectionned: ' + ''.join(dir))
    stxt.insert(INSERT, '\n[+] Start generating the application')
    try:
        if txt.get() == "my_app_name":
            set_text(dir.split("/")[-1])

        # Then generate the application
        generate_app(dir, "py", txt.get(), stxt, INSERT)
        # We print the message box to the screen
        messagebox.showinfo('Golem status', 'Your application will be generated here : \
                                           ' + dir + '/dist/' + txt.get())
    except: pass


#
# background_image = PhotoImage("./images/bg.jpg")
# background_label = Label(window, image=background_image)
# background_label.place(x=0, y=0, relwidth=1, relheight=1)
#

set_text("my_app_name")

btn = Button(window, text="Choose your project", bg="blue", fg="white", command=choose_project)
# We we specify the position of the widget
btn.pack(side=TOP, pady=5)

# To insert content, we can use INSERT
stxt.insert(INSERT, '[+] ---------------')
stxt.insert(INSERT, '\n[+] Collecting datas...')
stxt.insert(INSERT, '\n[+] Golem started successfully !')

window.mainloop()
