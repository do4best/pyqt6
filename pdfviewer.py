from tkinter import *
from tkinter import filedialog
from tkPDFViewer2 import tkPDFViewer as pdf
import os


root = Tk()
root.geometry("700x700+400+100")
root.title("PDF Viewer")
root.configure(bg="black")
def browseFiles():
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),title='Select PDF File',filetypes=(("PDF File","pdf"),("PDF File","PDF"),("All File",".txt")))
    v1 = pdf.ShowPdf()
    v2 = v1.pdf_view(root,pdf_location=open(filename,"r"),width=77,height=100)
    v2.pack(pady=(0,0))


Button(root,text="Open PDF",command=browseFiles,width=50,font='arial,30',bd=4).pack()

root.mainloop()

