from contextlib import contextmanager
import sqlite3


class Database:

    def connect_to_db(self):
        self.conn = sqlite3.connect("sqlite.db", check_same_thread=False)
        self.cur = self.conn.cursor()

    def create_table(self):
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS patients (
                id INTEGER PRIMARY KEY,
                name TEXT,
                age INTEGER
            )
        """)

    def get_all(self) -> list:
        self.cur.execute("SELECT * FROM patients")
        rows = self.cur.fetchall()
        return [self._row_to_dict(row) for row in rows]

    def get(self, id: int) -> dict | None:
        self.cur.execute("""
            SELECT * FROM patients WHERE id = ?
        """, (id,))
        row = self.cur.fetchone()
        return self._row_to_dict(row) if row else None

    def create(self, item) -> int:
        self.cur.execute("SELECT MAX(id) FROM patients")
        result = self.cur.fetchone()
        new_id = (result[0] or 0) + 1

        data = item.model_dump(exclude={"appointments"})
        data["id"] = new_id

        self.cur.execute("""
            INSERT INTO patients (id, name, age)
            VALUES (:id, :name, :age)
        """, data)

        self.conn.commit()
        return new_id

    def update(self, id: int, item) -> dict | None:
        data = item.model_dump(exclude={"appointments"})
        data["id"] = id
        
        self.cur.execute("""
            UPDATE patients
            SET name = :name, 
                age = :age
            WHERE id = :id
        """, data)
        
        self.conn.commit()
        return self.get(id)

    def delete(self, id: int):
        self.cur.execute("""
            DELETE FROM patients WHERE id = ?
        """, (id,))
        self.conn.commit()

    def close(self):
        self.conn.close()

    def _row_to_dict(self, row) -> dict:
        return {
            "id": row[0],
            "name": row[1],
            "age": row[2],
            "appoimtments": []

        }
        

@contextmanager
def managed_db():
    db = Database()
    db.connect_to_db()
    db.create_table()
    try:
        yield db
    finally:
        db.close()