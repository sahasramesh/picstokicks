import os
import webbrowser
import tkinter as tk
from tkinter import *
from PIL import Image, ImageFont, ImageDraw, ImageTk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory


#/Users/sahasramesh/Documents/python/picstokicks/test.jpg
def Kicks(tested, name):
    def makeLayer(testpath, layerpath, num):
        def makePal(path, number):
            tester = Image.open(path).convert('RGBA')
            tdatas = tester.getdata()
            word_counter = {}
            for word in tdatas:
                if word in word_counter:
                    word_counter[word] += 1
                else:
                    word_counter[word] = 1

            popular_words = sorted(word_counter, key = word_counter.get, reverse = True)
            palette = popular_words[:number]
            return palette

        layerPal = makePal(layerpath, 3)
        testPal = makePal(testpath, 6)

        for i in testPal:
            if i[3] == 0:
                testPal.remove(i)

        testPal = testPal + testPal

        l = layerPal[1]
        if len(layerPal) == 3:
            l2 = layerPal[2]
        p = testPal[num]

        c = Image.open(layerpath).convert('RGBA')
        cdatas = c.getdata()
        cData = []
        for item in cdatas:
            if item == (l[0], l[1], l[2], 255):
                cData.append((p[0], p[1], p[2], 255))
            elif item == (l2[0], l2[1], l2[2], 255):
                cData.append((p[0], p[1], p[2], 235))
            else:
                cData.append((255, 255, 255, 0))
        c.putdata(cData)

        return c

    c1 = makeLayer(tested, '/Users/sahasramesh/Documents/python/picstokicks/layers/9_swoosh.png', 0)
    c2 = makeLayer(tested, '/Users/sahasramesh/Documents/python/picstokicks/layers/8_quarter.png', 1)
    c3 = makeLayer(tested, '/Users/sahasramesh/Documents/python/picstokicks/layers/7_tongue_vamp.png', 2)
    c4 = makeLayer(tested, '/Users/sahasramesh/Documents/python/picstokicks/layers/6_foxing_tip.png', 3)
    c5 = makeLayer(tested, '/Users/sahasramesh/Documents/python/picstokicks/layers/5_outsole.png', 4)
    c6 = makeLayer(tested, '/Users/sahasramesh/Documents/python/picstokicks/layers/4_midsole_tongueTop.png', 5)
    c7 = makeLayer(tested, '/Users/sahasramesh/Documents/python/picstokicks/layers/3_eyestay_backtab.png', 6)
    c8 = makeLayer(tested, '/Users/sahasramesh/Documents/python/picstokicks/layers/2_strap.png', 7)
    c9 = makeLayer(tested, '/Users/sahasramesh/Documents/python/picstokicks/layers/1_laces.png', 8)

    c1.paste(c2, (0, 0), mask=c2.convert('RGBA'))
    c1.paste(c3, (0, 0), mask=c3.convert('RGBA'))
    c1.paste(c4, (0, 0), mask=c4.convert('RGBA'))
    c1.paste(c5, (0, 0), mask=c5.convert('RGBA'))
    c1.paste(c6, (0, 0), mask=c6.convert('RGBA'))
    c1.paste(c7, (0, 0), mask=c7.convert('RGBA'))
    c1.paste(c8, (0, 0), mask=c8.convert('RGBA'))
    c1.paste(c9, (0, 0), mask=c9.convert('RGBA'))

    t1 = Image.open('/Users/sahasramesh/Documents/python/picstokicks/layers/0_outline.png')
    c1.paste(t1, (0, 0), mask=t1.convert('RGBA'))

    draw = ImageDraw.Draw(c1)
    font = ImageFont.truetype('nike.ttf', 40)
    text = "AIR FORCE ONE HIGH 07 SE'" + str(name.upper()) + "'"
    draw.text((50, 815), text, fill ="black", font = font, align ="center")
    draw.text((640, 60), "SAHASRAMESH.COM", fill ="black", font = font, align ="center")

    return c1

window = Tk()
window.title("PICSTOKICKS")
window.geometry('240x250')
window.resizable(width=False, height=False)
window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())

font = 'Arial'
n = 14

#button functions
def makeAble(*args):
    u = stringvar.get()
    x = stringvar1.get()

    if u and x:
        btn2.config(state='normal')
    else:
        try:
            btn2.config(state='disabled')
        except NameError:
            pass

def pathbtn():
    filename = askopenfilename(title='Select File')
    v1 = StringVar(window, value=filename)
    txt.delete(0, END)
    txt.insert(0, filename)

    return filename, v1, txt

def clearbtn():
    txt.delete(0, END)
    txt.insert(0, "")
    txt1.delete(0, END)
    txt1.insert(0, "")

def kickbtn():
    Kicks(txt.get(), txt1.get()).show()

def tagbtn():
    webbrowser.open("http://sahasramesh.com")

#vars check if text boxes are populated
stringvar = tk.StringVar(window)
stringvar1 = tk.StringVar(window)

stringvar.trace("w", makeAble)
stringvar1.trace("w", makeAble)

#(0,0) title
lbl = Label(window, text="PICSTOKICKS", font=(font, n))
lbl.grid(column=0, row=0, padx=(0,0), pady=(10, 15))

#(0,1) path prompt text
lbl1 = Label(window, text="Source image: ", font=(font, n), anchor='w')
lbl1.grid(column=0, row=1)

#(0,2) path text box
txt = Entry(window, textvariable=stringvar, width=20, font=(font, n))
txt.grid(column=0, row=2, padx=(10,0), pady=(0, 15))

#(1,2) path button
btn = Button(window, text="...", command=pathbtn, font=(font, n))
btn.grid(column=1, row=2, padx=(5,0), pady=(0, 15))

#(0,3) name prompt text
lbl3 = Label(window, text="Name: ", font=(font, n), anchor=W)
lbl3.grid(column=0, row=3, padx=(0,0), pady=(0, 0))

#(0,4) name text box
txt1 = Entry(window, textvariable=stringvar1, width=20, font=(font, n))
txt1.grid(column=0, row=4, padx=(10,0), pady=(0, 20))

#(0,5) frame for buttons
fr1 = Frame(window)
fr1.grid(column=0, row=5)

btn1 = Button(fr1, text="Clear", command=clearbtn, font=(font, n))
btn1.pack(side=LEFT)

btn2 = Button(fr1, text="Make kick", command=kickbtn, font=(font, n))
btn2.pack(side=LEFT)
btn2.config(state='disabled')

#(0,7) tag frame
fr1 = Frame(window)
fr1.grid(column=0, row=6, padx=(0,0), pady=(25, 0))

#tag
tag = Label(fr1, text="An original project by ", font=('Courier', 8))
tag.pack(side=LEFT)

#tag
btn4 = Button(fr1, text="Sahas Ramesh", fg='#FF4500', anchor=W, highlightbackground='white', highlightcolor='white', highlightthickness=0, command=tagbtn, font=('Courier', 8))
btn4.pack(side=LEFT)

window.mainloop()
