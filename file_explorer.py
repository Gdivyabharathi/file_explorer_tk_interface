import os
import psutil
import tkinter as tk
from tkinter import ttk
import socket
from threading import Thread
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
folder = chr(128193)
empty_folder = chr(128194)
file = chr(128196)
disc = chr(128436)
c_path=""
print("file_explorer")
def print_windows_volumes():
    partitions = psutil.disk_partitions()
    lt = []
    for partition in partitions:
        if 'cdrom' in partition.opts or partition.fstype == '':
            continue
        usage = psutil.disk_usage(partition.mountpoint)
        lt.append(f"{partition.device}\nT:{convert_bytes(usage.total)}\nU:{convert_bytes(usage.used)},F:{convert_bytes(usage.free)}\nP:{usage.percent}%")
    return lt

def convert_bytes(byte_size):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if byte_size < 1024.0:break
        byte_size /= 1024.0
    return f"{byte_size:.2f} {unit}"
def pop_win(e, tp, c=0, r=0):
    c, r = c, r
    if tp == disc:fsz = 30
    else:fsz = 20
    if len(e) > 20:lm = 15
    else:lm = 7
    def wrp(e):
        et = ""
        if len(e) > 10:et = e[:len(e)//2] + "\n" + e[len(e)//2:]
        else:et = e
        return et
    for i in enumerate(e):
        vlm = i[1].split("\n")[0]
        if c < lm:
            lb = tk.Label(inner_frame, text=tp, bg='black', fg='#87CEEB', font=("times new roman", fsz), anchor='center')
            lb.grid(row=r, column=c)
            lb1 = tk.Label(inner_frame, text=wrp(i[1]), font=("times new roman", 10), bg='black', fg='#87CEEB', anchor='center')
            lb1.grid(row=r+1, column=c)
            lb.bind("<Button-1>", lambda x, e=vlm: chk_fldrs(e))
            lb.bind("<Enter>", lambda x, e=lb: e.config(relief='raised'))
            lb.bind("<Leave>", lambda x, e=lb: e.config(relief='flat'))
            lb1.bind("<Button-1>", lambda x, e=vlm: chk_fldrs(e))
            lb1.bind("<Enter>", lambda x, e=lb1: e.config(relief='raised'))
            lb1.bind("<Leave>", lambda x, e=lb1: e.config(relief='flat'))
            c += 1
        elif c == lm:
            lb = tk.Label(inner_frame, text=tp, bg='black', fg='#87CEEB', font=("times new roman", fsz), anchor='center')
            lb.grid(row=r, column=c)
            lb1 = tk.Label(inner_frame, text=wrp(i[1]), font=("times new roman", 10), bg='black', fg='#87CEEB', anchor='center')
            lb1.grid(row=r+1, column=c)
            lb.bind("<Button-1>", lambda x, e=vlm: chk_fldrs(e))
            lb.bind("<Enter>", lambda x, e=lb: e.config(relief='raised'))
            lb.bind("<Leave>", lambda x, e=lb: e.config(relief='flat'))
            lb1.bind("<Button-1>", lambda x, e=vlm: chk_fldrs(e))
            lb1.bind("<Enter>", lambda x, e=lb1: e.config(relief='raised'))
            lb1.bind("<Leave>", lambda x, e=lb1: e.config(relief='flat'))
            c = 0
            r += 2
    return c, r

def snd_addr(adr):
    sock.sendto(adr.encode(),("127.0.0.1",12430))

def g_b(x):
    global c_path
    print(c_path)
    if len(c_path)>2:
        c_path="\\".join(c_path.split("\\")[:-1])
        chk_fldrs(v=0)
    else:
        c_path=''
        for i in inner_frame.winfo_children():
            i.destroy()
        pop_win(print_windows_volumes(), disc)
        
def chk_fldrs(e=None,v=1):
    global c_path
    if v==1:
        if ':' in e:c_path=c_path+e
        else:c_path=c_path+"\\"+e
        e=c_path
    else:
        e=c_path
    if os.path.isdir(c_path)==False:
        snd_addr(c_path)
        et = c_path.split("\\")[:-1]
        et= [i.replace("\\","") for i in et]
        c_path="\\".join(et)
        e=c_path
    else:
        ln = os.listdir(e)
        fldrs = [folder for folder in os.listdir(e) if os.path.isdir(os.path.join(e, folder))]
        fls = [folder for folder in os.listdir(e) if os.path.isdir(os.path.join(e, folder)) == False]
        for i in inner_frame.winfo_children():
            i.destroy()
        c, r = pop_win(fldrs, folder)
        pop_win(fls, file, c=c, r=r)
def on_mouse_wheel(event):
    if event.state == 8:
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
    elif event.state == 9:
        canvas.xview_scroll(int(-1 * (event.delta / 120)), "units")

t1,t2,t3=(2540+250,380+250),(699+250,221+250),(2313+250,470+250)
sz=450
t1=((t1[0]-sz)+440,t1[1]-sz)
t2=(t2[0]-sz,t2[1]-sz)
t3=(t3[0]-sz,t3[1]-sz)
d1=(f'-{t1[0]}',f'+{t1[1]}')
d2=(f'+{t2[0]}',f'+{t2[1]}')
d3=(f'+{t3[0]}',f'+{t3[1]}')

root = tk.Tk()
root.configure(background='black')
root.title("Scrollable Frame Example")
#root.overrideredirect(True)
max_canvas_width = 800
max_canvas_height = 300
canvas = tk.Canvas(root, bg="black", width=max_canvas_width, height=max_canvas_height,highlightthickness=0)
canvas.pack(side="left", fill="both", expand=True)
inner_frame = tk.Frame(canvas, bg="black")
canvas.create_window((0, 0), window=inner_frame, anchor="nw")
pop_win(print_windows_volumes(), disc)
inner_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.grid_propagate(False)
canvas.create_rectangle(0, 0, max_canvas_width, max_canvas_height, outline="white")
root.bind_all("<MouseWheel>", on_mouse_wheel)
root.bind("<BackSpace>",g_b)
root.bind("<Control-c>",lambda x: pop_win(print_windows_volumes(), disc))
root.mainloop()


