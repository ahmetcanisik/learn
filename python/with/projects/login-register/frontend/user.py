from backend.auth import login, register

class UserAuth:
    def __init__(self):
        self.logged_user = {
            "username": None,
            "password": None
        }
    
    def sign_in(self):
        print("Login")
        username = input("Username or Email: ")
        password = input("Password: ")
        
        self.logged_user = login(username=username, password=password)
        
        if self.logged_user["username"] is not None:
            print(f"Hello {self.logged_user["username"]}")
        else:
            print(f"Böyle bir kullanıcı bulunamadı Can't find the {username}")
            want_to_signup = input("You want to Sign up now? (y/n) ").lower().strip()
            
            while True:
                if want_to_signup == "y" or want_to_signup == "yes" or want_to_signup == "":
                    self.sign_up()
                    break
                elif want_to_signup == "n" or want_to_signup == "no":
                    self.sign_in()
                    break
                else:
                    continue
    
    def sign_up(self):
        username = None
        email = None
        password = None
        
        while username == None:
            username = input("Username: ")
            
            if len(username) > 50:
                continue
            else:
                break
        
        while email == None:
            email = input("Email: ")
            
        while password == None:
            password = input("Password: ")
            if len(password) > 72:
                continue
            else:
                break
        
        register(username=username, email=email, password=password)
        print("Your registiration completed!")