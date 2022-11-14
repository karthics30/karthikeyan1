from tkinter.ttk import*
from tkinter import*
import mysql.connector as mysql
import random
from datetime import datetime

root= Tk()
root.geometry("1200x650+100+20")
root.title("RESTAURANT MANAGEMENT SYSTEM")

f= Frame(root, bd=10, relief=GROOVE)
f.pack(side=TOP)

f1 = Frame(root, bd=5, height=400,width=300, relief= RAISED)
f1.pack(side=LEFT,fill="both", expand=1)

f2 = Frame(root, bd=5,height=400, width=300, relief=RAISED)

f3 = Frame(root,bd=10,bg='cyan', height=400,width=300,relief=GROOVE)
f3.pack(side=BOTTOM)

lbl_info= Label(f, font=('aria', 30, 'bold'),bg='sky blue',text="MURUGAN IDLY KADAI")
lbl_info.grid(row=0, column=0)

now = datetime.now()
localtime = now.strftime("%d/%m/%Y %H:%M:%S")

rand         = StringVar()
Moongdalidli = StringVar()
Oatsravaidli = StringVar()
Quickravaidli= StringVar()
Soojiidli     = StringVar()
Doubleduckeridli = StringVar()
Pohaidli      = StringVar()
podiidli      = StringVar()
sambaridli    = StringVar()
miniidli      = StringVar()
kushbooidli   = StringVar()
barleyidli    = StringVar()
spinachidli   = StringVar()
Total          = StringVar()
Tax            = StringVar()
cost           = StringVar()
date           = StringVar()
service_charge = StringVar()

lbl_Moongdalidli = Label(f1, font=('aria', 20, 'bold'),text="Moong dal idli Rs.180")
lbl_Moongdalidli.grid(row=1,column=0)
txt_Moongdalidli = Entry(f1, font=('ariel', 20, 'bold'),textvariable=Moongdalidli)
txt_Moongdalidli.grid(row=1,column=1)

lbl_Oatsravaidli = Label(f1, font=('aria', 20, 'bold'),text="Oats rava idli Rs.150")
lbl_Oatsravaidli.grid(row=2,column=0)
txt_Oatsravaidli = Entry(f1, font=('ariel', 20, 'bold'),textvariable=Oatsravaidli)
txt_Oatsravaidli.grid(row=2,column=1)

lbl_Quickravaidli = Label(f1, font=('aria', 20, 'bold'),text="Quick rava idli Rs.150")
lbl_Quickravaidli.grid(row=3,column=0)
txt_Quickravaidli= Entry(f1, font=('ariel', 20, 'bold'),textvariable=Quickravaidli)
txt_Quickravaidli.grid(row=3,column=1)

lbl_Soojiidli  = Label(f1, font=('aria', 20, 'bold'),text="Sooji idli  Rs.200")
lbl_Soojiidli .grid(row=4,column=0)
txt_Soojiidli  = Entry(f1, font=('ariel', 20, 'bold'),textvariable=Soojiidli )
txt_Soojiidli .grid(row=4,column=1)

lbl_Doubleduckeridli  = Label(f1, font=('aria', 20, 'bold'),text="Double ducker idli Rs.200")
lbl_Doubleduckeridli .grid(row=5,column=0)
txt_Doubleduckeridli = Entry(f1, font=('ariel', 20, 'bold'),textvariable=Doubleduckeridli)
txt_Doubleduckeridli.grid(row=5,column=1)

lbl_Pohaidli  = Label(f1, font=('aria', 20, 'bold'),text="Poha idli   Rs.200")
lbl_Pohaidli.grid(row=6,column=0)
txt_Pohaidli = Entry(f1, font=('ariel', 20, 'bold'),textvariable=Pohaidli )
txt_Pohaidli.grid(row=6,column=1)

lbl_podiidli  = Label(f1, font=('aria', 20, 'bold'),text="podi idli   Rs.150")
lbl_podiidli.grid(row=7,column=0)
txt_podiidli = Entry(f1, font=('ariel', 20, 'bold'),textvariable=podiidli )
txt_podiidli.grid(row=7,column=1)

lbl_sambaridli  = Label(f1, font=('aria', 20, 'bold'),text="sambar idli   Rs.160")
lbl_sambaridli.grid(row=8,column=0)
txt_sambaridli = Entry(f1, font=('ariel', 20, 'bold'),textvariable=sambaridli )
txt_sambaridli.grid(row=8,column=1)

lbl_miniidli  = Label(f1, font=('aria', 20, 'bold'),text="mini idli   Rs.165")
lbl_miniidli.grid(row=9,column=0)
txt_miniidli = Entry(f1, font=('ariel', 20, 'bold'),textvariable=miniidli )
txt_miniidli.grid(row=9,column=1)

lbl_kushbooidli  = Label(f1, font=('aria', 20, 'bold'),text="kushboo idli   Rs.195")
lbl_kushbooidli.grid(row=10,column=0)
txt_kushbooidli = Entry(f1, font=('ariel', 20, 'bold'),textvariable=kushbooidli )
txt_kushbooidli.grid(row=10,column=1)

lbl_barleyidli  = Label(f1, font=('aria', 20, 'bold'),text="barley idli   Rs.200")
lbl_barleyidli.grid(row=11,column=0)
txt_barleyidli = Entry(f1, font=('ariel', 20, 'bold'),textvariable=barleyidli )
txt_barleyidli.grid(row=11,column=1)

lbl_spinachidli  = Label(f1, font=('aria', 20, 'bold'),text="spinach idli   Rs.150")
lbl_spinachidli.grid(row=12,column=0)
txt_spinachidli = Entry(f1, font=('ariel', 20, 'bold'),textvariable=spinachidli )
txt_spinachidli.grid(row=12,column=1)

def generate_bill():
    bill_no = str(random.randint(50, 500))
    rand.set(bill_no)
    date.set(localtime)
    try: qm = int(Moongdalidli.get())
    except: qm = 0
    try: qo = int(Oatsravaidli.get())
    except: qo = 0
    try: qq = int(Quickravaidli.get())
    except: qq = 0
    try: qs = int(Soojiidli.get())
    except: qs = 0
    try: qd = int(Doubleduckeridli.get())
    except: qd = 0
    try: qp = int(Pohaidli.get())
    except: qp = 0
    try: qt = int(podiidli.get())
    except: qt =0
    try: qa = int(sambaridli.get())
    except: qa= 0
    try: qb = int(miniidli.get())
    except: qb= 0
    try: qc = int(kushbooidli.get())
    except: qc= 0
    try: qe = int(barleyidli.get())
    except: qe= 0
    try: qf = int(spinachidli.get())
    except: qf= 0

    costofmoongdalidli = qm * 180 
    costofoatsravaidli = qo * 150
    costofquickravaidli = qq * 150
    costofsoojiidli    = qs * 200
    costofdoubleducker = qd * 200
    costofpohaidli     = qp * 200
    costofpodiidli     = qt * 150
    costofsambaridli   = qa * 160
    costofminiidli     = qb * 165
    costofkushbooidli  = qc * 195
    costofbarleyidli   = qe * 200
    costofspinachidli  = qf * 150

    f2.pack(side=RIGHT, fill="both", expand=1)
    f2.configure(background="light yellow")

    lbl_bill = Label(f2, font=('aria', 18, 'bold'), text="Bill no")
    lbl_bill.grid(row=1,column=0)

    lbl_date = Label(f2, font=('aria', 18, 'bold'), text="Date")
    lbl_date.grid(row=2,column=0)

    lbl_cost = Label(f2, font=('aria', 18, 'bold'), text="Cost")
    lbl_cost.grid(row=3,column=0)
    
    lbl_service = Label(f2, font=('aria', 18, 'bold'), text="Service charge")
    lbl_service.grid(row=4,column=0)
    
    lbl_tax = Label(f2, font=('aria', 18, 'bold'), text="Tax")
    lbl_tax.grid(row=5,column=0)
    
    lbl_total = Label(f2, font=('aria', 18, 'bold'), text="Total")
    lbl_total.grid(row=6,column=0)
    
    Totalcost= costofmoongdalidli + costofoatsravaidli + costofquickravaidli + costofsoojiidli + costofdoubleducker + costofpohaidli + costofpodiidli + costofsambaridli + costofminiidli + costofkushbooidli + costofbarleyidli + costofspinachidli
    costofmeal =  "Rs.", str('%.2f' % Totalcost)
    payTax = (Totalcost * 0.18)
    paidTax = "Rs.", str('%.2f' % payTax)
    ser_charge = (Totalcost * 0.01)
    service = "Rs.", str('%.2f' % ser_charge)
    overall = payTax + Totalcost + ser_charge
    total = "Rs.", str('%.2f' % overall)

    service_charge.set(service)
    cost.set(costofmeal)
    Tax.set(paidTax)
    Total.set(total)

txt_bill = Entry(f2, font=('ariel', 18, 'bold'),textvariable=rand)
txt_bill.grid(row=1, column=1)

txt_date = Entry(f2, font=('ariel', 18, 'bold'),textvariable=date)
txt_date.grid(row=2, column=1)

txt_cost = Entry(f2, font=('ariel', 18, 'bold'),textvariable=cost)
txt_cost.grid(row=3, column=1)

txt_service = Entry(f2, font=('ariel', 18, 'bold'),textvariable=service_charge)
txt_service.grid(row=4, column=1)

txt_tax = Entry(f2, font=('ariel', 18, 'bold'),textvariable=Tax)
txt_tax.grid(row=5, column=1)

txt_total = Entry(f2, font=('ariel', 18, 'bold'),textvariable=Total)
txt_total.grid(row=6, column=1)

def qexit():
    root.destroy()
def reset():
    Moongdalidli.set('') 
    Oatsravaidli.set('')  
    Quickravaidli.set('') 
    Soojiidli.set('')      
    Doubleduckeridli.set('')  
    Pohaidli.set('')
    podiidli.set('')
    sambaridli.set('')
    miniidli.set('')
    kushbooidli.set('')
    barleyidli.set('')
    spinachidli.set('')
    date.set('')
    f2.pack_forget()

btn_Total = Button(f1, bd=5, fg="black", font=('ariel', 16, 'bold'),text="CALCULATE BILL",command=generate_bill)
btn_Total.grid(row=13,column=0)

btn_Reset = Button(f1, bd=5, fg="black", font=('ariel', 16, 'bold'),text="RESET",command=reset)
btn_Reset.grid(row=13,column=1)

btn_Exit = Button(f1, bd=5, fg="black", font=('ariel', 16, 'bold'),text="EXIT",command=qexit)
btn_Exit.grid(row=13,column=2)

#Calculator

operator=''#7+9
def buttonClick(numbers):#9
    global operator
    operator=operator+numbers
    calculaterField.delete(0,END)
    calculaterField.insert(END,operator)

def clear():
    global operator
    operator=''
    calculaterField.delete(0,END)

def answer():
    global operator
    result=str(eval(operator))
    calculaterField.delete(0,END)
    calculaterField.insert(0,result)
    operator=''

calculaterField=Entry(f3,font=('arial',16,'bold'),width=32,bd=4)
calculaterField.grid(row=0,column=0,columnspan=4)

button7=Button(f3,text='7',font=('arial',16,'bold'),fg='white',bg='blue',bd=6,width=6,command=lambda:buttonClick('7'))
button7.grid(row=1,column=0)

button8=Button(f3,text='8',font=('arial',16,'bold'),fg='white',bg='blue',bd=6,width=6,command=lambda:buttonClick('8'))
button8.grid(row=1,column=1)

button9=Button(f3,text='9',font=('arial',16,'bold'),fg='white',bg='blue',bd=6,width=6,command=lambda:buttonClick('9'))
button9.grid(row=1,column=2)

buttonPlus=Button(f3,text='+',font=('arial',16,'bold'),fg='white',bg='blue',bd=6,width=6,command=lambda:buttonClick('+'))
buttonPlus.grid(row=1,column=3)

button4=Button(f3,text='4',font=('arial',16,'bold'),fg='white',bg='blue',bd=6,width=6,command=lambda:buttonClick('4'))
button4.grid(row=2,column=0)

button5=Button(f3,text='5',font=('arial',16,'bold'),fg='red4',bg='white',bd=6,width=6,command=lambda:buttonClick('5'))
button5.grid(row=2,column=1)

button6=Button(f3,text='6',font=('arial',16,'bold'),fg='red4',bg='white',bd=6,width=6,command=lambda:buttonClick('6'))
button6.grid(row=2,column=2)

buttonMinus=Button(f3,text='-',font=('arial',16,'bold'),fg='white',bg='blue',bd=6,width=6,command=lambda:buttonClick('-'))
buttonMinus.grid(row=2,column=3)

button1=Button(f3,text='1',font=('arial',16,'bold'),fg='white',bg='blue',bd=6,width=6,command=lambda:buttonClick('1'))
button1.grid(row=3,column=0)

button2=Button(f3,text='2',font=('arial',16,'bold'),fg='red4',bg='white',bd=6,width=6,command=lambda:buttonClick('2'))
button2.grid(row=3,column=1)

button3=Button(f3,text='3',font=('arial',16,'bold'),fg='red4',bg='white',bd=6,width=6,command=lambda:buttonClick('3'))
button3.grid(row=3,column=2)

buttonMult=Button(f3,text='*',font=('arial',16,'bold'),fg='white',bg='blue',bd=6,width=6,command=lambda:buttonClick('*'))
buttonMult.grid(row=3,column=3)

buttonAns=Button(f3,text='Ans',font=('arial',16,'bold'),fg='white',bg='blue',bd=6,width=6,command=answer)
buttonAns.grid(row=4,column=0)

buttonClear=Button(f3,text='Clear',font=('arial',16,'bold'),fg='white',bg='blue',bd=6,width=6,command=clear)
buttonClear.grid(row=4,column=1)

button0=Button(f3,text='0',font=('arial',16,'bold'),fg='white',bg='blue',bd=6,width=6,command=lambda:buttonClick('0'))
button0.grid(row=4,column=2)

buttonDiv=Button(f3,text='/',font=('arial',16,'bold'),fg='white',bg='blue',bd=6,width=6,command=lambda:buttonClick('/'))
buttonDiv.grid(row=4,column=3)

root.mainloop()







