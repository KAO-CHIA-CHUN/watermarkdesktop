#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter, win32api, win32con, pywintypes,os
import socket
import getpass
import tkinter.font as tkFont
import platform
import time
import os
from PIL import Image, ImageTk 

exists=os.path.exists("C:/no.txtTxt")

'''
if exists:
    print("不添加注冊表")
else:
    name = 'translate'
    path = 'C:\\ProgramFiles(x86)\\LANDesk\\LDClient\\sdmcache\\soft\\showText.exe'
    KeyName = 'Software\\Microsoft\\Windows\\CurrentVersion\\Run'
    try:
        key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER, KeyName, 0, win32con.KEY_ALL_ACCESS)
        win32api.RegSetValueEx(key, name, 0, win32con.REG_SZ, path)
        win32api.RegCloseKey(key)
    except:
        print('添加失敗')
    print('註冊表添加成功！')
'''

hostname = socket.gethostname()
Compute_addr=socket.gethostbyname(hostname)
userName = getpass.getuser()
def gettime():
    timestr = time.strftime("%Y-%m-%d %H:%M\n\n\n\n\n\n\n\n")
    lb.configure(text=timestr)
    root5.after(1000, gettime)

show='TEST-TEST\n{}\n{}\n{}\n'.format(hostname , userName,Compute_addr)
root = tkinter.Tk()
im=Image.open("img.png")
img=ImageTk.PhotoImage(im)
width = win32api.GetSystemMetrics(0)
height = win32api.GetSystemMetrics(1)
root.overrideredirect(True)
root.attributes("-alpha", 0.2)
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
root.geometry("%dx%d" %(w, h))

root.lift()
root.wm_attributes("-topmost", True)
root.wm_attributes("-disabled", True)
root.wm_attributes("-transparentcolor", "white")
hWindow = pywintypes.HANDLE(int(root.frame(), 16))
exStyle = win32con.WS_EX_COMPOSITED | win32con.WS_EX_LAYERED | win32con.WS_EX_NOACTIVATE | win32con.WS_EX_TOPMOST | win32con.WS_EX_TRANSPARENT
win32api.SetWindowLong(hWindow, win32con.GWL_EXSTYLE, exStyle)

root1 = tkinter.Tk()
width = win32api.GetSystemMetrics(0)
height = win32api.GetSystemMetrics(1)
root1.overrideredirect(True)
root1.attributes("-alpha", 0.2)
w = root1.winfo_screenwidth()
h = root1.winfo_screenheight()
root1.geometry("%dx%d" %(w, h))

root1.lift()
root1.wm_attributes("-topmost", True)
root1.wm_attributes("-disabled", True)
root1.wm_attributes("-transparentcolor", "white")
hWindow = pywintypes.HANDLE(int(root1.frame(), 16))
exStyle = win32con.WS_EX_COMPOSITED | win32con.WS_EX_LAYERED | win32con.WS_EX_NOACTIVATE | win32con.WS_EX_TOPMOST | win32con.WS_EX_TRANSPARENT
win32api.SetWindowLong(hWindow, win32con.GWL_EXSTYLE, exStyle)

root2 = tkinter.Tk()
width = win32api.GetSystemMetrics(0)
height = win32api.GetSystemMetrics(1)
root2.overrideredirect(True)
root2.attributes("-alpha", 0.2)
w = root2.winfo_screenwidth()
h = root2.winfo_screenheight()
root2.geometry("%dx%d" %(w, h))

root2.lift() 
root2.wm_attributes("-topmost", True)
root2.wm_attributes("-disabled", True)
root2.wm_attributes("-transparentcolor", "white")
hWindow = pywintypes.HANDLE(int(root2.frame(), 16))
exStyle = win32con.WS_EX_COMPOSITED | win32con.WS_EX_LAYERED | win32con.WS_EX_NOACTIVATE | win32con.WS_EX_TOPMOST | win32con.WS_EX_TRANSPARENT
win32api.SetWindowLong(hWindow, win32con.GWL_EXSTYLE, exStyle)

root3 = tkinter.Tk()
width = win32api.GetSystemMetrics(0)
height = win32api.GetSystemMetrics(1)
root3.overrideredirect(True)
root3.attributes("-alpha", 0.2)
w = root3.winfo_screenwidth()
h = root3.winfo_screenheight()
root3.geometry("%dx%d" %(w, h))

root3.lift()
root3.wm_attributes("-topmost", True)
root3.wm_attributes("-disabled", True)
root3.wm_attributes("-transparentcolor", "white")
hWindow = pywintypes.HANDLE(int(root3.frame(), 16))
exStyle = win32con.WS_EX_COMPOSITED | win32con.WS_EX_LAYERED | win32con.WS_EX_NOACTIVATE | win32con.WS_EX_TOPMOST | win32con.WS_EX_TRANSPARENT
win32api.SetWindowLong(hWindow, win32con.GWL_EXSTYLE, exStyle)

root4 = tkinter.Tk()
width = win32api.GetSystemMetrics(0)
height = win32api.GetSystemMetrics(1)
root4.overrideredirect(True)
root4.attributes("-alpha", 0.2)
w = root4.winfo_screenwidth()
h = root4.winfo_screenheight()
root4.geometry("%dx%d" %(w, h))

root4.lift()
root4.wm_attributes("-topmost", True)
root4.wm_attributes("-disabled", True)
root4.wm_attributes("-transparentcolor", "white")
hWindow = pywintypes.HANDLE(int(root4.frame(), 16))
exStyle = win32con.WS_EX_COMPOSITED | win32con.WS_EX_LAYERED | win32con.WS_EX_NOACTIVATE | win32con.WS_EX_TOPMOST | win32con.WS_EX_TRANSPARENT
win32api.SetWindowLong(hWindow, win32con.GWL_EXSTYLE, exStyle)

root5 = tkinter.Tk()
width = win32api.GetSystemMetrics(0)
height = win32api.GetSystemMetrics(1)
root5.overrideredirect(True)
root5.attributes("-alpha", 0.2)
w = root5.winfo_screenwidth()
h = root5.winfo_screenheight()
root5.geometry("%dx%d" %(w, h))

root5.lift()
root5.wm_attributes("-topmost", True)
root5.wm_attributes("-disabled", True)
root5.wm_attributes("-transparentcolor", "white")
hWindow = pywintypes.HANDLE(int(root5.frame(), 16))
exStyle = win32con.WS_EX_COMPOSITED | win32con.WS_EX_LAYERED | win32con.WS_EX_NOACTIVATE | win32con.WS_EX_TOPMOST | win32con.WS_EX_TRANSPARENT
win32api.SetWindowLong(hWindow, win32con.GWL_EXSTYLE, exStyle)
lb = tkinter.Label(root5, text='', font=('Times','32','italic','normal'), fg='#708090',bg='white',width = 1000,height = 1000,anchor = 's')
lb.pack()
gettime()

root6 = tkinter.Tk()
width = win32api.GetSystemMetrics(0)
height = win32api.GetSystemMetrics(1)
root6.overrideredirect(True)
root6.attributes("-alpha", 0.2)
w = root6.winfo_screenwidth()
h = root6.winfo_screenheight()
root6.geometry("%dx%d" %(w, h))

root6.lift()
root6.wm_attributes("-topmost", True)
root6.wm_attributes("-disabled", True)
root6.wm_attributes("-transparentcolor", "white")
hWindow = pywintypes.HANDLE(int(root6.frame(), 16))
exStyle = win32con.WS_EX_COMPOSITED | win32con.WS_EX_LAYERED | win32con.WS_EX_NOACTIVATE | win32con.WS_EX_TOPMOST | win32con.WS_EX_TRANSPARENT
win32api.SetWindowLong(hWindow, win32con.GWL_EXSTYLE, exStyle)

tkinter.Label(root,image=img, fg='#708090',bg='white',width = 1920,height = 1080,anchor = 'nw').pack() #左上
tkinter.Label(root1,text=show, font=('Times','32','italic','normal'), fg='#708090', bg='white',width = 1000,height = 1000,anchor = 'se').pack() #左下
tkinter.Label(root2,text=show, font=('Times','32','italic','normal'), fg='#708090', bg='white',width = 1000,height = 1000,anchor = 'ne').pack() #右上
tkinter.Label(root3,text=show, font=('Times','32','italic','normal'), fg='#708090', bg='white',width = 1000,height = 1000,anchor = 'sw').pack() #右下
tkinter.Label(root4,text=show, font=('Times','32','italic','normal'), fg='#708090', bg='white',width = 1000,height = 1000,anchor = 'center').pack() #中間
tkinter.Label(root6,text=show, font=('Times','32','italic','normal'), fg='#708090', bg='white',width = 1000,height = 1000,anchor = 'nw').pack() #左上


if exists:
    print("不顯示")
else:
    root.mainloop()
    root1.mainloop()
    root2.mainloop()
    root3.mainloop()
    root4.mainloop()
    root5.mainloop()
    root6.mainloop()

