from tkinter import *
import backend



def view_back():
    s1.delete(0,END)
    for row in backend.viewall():
        s1.insert(END,row)

def search_back():
    s1.delete(0,END)
    for row in backend.search(e1_value.get(),e2_value.get(),e3_value.get(),e4_value.get()):
        s1.insert(END,row)

def add_back():
    s1.delete(0,END)
    backend.add(e1_value.get(),e2_value.get(),e3_value.get(),e4_value.get())
    s1.insert(END,e1_value.get(),e2_value.get(),e3_value.get(),e4_value.get())

def get_selected_row(event):
    try:
        global sel_tuple
        index=s1.curselection()[0]
        sel_tuple=s1.get(index)
        e1.delete(0,END)
        e1.insert(END,sel_tuple[1])
        e2.delete(0,END)
        e2.insert(END,sel_tuple[2])
        e3.delete(0,END)
        e3.insert(END,sel_tuple[3])
        e4.delete(0,END)
        e4.insert(END,sel_tuple[4])
    except IndexError:
        pass
    return sel_tuple

def delete_back():
    tup=get_selected_row(s1)
    backend.delete(tup[0])


def update_back():
    tup=get_selected_row(s1)
    backend.update(tup[0],e1_value.get(),e2_value.get(),e3_value.get(),e4_value.get())    

window = Tk()

window.wm_title("BookStore")

l1 = Label(window, text="Title")
l1.grid(row=0,column=0)

l1 = Label(window, text="Author")
l1.grid(row=0,column=2)

l1 = Label(window, text="Year")
l1.grid(row=1,column=0)

l1 = Label(window, text="ISBN")
l1.grid(row=1,column=2)

e1_value=StringVar()
e1=Entry(window,width=12,textvariable=e1_value)
e1.grid(row=0,column=1)

e2_value=StringVar()
e2=Entry(window,width=12,textvariable=e2_value)
e2.grid(row=0,column=3)

e3_value=StringVar()
e3=Entry(window,width=12,textvariable=e3_value)
e3.grid(row=1,column=1)

e4_value=StringVar()
e4=Entry(window,width=12,textvariable=e4_value)
e4.grid(row=1,column=3)

s1=Listbox(window,height=10,width=35)
s1.grid(row=3,column=0,rowspan=6,columnspan=2)

s1.bind('<<ListBoxSelect>>',get_selected_row)

scroll = Scrollbar(window)
scroll.grid(row=2,column=2,rowspan=6)

s1.configure(yscrollcommand=scroll.set)
scroll.configure(command=s1.yview)

view = Button(window,text="Veiw All",width=20,command=view_back)
view.grid(row=3,column=3)

search = Button(window,text="Search Entry",width=20,command=search_back)
search.grid(row=4,column=3)

add = Button(window,text="Add Entry",width=20,command=add_back)
add.grid(row=5,column=3)

update = Button(window,text="Update",width=20,command=update_back)
update.grid(row=6,column=3)

delete = Button(window,text="Delete",width=20,command=delete_back)
delete.grid(row=7,column=3)

close = Button(window,text="Close",width=20,command=window.destroy)
close.grid(row=8,column=3)

window.mainloop()