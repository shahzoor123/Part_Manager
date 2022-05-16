from tkinter import *

app = Tk()

part_text = StringVar()
part_label = Label(app, text='Part Name', font=('bold', 12), pady=20)
part_label.grid(row=0, column=0 , sticky=W)
part_entry = Entry(app, textvariable=part_text)
part_entry.grid(row=0, column=1)

customer_text = StringVar()
customer_label = Label(app, text='Customer', font=('bold', 12), pady=20)
customer_label.grid(row=0, column=0 , sticky=W)
customer_entry = Entry(app, textvariable=customer_text)
customer_entry.grid(row=0, column=1)

part_text = StringVar()
part_label = Label(app, text='Part Name', font=('bold', 12), pady=20)
part_label.grid(row=0, column=0 , sticky=W)
part_entry = Entry(app, textvariable=part_text)
part_entry.grid(row=0, column=1)

part_text = StringVar()
part_label = Label(app, text='Part Name', font=('bold', 12), pady=20)
part_label.grid(row=0, column=0 , sticky=W)
part_entry = Entry(app, textvariable=part_text)
part_entry.grid(row=0, column=1)


app.title('Part Manager')
app.geometry('700x350')

app.mainloop()