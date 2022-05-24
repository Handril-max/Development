#py:3
#Handrilsoft
#Abot system windows cartoon
import time
def display_show(root,startint,endint,sw,sh,wid,win_hig):#in
    for h in range(startint,endint):
        i = h*(100/endint)
        wc_wid = (wid/100)*i
        wc_hig = (win_hig/100)*i
        x = (((sw/i)*i)-wc_wid)/2
        y = (sh-wc_hig)/(i/50)
        root.geometry('%dx%d+%d+%d'%(wc_wid,wc_hig,x,y))
        root.update()

def to_hide(root,startint,endint,sw,sh,wid,win_hig):#hide
    for h in range(startint,endint)[::-1]:
        i = h*(100/endint)
        wc_wid = (wid/100)*i
        wc_hig = (win_hig/100)*i
        x = (((sw/i)*i)-wc_wid)/2
        y = (sh-wc_hig)/(i/50)
        root.geometry('%dx%d+%d+%d'%(wc_wid,wc_hig,x,y))
        root.update()

def to_show_tool(root):#tool_win_sow
    for h in range(0, 100, 10):
        root.wm_attributes("-alpha", h/100)  # 透明度
        root.update()
        time.sleep(0.013)

def to_hide_tool(root):#tool_win_hode
    for h in range(0, 100, 10)[::-1]:
        root.wm_attributes("-alpha", h/100)  # 透明度
        root.update()
        time.sleep(0.013)


def intend_display(root,startint,endint,sw,sh,wid,win_hig):#desteroy
    for h in range(startint,endint)[:-1]:
        i = h*(100/endint)
        wc_wid = (wid/100)*i
        wc_hig = (win_hig/100)*i
        x = (((sw/i)*i)-wc_wid)/2
        y = (sh-wc_hig)/(i/50)
        root.geometry('%dx%d+%d+%d'%(wc_wid,wc_hig,x,y))
        root.update()
        
    
