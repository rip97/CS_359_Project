# @Author: Joshua Espana
# @Date: 4-23-2023
# @Description: Provides CRUD functionality for the digtial display table

import sqlite3

# Provides CRUD functionality for the digtial display table
class database_manager:
    # initializes database connection
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS DigitalDisplay (
                serialNo TEXT PRIMARY KEY,
                schedulerSystem TEXT,
                modelNo TEXT
            )
        """)
        self.conn.commit()

    # Checks if a provided serial number is unique or if it has already been used
    def isSerialNumberUnique(self, serialNo):
        rows = self.read()
        for row in rows:
            if(row[0] == serialNo):
                return False
        return True

    # Creates a new digital display
    def create(self, serialNo, schedulerSystem, modelNo):
        try:
            self.cursor.execute("""
                INSERT INTO DigitalDisplay (serialNo, schedulerSystem, modelNo)
                VALUES (?, ?, ?)
            """, (serialNo, schedulerSystem, modelNo))
            self.conn.commit()
            print("Record created successfully")
        except Exception as e:
            print("Error creating record: ", e)

    # Reads from the digital display table. If no serialNo is provided, reads all data.
    def read(self, serialNo=None):
        try:
            if serialNo:
                self.cursor.execute("""
                    SELECT * FROM DigitalDisplay WHERE serialNo=?
                """, (serialNo,))
            else:
                self.cursor.execute("""
                    SELECT * FROM DigitalDisplay
                """)
            rows = self.cursor.fetchall()
            return rows
            # for row in rows:
            #     print("Serial No: ", row[0])
            #     print("Scheduler System: ", row[1])
            #     print("Model No: ", row[2])
        except Exception as e:
            print("Error reading records: ", e)
            return []

    # Updates a digital display.
    def update(self, serialNo, schedulerSystem=None, modelNo=None):
        try:
            if schedulerSystem and modelNo:
                self.cursor.execute("""
                    UPDATE DigitalDisplay SET schedulerSystem=?, modelNo=? WHERE serialNo=?
                """, (schedulerSystem, modelNo, serialNo))
            elif schedulerSystem:
                self.cursor.execute("""
                    UPDATE DigitalDisplay SET schedulerSystem=? WHERE serialNo=?
                """, (schedulerSystem, serialNo))
            elif modelNo:
                self.cursor.execute("""
                    UPDATE DigitalDisplay SET modelNo=? WHERE serialNo=?
                """, (modelNo, serialNo))
            else:
                print("No fields to update")
                return
            self.conn.commit()
            print("Record updated successfully")
        except Exception as e:
            print("Error updating record: ", e)

    # Deletes a digital display using the provided serail no
    def delete(self, serialNo):
        try:
            self.cursor.execute("""
                DELETE FROM DigitalDisplay WHERE serialNo=?
            """, (serialNo,))
            self.conn.commit()
            print("Record deleted successfully")
        except Exception as e:
            print("Error deleting record: ", e)

    def __del__(self):
        self.cursor.close()
        self.conn.close()


# How to use:
# # create an instance of database_manager class
# db = database_manager("abc.sqlite")

# # create a record
# db.create("ABC123", "Scheduler A", "Model X")

# # read all records
# db.read()

# # read a specific record
# db.read("ABC123")

# # update a record
# db.update("ABC123", schedulerSystem="Scheduler B")

# # delete a record
# db.delete("ABC123")
