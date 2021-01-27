from tkinter.filedialog import askopenfilename
import tkinter as tk
import mainFunc as vv

class App(tk.Frame):
    filename = ""
    bgFilename = ""
    hd = True
    fps = 30

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.grid()
        self.createWidget()

    def createWidget(self):
        self.l1 = tk.Label(self,text= "File")
        self.l1.grid(row=0, column=0, sticky = tk.W,padx=5,pady=5)
        self.l1.config(font=44)

        self.e = tk.Entry(self, width= 30)
        self.e.insert(0, "Enter the path of target img")
        self.e.grid(row=1, column=0,sticky = tk.N+tk.S, rowspan = 1)
        self.b = tk.Button(self, text="Open Folder", command = self.getTarget)
        self.b.grid(row=1, column=1) 
        
        self.e1 = tk.Entry(self, width= 30)
        self.e1.insert(0, "Enter the path of background img")
        self.e1.grid(row=2, sticky = tk.W+tk.S)
        self.b1 = tk.Button(self, text="Open Folder", command = self.getBg)
        self.b1.grid(row=2, column=1, sticky = tk.E) 

        self.l2 = tk.Label(self,text= "Quality")
        self.l2.grid(row=4, sticky = tk.W,padx=5,pady=5)
        self.l2.config(font=44)

        self.var1 = tk.BooleanVar(self)
        self.var2 = tk.BooleanVar(self)
        self.var1.set(False)
        self.var2.set(True)

        self.c1 = tk.Checkbutton(self, text="High", variable=self.var1, command=self.cb1Toggle)
        self.c1.grid(row=5, column=0, sticky=tk.W)
        self.c2 = tk.Checkbutton(self, text="Low (Zoom only recieves low)", variable=self.var2, command=self.cb2Toggle)
        self.c2.grid(row=6, column=0, sticky=tk.W)
        
        self.l3 = tk.Label(self,text= "Fps")
        self.l3.grid(row=7, column=0, sticky = tk.W,padx=5,pady=5)
        self.l3.config(font=32)

        self.e3 = tk.Entry(self, width= 5)
        self.e3.insert(0, "30")
        self.e3.grid(row=7, column=0,sticky = tk.E )
        
        self.b3 = tk.Button(self, text="Start", command = self.getAllData)
        self.b3.grid(row=8) 

        self.t = tk.Text(self, height=19, width = 40)
        self.t.grid(row=9, columnspan=10) 
        self.pl = PrintLogger(self.t)
        

    def getTarget(self):
        fn = askopenfilename()
        self.e.delete(0, tk.END)
        self.e.insert(0, fn)

    def getBg(self):
        bg = askopenfilename()
        self.e1.delete(0, tk.END)
        self.e1.insert(0, bg)

    def cb1Toggle(self):
        self.c2.toggle()

    def cb2Toggle(self):
        self.c1.toggle()

    def getAllData(self):
        self.filename = self.e.get()
        self.bgFilename = self.e1.get()
        self.hd = self.var1.get()
        self.fps = self.e3.get()
        vv.main(self)
        exit()

    def writeInTextBox(self, text):
        PrintLogger(self.t).write(text)
        PrintLogger(self.t).write("\n")

    def closing(self):
        self.quit()
    
        
        
class PrintLogger():
    def __init__(self, textbox):
        self.textbox = textbox 

    def write(self, text):
        self.textbox.insert(tk.END, text)
        # could also scroll to end of textbox here to make sure always visible
        self.textbox.see("end")

    def flush(self): 
        pass



if __name__ == "__main__":
    root = tk.Tk()
    root.title('Virtual Video')
    root.geometry('300x500')
    app = App(root)
    root.wm_protocol("WM_DELETE_WINDOW", app.closing)
    root.mainloop()

