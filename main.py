import os
import time as t
import subprocess
import tkinter
from tkinter import StringVar, ttk, font
from tkinter.messagebox import showinfo
from PIL import Image,ImageTk
import webbrowser

time=0
def donation():
    webbrowser.open_new("https://bit.ly/3T874L8")
def operator(operation_type=None):
    global time
    
    if operation_type:
        os.system("shutdown -a")
    else:
        alignment_result = alignment_var.get()
        if alignment_result=="Shutdown":
            command="shutdown -s -t " + str(time)
            os.system(command)
        elif alignment_result=="Restart":
            command="shutdown -r -t " + str(time)
            os.system(command)
        """
        elif alignment_result=="Log-out":
            command="timeout -t " + str(time) + " /nobreak && shutdown -l"
            f = open("operation.bat", "w")
            f.write(command)
            f.close()
            print(os.getcwdb())
            tmp=os.path.dirname(os.path.abspath(__file__))
            try:
                subprocess.run(command, capture_output=True)
                #os.spawnl(os.P_DETACH, command)
            except Exception as inst:
                print(type(inst))    # the exception instance
                print(inst.args)     # arguments stored in .args
                print(inst)          # __str__ allows args to be printed directly,
                                    # but may be overridden in exception subclasses
            print("Executed!")
        elif alignment_result=="Hybernate":
            command="timeout -t " + str(time) + " /nobreak && shutdown -h"
            f = open("operation.bat", "w")
            f.write(command)
            f.close()
            tmp=os.path.dirname(os.path.abspath(__file__))
            try:
                #tmp_process=subprocess.call([r"{}\operation.bat".format(tmp)])
                #os.spawnl(os.P_DETACH, [r"{}\operation.bat".format(tmp)])
                print(type(time))
                print("sleeping for ", str(time))
                t.sleep(time)
                print("slept")
                os.system("shutdown -h -f")
            except:
                print("An error occured")
            print("Executed!")
        """
def replace_ops_str():
    alignment_result = alignment_var.get()
    if alignment_result=="Shutdown":
        operation_name="shutdown"
    elif alignment_result=="Restart":
        operation_name="restart"
    """    
    elif alignment_result=="Log-out":
        operation_name="log-out"
    elif alignment_result=="Hybernate":
        operation_name="hybernation"
    """
    tmp_str=user_receiving_text.get()
    for i in ["shutdown", "restart"]:
        tmp_str = tmp_str.replace(i, operation_name)
    user_receiving_text.set(tmp_str)

def timer(operation_string, requested_time):
    global time_string
    global time
    time_string = operation_string
    time=requested_time
    operation_name=""
    alignment_result = alignment_var.get()
    if alignment_result=="Shutdown":
        operation_name="shutdown"
    elif alignment_result=="Restart":
        operation_name="restart"
    """
    elif alignment_result=="Log-out":
        operation_name="log-out"
    elif alignment_result=="Hybernate":
        operation_name="hybernation"
    """
    #print("time is: ",time)
    if time_string!="Immediately":
        user_receiving_text.set("There will be a " + operation_name + " in " + time_string.lower()+".")
    else:
        user_receiving_text.set("There will be a " + operation_name + " " + time_string.lower()+".")

def time_validator(selected_time_raw_value, selected_time_unit):
    global time_string
    global time
    selected_time_raw_value=int(float(selected_time_raw_value))
    selected_time_value.set(selected_time_raw_value)
    valid=False
    operation_name=""
    alignment_result = alignment_var.get()
    if alignment_result=="Shutdown":
        operation_name="shutdown"
    elif alignment_result=="Restart":
        operation_name="restart"
    """
    elif alignment_result=="Log-out":
        operation_name="log-out"
    elif alignment_result=="Hybernate":
        operation_name="hybernation"
    """
    if selected_time_raw_value>=0:
        if selected_time_unit=="Day(s)":
            if selected_time_raw_value>3650:
                showinfo("Invalid Request", "The request must be within the 10-year length.")
            else:
                valid=True
                time_string= str(selected_time_raw_value)+ " Day"
                time= selected_time_raw_value*86400
        elif selected_time_unit=="Hour(s)":
            if selected_time_raw_value>87600:
                showinfo("Invalid Request", "The request must be within the 10-year length.")
            else:
                valid=True
                time_string= str(selected_time_raw_value)+ " Hour"
                time= selected_time_raw_value*3600
        elif selected_time_unit=="Minute(s)":
            if selected_time_raw_value>5256000:
                showinfo("Invalid Request", "The request must be within the 10-year length.")
            else:
                valid=True
                time_string= str(selected_time_raw_value)+ " Minute"
                time= selected_time_raw_value*60     
        if valid:
            if selected_time_raw_value>1:
                time_string+="s"
            user_receiving_text.set("There will be a " + operation_name + " in " + time_string.lower()+".")
    else:
        showinfo("Invalid Request", "Please enter a positive value.")
    #print(time_string, time, selected_time_value, selected_time_unit)

def load_main_menu():
    root = tkinter.Tk()
    #widget_style = ttk.Style()
    #widget_style.configure(".", font=("HP Simplified", 12))
    widget_style = ttk.Style()
    widget_style.configure(".", background="blue")

    button_style = ttk.Style()
    button_style.configure("Wild.TRadiobutton",foreground="white", font="bold")

    button_style2 = ttk.Style()
    button_style2.configure("Wild.TButton",foreground="black", font="bold")

    root.resizable(False, False)
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    font1 = font.Font(family="HP Simplified", size=15)  
    font2 = font.Font(family="HP Simplified Light") 
    #sg = ttk.Sizegrip(root)
    #sg.grid(row=1, sticky=tkinter.SE)
    time_string = StringVar()
    #time_string.set=""
    root.geometry("800x450")
    root.configure(background="#232423")
    root.title("Shutdown Wizard")
    root.iconbitmap("SW.ico")


    #root.update_idletasks()
    #root.overrideredirect(True)
    #button_border = tkinter.Frame(root, highlightbackground = "black", highlightthickness = 2, bd=0)
    button_immediately = ttk.Button(root, text="Immediately", command=lambda: timer("Immediately",0),width=26).place(x=35,y=30)
    button_1_minute = ttk.Button(root, text="1 Minute", command=lambda: timer("1 Minute",60)).place(x=35,y=70)
    button_5_minutes = ttk.Button(root, text="5 Minutes", command=lambda: timer("5 Minutes",300)).place(x=35,y=110)
    button_15_minutes = ttk.Button(root, text="15 Minutes", command=lambda: timer("15 Minutes",900)).place(x=35,y=150)
    button_30_minutes = ttk.Button(root, text="30 Minutes", command=lambda: timer("30 Minutes",1800)).place(x=35,y=190)
    button_45_minutes = ttk.Button(root, text="45 Minutes", command=lambda: timer("45 Minutes",2700)).place(x=35,y=230)
    button_1_hour = ttk.Button(root, text="1 Hour", command=lambda: timer("1 Hour",3600)).place(x=155,y=70)
    button_2_hours = ttk.Button(root, text="2 Hours", command=lambda: timer("2 Hours",7200)).place(x=155,y=110)
    button_8_hours = ttk.Button(root, text="8 Hours", command=lambda: timer("8 Hours",28800)).place(x=155,y=150)
    button_12_hours = ttk.Button(root, text="12 Hours", command=lambda: timer("12 Hours",43200)).place(x=155,y=190)
    button_24_hours = ttk.Button(root, text="24 Hours", command=lambda: timer("24 Hours",86400)).place(x=155,y=230)
    separator = ttk.Separator(root, orient='vertical').place(x=300, y=0, width=5, height=450)
    separator2 = ttk.Separator(root, orient='horizontal').place(x=35, y=290, width=220, height=5)
    separator3 = ttk.Separator(root, orient='horizontal').place(x=35, y=315, width=220, height=5)
    label_or = ttk.Label(root, text="OR", foreground="white").place(x=133, y=295)
    #l1 = ttk.Label(text="OR", style="BW.TLabel").place(x=133,y=295)
    selected_time_value = StringVar(value=1)
    spin_box = ttk.Spinbox(root, from_=1, to=315360000, justify="center", increment=1, textvariable=selected_time_value, wrap=True).place(x=35, y= 350, width=100)
    selected_time_unit = StringVar()
    selected_time_unit.set("Minute(s)")
    time_unit_combo_box = ttk.Combobox(root, textvariable=selected_time_unit)
    time_unit_combo_box["values"]=["Minute(s)","Hour(s)","Day(s)"]
    time_unit_combo_box["state"]="readonly"
    time_unit_combo_box.place(x=155, y= 350, width=99)
    button_apply_manual_timer = ttk.Button(root, text="Set", command=lambda: time_validator(selected_time_value.get(), selected_time_unit.get()), width=26).place(x=35,y=385)

    label_ui_sentence = ttk.Label(root, text = "Welcome to the Shutdown Wizard!", foreground="white", font= font1, width=37, anchor="n").place(x=355, y= 30)
    #label_frame = ttk.LabelFrame(root, text='Operation').place(x=355,y=30)
    separator4 = ttk.Separator(root, orient='horizontal').place(x=355, y=213, width=411, height=30)
    global alignment_var
    alignment_var = StringVar(None, "Shutdown")
    global user_receiving_text
    user_receiving_text = StringVar()
    user_receiving_text.set("...Awaiting selections...")
    label_operation_information = ttk.Label(root, textvariable = user_receiving_text, foreground="white", font= font1, width=37, anchor="n").place(x=355, y= 180)
    radio_restart = ttk.Radiobutton(root, text="Restart", value="Restart",style="Wild.TRadiobutton", variable=alignment_var, command=lambda: replace_ops_str()).place(x=460, y=215)
    radio_shutdown = ttk.Radiobutton(root, text="Shutdown", value="Shutdown",style="Wild.TRadiobutton", variable=alignment_var, command=lambda: replace_ops_str()).place(x=565, y=215)
    #radio_log_out = ttk.Radiobutton(root, text="Log-out", value="Log-out", variable=alignment_var, command=lambda: replace_ops_str()).place(x=565, y=215)
    #radio_hybernate = ttk.Radiobutton(root, text="Hybernate", value="Hybernate", variable=alignment_var, command=lambda: replace_ops_str()).place(x=670, y=215)
    button_abort = ttk.Button(root, text="Abort Any Operation", command=lambda: operator("abort")).place(x=510, y=253, width= 150, height=40)
    button_run = ttk.Button(root, text="Confirm", command=lambda: operator()).place(x=668, y=253, height=40)

    label_ui_sentence = ttk.Button(root, text = "Please Support \U0001F5A4",style="Wild.TButton", width=20, command=lambda: donation()).place(x=575, y= 385)
    #print("time in mainloop: ",time)
    root.mainloop()
def operation_scheduled():
    return False

if __name__ == '__main__':
    if operation_scheduled():
        pass
    else:
        load_main_menu()