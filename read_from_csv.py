import csv

def read_from_csv(file, school_or_district):
    if school_or_district == "School":
        return combine_columns_school(find_lines(file))
    else:
        return combine_columns_district(find_lines(file))

def find_lines(file):
    with open(file, 'r') as data:
        CSVReader = csv.reader(data)
        return [row for row in CSVReader][1:]

def combine_columns_school(lines):
    ans = []
    for line in lines:
        grades = (line[10] + ";" + line[11] + ";" + line[12]).split(";")
        strippedGrades = [grade_pair.replace(" ", "").split(":")[1] for grade_pair in grades]
        ans.append([line[1], line[5] + " " + line[6]] + strippedGrades)
    return ans

def combine_columns_district(lines):
    ans = []
    for line in lines:
        grades = (line[11] + ";" + line[12] + ";" + line[13]).split(";")
        strippedGrades = [grade_pair.strip(" ").split(":")[1] for grade_pair in grades]
        ans.append([line[1], line[4] + " " + line[5]] + strippedGrades)
    return ans

