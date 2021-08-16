from tkinter import *
import sqlite3

root = Tk()
root.title("Database Address Book")
root.iconbitmap("D:/hello.ico")

conn = sqlite3.connect("Address_book.db")
c = conn.cursor()

c.execute("""CREATE TABLE addresses(
        first_name text,
        last_name text,
        address text,
        city text,
        state text,
        zipcode integer
) """)
print("Table created succesfully")


conn.commit()

conn.close()

mainloop()