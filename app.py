import sys

def allocate_room(cgpa):
    if 9.0 <= cgpa <= 10.0:
        return "Premium AC Room"
    elif 8.0 <= cgpa < 9.0:
        return "AC Room"
    elif 7.0 <= cgpa < 8.0:
        return "Deluxe Non-AC"
    elif 6.0 <= cgpa < 7.0:
        return "Standard Room"
    else:
        return "Not Eligible"

def student_details(name="Renuka", usn="1RV23BCA045", year="2nd Year", cgpa=8.6):
    room = allocate_room(float(cgpa))
    print("Hostel Allocation Details")
    print("--------------------------")
    print(f"Name          : {name}")
    print(f"USN           : {usn}")
    print(f"Year of Study : {year}")
    print(f"CGPA          : {cgpa}")
    print(f"Room Category : {room}")

if __name__ == "__main__":
    # Accept command-line arguments (from Jenkins parameters)
    args = sys.argv[1:]
    if len(args) == 4:
        student_details(*args)
    else:
        student_details()
