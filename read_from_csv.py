import csv

def read_from_csv(file, select_mode):
    lines = find_lines(file)
    if select_mode == "School_Weeks":
        return select_columns_for_covid_school(lines)
    elif select_mode == "District_Weeks":
        return select_columns_for_covid_district(lines)
    elif select_mode == "Schools":
        return select_columns_school(lines)

def find_lines(file):
    with open(file, 'r') as data:
        CSVReader = csv.reader(data)
        return [row for row in CSVReader][1:]

def select_columns_for_covid_school(lines):
    ans = []
    for line in lines:
        grades = (line[10] + ";" + line[11] + ";" + line[12]).split(";")
        strippedGrades = [grade_pair.replace(" ", "").split(":")[1] for grade_pair in grades]
        ans.append([line[1], line[5] + " " + line[6]] + strippedGrades)
    return ans

def select_columns_for_covid_district(lines):
    ans = []
    for line in lines:
        grades = (line[11] + ";" + line[12] + ";" + line[13]).split(";")
        strippedGrades = [grade_pair.strip(" ").split(":")[1] for grade_pair in grades]
        ans.append([line[1], line[4] + " " + line[5]] + strippedGrades)
    return ans

def select_columns_school(lines):
    return [[line[i] for i in range(5)] for line in lines]
