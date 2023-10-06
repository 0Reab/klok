import tkinter as tk
from tkinter import ttk
import datetime
from tkcalendar import Calendar
import matplotlib.pyplot as plt
import numpy as np


# using now() to get current time
current_time = datetime.datetime.now()
#print(current_time)
#time_start = current_time
#time_end = current_time
time_tracked_start = list()
time_tracked_stop = list()
sessions_tracked = list()


def start_tracking():
    time_start = output_string.set(datetime.datetime.now())

    if time_tracked_start.__len__() <= time_tracked_stop.__len__():
        time_tracked_start.append("START " + str(datetime.datetime.now()))
        print(time_tracked_start)


def stop_tracking():
    time_end = output_string.set(datetime.datetime.now())

    if time_tracked_start.__len__() >= time_tracked_stop.__len__() or time_tracked_start.__len__() == 0:
        time_tracked_stop.append("END "+ str(datetime.datetime.now()))
        print(time_tracked_stop)
    #time_end = current_time

def cal():
    cal = Calendar(selectmode="day")


window = tk.Tk()
window.title("Clock")
window.geometry("1000x700")

title_label = ttk.Label(master=window,
                        text=current_time,
                        font="Calibri 24 bold")

title_label.pack()

input_frame = ttk.Frame(master=window)
entry = ttk.Entry(master=input_frame)
button_start = ttk.Button(master=input_frame,
                          text="Start tracking",
                          command=start_tracking)

button_stop = ttk.Button(master=input_frame,
                         text="Stop tracking",
                         command=stop_tracking)

output_string = tk.StringVar()
output_label = ttk.Label(master=window,
                         text="Output",
                         font="Calibri 24",
                         textvariable=output_string)
# button that displays the plot
plot_button = ttk.Button(master=window,
                     command=plt,
                         width=10,
                     text="Plot")

# place the button
# in main window
plot_button.pack()

input_frame.pack(pady=10)
entry.pack(side="left", padx=10)
button_start.pack(side="left", padx=10)
button_stop.pack()
output_label.pack(pady=5)
#w.pack(side="left")

window.mainloop()