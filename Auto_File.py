import tkinter as tk
from tkinter import *
import os

root = Tk()
root.iconbitmap(r"\\Ctc-app01\Test_Center\Component\2_Lab Report\2_5_待写报告\CTCF0950 马乐义\签名" + "\\" + "Control_Panel.ico")
root.title("文件生成器")
root.geometry("500x100+30+20")
root.resizable(width=True, height=True)

group = LabelFrame(root, text="", font=("黑体", 12))
group.grid(row=0, column=2, pady=10, sticky=N)

Label(group, text="路径 :").grid(row=0, column=0)
var1 = StringVar()
e1 = Entry(group, textvariable=var1, width=50)
e1.grid(row=0, column=1, pady=5)


def create_file():
    R_path = e1.get()
    os.makedirs(R_path + './DATA')
    os.makedirs(R_path + './DATA'+ './Before')
    os.makedirs(R_path + './DATA' + './After')
    os.makedirs(R_path + './DATA'+ './Setup')
    os.makedirs(R_path + './DATA' + './A')
    os.makedirs(R_path + './DATA' + './B')
    os.makedirs(R_path + './DATA' + './S')

Button(group,text="生成文件",command=create_file).grid(row=0,column=2,padx=5)

group.grid(sticky=NW, padx=20, pady=30)

mainloop()
