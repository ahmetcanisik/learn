#!/usr/bin/env python3
from frontend.gui import LoginRegisterApp

def main():
    app = LoginRegisterApp()
    app.title("Login-Register")
    app.geometry("400x500")
    app.mainloop()
    

if __name__ == "__main__":
    main()