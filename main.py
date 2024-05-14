from tkinter import *

#entry , #label , button
#km to miles = /1.609

window = Tk()
window.minsize(width= 400,height=50)
window.title("km to miles")
window.config(padx=20,pady=20)


def click_button():
    km_value = float(ent.get())
    lbm["text"] = round(km_value / 1.609 , 2)


#entry
ent = Entry(width=16)
ent.insert(END,string = "0")
ent.grid(column= 1, row=0)



#label0
lb = Label(text="is equal to")
lb.grid(column=0, row=1)

#label1
lbm = Label(text=0)
lbm.grid(column=1,row=1)

#label2
lb2 = Label(text="Km")
lb2.grid(column=2,row=0)

#label3
lb3 = Label(text="Miles")
lb3.grid(column=2,row=1)

#button
calculate = Button(text="Calculate",command=click_button)
calculate.grid(column=1,row=2)








window.mainloop()