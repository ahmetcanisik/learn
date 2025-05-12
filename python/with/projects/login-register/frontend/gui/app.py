import customtkinter
from frontend.user import UserAuth
from frontend.gui.components import LoginFrame


class LoginRegisterApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.user = UserAuth()

        self.title("LoginRegister")
        self.geometry("400x220")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.registerButton = customtkinter.CTkButton(
            self, text="register", command=self.registerButton_callback
        )
        self.registerButton.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        self.loginButton = customtkinter.CTkButton(
            self, text="login", command=self.loginButton_callback
        )
        self.loginButton.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

    def registerButton_callback(self):
        self.registerButton.grid_remove()
        self.loginButton.grid_remove()

        self.loginFrame = LoginFrame(self)
        self.loginButton.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        print("clicked button")

    def loginButton_callback(self):
        self.registerButton.grid_remove()
        self.loginButton.grid_remove()

        self.loginFrame = LoginFrame(self)
        self.loginButton.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        print("clicked button")
