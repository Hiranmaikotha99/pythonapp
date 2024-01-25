import sqlite3

class Database:
    def __init__(self,db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS Students (id INTEGER PRIMARY KEY, StudentID INTEGER, Firstname text, Lastname text, Courses text, Grade text)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM Students")
        rows = self.cur.fetchall()
        return rows

    def insert(self, StudentID, FirstName, LastName,Courses, Grade):
        self.cur.execute("INSERT INTO Students VALUES (NULL, ?, ?, ?, ? , ? )",
                         ( StudentID, FirstName, LastName,Courses, Grade))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM students WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, StudentID, FirstName, LastName, Courses, Grade):
        self.cur.execute("UPDATE students SET StudentID = ?, FirstName = ?, LastName = ?, Courses = ?, Grade = ? WHERE ID = ? ",
                         ( StudentID, FirstName, LastName, Courses, Grade, id ))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
        
db = Database('studentmanagement.db')
db.insert( "55" , "Hiranmai", "Kotha", "Data Networks, Mobile Technologies, Next generation", "89%")
db.insert(" 56","rutul", "Joshi", "Data Networks, Mobile Technologies, Next generation", "86%")
db.insert( "57" , "Kiran", "Bala", "Data Networks, Mobile Technologies, Next generation", "85%")