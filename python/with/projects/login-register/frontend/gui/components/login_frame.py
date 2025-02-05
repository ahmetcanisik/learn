import customtkinter

class LoginFrame:
    def __init__(self, master):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        
        self.title = customtkinter.CTkLabel(self, text="Login", fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")
        
        self.usernameInput = customtkinter.CTkTextbox(self, corner_radius=6)
        self.usernameInput.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="ew")