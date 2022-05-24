from enum import auto
from tkinter import *
import tkinter as tk
from sys_windoweng import *
import H_hardware_gethardware as gw

root = HandrilApp('Hardwear')
root['bg']='white'
entryframe = tk.Frame(root,height=10,bg='white')

funframe2 = tk.Frame(root,height=10,bg='white')
bottomframe = tk.Frame(root,height=10,bg='white')
title = tk.Label(root, text="设备管理&信息", height=1, bg='white',fg='black',font=('等线' ,18))
title.place(x=5,y=10)
#Entery
tip = tk.Label(entryframe, text="在此管理查看你的基本硬件信息", height=1, bg='white',fg='black')
tip.pack(side='left', padx=0, pady=5)

#fun mode
funframe = tk.Frame(root,height=10,bg='#003371')
toinfo = tk.Label(funframe, text=gw.GetHostName(), height=1, bg='#003371',fg='white',bd=0,font=('等线' ,11))
toinfo.pack(side='right', padx=5, pady=0)
funframe.place(x=5,y=75)

def cpu_info():
    funframe2 = tk.Frame(root,height=10,bg='white')
    toinfo = tk.Label(funframe2, text="处理器", height=1, bg='white',fg='black',bd=0,font=('等线' ,15))
    toinfo.pack(side='right', padx=5, pady=0)
    toinfo.config(cursor='hand2')
    funframe2.place(x=0,y=105)
    funframe3 = tk.Frame(root,height=10,bg='white')
    toinfo = tk.Label(funframe3, text=str(gw.GetOSInfo()), bg='white',fg='black',bd=0)
    toinfo.pack(side='right', padx=5, pady=0)
    funframe3.place(x=5,y=135)

    funframe4 = tk.Frame(root,height=10,bg='white')
    toinfo = tk.Label(funframe4, text=str(gw.GetCpuInfo.count()), bg='white',fg='black',bd=0)
    toinfo.pack(side='right', padx=5, pady=0)
    funframe4.place(x=5,y=155)

    funframe5 = tk.Frame(root,height=10,bg='white')
    toinfo = tk.Label(funframe5, text=str(gw.GetCpuInfo.thread()), bg='white',fg='black',bd=0)
    toinfo.pack(side='right', padx=5, pady=0)
    funframe5.place(x=5,y=175)

    funframe6 = tk.Frame(root,height=10,bg='white')
    toinfo = tk.Label(funframe6, text=str(gw.GetCpuInfo.freq()), bg='white',fg='black',bd=0)
    toinfo.pack(side='right', padx=5, pady=0)
    funframe6.place(x=5,y=195)

    funframe61 = tk.Frame(root,height=10,bg='white')
    toinfo = tk.Label(funframe61, bg='white',fg='black',bd=0)
    def info_t():
        toinfo.config(text='开机时间：'+str(round(gw.GetTimeStmp()))+'s')
        toinfo.after(1000,info_t)
    info_t()
    toinfo.pack(side='right', padx=5, pady=0)
    funframe61.place(x=5,y=215)

def mem_info():
    funframe7 = tk.Frame(root,height=10,bg='white')
    toinfo = tk.Label(funframe7, text="内存", height=1, bg='white',fg='black',bd=0,font=('等线' ,15))
    toinfo.pack(side='right', padx=5, pady=0)
    toinfo.config(cursor='hand2')
    funframe7.place(x=0,y=235)

    funframe8 = tk.Frame(root,height=10,bg='white')
    toinfo = tk.Label(funframe8, text=str(gw.GetTotalMemory()), bg='white',fg='black',bd=0)
    toinfo.pack(side='right', padx=5, pady=0)
    funframe8.place(x=5,y=265)

def net_info():
    funframe7 = tk.Frame(root,height=10,bg='white')
    toinfo = tk.Label(funframe7, text="网络", height=1, bg='white',fg='black',bd=0,font=('等线' ,15))
    toinfo.pack(side='right', padx=5, pady=0)
    toinfo.config(cursor='hand2')
    funframe7.place(x=0,y=285)

    funframe8 = tk.Frame(root,height=10,bg='white')
    toinfo = tk.Label(funframe8, text=str(gw.GetMacAddress()), bg='white',fg='black',bd=0,anchor='w',justify='left')
    toinfo.pack(side='right', padx=5, pady=0)
    funframe8.place(x=5,y=315)
    
mem_info()
cpu_info()
net_info()
entryframe.place(x=5,y=40)
bottomframe.pack(side='bottom')
root.mainloop()
    

