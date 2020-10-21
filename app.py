from tkinter import *
from tkinter.ttk import Combobox
import tkinter.messagebox
import subprocess
import threading

class Googles:
    def __init__(self,root):
        self.root=root
        self.root.title("Wifi and password")
        self.root.geometry("500x405")
        self.root.iconbitmap("logo1012.ico")
        self.root.resizable(0,0)

    


#=================================================================================#

        def clear():
            
            text.delete("1.0","end")

        def searchs():
            try:
                with open("C:/TEMP/wifi.txt","w") as f:
                    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
                    profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
                    f.write("{:<30}| {:<}".format("Wi-Fi Name", "Password")+"\n") 
                    f.write("----------------------------------------------"+"\n") 
                    for i in profiles:
                        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
                        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
                        try:
                            f.write("{:<30}=  {:<}".format(i, results[0])+"\n\n")
                        except IndexError:
                            f.write("{:<30}=  {:<}".format(i, "")+"\n\n")

                    
                    pass
                with open("C:/TEMP/wifi.txt","r") as f:
                    text.insert("end",f.read())

                
            except Exception as e:
                #print(e)
                tkinter.messagebox.showerror("Error","Please Enter only Domain Name")

        def thread_search():
            t1=threading.Thread(target=searchs)
            t1.start()
                

#==================================================================================#
        def on_enter1(e):
            but_search['background']="black"
            but_search['foreground']="cyan"
  
        def on_leave1(e):
            but_search['background']="SystemButtonFace"
            but_search['foreground']="SystemButtonText"

        def on_enter2(e):
            but_clear['background']="black"
            but_clear['foreground']="cyan"
  
        def on_leave2(e):
            but_clear['background']="SystemButtonFace"
            but_clear['foreground']="SystemButtonText"

#==================================================================================#
        mainframe=Frame(self.root,width=500,height=405,bd=3,relief="ridge")
        mainframe.place(x=0,y=0)

        firstframe=Frame(mainframe,width=494,height=100,bd=3,relief="ridge")
        firstframe.place(x=0,y=0)

        secondframe=Frame(mainframe,width=494,height=297,bd=3,relief="ridge")
        secondframe.place(x=0,y=100)

#================================firstframe===================================================#

        lab_frame=LabelFrame(firstframe,width=488,height=95,text="Wifi and password",bg="#89b0ae",fg="white")
        lab_frame.place(x=0,y=0)
#==============================================================================================#


        but_search=Button(lab_frame,width=13,text="Wifi",font=('times new roman',12),cursor="hand2",command=thread_search)
        but_search.place(x=50,y=30)
        but_search.bind("<Enter>",on_enter1)
        but_search.bind("<Leave>",on_leave1)

        but_clear=Button(lab_frame,width=13,text="Clear",font=('times new roman',12),cursor="hand2",command=clear)
        but_clear.place(x=300,y=30)
        but_clear.bind("<Enter>",on_enter2)
        but_clear.bind("<Leave>",on_leave2)

#=============================================================================================================#
        scol=Scrollbar(secondframe,orient="vertical")
        scol.place(relx=1, rely=0, relheight=1, anchor='ne')
        
        text=Text(secondframe,height=15,width=58,font=('times new roman',12),yscrollcommand=scol.set,relief="sunken",bd=3,fg="black")      
        text.place(x=0,y=0)
        scol.config(command=text.yview)



if __name__ == "__main__":
    root=Tk()
    app=Googles(root)
    root.mainloop()