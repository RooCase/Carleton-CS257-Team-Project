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

    def help_import_weeks_from_line(self, lines):
        cursor = self.connection.cursor()
        for line in lines:
            cursor.execute("INSERT INTO weekly_modes VALUES (%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s);", line)
        self.connection.commit()

    def import_covid_weeks(self):
        cursor = self.connection.cursor()
        cursor.execute("TRUNCATE TABLE weekly_modes");
        self.help_import_weeks_from_line(read_from_csv("Data/Minnesota_Schools_Modified.csv", "School_Weeks"))
        self.help_import_weeks_from_line(read_from_csv("Data/Minnesota_Districts_LearningModelData_Modified.csv", "District_Weeks"))

    def import_schools(self):
        cursor = self.connection.cursor()
        cursor.execute("TRUNCATE TABLE schools")
        cursor.execute("DROP TABLE distinct_schools")
        lines = read_from_csv("Data/Minnesota_Schools_Modified.csv", "Schools")
        for line in lines:
            cursor.execute("INSERT INTO schools VALUES (%s, %s, %s, %s,%s);", line)
        cursor.execute("SELECT DISTINCT * INTO distinct_schools FROM schools")
        self.connection.commit()

    def get_available_grades(self, weekly_table):
        return [i-2 for i in range(2, 15) if weekly_table[0][i] != "NA"]

    def get_identity_by_name(self, name):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM weekly_modes WHERE object_name = %s", (name,))
        records = cursor.fetchall()
        return (self.get_available_grades(records), records)

    def get_school_by_name(self, name):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM distinct_schools WHERE school_name = %s", (name,))
        records = cursor.fetchall()
        return records

    def filter_schools(self, charter):
        cursor = self.connection.cursor()
        print(charter)
        if charter == "select":
            charter = "'Yes', 'No'"
        # if grade == "select":
        #     grade = "0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12"
        cursor.execute(f"SELECT * FROM distinct_schools WHERE charter IN ({charter})")
        records = cursor.fetchall()
        print(records)
        return records

my_source = DataSource()
# my_source.import_covid_weeks()
# my_source.import_schools()
# print(my_source.get_school_by_name("Academy For Sciences & Agriculture (AFSA) High School"))