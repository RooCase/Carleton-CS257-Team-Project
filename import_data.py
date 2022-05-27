import psycopg2
import psqlConfig as config
from read_from_csv import *

class ImportDataSource():
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
        """
        This fn helps import_covid_weeks. It takes parsed and reduced CSV as parameter.
        :param: list of lists (Parsed and reduced CSV)
        :return: NA
        """
        cursor = self.connection.cursor()
        for line in lines:
            cursor.execute("INSERT INTO weekly_modes VALUES (%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s);", line)
        self.connection.commit()

    def import_covid_weeks(self):
        """
        This fn imports weekly covid data of schools and districts from CSV to weekly_modes table. Requires table to be initialized before running.
        :param: NA
        :return: NA
        """
        print("importing covid weeks")
        cursor = self.connection.cursor()
        cursor.execute("""
            DROP TABLE IF EXISTS weekly_modes;
            CREATE TABLE  weekly_modes (
                name varchar(255),
                weekDates varchar(255),
                kindergarten varchar(255),
                grade1 varchar(255),
                grade2 varchar(255),
                grade3 varchar(255),
                grade4 varchar(255),
                grade5 varchar(255),
                grade6 varchar(255),
                grade7 varchar(255),
                grade8 varchar(255),
                grade9 varchar(255),
                grade10 varchar(255),
                grade11 varchar(255),
                grade12 varchar(255)
            )
        """)
        self.help_import_weeks_from_line(reduce_for_weekly_school("Data/Minnesota_Schools_Modified.csv"))
        self.help_import_weeks_from_line(reduce_for_weekly_district("Data/Minnesota_Districts_LearningModelData_Modified.csv"))

    def import_schools(self):
        """
        This fn imports school data from CSV to school table. Requires table to be initialized before running.
        :param: NA
        :return: NA
        """
        cursor = self.connection.cursor()
        cursor.execute("""
            DROP TABLE IF EXISTS schools;
            CREATE TABLE schools (
                charter varchar(255),
                school_name varchar(255),
                school_type varchar(255),
                district_name varchar(255),
                enrollment SMALLINT,
                available_grades INT[13]
            )
        """)
        lines = reduce_for_school("Data/Minnesota_Schools_Modified.csv")
        for line in lines:
            print(line[1])
            available_grades = self.get_available_grades(self.get_identity_by_name_single(line[1]))            
            line.append(available_grades)
            cursor.execute("INSERT INTO schools VALUES (%s, %s, %s, %s, %s, %s);", line)
        self.connection.commit()

    def import_districts(self):
        """
        This fn imports district data from CSV to districts table. Requires table to be initialized before running.
        :param: NA
        :return: NA
        """
        cursor = self.connection.cursor()
        cursor.execute("""DROP TABLE IF EXISTS districts;
            CREATE TABLE districts (
                districtName varchar(255),
                districtType varchar(255),
                enrollment INTEGER
            )
            """)
        lines = reduce_for_district("Data/Minnesota_Districts_LearningModelData_Modified.csv")
        for line in lines:
            print(line[0])
            cursor.execute("INSERT INTO districts VALUES (%s, %s, %s);", line)
        self.connection.commit()

    def get_available_grades(self, week):
        """
        This fn gets a week data and returns grades that organization includes
        :param: week data for either school or district
        :return: list of included grades as numbers (0 is Kindergarden). 
        """
        return [i-2 for i in range(2, 15) if week[i] != "NA"] + [-1]

    def get_identity_by_name_single(self, name):
        """
        This fn gets a name and returns available grades and weekly covid data
        :param: name of either school or district
        :return: available grades and weekly data as tuple
        """
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM weekly_modes WHERE name = %s", (name,))
        records = cursor.fetchall()
        return records[0]

    def import_data(self):
        """
        import every data. Note that import_schools is dependent on import_covid_weeks
        :param name: NA
        :return: NA
        """
        self.import_covid_weeks()
        self.import_schools()
        self.import_districts()

my_source = ImportDataSource()
my_source.import_data()
# print(my_source.get_identity_by_name("Paladin Career And Tech High School"))
# print(my_source.get_district_data(my_source.get_district_names()[0][0]))