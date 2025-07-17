import tkinter
import requests

app = tkinter.Tk()
app.title("Test Tk App")
app.geometry("400x300")

url = "https://example.com"

def get_request_status_code():
    res = requests.get(url)
    print(res.status_code)

btn = tkinter.Button(app, text="Request", padx=10, pady=10, command=get_request_status_code)
btn.pack()

app.mainloop()