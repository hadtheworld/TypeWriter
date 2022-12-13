import keyboard
import time
import tkinter as tk
import random
class check_box:
    rec=[]
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.root=tk.Tk()
        self.canvas1=tk.Canvas(self.root,width=self.x,height=self.y)
        self.canvas1.pack() 
        self.entry=tk.Entry(self.root)
        self.canvas1.create_window(self.x//2,self.y//2+((self.y//2)//2),window=self.entry)
        self.root.title("Enter inour number ans press Enter to cintunue!!:\nctrl+y to start\nctrl+k to stop and restart")
        self.button1=tk.Button(text='YES',command=self.execute)
        self.canvas1.create_window((self.x//2)-((self.x//2)//2),(self.y//2)-((self.y//2)//2),window=self.button1)
        self.button2=tk.Button(text='NO',command=self.root.destroy)
        self.canvas1.create_window((self.x//2)+((self.x//2)//2),(self.y//2)-((self.y//2)//2),window=self.button2)
    def CheckBox(self):
        self.root.mainloop()
    def execute(self):
        inp=int(self.entry.get())
        if inp in self.rec or inp<1 or inp>10:
            print("wrong input")
            return
        while True:
            if (keyboard.is_pressed("ctrl+y")):
                obj=TypeWriter(inp)
                obj.write()
                break
            if(keyboard.is_pressed("ctrl+k")):
                return
        self.rec.append(inp)
        if len(self.rec)==10:
            self.rec.clear()
        return
    

class TypeWriter:
    def __init__(self,b):
        self.file_number=b
    def write(self):
        c="input"+str(self.file_number)+".txt"
        file=open(c,'r')
        s=""
        for i in file:
            s+=i 
        ans2=list(map(str,s.split('\n')))
        for i in range(len(ans2)):
            ans2[i]+='\n'
        for ans in ans2:
            for i in ans:
                time.sleep(round(random.uniform(0.03,0.05),2))
                keyboard.write(i)
window=check_box(400,300)
window.CheckBox()