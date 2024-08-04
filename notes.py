import tkinter as tk
import socket
from threading import Thread
from idlelib.percolator import Percolator
from idlelib.colorizer import ColorDelegator

sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(("127.0.0.1",12430))

root=tk.Tk()
root.configure(bg='black')
#root.overrideredirect(True)
#root.geometry("810x454+0+0")

print("notes")
tx=tk.Text(root,font=("times new roman",12),bd=0,bg="black",fg="#87ceeb",height=15,width=65,highlightthickness=0)
tx.grid(row=0,column=0,sticky="nsew")
#Percolator(tx).insertfilter(ColorDelegator())
root.grid_rowconfigure(0,weight=1)
root.grid_columnconfigure(0,weight=1)

def ent():
	root.focus_set()
	root.winfo_children()[0].config(state='normal')
def gt():
	root.winfo_children()[0].config(state='disable')


def _gt_dt(sock):
    while root:
        dt = sock.recvfrom(2046)
        #print(dt)
        #print(dt[0].decode())
        dt=dt[0].decode()
        with open(dt,'r') as f:
            try:
                d=f.read()
            except:
                d="Error in reading the file"
        tx.delete(0.0,"end")
        tx.insert('end',d)
        
    
th=Thread(target=_gt_dt,args=[sock,])
th.start()
root.bind("<Enter>",lambda x:ent)
root.bind("<Leave>",lambda x:gt)

root.mainloop()
root=False
