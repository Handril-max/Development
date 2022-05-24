# py:3
# HandrilOS Handrilsoft2021
# HFS_tkinter_GUImode_of_Hanchen_Architecture
#app window engine
# Handril PC screen
# -*- coding:utf-8 -*-
import os
import sys
import time
from turtle import title
import psutil
import six
import shutil
import string
import glob
import webbrowser
import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.messagebox
from PIL import ImageTk, Image, ImageFilter
from tkinter import filedialog
from shutil import *
import sys_win_cartoon as swc
winnum = 0
            
class HandrilApp(tk.Tk):
    root_x, root_y, abs_x, abs_y = 0, 0, 0, 0
    width, height = None, None

    def __init__(self, title,topmost=True, alpha=1, bg="#F0F0F0", width=None, height=None):
        super().__init__()
        self["bg"] = bg
        self.width, self.height = width, height
        self.title = title
        self.overrideredirect(True)
        self.wm_attributes("-alpha", alpha)  # 透明度
        self.wm_attributes("-toolwindow", True)  # 置为工具窗口
        self.wm_attributes("-topmost", topmost)  # 永远处于顶层
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        self.config(cursor='circle')
        self.bind('<Button-3>',self._startmove,add='+')#移动
        self.bind('<B3-Motion>', self._on_move,add='+')
        menubar = tk.Menu(self)
        filemenu = tk.Menu(menubar, tearoff=0)  # tearoff意为下拉
        def max():
            self.geometry("%sx%s+%s+%s" % (sw,sh-25,0,25))
        def hide():
            swc.to_hide(self,1,100,sw,sh,sw/2,sh/2)
        def reshow():
            swc.display_show(self,1,100,sw,sh,sw/2,sh/2)
        def jump2():
            bottomtype.destroy()
            swc.intend_display(self,1,40,sw,sh,sw/2,sh/2)
            self.destroy()
        def jump1(_):
            jump2()
        filemenu.add_command(label='最大化',command=max)
        filemenu.add_command(label='最小化',command=hide)
        filemenu.add_command(label='恢复窗口',command=reshow)
        filemenu.add_command(label='关闭窗口',command=jump2)
        # 创建编辑菜单
        editmenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label=self.title,menu=filemenu)
        self.config(menu=menubar)
        swc.display_show(self,1,100,sw,sh,sw/2,sh/2)
        #小横条
        
        bottomtype = tk.Canvas(self,width=sw/6,height=5,bg='black')
        bottomtype.bind('<Leave>',jump1)
        bottomtype.pack(side='bottom')
        
        def win_close(_):
            #cpk.unpathfilewrite("apppath.psw", "w", "标签")
            swc.intend_display(self,1,40,sw,sh,sw/2,sh/2)
            self.destroy()
        self.bind('<Alt-F4>',win_close)


    def _startmove(self,event):#记录开始移动的坐标
        self.startx=event.x
        self.starty=event.y
    def _on_move(self, event):
        self.geometry("+%s+%s" % (self.winfo_x()+(event.x-self.startx),self.winfo_y()+(event.y-self.starty)))
                    
