from tkinter import *

app = Tk()

part_text = StringVar()
part_label = Label(app, text='Part Name', font=('bold', 12), pady=20)
part_label.grid(row=0, column=0 , sticky=W)
part_entry = Entry(app, textvariable=part_text)
part_entry.grid(row=0, column=1)

customer_text = StringVar()
customer_label = Label(app, text='Customer', font=('bold', 12))
customer_label.grid(row=0, column=2 , sticky=W)
customer_entry = Entry(app, textvariable=customer_text)
customer_entry.grid(row=0, column=3)

retailer_text = StringVar()
retailer_label = Label(app, text='Retailer', font=('bold', 12))
retailer_label.grid(row=1, column=0 , sticky=W)
retailer_entry = Entry(app, textvariable=retailer_text)
retailer_entry.grid(row=1, column=1)

price_text = StringVar()
price_label = Label(app, text='Price', font=('bold', 12))
price_label.grid(row=1, column=2 , sticky=W)
price_entry = Entry(app, textvariable=price_text)
price_entry.grid(row=1, column=3)


parts_list = Listbox(app, height=8, width=50 )
parts_list.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20 , padx=20)


scrollbar =Scrollbar(app)
scrollbar.grid(row=3, column=3)

parts_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=parts_list.yview)

add_btn = Button(app, text='Add Parts' , width=12, command=add_item)


app.title('Part Manager')
app.geometry('700x350')

app.mainloop()