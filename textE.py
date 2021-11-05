from tkinter import *
import datetime,sys,time
import webbrowser
import os
from calendar import *
from tkinter.messagebox import *
from tkinter.filedialog import askopenfilename,asksaveasfilename
from tkinter.colorchooser import askcolor
#================================================================
# Actualizarea codului pe github
#================================================================
def push():
    os.system("./gitpush.sh")
# ===============================================================
#
#================================================================
def line():
    lin="_"*60
    text.insert(INSERT,lin)
def ti():
    tim = time.localtime()
    text.insert(INSERT, tim)
def date():
    data=datetime.date.today()
    text.insert(INSERT,data)
def normal():
    text.config(font=("Segio UI",20))
def bold():
    text.config(font=('Segio UI',20,'bold'))
def underline():
    text.config(font=('Segio UI',20,'underline'))
def italic():
    text.config(font=('Segio UI',20,'italic'))
def font():
    (triple,color)=askcolor()
    if color:
        text.config(foreground=color)
def kill():
    text.destroy()
    sys.exit()
def select_all(event=None):
    text.tag_add('sel', '1.0', 'end')
    return "break"
def ope():
    text.delete(1.0,END)
    file=askopenfilename(initialdir="/",title="select file",filetype=(('executables','*.exe'),('all files','*.*'),('python files','*.py')))
    print(file)
    file=open(file,"r")
    if file!='':
        txt=file.read()
        text.insert(INSERT,txt)
    elif file[-2:] in ('py'):
    	txt=file.read()
    	text.insert(INSERT,txt)

    else:
        pass
def save():
    filename=asksaveasfilename(initialdir='/',title='save as',filetype=(('c file','*.c,*.c++'),('python file','.py')))
    if filename:
        alltext=text.get(1.0,END)
        with open(filename,'w') as f:
            f.write(alltext)
def copy():
    text.clipboard_clear()
    text.clipboard_append(text.selection_get())
def paste():
    try:
        teext=text.selection_get(selection='CLIPBOARD')
        text.insert(INSERT,teext)
    except:
        showerror('ERROR',"Your can't paste something ")
def clear():
    sel=text.get(SEL_FIRST,SEL_LAST)
    text.delete(SEL_FIRST,SEL_LAST)
def clearall():
    text.delete(1.0,END)
def background():
    (triple,color)=askcolor()
    if color:
        text.config(background=color)
def about():
    ad=Toplevel(root)
    txt="programmer:Tomdieu ivan\n Realised by Navi TOM (c)copyright 2020\n www.pycharm.org"
    la=Label(ad,text=txt,foreground='blue')
    la.pack()
def web():
    webbrowser.open('http://www.pycharm.org')
root=Tk()
n=''
img=PhotoImage(file='logo.png')
root.iconphoto(False,img)
root.title('NAVI EDITOR')
menu=Menu(root)
filemenu=Menu(root,tearoff=0)
root.config(menu=menu)
menu.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="open",command=ope)
filemenu.add_command(label="save",command=save)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=kill)
modmenu=Menu(root,tearoff=0)
menu.add_cascade(label="Modification",menu=modmenu)
modmenu.add_command(label='copy',command=copy)
modmenu.add_command(label='paste',command=paste)
modmenu.add_separator()
modmenu.add_command(label="clear",command=clear)
modmenu.add_command(label="clearall",command=clearall)
insmenu=Menu(root,tearoff=0)
menu.add_cascade(label="date and line",menu=insmenu)
insmenu.add_command(label="Date",command=date)
insmenu.add_command(label="line",command=line)
insmenu.add_command(label="time",command=ti)
formatmenu=Menu(root,tearoff=0)
menu.add_cascade(label='Formating',menu=formatmenu)
formatmenu.add_cascade(label="color",command=font)
formatmenu.add_separator()
formatmenu.add_radiobutton(label='Normal',command=normal)
formatmenu.add_radiobutton(label='bold',command=bold)
formatmenu.add_radiobutton(label='underline',command=underline)
formatmenu.add_radiobutton(label="italic",command=italic)
persomenu=Menu(root,tearoff=0)
menu.add_cascade(label="personalise",menu=persomenu)
persomenu.add_command(label='background',command=background)
helpmenu=Menu(root,tearoff=0)
menu.add_cascade(label='?',menu=helpmenu)
helpmenu.add_command(label='about',command=about)
helpmenu.add_command(label="Github push", command=push)
helpmenu.add_command(label='website',command=web)
E=Entry(root)
E.pack()
E.focus_get()
def save1():
    global n
    n=E.get()
    if n=='':
        showinfo('Error','Invalid Name')
    else:
        with open(n,'w') as f:
            f.write(text.get(1.0,END))
    
Button(root,text='Save text',command=save1).pack()
text=Text(root,height=40,width=100,font=('Arial',12))
scroll=Scrollbar(root,command=text.yview)
text.config(yscrollcommand=scroll.set)
scroll.pack(side=RIGHT,fill=Y)
m=Menu(root,tearoff=0,bd=5)
m.add_command(label='cut')
m.add_command(label='copy',command=copy)
m.add_command(label='paste',command=paste)
m.add_command(label='reload')
m.add_separator()
m.add_command(label='rename')
m.add_command(label='Select All', underline=7, accelerator='Ctrl+A', command=select_all)
def do_popup(event):
    try:
        m.tk_popup(event.x_root,event.y_root)
    finally:
        m.grab_release()
text.bind("<Button-3>",do_popup)
text.bind('<Control-A>', select_all)
text.bind('<Control-a>', select_all)
text.pack()
root.resizable(0,0)
root.mainloop()
