import psycopg2
import psqlConfig as config
from read_from_csv import read_from_csv

class DataSource:
    def __init__(self):
        self.connection = self.connect()

    def connect(self):
        try:
            connection = psycopg2.connect(database=config.database, user=config.user, password=config.password, host="localhost")
        except Exception as e:
            print("Connection error: ", e)
            exit()
        return connection

    def import_weeks_from_line(self, lines):
        cursor = self.connection.cursor()
        for line in lines:
            cursor.execute("INSERT INTO weekly_modes VALUES (%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s);", line)
        self.connection.commit()

    def import_weeks(self):
        cursor = self.connection.cursor()
        cursor.execute("TRUNCATE TABLE weekly_modes");
        self.import_weeks_from_line(read_from_csv("Data/Minnesota_Schools_Modified.csv", "School"))
        self.import_weeks_from_line(read_from_csv("Data/Minnesota_Districts_LearningModelData_Modified.csv", "District"))

    def get_available_grades(self, weekly_table):
        return [i-2 for i in range(2, 15) if weekly_table[0][i] != "NA"]

    def get_identity_by_name(self, name):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM weekly_modes WHERE object_name = %s", (name,))
        records = cursor.fetchall()
        return (self.get_available_grades(records), records)

