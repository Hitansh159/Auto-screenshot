import tkinter
from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter import messagebox
import time
import cv2
import numpy as np
import pyautogui 
import ctypes 

def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

app = tkinter.Tk(); 

name = tkinter.StringVar()
path = tkinter.StringVar()
delay = tkinter.IntVar()
num = tkinter.IntVar()

def set_dir():
  Path.delete(0,len(path.get()))
  Path.insert(0, askdirectory())
  

def start_ss():
  for i in range(num.get()):
    time.sleep(delay.get())
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR )
    image_name = path.get() +"/"+ name.get() + str(i+1) + ".png"  
    cv2.imwrite(image_name, image)
    conti = Mbox('Screenshot taken', 'continue?', 4)
    if conti==6:
      continue
    else:
      break
  print(name.get(),path.get(),delay.get(),num.get())


app.title("Auto screenshot")

# labels
Label(app, text="Name Format ").grid(row=0)
Label(app, text="Path ").grid(row=1)
Label(app, text="Time(secs) ").grid(row=2)
Label(app, text="No. of SS ").grid(row=3)

# widgets
Name = Entry(app, textvariable=name)
Path = Entry(app, textvariable=path)
Browse = Button(app, text="Browse" , command=set_dir )
Time = Entry(app, textvariable=delay )
Number = Entry(app, textvariable=num )
Start = Button(app, text="Start",command=start_ss )

# placing widgets
Name.grid(row=0,column=1)
Path.grid(row=1,column=1)
Browse.grid(row=1,column=2)
Time.grid(row=2,column=1)
Number.grid(row=3,column=1)
Start.grid(row=4,column=1)



app.mainloop()

