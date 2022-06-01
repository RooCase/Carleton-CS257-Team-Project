import psycopg2
import psqlConfig as config
from flask import request

class InteractDataSource:
    def __init__(self):
        """Create connection"""
        self.connection = self.connect()

    def connect(self):
        """Connect to the database using psycopg"""
        try:
            connection = psycopg2.connect(database=config.database, user=config.user, password=config.password, host="localhost")
        except Exception as e:
            print("Connection error: ", e)
            exit()
        return connection

    def get_available_grades(self, week):
        """
        This fn gets a week data and returns grades that organization includes
        :param: week data for either school or district
        :return: list of included grades as numbers (0 is Kindergarden). 
        """
        return [i-2 for i in range(2, 15) if week[i] != "NA"] + [-1]

    def get_identity_by_name(self, name):
        """
        This fn gets a name and returns available grades and weekly covid data
        :param: name of either school or district
        :return: available grades and weekly data as tuple
        """
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM weekly_modes WHERE name = %s", (name,))
        records = cursor.fetchall()
        available_grades = self.get_available_grades(records[0])
        available_grades.remove(-1)
        return (available_grades, records)

    def get_school_by_name(self, name):
        """
        This fn gets a school name and returns list of info about it
        :param: name of school
        :return: school's info as tuple
        """
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM schools WHERE school_name = %s", (name,))
        return cursor.fetchall()[0]

    def get_district_by_name(self, district_name):
        """
        Retrieves data from a specified district
        :param name: provided name
        :return: information about specific district
        """
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM districts WHERE districtName = %s", (district_name,))
        return cursor.fetchall()[0]

    def filter_schools(self):
        """
        filters the school based on html request variables
        :param name: NA
        :return: matchin schools as list
        """
        enrollment, charter, grade = self.get_request_args()
        cursor = self.connection.cursor()
        cursor.execute(f"SELECT school_name FROM schools WHERE charter IN ({charter}) AND {grade} = any(available_grades) AND enrollment BETWEEN {enrollment} ORDER BY school_name ASC;")
        records = cursor.fetchall()
        print(records[0])
        return (enrollment, charter, grade, records)

    def get_request_args(self):
        """
        gets the request arguments
        :param name: NA
        :return: enrollment, charger, and grade arguments
        """
        # these initial values are tailored to display all schools
        enrollment = "0 AND 100000"
        charter = "'Yes', 'No'"
        grade = "-1"
        if "enrollment" in request.args:
            enrollment = request.args['enrollment']
        if "charter" in request.args:
            charter = request.args['charter']
        if "grade" in request.args:
            grade = request.args['grade']
        return enrollment, charter, grade

    def get_district_names(self):
        """
        A function to retrieve data from a SQL table on districts
        :param name: NA
        :return: a list of district school names
        """
        cursor = self.connection.cursor()
        cursor.execute("SELECT districtName FROM districts ORDER BY districtName ASC")
        return cursor.fetchall()

    def get_schools_by_district(self, district_name):
        """
        list schools of a district
        :param name: district_name
        :return: a list of schools in a district
        """
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM schools WHERE district_name = %s", (district_name,))
        records = cursor.fetchall()
        return records
