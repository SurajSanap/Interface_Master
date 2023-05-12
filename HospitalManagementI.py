from tkinter import *
import time
import ttkthemes
from tkinter import ttk,messagebox,filedialog
import pymysql
import pandas
#functionality Part

#Play sound***************
import pygame
sound_path = "HospitalM.mp3"
def play_sound(sound_path):
    pygame.mixer.init()
    pygame.mixer.music.load(sound_path)
    pygame.mixer.music.play()
play_sound(sound_path)

#*************************



def iexit():
    result=messagebox.askyesno('Confirm','Do you want to exit?')
    if result:
        root.destroy()
    else:
        pass
#EXPORT -----------------------------------
def export_data():
    url=filedialog.asksaveasfilename(defaultextension='.csv')
    indexing=HospitalTable.get_children()
    newlist=[]
    for index in indexing:
        content=HospitalTable.item(index)
        datalist=content['values']
        newlist.append(datalist)


    table=pandas.DataFrame(newlist,columns=['Id','Name','Mobile','Dieases','Address','Gender','DOB','Added Date','Added Time'])
    table.to_csv(url,index=False)
    messagebox.showinfo('Success','Data is saved succesfully')
#------------------------------------

def toplevel_data(title,button_text,command):
    global idEntry,phoneEntry,nameEntry,DieasesEntry,addressEntry,genderEntry,dobEntry,screen
    screen = Toplevel()
    screen.title(title)
    screen.grab_set()
    screen.resizable(False, False)
    idLabel = Label(screen, text='Id', font=('times new roman', 20, 'bold'))
    idLabel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    idEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    idEntry.grid(row=0, column=1, pady=15, padx=10)

    nameLabel = Label(screen, text='Name', font=('times new roman', 20, 'bold'))
    nameLabel.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    nameEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    nameEntry.grid(row=1, column=1, pady=15, padx=10)

    phoneLabel = Label(screen, text='Phone', font=('times new roman', 20, 'bold'))
    phoneLabel.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    phoneEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    phoneEntry.grid(row=2, column=1, pady=15, padx=10)

    DieasesLabel = Label(screen, text='Dieases', font=('times new roman', 20, 'bold'))
    DieasesLabel.grid(row=3, column=0, padx=30, pady=15, sticky=W)
    DieasesEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    DieasesEntry.grid(row=3, column=1, pady=15, padx=10)

    addressLabel = Label(screen, text='Address', font=('times new roman', 20, 'bold'))
    addressLabel.grid(row=4, column=0, padx=30, pady=15, sticky=W)
    addressEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    addressEntry.grid(row=4, column=1, pady=15, padx=10)

    genderLabel = Label(screen, text='Gender', font=('times new roman', 20, 'bold'))
    genderLabel.grid(row=5, column=0, padx=30, pady=15, sticky=W)
    genderEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    genderEntry.grid(row=5, column=1, pady=15, padx=10)

    dobLabel = Label(screen, text='D.O.B', font=('times new roman', 20, 'bold'))
    dobLabel.grid(row=6, column=0, padx=30, pady=15, sticky=W)
    dobEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    dobEntry.grid(row=6, column=1, pady=15, padx=10)

    Patient_button = ttk.Button(screen, text=button_text, command=command)
    Patient_button.grid(row=7, columnspan=2, pady=15)
    if title=='Update Patient':
        indexing = HospitalTable.focus()

        content = HospitalTable.item(indexing)
        listdata = content['values']
        idEntry.insert(0, listdata[0])
        nameEntry.insert(0, listdata[1])
        phoneEntry.insert(0, listdata[2])
        DieasesEntry.insert(0, listdata[3])
        addressEntry.insert(0, listdata[4])
        genderEntry.insert(0, listdata[5])
        dobEntry.insert(0, listdata[6])


def update_data():
    query='update Patient set name=%s,mobile=%s,Dieases=%s,address=%s,gender=%s,dob=%s,date=%s,time=%s where id=%s'
    mycursor.execute(query,(nameEntry.get(),phoneEntry.get(),DieasesEntry.get(),addressEntry.get(),
                            genderEntry.get(),dobEntry.get(),date,currenttime,idEntry.get()))
    con.commit()
    messagebox.showinfo('Success',f'Id {idEntry.get()} is modified successfully',parent=screen)
    screen.destroy()
    show_Patient()



def show_Patient():
    query = 'select * from Patient'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    HospitalTable.delete(*HospitalTable.get_children())
    for data in fetched_data:
        HospitalTable.insert('', END, values=data)



def delete_Patient():
    indexing=HospitalTable.focus()
    print(indexing)
    content=HospitalTable.item(indexing)
    content_id=content['values'][0]
    query='delete from Patient where id=%s'
    mycursor.execute(query,content_id)
    con.commit()
    messagebox.showinfo('Deleted',f'Id {content_id} is deleted succesfully')
    query='select * from Patient'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    HospitalTable.delete(*HospitalTable.get_children())
    for data in fetched_data:
        HospitalTable.insert('',END,values=data)




def search_data():
    query='select * from Patient where id=%s or name=%s or Dieases=%s or mobile=%s or address=%s or gender=%s or dob=%s'
    mycursor.execute(query,(idEntry.get(),nameEntry.get(),DieasesEntry.get(),phoneEntry.get(),addressEntry.get(),genderEntry.get(),dobEntry.get()))
    HospitalTable.delete(*HospitalTable.get_children())
    fetched_data=mycursor.fetchall()
    for data in fetched_data:
        HospitalTable.insert('',END,values=data)




def add_data():
    if idEntry.get()=='' or nameEntry.get()=='' or phoneEntry.get()=='' or DieasesEntry.get()=='' or addressEntry.get()=='' or genderEntry.get()=='' or dobEntry.get()=='':
        messagebox.showerror('Error','All Feilds are required',parent=screen)

    else:
        try:
            query='insert into Patient values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(query,(idEntry.get(),nameEntry.get(),phoneEntry.get(),DieasesEntry.get(),addressEntry.get(),
                                    genderEntry.get(),dobEntry.get(),date,currenttime))
            con.commit()
            result=messagebox.askyesno('Confirm','Data added successfully. Do you want to clean the form?',parent=screen)
            if result:
                idEntry.delete(0,END)
                nameEntry.delete(0,END)
                phoneEntry.delete(0,END)
                DieasesEntry.delete(0,END)
                addressEntry.delete(0,END)
                genderEntry.delete(0,END)
                dobEntry.delete(0,END)
            else:
                pass
        except:
            messagebox.showerror('Error','Id cannot be repeated',parent=screen)
            return


        query='select *from Patient'
        mycursor.execute(query)
        fetched_data=mycursor.fetchall()
        HospitalTable.delete(*HospitalTable.get_children())
        for data in fetched_data:
            HospitalTable.insert('',END,values=data)


def connect_database():
    def connect():
        global mycursor,con
        try:
            con=pymysql.connect(host='localhost',user='root',password='1234')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error...','Invalid Details',parent=connectWindow)
            return

        try:
            query='create database Hospitalmanagementsystem'
            mycursor.execute(query)
            query='use Hospitalmanagementsystem'
            mycursor.execute(query)
            query='create table Patient(id int not null primary key, name varchar(30),mobile varchar(10),Dieases varchar(30),' \
                  'address varchar(100),gender varchar(20),dob varchar(20),date varchar(50), time varchar(50))'
            mycursor.execute(query)
        except:
            query='use Hospitalmanagementsystem'
            mycursor.execute(query)
        messagebox.showinfo('Success', 'Database Connection is successful', parent=connectWindow)
        connectWindow.destroy()
        addPatientButton.config(state=NORMAL)
        searchPatientButton.config(state=NORMAL)
        updatePatientButton.config(state=NORMAL)
        showPatientButton.config(state=NORMAL)
        exportPatientButton.config(state=NORMAL)
        deletePatientButton.config(state=NORMAL)


    connectWindow=Toplevel()
    connectWindow.grab_set()
    connectWindow.geometry('470x250+730+230')
    connectWindow.title('Database Connection')
    connectWindow.resizable(0,0)

    hostnameLabel=Label(connectWindow,text='Host Name',font=('arial',20,'bold'))
    hostnameLabel.grid(row=0,column=0,padx=20)

    hostEntry=Entry(connectWindow,font=('roman',15,'bold'),bd=2)
    hostEntry.grid(row=0,column=1,padx=40,pady=20)

    usernameLabel = Label(connectWindow, text='User Name', font=('arial', 20, 'bold'))
    usernameLabel.grid(row=1, column=0, padx=20)

    usernameEntry = Entry(connectWindow, font=('roman', 15, 'bold'), bd=2)
    usernameEntry.grid(row=1, column=1, padx=40, pady=20)

    passwordLabel = Label(connectWindow, text='Password', font=('arial', 20, 'bold'))
    passwordLabel.grid(row=2, column=0, padx=20)

    passwordEntry = Entry(connectWindow, font=('roman', 15, 'bold'), bd=2)
    passwordEntry.grid(row=2, column=1, padx=40, pady=20)

    connectButton=ttk.Button(connectWindow,text='CONNECT',command=connect)
    connectButton.grid(row=3,columnspan=2)

count=0
text=''
def slider():
    global text,count
    # if count==len(s):
    #     count=0
    #     text=''
    text=text+s[count]
    sliderLabel.config(text=text)
    count+=1
    sliderLabel.after(90,slider)




def clock():
    global date,currenttime
    date=time.strftime('%d/%m/%Y')
    currenttime=time.strftime('%H:%M:%S')
    datetimeLabel.config(text=f'   Date: {date}\nTime: {currenttime}')
    datetimeLabel.after(1000,clock)



#GUI Part
root=ttkthemes.ThemedTk()

root.get_themes()

root.set_theme('radiance')

root.geometry('1174x680+0+0')
root.resizable(0,0)
root.title('Hospital Management System')

datetimeLabel=Label(root,font=('times new roman',18,'bold'),foreground='DarkRed')
datetimeLabel.place(x=5,y=5)
clock()
s='Hospital Management System' #s[count]=t when count is 1
sliderLabel=Label(root,font=('arial',28,'italic bold'),width=30)
sliderLabel.place(x=200,y=0)
slider()

connectButton=ttk.Button(root,text='Connect database',command=connect_database)
connectButton.place(x=980,y=0)

leftFrame=Frame(root)
leftFrame.place(x=50,y=80,width=300,height=600)

logo_image=PhotoImage(file='hospital pic.png')
logo_Label=Label(leftFrame,image=logo_image)
logo_Label.grid(row=0,column=0)

addPatientButton=ttk.Button(leftFrame,text='Add Patient',width=25,state=DISABLED,command=lambda :toplevel_data('Add Patient','Add',add_data))
addPatientButton.grid(row=1,column=0,pady=20)

searchPatientButton=ttk.Button(leftFrame,text='Search Patient',width=25,state=DISABLED,command=lambda :toplevel_data('Search Patient','Search',search_data))
searchPatientButton.grid(row=2,column=0,pady=20)

deletePatientButton=ttk.Button(leftFrame,text='Delete Patient',width=25,state=DISABLED,command=delete_Patient)
deletePatientButton.grid(row=3,column=0,pady=20)

updatePatientButton=ttk.Button(leftFrame,text='Update Patient',width=25,state=DISABLED,command=lambda :toplevel_data('Update Patient','Update',update_data))
updatePatientButton.grid(row=4,column=0,pady=20)

showPatientButton=ttk.Button(leftFrame,text='Show Patient',width=25,state=DISABLED,command=show_Patient)
showPatientButton.grid(row=5,column=0,pady=20)

exportPatientButton=ttk.Button(leftFrame,text='Export data',width=25,state=DISABLED,command=export_data)
exportPatientButton.grid(row=6,column=0,pady=20)

exitButton=ttk.Button(leftFrame,text='Exit',width=25,command=iexit)
exitButton.grid(row=7,column=0,pady=20)

rightFrame=Frame(root)
rightFrame.place(x=350,y=80,width=820,height=600)

scrollBarX=Scrollbar(rightFrame,orient=HORIZONTAL)
scrollBarY=Scrollbar(rightFrame,orient=VERTICAL)

HospitalTable=ttk.Treeview(rightFrame,columns=('Id','Name','Mobile','Dieases','Address','Gender',
                                 'D.O.B','Added Date','Added Time'),
                          xscrollcommand=scrollBarX.set,yscrollcommand=scrollBarY.set)

scrollBarX.config(command=HospitalTable.xview)
scrollBarY.config(command=HospitalTable.yview)

scrollBarX.pack(side=BOTTOM,fill=X)
scrollBarY.pack(side=RIGHT,fill=Y)

HospitalTable.pack(expand=1,fill=BOTH)

HospitalTable.heading('Id',text='Id')
HospitalTable.heading('Name',text='Name')
HospitalTable.heading('Mobile',text='Mobile No')
HospitalTable.heading('Dieases',text='Dieases')
HospitalTable.heading('Address',text='Address')
HospitalTable.heading('Gender',text='Gender')
HospitalTable.heading('D.O.B',text='D.O.B')
HospitalTable.heading('Added Date',text='Added Date')
HospitalTable.heading('Added Time',text='Added Time')

HospitalTable.column('Id',width=50,anchor=CENTER)
HospitalTable.column('Name',width=200,anchor=CENTER)
HospitalTable.column('Dieases',width=300,anchor=CENTER)
HospitalTable.column('Mobile',width=200,anchor=CENTER)
HospitalTable.column('Address',width=300,anchor=CENTER)
HospitalTable.column('Gender',width=100,anchor=CENTER)
HospitalTable.column('D.O.B',width=200,anchor=CENTER)
HospitalTable.column('Added Date',width=200,anchor=CENTER)
HospitalTable.column('Added Time',width=200,anchor=CENTER)

style=ttk.Style()

style.configure('Treeview', rowheight=40,font=('arial', 12, 'bold'), fieldbackground='khaki', background='wheat',)
style.configure('Treeview.Heading',font=('arial', 14, 'bold'),foreground='DodgerBlue')

HospitalTable.config(show='headings')

root.mainloop()

