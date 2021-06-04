

def main():
    grade_items = {}
    grade_in_English = input("English grade: ")
    #add element to dictionary
    grade_items.update({"English":int(grade_in_English)})
    grade_in_Math    = input("Math grade: ")
    grade_items.update({"Math": int(grade_in_Math)})
    grade_in_Global_studies = input("Global_studies grade: ")
    grade_items.update({"Global Studies": int(grade_in_Global_studies)})
    grade_in_Art    = input("Art grade: ")
    grade_items.update({"Art": int(grade_in_Art)})
    grade_in_Music = input("Music grade: ")
    grade_items.update({"Music":int(grade_in_Music)})
    list_of_grades = list(grade_items.values())
    average = sum(list_of_grades)/len(grade_items)
    print("===============================")
    print("your average is {} ".format(average))


main()

    