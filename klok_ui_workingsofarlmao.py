import customtkinter
import datetime
import pywinstyles

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

root = customtkinter.CTk()
root.geometry("1200x800")
#pywinstyles.apply_style(root, "acrylic")

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
frame.pack(pady=10,
           padx=20,
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

frame2 = customtkinter.CTkFrame(master=frame)
frame2.pack(pady=0,
           padx=70,
           fill='both',
           expand=True)

progressbar = customtkinter.CTkProgressBar(master=frame2,
                                           orientation="vertical",
                                           mode="determinate",
                                           width=100,
                                           height=70,
                                           corner_radius=2,
                                           progress_color="green")
progressbar.pack()
progressbar.place(x=80, y=40)
progressbar2 = customtkinter.CTkProgressBar(master=frame2,
                                           orientation="vertical",
                                           mode="determinate",
                                           width=100,
                                           height=70,
                                           corner_radius=2,
                                           progress_color="green")
progressbar2.pack()
progressbar2.place(x=200, y=40)

progressbar3 = customtkinter.CTkProgressBar(master=frame2,
                                           orientation="vertical",
                                           mode="determinate",
                                           width=100,
                                           height=70,
                                           corner_radius=2,
                                           progress_color="green")
progressbar3.pack()
progressbar3.place(x=320, y=40)

progressbar4 = customtkinter.CTkProgressBar(master=frame2,
                                           orientation="vertical",
                                           mode="determinate",
                                           width=100,
                                           height=70,
                                           corner_radius=2,
                                           progress_color="green")
progressbar4.pack()
progressbar4.place(x=440, y=40)

progressbar5 = customtkinter.CTkProgressBar(master=frame2,
                                           orientation="vertical",
                                           mode="determinate",
                                           width=100,
                                           height=70,
                                           corner_radius=2,
                                           progress_color="green")
progressbar3.pack()
progressbar3.place(x=320, y=40)

def progressbar(x_value, y_value):
    progressbar = customtkinter.CTkProgressBar(master=frame2,
                                               orientation="vertical",
                                               mode="determinate",
                                               width=100,
                                               height=70,
                                               corner_radius=2,
                                               progress_color="green")
    progressbar.pack()
    progressbar.place(x=x_value, y=y_value)

progressbar()


root.mainloop()