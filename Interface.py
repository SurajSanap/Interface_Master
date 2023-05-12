from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk
import subprocess
#+++++++++++++++++
import pygame
sound_path = "DigitalSysStart4.mp3"
def play_sound(sound_path):
    pygame.mixer.init()
    pygame.mixer.music.load(sound_path)
    pygame.mixer.music.play()
play_sound(sound_path)
#++++++++++++++++++

def Interface():
    if usernameEntry.get() == '' or passwordEntry.get() == '':
        messagebox.showerror('Error', 'Fields cannot be empty')
    elif usernameEntry.get() == 'Vehicle' and passwordEntry.get() == '1234':
        messagebox.showinfo('Welcome', 'Vehicle Management Selected')
    elif usernameEntry.get() == 'Student' and passwordEntry.get() == '1234':
        messagebox.showinfo('Welcome', 'Student Management Selected')
        subprocess.Popen(['python', 'StudentManagementI.py'])  # Open StudentManagementI.py
    elif usernameEntry.get() == 'Hospital' and passwordEntry.get() == '1234':
        messagebox.showinfo('Welcome', 'Hospital Management Selected')
        subprocess.Popen(['python', 'HospitalManagementI.py'])
    else:
        messagebox.showerror('Error', 'Please enter correct credentials')


window = Tk()
window.geometry('1280x650+0+0')
window.resizable(False, False)

backgroundImage = ImageTk.PhotoImage(file='bg.jpg')

bgLabel = Label(window, image=backgroundImage)
bgLabel.place(x=0, y=0)

loginFrame = Frame(window, bg='white', bd=5)
loginFrame.place(relx=0.5, rely=0.5, anchor=CENTER)

logoImage = PhotoImage(file='InterfaceIcon.png')

logoLabel = Label(loginFrame, image=logoImage)
logoLabel.grid(row=0, column=0, columnspan=2, pady=10)

usernameImage = PhotoImage(file='ini.png')
usernameLabel = Label(loginFrame, image=usernameImage, text='Choose Interface', compound=LEFT,
                      font=('times new roman', 20, 'bold'), bg='white')
usernameLabel.grid(row=1, column=0, pady=10, padx=20)

# Declare usernameEntry globally
global usernameEntry

# Create a style object
style = ttk.Style()
# Configure the style for the combobox
style.configure('TCombobox', borderwidth=5, foreground='royalblue')

usernameEntry = ttk.Combobox(loginFrame, font=('times new roman', 20, 'bold'), foreground='royalblue')
usernameEntry.grid(row=1, column=1, pady=10, padx=20)

passwordImage = PhotoImage(file='password.png')
passwordLabel = Label(loginFrame, image=passwordImage, text='Password', compound=LEFT,
                      font=('times new roman', 20, 'bold'), bg='white')
passwordLabel.grid(row=2, column=0, pady=10, padx=20)

passwordEntry = Entry(loginFrame, font=('times new roman', 20, 'bold'), bd=5, fg='blue')
passwordEntry.grid(row=2, column=1, pady=10, padx=20)

loginButton = Button(loginFrame, text='Interface', font=('times new roman', 14, 'bold'), width=25,
                     fg='white', bg='blue', activebackground='yellow',
                     activeforeground='white', cursor='hand2', command=Interface)
loginButton.grid(row=3, column=1, pady=10)

Options = ['Student', 'Hospital', 'Vehicle','Agriculture']
usernameLabel['text'] = 'Choose Interface: '
usernameEntry['values'] = Options
usernameEntry.current(0)

window.mainloop()
