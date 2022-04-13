# file for parsing the rows from the dataset as School objects and doing operations with them

dummy_school = "Yes,Academia Cesar Chavez Charter School,Regular school,Academia Cesar Chavez Charter Schools,518," \
               "8/30/20,9/4/20,Closed,,,K: No Data Available; Gr1: No Data Available; Gr2: No Data Available; Gr3: No " \
               "Data Available; Gr4: No Data Available; Gr5: No Data Available,Gr6: No Data Available; Gr7: No Data " \
               "Available; Gr8: No Data Available,Gr9: NA; Gr10: NA; Gr11: NA; Gr12: NA,,,55 "

# class for School objects
class School:
    def __init__(self, charter, district, name, type, size, k5, k8, k12):
        self.charter = charter
        self.district = district
        self.name = name
        self.type = type
        self.size = size
        self.k5 = k5
        self.k8 = k8
        self.k12 = k12

    #printing out the information about the school
    def get_school_info(self, name):
        #add a fancy function to show the possible grades here

        info = f"""
        School name: {name}
        This is a {type} school with a student body of {size} students.
        It is located in {district}.
        """
        return info
