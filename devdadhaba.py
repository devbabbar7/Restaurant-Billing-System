from tkinter import *
from tkinter import filedialog,messagebox
import random
import time
import requests

#Functions

def reset():
    textReceipt.delete(1.0,END)
    e_butter.set('0')
    e_paneer.set('0')
    e_damaloo.set('0')
    e_daal.set('0')
    e_soyabin.set('0')
    e_rajma.set('0')
    e_kofta.set('0')
    e_mixveg.set('0')
    e_daaltadka.set('0')

    e_garlicnaan.set('0')
    e_butterroti.set('0')
    e_butternaan.set('0')
    e_stuffnaan.set('0')
    e_missiroti.set('0')
    e_makkiroti.set('0')
    e_plainroti.set('0')
    e_parantha.set('0')
    e_paneernaan.set('0')

    e_kitkat.set('0')
    e_mango.set('0')
    e_apple.set('0')
    e_vanilla.set('0')
    e_strawberry.set('0')
    e_brownie.set('0')
    e_pineapple.set('0')
    e_chocolate.set('0')
    e_blackforest.set('0')

    textpaneer.config(state=DISABLED)
    textbutter.config(state=DISABLED)
    textdamaloo.config(state=DISABLED)
    textdaal.config(state=DISABLED)
    textsoyabin.config(state=DISABLED)
    textmixveg.config(state=DISABLED)
    textdaaltadka.config(state=DISABLED)
    textkofta.config(state=DISABLED)
    textrajma.config(state=DISABLED)

    textgarlicnaan.config(state=DISABLED)
    textbutterroti.config(state=DISABLED)
    textmakkiroti.config(state=DISABLED)
    textstuffnaan.config(state=DISABLED)
    textmissiroti.config(state=DISABLED)
    textparantha.config(state=DISABLED)
    textplainroti.config(state=DISABLED)
    textbutternaan.config(state=DISABLED)
    textpaneernaan.config(state=DISABLED)

    textmango.config(state=DISABLED)
    textapple.config(state=DISABLED)
    textkitkat.config(state=DISABLED)
    textvanilla.config(state=DISABLED)
    textstrawberry.config(state=DISABLED)
    textbrownie.config(state=DISABLED)
    textpineapple.config(state=DISABLED)
    textchocolate.config(state=DISABLED)
    textblackforest.config(state=DISABLED)

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)
    var25.set(0)
    var26.set(0)
    var27.set(0)

    costofrotivar.set('')
    costoffoodvar.set('')
    costoficecreamvar.set('')
    subtotalvar.set('')
    gsttaxvar.set('')
    totalcostvar.set('')

def save():
    if textReceipt.get(1.0,END)=='\n':
        pass
    else:
        url=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
        if url==None:
            pass
        else:

            bill_data=textReceipt.get(1.0,END)
            url.write(bill_data)
            url.close()
            messagebox.showinfo('Information','Your Bill Is Succesfully Saved')

def receipt():
    global billnumber,date
    if costoffoodvar.get() != '' or costoficecreamvar.get() != '' or costofrotivar.get() != '':
        textReceipt.delete(1.0,END)
        x=random.randint(100,10000)
        billnumber='BILL'+str(x)
        date=time.strftime('%d/%m/%Y')
        textReceipt.insert(END,'Receipt Ref:\t\t'+billnumber+'\t\t'+date+'\n')
        textReceipt.insert(END,'***************************************************************\n')
        textReceipt.insert(END,'Items:\t\t Cost Of Items(Rs)\n')
        textReceipt.insert(END,'***************************************************************\n')
        if e_paneer.get()!='0':
            textReceipt.insert(END,f'Shahi Paneer\t\t\t{int(e_paneer.get())*200}\n\n')

        if e_butter.get()!='0':
            textReceipt.insert(END,f'Butter Paneer Masala\t\t\t{int(e_butter.get())*210}\n\n')

        if e_daal.get()!='0':
            textReceipt.insert(END,f'Dal Makhani\t\t\t{int(e_daal.get())*160}\n\n')

        if e_rajma.get() != '0':
            textReceipt.insert(END, f'Rajma\t\t\t{int(e_rajma.get()) * 170}\n\n')

        if e_damaloo.get() != '0':
            textReceipt.insert(END, f'Dam Aloo\t\t\t{int(e_damaloo.get()) * 180}\n\n')

        if e_mixveg.get() != '0':
            textReceipt.insert(END, f'Mix Veg\t\t\t{int(e_mixveg.get()) * 180}\n\n')

        if e_soyabin.get() != '0':
            textReceipt.insert(END, f'Soyabin Chaap\t\t\t{int(e_soyabin.get()) * 180}\n\n')

        if e_daaltadka.get() != '0':
            textReceipt.insert(END, f'Daal Tadka\t\t\t{int(e_daaltadka.get()) * 160}\n\n')

        if e_kofta.get() != '0':
            textReceipt.insert(END, f'Malai Kofta\t\t\t{int(e_kofta.get()) * 180}\n\n')

        if e_garlicnaan.get() != '0':
            textReceipt.insert(END, f'Garlic Naan\t\t\t{int(e_garlicnaan.get()) * 50}\n\n')

        if e_butterroti.get() != '0':
            textReceipt.insert(END, f'Butter Roti\t\t\t{int(e_butterroti.get()) * 40}\n\n')

        if e_butternaan.get() != '0':
            textReceipt.insert(END, f'Butter Naan\t\t\t{int(e_butternaan.get()) * 80}\n\n')

        if e_missiroti.get() != '0':
            textReceipt.insert(END, f'Missi Roti\t\t\t{int(e_missiroti.get()) * 30}\n\n')

        if e_makkiroti.get() != '0':
            textReceipt.insert(END, f'Makki Roti\t\t\t{int(e_makkiroti.get()) * 40}\n\n')

        if e_stuffnaan.get() != '0':
            textReceipt.insert(END, f'Stuff Naan\t\t\t{int(e_stuffnaan.get()) * 60}\n\n')

        if e_plainroti.get() != '0':
            textReceipt.insert(END, f'Plain Roti\t\t\t{int(e_plainroti.get()) * 20}\n\n')

        if e_parantha.get() != '0':
            textReceipt.insert(END, f'Parantha\t\t\t{int(e_parantha.get()) * 50}\n\n')

        if e_paneernaan.get() != '0':
            textReceipt.insert(END, f'Paneer Naan\t\t\t{int(e_paneernaan.get()) * 80}\n\n')

        if e_mango.get() != '0':
            textReceipt.insert(END, f'Mango\t\t\t{int(e_mango.get()) * 40}\n\n')

        if e_apple.get() != '0':
            textReceipt.insert(END, f'Apple\t\t\t{int(e_apple.get()) * 30}\n\n')

        if e_kitkat.get() != '0':
            textReceipt.insert(END, f'Kitkat\t\t\t{int(e_kitkat.get()) * 50}\n\n')

        if e_strawberry.get() != '0':
            textReceipt.insert(END, f'Strawberry\t\t\t{int(e_strawberry.get()) * 45}\n\n')

        if e_brownie.get() != '0':
            textReceipt.insert(END, f'Brownie\t\t\t{int(e_brownie.get()) * 80}\n\n')

        if e_pineapple.get() != '0':
            textReceipt.insert(END, f'Pineapple\t\t\t{int(e_pineapple.get()) * 62}\n\n')

        if e_chocolate.get() != '0':
            textReceipt.insert(END, f'Chocolate\t\t\t{int(e_chocolate.get()) * 70}\n\n')

        if e_blackforest.get() != '0':
            textReceipt.insert(END, f'Black Forest\t\t\t{int(e_blackforest.get()) * 55}\n\n')

        if e_vanilla.get() != '0':
            textReceipt.insert(END, f'Vanilla\t\t\t{int(e_vanilla.get()) * 55}\n\n')

        textReceipt.insert(END,'***************************************************************\n')
        if costoffoodvar.get()!='0 Rs':
            textReceipt.insert(END,f'Cost Of Food\t\t\t{priceofFood}Rs\n\n')
        if costofrotivar.get() != '0 Rs':
            textReceipt.insert(END,f'Cost Of Roti\t\t\t{priceofroti}Rs\n\n')
        if costoficecreamvar.get() != '0 Rs':
            textReceipt.insert(END,f'Cost Of Ice-Cream\t\t\t{priceofIceCream}Rs\n\n')

        textReceipt.insert(END, f'Sub Total\t\t\t{subtotalofItems}Rs\n\n')
        textReceipt.insert(END, f'GST Tax\t\t\t{gsttax}Rs\n\n')
        textReceipt.insert(END, f'Total Cost\t\t\t{tottalcost}Rs\n\n')
        textReceipt.insert(END,'***************************************************************\n')

    else:
        messagebox.showerror('Error','No Item Is selected')



def totalcost():
    global priceofFood,priceofroti,priceofIceCream,subtotalofItems, tottalcost, gsttax
    if var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var4.get() != 0 or var5.get() != 0 or \
        var6.get() != 0 or var7.get() != 0 or var8.get() != 0 or var9.get() != 0 or var10.get() != 0 or\
        var11.get() != 0 or var12.get() != 0 or var13.get() != 0 or var14.get() != 0 or var15.get() != 0 or \
        var16.get() != 0 or var17.get() != 0 or var18.get() != 0 or var19.get() != 0 or var20.get() != 0 or \
        var21.get() != 0 or var22.get() != 0 or var23.get() != 0 or var24.get() != 0 or var25.get() != 0 or\
        var26.get() != 0 or var27.get() != 0:

        item1=int(e_paneer.get())
        item2=int(e_butter.get())
        item3=int(e_daal.get())
        item4 = int(e_damaloo.get())
        item5 = int(e_soyabin.get())
        item6 = int(e_rajma.get())
        item7 = int(e_kofta.get())
        item8 = int(e_mixveg.get())
        item9 = int(e_daaltadka.get())

        item10 = int(e_garlicnaan.get())
        item11 = int(e_butterroti.get())
        item12 = int(e_butternaan.get())
        item13 = int(e_missiroti.get())
        item14 = int(e_makkiroti.get())
        item15 = int(e_stuffnaan.get())
        item16 = int(e_plainroti.get())
        item17 = int(e_parantha.get())
        item18 = int(e_paneernaan.get())

        item19 = int(e_mango.get())
        item20 = int(e_apple.get())
        item21 = int(e_kitkat.get())
        item22 = int(e_vanilla.get())
        item23 = int(e_strawberry.get())
        item24 = int(e_brownie.get())
        item25 = int(e_pineapple.get())
        item26 = int(e_chocolate.get())
        item27 = int(e_blackforest.get())

        priceofFood=(item1*200)+(item2*210)+(item3*160)+(item4*180)+ (item5*180) + (item6 * 170) + (item7 * 180) \
                    + (item8 * 180) + (item9 * 160)

        priceofroti=(item10*50)+(item11*40)+ (item12 * 80) + (item13 * 30) + (item14 * 40) + (item15 * 60) \
                      + (item16 * 20) + (item17 * 50) + (item18 * 80)

        priceofIceCream=(item19*40)+(item20*30)+ (item21 * 50) + (item22 * 55) + (item23 * 45) + (item24 * 80) \
                     + (item25 * 62) + (item26 * 70) + (item27 * 55)

        costoffoodvar.set(str(priceofFood)+ ' Rs')
        costofrotivar.set(str(priceofroti)+ ' Rs')
        costoficecreamvar.set(str(priceofIceCream)+ ' Rs')

        subtotalofItems=priceofFood+priceofroti+priceofIceCream
        subtotalvar.set(str(subtotalofItems)+' Rs')

        gsttax = int(subtotalofItems*0.05)
        gsttaxvar.set(str(gsttax)+' Rs')
        tottalcost=subtotalofItems+gsttax
        totalcostvar.set(str(tottalcost)+' Rs')

    else:
        messagebox.showerror('Error','No Item Is selected')



def paneer():
    if var1.get()==1:
        textpaneer.config(state=NORMAL)
        textpaneer.delete(0,END)
        textpaneer.focus()
    else:
        textpaneer.config(state=DISABLED)
        e_paneer.set('0')

def butter():
    if var2.get()==1:
        textbutter.config(state=NORMAL)
        textbutter.delete(0,END)
        textbutter.focus()

    else:
        textbutter.config(state=DISABLED)
        e_butter.set('0')

def daal():
    if var3.get()==1:
        textdaal.config(state=NORMAL)
        textdaal.delete(0,END)
        textdaal.focus()

    else:
        textdaal.config(state=DISABLED)
        e_daal.set('0')

def damaloo():
    if var4.get() == 1:
        textdamaloo.config(state=NORMAL)
        textdamaloo.focus()
        textdamaloo.delete(0, END)
    elif var4.get() == 0:
        textdamaloo.config(state=DISABLED)
        e_damaloo.set('0')


def soyabin():
    if var5.get() == 1:
        textsoyabin.config(state=NORMAL)
        textsoyabin.focus()
        textsoyabin.delete(0, END)
    elif var5.get() == 0:
        textsoyabin.config(state=DISABLED)
        e_soyabin.set('0')


def rajma():
    if var6.get() == 1:
        textrajma.config(state=NORMAL)
        textrajma.focus()
        textrajma.delete(0, END)
    elif var6.get() == 0:
        textrajma.config(state=DISABLED)
        e_rajma.set('0')


def kofta():
    if var7.get() == 1:
        textkofta.config(state=NORMAL)
        textkofta.focus()
        textkofta.delete(0, END)
    elif var7.get() == 0:
        textkofta.config(state=DISABLED)
        e_kofta.set('0')


def mixveg():
    if var8.get() == 1:
        textmixveg.config(state=NORMAL)
        textmixveg.focus()
        textmixveg.delete(0, END)
    elif var8.get() == 0:
        textmixveg.config(state=DISABLED)
        e_mixveg.set('0')


def daaltadka():
    if var9.get() == 1:
        textdaaltadka.config(state=NORMAL)
        textdaaltadka.focus()
        textdaaltadka.delete(0, END)
    elif var9.get() == 0:
        textdaaltadka.config(state=DISABLED)
        e_daaltadka.set('0')


def garlicnaan():
    if var10.get() == 1:
        textgarlicnaan.config(state=NORMAL)
        textgarlicnaan.focus()
        textgarlicnaan.delete(0, END)
    elif var10.get() == 0:
        textgarlicnaan.config(state=DISABLED)
        e_garlicnaan.set('0')


def butterroti():
    if var11.get() == 1:
        textbutterroti.config(state=NORMAL)
        textbutterroti.focus()
        textbutterroti.delete(0, END)
    elif var11.get() == 0:
        textbutterroti.config(state=DISABLED)
        e_butterroti.set('0')


def butternaan():
    if var12.get() == 1:
        textbutternaan.config(state=NORMAL)
        textbutternaan.focus()
        textbutternaan.delete(0, END)
    elif var12.get() == 0:
        textbutternaan.config(state=DISABLED)
        e_butternaan.set('0')


def missiroti():
    if var13.get() == 1:
        textmissiroti.config(state=NORMAL)
        textmissiroti.focus()
        textmissiroti.delete(0, END)
    elif var13.get() == 0:
        textmissiroti.config(state=DISABLED)
        e_missiroti.set('0')


def makkiroti():
    if var14.get() == 1:
        textmakkiroti.config(state=NORMAL)
        textmakkiroti.focus()
        textmakkiroti.delete(0, END)
    elif var14.get() == 0:
        textmakkiroti.config(state=DISABLED)
        e_makkiroti.set('0')


def stuffnaan():
    if var15.get() == 1:
        textstuffnaan.config(state=NORMAL)
        textstuffnaan.focus()
        textstuffnaan.delete(0, END)
    elif var15.get() == 0:
        textstuffnaan.config(state=DISABLED)
        e_stuffnaan.set('0')


def plainroti():
    if var16.get() == 1:
        textplainroti.config(state=NORMAL)
        textplainroti.focus()
        textplainroti.delete(0, END)
    elif var16.get() == 0:
        textplainroti.config(state=DISABLED)
        e_plainroti.set('0')


def parantha():
    if var17.get() == 1:
        textparantha.config(state=NORMAL)
        textparantha.focus()
        textparantha.delete(0, END)
    elif var17.get() == 0:
        textparantha.config(state=DISABLED)
        e_parantha.set('0')


def paneernaan():
    if var18.get() == 1:
        textpaneernaan.config(state=NORMAL)
        textpaneernaan.focus()
        textpaneernaan.delete(0, END)
    elif var18.get() == 0:
        textpaneernaan.config(state=DISABLED)
        e_paneernaan.set('0')


def mango():
    if var19.get() == 1:
        textmango.config(state=NORMAL)
        textmango.focus()
        textmango.delete(0, END)
    elif var19.get() == 0:
        textmango.config(state=DISABLED)
        e_mango.set('0')


def apple():
    if var20.get() == 1:
        textapple.config(state=NORMAL)
        textapple.focus()
        textapple.delete(0, END)
    elif var20.get() == 0:
        textapple.config(state=DISABLED)
        e_apple.set('0')


def kitkat():
    if var21.get() == 1:
        textkitkat.config(state=NORMAL)
        textkitkat.focus()
        textkitkat.delete(0, END)
    elif var21.get() == 0:
        textkitkat.config(state=DISABLED)
        e_kitkat.set('0')


def vanilla():
    if var22.get() == 1:
        textvanilla.config(state=NORMAL)
        textvanilla.focus()
        textvanilla.delete(0, END)
    elif var22.get() == 0:
        textvanilla.config(state=DISABLED)
        e_vanilla.set('0')


def strawberry():
    if var23.get() == 1:
        textstrawberry.config(state=NORMAL)
        textstrawberry.focus()
        textstrawberry.delete(0, END)
    elif var23.get() == 0:
        textstrawberry.config(state=DISABLED)
        e_strawberry.set('0')


def brownie():
    if var24.get() == 1:
        textbrownie.config(state=NORMAL)
        textbrownie.focus()
        textbrownie.delete(0, END)
    elif var24.get() == 0:
        textbrownie.config(state=DISABLED)
        e_brownie.set('0')


def pineapple():
    if var25.get() == 1:
        textpineapple.config(state=NORMAL)
        textpineapple.focus()
        textpineapple.delete(0, END)
    elif var25.get() == 0:
        textpineapple.config(state=DISABLED)
        e_pineapple.set('0')


def chocolate():
    if var26.get() == 1:
        textchocolate.config(state=NORMAL)
        textchocolate.focus()
        textchocolate.delete(0, END)
    elif var26.get() == 0:
        textchocolate.config(state=DISABLED)
        e_chocolate.set('0')


def blackforest():
    if var27.get() == 1:
        textblackforest.config(state=NORMAL)
        textblackforest.focus()
        textblackforest.delete(0, END)
    elif var27.get() == 0:
        textblackforest.config(state=DISABLED)
        e_blackforest.set('0')



root=Tk()

root.geometry('1270x690+0+0')

root.resizable(0,0)

root.title('Restaurant Management System created by Dev Babbar')

root.config(bg='purple4')

topFrame=Frame(root,bd=10,relief=RIDGE,bg='purple4')
topFrame.pack(side=TOP)

labelTitle=Label(topFrame,text='Dev Da Dhaba',font=('arial',30,'bold'),fg='yellow',bd=9,
                 bg='purple1',width=51)
labelTitle.grid(row=0,column=0)

#frames

menuFrame=Frame(root,bd=10,relief=RIDGE,bg='purple4')
menuFrame.pack(side=LEFT)

costFrame=Frame(menuFrame,bd=4,relief=RIDGE,bg='purple4',pady=10)
costFrame.pack(side=BOTTOM)

foodFrame=LabelFrame(menuFrame,text='Food',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='purple1',)
foodFrame.pack(side=LEFT)

rotiFrame=LabelFrame(menuFrame,text='Roti',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='purple1')
rotiFrame.pack(side=LEFT)

icecreamFrame=LabelFrame(menuFrame,text='Ice-Cream',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='purple1')
icecreamFrame.pack(side=LEFT)

rightFrame=Frame(root,bd=15,relief=RIDGE,bg='purple1')
rightFrame.pack(side=RIGHT)

calculatorFrame=Frame(rightFrame,bd=1,relief=RIDGE,bg='purple1')
calculatorFrame.pack()

recieptFrame=Frame(rightFrame,bd=4,relief=RIDGE,bg='purple1')
recieptFrame.pack()

buttonFrame=Frame(rightFrame,bd=3,relief=RIDGE,bg='purple1')
buttonFrame.pack()

#Variables

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()
var19 = IntVar()
var20 = IntVar()
var21 = IntVar()
var22 = IntVar()
var23 = IntVar()
var24 = IntVar()
var25 = IntVar()
var26 = IntVar()
var27 = IntVar()

e_paneer=StringVar()
e_butter=StringVar()
e_damaloo = StringVar()
e_rajma = StringVar()
e_daal = StringVar()
e_kofta = StringVar()
e_soyabin = StringVar()
e_daaltadka = StringVar()
e_mixveg = StringVar()

e_garlicnaan=StringVar()
e_butterroti = StringVar()
e_butternaan = StringVar()
e_missiroti = StringVar()
e_stuffnaan = StringVar()
e_makkiroti = StringVar()
e_plainroti = StringVar()
e_parantha = StringVar()
e_paneernaan = StringVar()

e_mango=StringVar()
e_kitkat = StringVar()
e_vanilla = StringVar()
e_apple = StringVar()
e_blackforest = StringVar()
e_strawberry = StringVar()
e_brownie = StringVar()
e_pineapple = StringVar()
e_chocolate = StringVar()

costoffoodvar=StringVar()
costofrotivar=StringVar()
costoficecreamvar=StringVar()
subtotalvar=StringVar()
gsttaxvar=StringVar()
totalcostvar=StringVar()

e_paneer.set('0')
e_butter.set('0')
e_damaloo.set('0')
e_daal.set('0')
e_soyabin.set('0')
e_rajma.set('0')
e_kofta.set('0')
e_daaltadka.set('0')
e_mixveg.set('0')

e_garlicnaan.set('0')
e_butterroti.set('0')
e_butternaan.set('0')
e_stuffnaan.set('0')
e_missiroti.set('0')
e_makkiroti.set('0')
e_plainroti.set('0')
e_parantha.set('0')
e_paneernaan.set('0')

e_kitkat.set('0')
e_strawberry.set('0')
e_pineapple.set('0')
e_apple.set('0')
e_chocolate.set('0')
e_mango.set('0')
e_blackforest.set('0')
e_brownie.set('0')
e_vanilla.set('0')

##FOOD

paneer=Checkbutton(foodFrame,text='Shahi Paneer',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var1
                 ,command=paneer)
paneer.grid(row=0,column=0,sticky=W)

butter=Checkbutton(foodFrame,text='Butter Paneer',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var2
                 ,command=butter)
butter.grid(row=1,column=0,sticky=W)

daal=Checkbutton(foodFrame,text='Dal Makhani',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var3
                 ,command=daal)
daal.grid(row=2,column=0,sticky=W)

damaloo=Checkbutton(foodFrame,text='Dam Aloo',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var4
                  ,command=damaloo)
damaloo.grid(row=3,column=0,sticky=W)

soyabin=Checkbutton(foodFrame,text='Soyabin Chaap',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var5
                  ,command=soyabin)
soyabin.grid(row=4,column=0,sticky=W)

rajma=Checkbutton(foodFrame,text='Rajma',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var6
                   ,command=rajma)
rajma.grid(row=5,column=0,sticky=W)

kofta=Checkbutton(foodFrame,text='Malai Kofta',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var7,
                   command=kofta)
kofta.grid(row=6,column=0,sticky=W)

mixveg=Checkbutton(foodFrame,text='Mix Veg',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var8
                   ,command=mixveg)
mixveg.grid(row=7,column=0,sticky=W)

daaltadka=Checkbutton(foodFrame,text='Daal Tadka',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var9
                    ,command=daaltadka)
daaltadka.grid(row=8,column=0,sticky=W)

#Entry Fields for Food Items

textpaneer=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=4,state=DISABLED,textvariable=e_paneer)
textpaneer.grid(row=0,column=1)

textbutter=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=4,state=DISABLED,textvariable=e_butter)
textbutter.grid(row=1,column=1)

textdaal=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=4,state=DISABLED,textvariable=e_daal)
textdaal.grid(row=2,column=1)

textdamaloo = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=4, state=DISABLED, textvariable=e_damaloo)
textdamaloo.grid(row=3, column=1)

textsoyabin = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=4, state=DISABLED, textvariable=e_soyabin)
textsoyabin.grid(row=4, column=1)

textrajma = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=4, state=DISABLED, textvariable=e_rajma)
textrajma.grid(row=5, column=1)

textkofta = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=4, state=DISABLED, textvariable=e_kofta)
textkofta.grid(row=6, column=1)

textmixveg = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=4, state=DISABLED, textvariable=e_mixveg)
textmixveg.grid(row=7, column=1)

textdaaltadka = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=4, state=DISABLED, textvariable=e_daaltadka)
textdaaltadka.grid(row=8, column=1)

#roti

garlicnaan=Checkbutton(rotiFrame,text='Garlic Naan',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var10
                  ,command=garlicnaan)
garlicnaan.grid(row=0,column=0,sticky=W)

butterroti=Checkbutton(rotiFrame,text='Butter Roti',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var11
                   ,command=butterroti)
butterroti.grid(row=1,column=0,sticky=W)

butternaan=Checkbutton(rotiFrame,text='Butter Naan',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var12
                   ,command=butternaan)
butternaan.grid(row=2,column=0,sticky=W)

missiroti=Checkbutton(rotiFrame,text='Missi Roti',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var13
                     ,command=missiroti)
missiroti.grid(row=3,column=0,sticky=W)

makkiroti=Checkbutton(rotiFrame,text='Makki Roti',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var14
                     ,command=makkiroti)
makkiroti.grid(row=4,column=0,sticky=W)

stuffnaan=Checkbutton(rotiFrame,text='Stuff Naan',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var15
                     ,command=stuffnaan)
stuffnaan.grid(row=5,column=0,sticky=W)

plainroti=Checkbutton(rotiFrame,text='Plain Roti',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var16
                      ,command=plainroti)
plainroti.grid(row=6,column=0,sticky=W)

parantha=Checkbutton(rotiFrame,text='Parantha',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var17
                      ,command=parantha)
parantha.grid(row=7,column=0,sticky=W)

paneernaan=Checkbutton(rotiFrame,text='Paneer Naan',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var18
                       ,command=paneernaan)
paneernaan.grid(row=8,column=0,sticky=W)

#entry fields for drink items

textgarlicnaan = Entry(rotiFrame, font=('arial', 18, 'bold'), bd=7, width=4, state=DISABLED, textvariable=e_garlicnaan)
textgarlicnaan.grid(row=0, column=1)

textbutterroti = Entry(rotiFrame, font=('arial', 18, 'bold'), bd=7, width=4, state=DISABLED, textvariable=e_butterroti)
textbutterroti.grid(row=1, column=1)

textbutternaan = Entry(rotiFrame, font=('arial', 18, 'bold'), bd=7, width=4, state=DISABLED, textvariable=e_butternaan)
textbutternaan.grid(row=2, column=1)

textmissiroti = Entry(rotiFrame, font=('arial', 18, 'bold'), bd=7, width=4, state=DISABLED, textvariable=e_missiroti)
textmissiroti.grid(row=3, column=1)

textmakkiroti = Entry(rotiFrame, font=('arial', 18, 'bold'), bd=7, width=4, state=DISABLED, textvariable=e_makkiroti)
textmakkiroti.grid(row=4, column=1)

textstuffnaan = Entry(rotiFrame, font=('arial', 18, 'bold'), bd=7, width=4, state=DISABLED, textvariable=e_stuffnaan)
textstuffnaan.grid(row=5, column=1)

textplainroti = Entry(rotiFrame, font=('arial', 18, 'bold'), bd=7, width=4, state=DISABLED,textvariable=e_plainroti)
textplainroti.grid(row=6, column=1)

textparantha = Entry(rotiFrame, font=('arial', 18, 'bold'), bd=7, width=4, state=DISABLED, textvariable=e_parantha)
textparantha.grid(row=7, column=1)

textpaneernaan = Entry(rotiFrame, font=('arial', 18, 'bold'), bd=7, width=4, state=DISABLED, textvariable=e_paneernaan)
textpaneernaan.grid(row=8, column=1)

#IceCream

mangocake=Checkbutton(icecreamFrame,text='Mango',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var19
                     ,command=mango)
mangocake.grid(row=0,column=0,sticky=W)

applecake=Checkbutton(icecreamFrame,text='Apple',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var20
                      ,command=apple)
applecake.grid(row=1,column=0,sticky=W)

kitkatcake=Checkbutton(icecreamFrame,text='Kitkat',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var21
                       ,command=kitkat)
kitkatcake.grid(row=2,column=0,sticky=W)

vanillacake=Checkbutton(icecreamFrame,text='Vanilla',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var22
                        ,command=vanilla)
vanillacake.grid(row=3,column=0,sticky=W)

strawberrycake=Checkbutton(icecreamFrame,text='Strawberry',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var23
                       ,command=strawberry)
strawberrycake.grid(row=4,column=0,sticky=W)

browniecake=Checkbutton(icecreamFrame,text='Brownie',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var24
                        ,command=brownie)
browniecake.grid(row=5,column=0,sticky=W)

pineapplecake=Checkbutton(icecreamFrame,text='Pineapple',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var25
                          ,command=pineapple)
pineapplecake.grid(row=6,column=0,sticky=W)

chocolatecake=Checkbutton(icecreamFrame,text='Chocolate',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var26
                          ,command=chocolate)
chocolatecake.grid(row=7,column=0,sticky=W)

blackforestcake=Checkbutton(icecreamFrame,text='Black Forest',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var27
                            ,command=blackforest)
blackforestcake.grid(row=8,column=0,sticky=W)

#entry fields for icecream

textmango = Entry(icecreamFrame, font=('arial', 18, 'bold'), bd=7, width=4, state=DISABLED, textvariable=e_mango)
textmango.grid(row=0, column=1)

textapple = Entry(icecreamFrame, font=('arial', 18, 'bold'), bd=7, width=4, state=DISABLED, textvariable=e_apple)
textapple.grid(row=1, column=1)

textkitkat = Entry(icecreamFrame, font=('arial', 18, 'bold'), bd=7, width=4, state=DISABLED, textvariable=e_kitkat)
textkitkat.grid(row=2, column=1)

textvanilla = Entry(icecreamFrame, font=('arial', 18, 'bold'), bd=7, width=4, state=DISABLED, textvariable=e_vanilla)
textvanilla.grid(row=3, column=1)

textstrawberry = Entry(icecreamFrame, font=('arial', 18, 'bold'), bd=7, width=4, state=DISABLED, textvariable=e_strawberry)
textstrawberry.grid(row=4, column=1)

textbrownie = Entry(icecreamFrame, font=('arial', 18, 'bold'), bd=7, width=4, state=DISABLED, textvariable=e_brownie)
textbrownie.grid(row=5, column=1)

textpineapple = Entry(icecreamFrame, font=('arial', 18, 'bold'), bd=7, width=4, state=DISABLED, textvariable=e_pineapple)
textpineapple.grid(row=6, column=1)

textchocolate = Entry(icecreamFrame, font=('arial', 18, 'bold'), bd=7, width=4, state=DISABLED, textvariable=e_chocolate)
textchocolate.grid(row=7, column=1)

textblackforest = Entry(icecreamFrame, font=('arial', 18, 'bold'), bd=7, width=4, state=DISABLED,textvariable=e_blackforest)
textblackforest.grid(row=8, column=1)

#costlabels & entry fields

labelCostofFood=Label(costFrame,text='Cost of Food',font=('arial',16,'bold'),bg='purple4',fg='white')
labelCostofFood.grid(row=0,column=0)

textCostofFood=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costoffoodvar)
textCostofFood.grid(row=0,column=1,padx=41)

labelCostofroti=Label(costFrame,text='Cost of Roti',font=('arial',16,'bold'),bg='purple4',fg='white')
labelCostofroti.grid(row=1,column=0)

textCostofroti=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costofrotivar)
textCostofroti.grid(row=1,column=1,padx=41)

labelCostofIceCream=Label(costFrame,text='Cost of Ice-Cream',font=('arial',16,'bold'),bg='purple4',fg='white')
labelCostofIceCream.grid(row=2,column=0)

textCostofIceCream=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costoficecreamvar)
textCostofIceCream.grid(row=2,column=1,padx=41)

labelSubTotal=Label(costFrame,text='Sub Total',font=('arial',16,'bold'),bg='purple4',fg='white')
labelSubTotal.grid(row=0,column=2)

textSubTotal=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=subtotalvar)
textSubTotal.grid(row=0,column=3,padx=41)

labelgsttax=Label(costFrame,text='GST Tax',font=('arial',16,'bold'),bg='purple4',fg='white')
labelgsttax.grid(row=1,column=2)

textgsttax=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=gsttaxvar)
textgsttax.grid(row=1,column=3,padx=41)

labelTotalCost=Label(costFrame,text='Total Cost',font=('arial',16,'bold'),bg='purple4',fg='white')
labelTotalCost.grid(row=2,column=2)

textTotalCost=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=totalcostvar)
textTotalCost.grid(row=2,column=3,padx=41)

#Buttons

buttonTotal=Button(buttonFrame,text='Total',font=('arial',14,'bold'),fg='white',bg='purple1',bd=3,padx=5,
                   command=totalcost)
buttonTotal.grid(row=0,column=0)

buttonReceipt=Button(buttonFrame,text='Receipt',font=('arial',14,'bold'),fg='white',bg='purple1',bd=3,padx=5
                     ,command=receipt)
buttonReceipt.grid(row=0,column=1)

buttonSave=Button(buttonFrame,text='Save',font=('arial',14,'bold'),fg='white',bg='purple1',bd=3,padx=5
                  ,command=save)
buttonSave.grid(row=0,column=2)

buttonReset=Button(buttonFrame,text='Reset',font=('arial',14,'bold'),fg='white',bg='purple1',bd=3,padx=5,
                   command=reset)
buttonReset.grid(row=0,column=4)

#textarea for receipt

textReceipt=Text(recieptFrame,font=('arial',12,'bold'),bd=3,width=42,height=14)
textReceipt.grid(row=0,column=0)

#Calculator
operator='' #7+9
def buttonClick(numbers): #9
    global operator
    operator=operator+numbers
    calculatorField.delete(0,END)
    calculatorField.insert(END,operator)

def clear():
    global operator
    operator=''
    calculatorField.delete(0,END)

def answer():
    global operator
    result=str(eval(operator))
    calculatorField.delete(0,END)
    calculatorField.insert(0,result)
    operator=''



calculatorField=Entry(calculatorFrame,font=('arial',16,'bold'),width=32,bd=4)
calculatorField.grid(row=0,column=0,columnspan=4)

button7=Button(calculatorFrame,text='7',font=('arial',16,'bold'),fg='yellow',bg='purple1',bd=6,width=4,
               command=lambda:buttonClick('7'))
button7.grid(row=1,column=0)

button8=Button(calculatorFrame,text='8',font=('arial',16,'bold'),fg='yellow',bg='purple1',bd=6,width=4,
               command=lambda:buttonClick('8'))
button8.grid(row=1,column=1)

button9=Button(calculatorFrame,text='9',font=('arial',16,'bold'),fg='yellow',bg='purple1',bd=6,width=4
               ,command=lambda:buttonClick('9'))
button9.grid(row=1,column=2)

buttonPlus=Button(calculatorFrame,text='+',font=('arial',16,'bold'),fg='yellow',bg='purple1',bd=6,width=4
                  ,command=lambda:buttonClick('+'))
buttonPlus.grid(row=1,column=3)

button4=Button(calculatorFrame,text='4',font=('arial',16,'bold'),fg='yellow',bg='purple1',bd=6,width=4
               ,command=lambda:buttonClick('4'))
button4.grid(row=2,column=0)

button5=Button(calculatorFrame,text='5',font=('arial',16,'bold'),fg='purple1',bg='white',bd=6,width=4
               ,command=lambda:buttonClick('5'))
button5.grid(row=2,column=1)

button6=Button(calculatorFrame,text='6',font=('arial',16,'bold'),fg='purple1',bg='white',bd=6,width=4
               ,command=lambda:buttonClick('6'))
button6.grid(row=2,column=2)

buttonMinus=Button(calculatorFrame,text='-',font=('arial',16,'bold'),fg='yellow',bg='purple1',bd=6,width=4
                   ,command=lambda:buttonClick('-'))
buttonMinus.grid(row=2,column=3)

button1=Button(calculatorFrame,text='1',font=('arial',16,'bold'),fg='yellow',bg='purple1',bd=6,width=4
               ,command=lambda:buttonClick('1'))
button1.grid(row=3,column=0)

button2=Button(calculatorFrame,text='2',font=('arial',16,'bold'),fg='purple1',bg='white',bd=6,width=4
               ,command=lambda:buttonClick('2'))
button2.grid(row=3,column=1)

button3=Button(calculatorFrame,text='3',font=('arial',16,'bold'),fg='purple1',bg='white',bd=6,width=4
               ,command=lambda:buttonClick('3'))
button3.grid(row=3,column=2)

buttonMult=Button(calculatorFrame,text='*',font=('arial',16,'bold'),fg='yellow',bg='purple1',bd=6,width=4
                  ,command=lambda:buttonClick('*'))
buttonMult.grid(row=3,column=3)

buttonAns=Button(calculatorFrame,text='Ans',font=('arial',16,'bold'),fg='yellow',bg='purple1',bd=6,width=4,
                 command=answer)
buttonAns.grid(row=4,column=0)

buttonClear=Button(calculatorFrame,text='Clear',font=('arial',16,'bold'),fg='yellow',bg='purple1',bd=6,width=4
                   ,command=clear)
buttonClear.grid(row=4,column=1)

button0=Button(calculatorFrame,text='0',font=('arial',16,'bold'),fg='yellow',bg='purple1',bd=6,width=4
               ,command=lambda:buttonClick('0'))
button0.grid(row=4,column=2)

buttonDiv=Button(calculatorFrame,text='/',font=('arial',16,'bold'),fg='yellow',bg='purple1',bd=6,width=4,
                 command=lambda:buttonClick('/'))
buttonDiv.grid(row=4,column=3)

root.mainloop()