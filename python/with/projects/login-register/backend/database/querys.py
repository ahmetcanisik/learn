from . import connect_db


def create_user_table():
    execute_query(
        """CREATE TABLE IF NOT EXISTS Users ( 
        id INTEGER PRIMARY KEY,
        username VARCHAR(50) UNIQUE NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password VARCHAR(72) NOT NULL,
        role VARCHAR(5) NOT NULL,
        login_date DATETIME NOT NULL 
    );"""
    )


def execute_query(query, params=()):
    """SQL sorgularını çalıştıran fonksiyon"""
    conn = connect_db()
    cur = conn.cursor()

    try:
        cur.execute(query, params)

        # Eğer SELECT sorgusu ise, sonucu döndür
        if query.lstrip().upper().startswith("SELECT"):
            res = cur.fetchall()
        else:
            conn.commit()  # Değişiklikleri kaydet
            res = None  # SELECT dışı sorgular sonuç döndürmez

    except Exception as e:
        print(f"Database error: {e}")
        res = None

    finally:
        conn.close()  # Bağlantıyı kapat

    return res
