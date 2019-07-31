##################################################################################################################################
#####################################################     Sudhansu Kumar     #####################################################
#####################################################     MCA-MCU 2017-2019     ##################################################
##################################################################################################################################
 
import tkinter as tk
from tkinter import *
import pyqrcode
import png
from pyqrcode import QRCode 
from PIL import Image
import barcode
from barcode.writer import ImageWriter

root = tk.Tk()

Label(root,text="Bar & QR Code",bg="PaleGreen4",font = "Georgia 16 bold",fg="salmon").grid(row=0,column=3)
Label(root,text="Generate Bar Code",fg = "red",font = "Times 15").grid(row=1,column=2)
Label(root,text="Generate QR Code",fg = "red",font = "Times 15").grid(row=1,column=4)

def barsave():
    barcodes=barEntry.get("1.0",END)
    ean = barcode.get('ean14', barcodes, writer=ImageWriter())
    barfile_name = barfilename.get("1.0","end-1c")
    filename = ean.save(barfile_name)
    barEntry.delete('1.0', END)
    barfilename.delete('1.0', END)
    #print(filename)
    #print(ean.get_fullcode())
Label(root,text="Enter BarCode",fg = "light green",bg = "dark green",font = "Georgia 12 italic").grid(rowspan=2,row=2,column=1)
barEntry=Text(root, height=1, width=15,font = "Georgia 14")
barEntry.grid(rowspan=2,row=2,columnspan=2,column=2)
Label(root,text="Enter File Name",fg = "light green",bg = "dark green",font = "Georgia 12 italic").grid(rowspan=4,row=4,column=1)
barfilename=Text(root, height=1, width=15,font = "Georgia 14")
barfilename.grid(rowspan=4,row=4,columnspan=2,column=2)
Button(root, text="SubmitBar", command=lambda: barsave(),activebackground="turquoise",
          font="Bookman 10 bold",bg="cyan").grid(rowspan=8,row=8,columnspan=2,column=1)

def save():
    inputValue=iv.get("1.0",END)
    url = pyqrcode.create(inputValue)
    file_name = textBox.get("1.0","end-1c")
    with open(file_name + '.png', 'w') as file_object:
        #file_object.write(file_name)
        url.png(file_name,scale=3)
        #url.svg(file_name, scale = 4)

        iv.delete('1.0', END)
        textBox.delete('1.0', END)
   
Label(root,text="Enter QR-Code",fg = "light green",bg = "dark green",font = "Georgia 12 italic").grid(rowspan=2,row=2,column=4)
iv=Text(root, height=1, width=15,font = "Georgia 14")
iv.grid(rowspan=2,row=2,column=5)
Label(root,text="Enter File Name",fg = "light green",bg = "dark green",font = "Georgia 12 italic").grid(rowspan=4,row=4,column=4)
textBox=Text(root, height=1, width=15,font = "Georgia 14")
textBox.grid(rowspan=4,row=4,column=5)
Button(root, text="Submit QR", command=lambda: save(),activebackground="turquoise",
          font="Bookman 10 bold",bg="cyan").grid(rowspan=8,row=8,columnspan=8,column=4)

root.title("QR & Bar Code Generator")
root.configure(bg="misty rose")
root.geometry("850x300")
root.mainloop()

##-------- BarCode type with Digit Length ----------##
""" Bar_type            Digit_Length       Answer_type 
    ean8                7 digit            12345670
    ean13               12 digit           1234567891231
    ean14               13 digit           12345678912343
    upcA/upc            11 digit           123456789128
    pzn                 6 digit            PZN-1234562"""





