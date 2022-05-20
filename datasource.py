import psycopg2
import psqlConfig as config

class DataSource:
    # initializing the object
    def __init__(self):
        self.connection = self.connect()

    # connecting to the database
    def connect(self):
        try:
            connection = psycopg2.connect(database=config.database, user=config.user, password=config.password,
                                          host="localhost")
        except Exception as e:
            print("Connection error: ", e)
            exit()
        return connection

    # test method for returning all schools
    def getAllSchools(self):
        try:
            # setting up a cursor
            cursor = self.connection.cursor()

            # initializing a query
            query = "SELECT * FROM schools"

            # executing the query
            cursor.execute(query)
            print(cursor.fetchall())

        except Exception as e:
            print("Something went wrong when executing the query: ", e)
            return None

    # getting schools with staff count above certain number
    def getSchoolsAboveStaffCount(self, staffcount):
        try:
            # set up a cursor
            cursor = self.connection.cursor()

            # using %s as a placeholder for the variable
            query = "SELECT * FROM schools WHERE staffcount>%s ORDER BY staffcount DESC"

            # executing the query and saying that the staffcount variable
            # should be placed where %s was, the trailing comma is important!
            cursor.execute(query, (staffcount,))
            print(cursor.fetchall())

        except Exception as e:
            print("Something went wrong when executing the query: ", e)
            return None

    def getDistrictNames(self):
        """
        A function to retrieve data from a SQL table on districts
        :return: a list of district school names
        """
        cursor = self.connection.cursor()

        # initializing a query
        query = "SELECT districtName FROM districts"

        # executing the query
        cursor.execute(query)
        print(cursor.fetchall())

    def getDistrictData(self, name):
        """
        Retrieves data from a specified district
        :param name: provided name
        :return: information about specific district
        """
        cursor = self.connection.cursor()

        # initializing a query
        query = "SELECT * FROM districts WHERE districtName=" + "'" +name+"'"

        # executing the query
        cursor.execute(query)
        print(cursor.fetchall())




if __name__ == '__main__':
    my_source = DataSource()
    my_source.connect()
    my_source.getDistrictNames()