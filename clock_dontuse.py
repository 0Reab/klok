import customtkinter
import datetime

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

root = customtkinter.CTk()
root.geometry("1200x800")

current_time = datetime.datetime.now()
time_start = list()
time_stop = list()
sessions_tracked = list()

def start_tracking():
    output_string.set(datetime.datetime.now())

    if len(time_start) <= len(time_stop):
        time_start.append("START " + str(datetime.datetime.now()))
        print(time_start)

def stop_tracking():
    output_string.set(datetime.datetime.now())

    if len(time_start) >= len(time_stop) or len(time_start) == 0:
        time_stop.append("END "+ str(datetime.datetime.now()))
        print(time_stop)

def trest():
    print('lol')

output_string = customtkinter.StringVar()
#--------------------------------------------------------------------------------------------------------------
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20,
           padx=60,
           fill='both',
           expand=True)
#--------------------------------------------------------------------------------------------------------------
label = customtkinter.CTkLabel(master=frame,
                               text="Klok",
                               font=("Roboto", 24))
label.pack(pady=12, padx=10)
#--------------------------------------------------------------------------------------------------------------
output_label = customtkinter.CTkLabel(master=frame,
                                      text="Output",
                                      font=("Calibri", 24),
                                      textvariable=output_string)
output_label.pack(padx=10, pady=12)
#--------------------------------------------------------------------------------------------------------------
button_start = customtkinter.CTkButton(master=frame,
                                       text="Start Tracking",
                                       font=("Roboto", 18),
                                       command=start_tracking)
button_start.pack(padx=10, pady=12)
#--------------------------------------------------------------------------------------------------------------
button_stop = customtkinter.CTkButton(master=frame,
                                      text="Stop Tracking",
                                      font=("Roboto", 18),
                                      command=stop_tracking)
button_stop.pack(padx=10, pady=12)
#--------------------------------------------------------------------------------------------------------------
checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember")
checkbox.pack(padx=10, pady=12)
#--------------------------------------------------------------------------------------------------------------
root.mainloop()