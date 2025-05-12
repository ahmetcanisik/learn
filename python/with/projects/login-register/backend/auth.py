from backend.database.querys import create_user_table, execute_query


def login(username, password):
    create_user_table()

    res = execute_query(
        f"SELECT username, password FROM Users WHERE (username = ? OR email = ?) AND password = ?",
        (username, username, password),
    )

    if len(res) >= 0:
        usr, pw = (None, None)
        for r in res:
            usr, pw = r
        return {"username": usr, "password": pw}
    else:
        print("User not found!")
        return


def register(username, email, password):
    if username is not None and email is not None and password is not None:
        create_user_table()
        execute_query(
            f"INSERT INTO Users (username, email, password, role, login_date) VALUES (?, ?, ?, ?, (SELECT DATETIME()))",
            (username, email, password, "user"),
        )
        return {"username": username, "email": email, "password": password}
    else:
        print("Registiration failed!")
        return
