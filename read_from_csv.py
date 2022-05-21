"""
These functions help us in parsing the CSV files and remove unnecessary columns
Written by Batmend Batsaikhan and Roo Case
"""

import csv

def uniquify_list_of_lists(list_of_lists):
    """
    This fn removes duplicate values in the given list. 
    :param: list of lists.
    :return: unique list of lists.
    """
    list_of_tuple = [tuple(my_list) for my_list in list_of_lists]
    # We use set to remove duplicates
    set_of_tuple = set(list_of_tuple)
    list_of_lists = [list(my_tuple) for my_tuple in set_of_tuple]
    return list_of_lists

def find_lines(file):
    """
    This fn parses the CSV file line by line.
    :param: relative file path.
    :return: list of list where each sublist represent a line. Lines are split by commas.
    """
    with open(file, 'r') as data:
        CSVReader = csv.reader(data)
        return [row for row in CSVReader][1:]

def reduce_for_weekly_school(file):
    """
    This fn receives parsed CSV and reduces it into essential columns for weekly school covid data. Note that it also combines some columns.
    :param: list of lists (parsed CSV).
    :return: list of lists (reduced for weekly school covid data).
    """
    lines = find_lines(file)
    ans = []
    for line in lines:
        # combines columns with ; so that we demilit them. This ingenuity is found by Roo.
        grades = (line[10] + ";" + line[11] + ";" + line[12]).split(";")
        strippedGrades = [grade_pair.replace(" ", "").split(":")[1] for grade_pair in grades]
        ans.append([line[1], line[5] + " " + line[6]] + strippedGrades)
    return ans

def reduce_for_weekly_district(file):
    """
    This fn receives parsed CSV and reduces it into essential columns for weekly district covid data. Note that it also combines some columns.
    :param: list of lists (parsed CSV).
    :return: list of lists (reduced for weekly district covid data).
    """
    lines = find_lines(file)
    ans = []
    for line in lines:
        grades = (line[11] + ";" + line[12] + ";" + line[13]).split(";")
        strippedGrades = [grade_pair.strip(" ").split(":")[1] for grade_pair in grades]
        ans.append([line[0], line[4] + " " + line[5]] + strippedGrades)
    return ans

def reduce_for_school(file):
    """
    This fn gets a file, parse it, and get essential columns for school.
    :param: relative file path
    :return: list of lists (reduced for school data).
    """
    lines = find_lines(file)
    ans = [[line[i] for i in range(5)] for line in lines]
    return uniquify_list_of_lists(ans)

def reduce_for_district(file):
    """
    This fn gets a file, parse it, and get essential columns for district.
    :param: relative file path
    :return: list of lists (reduced for district data).
    """
    lines = find_lines(file)
    ans = [[line[i] for i in range(3)] for line in lines]
    return uniquify_list_of_lists(ans)
