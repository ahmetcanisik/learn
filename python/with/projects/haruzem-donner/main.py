import tkinter
from selenium import webdriver

app = tkinter.Tk()
app.title("Haruzem Donner")
app.geometry("300x200")

button_frame = tkinter.Frame(app)
button_frame.pack(pady=20)

start_button = tkinter.Button(button_frame, text="Start", command=lambda: print("Start clicked!"))
start_button.pack(side="left", padx=10)

stop_button = tkinter.Button(button_frame, text="Stop", command=lambda: print("Stop clicked!"))
stop_button.pack(side="left", padx=10)

app.mainloop()