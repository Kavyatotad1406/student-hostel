def calculate_grade(avg):
    if 90 <= avg <= 100:
        return "S"
    elif 80 <= avg < 90:
        return "A"
    elif 65 <= avg < 80:
        return "B"
    elif 50 <= avg < 65:
        return "C"
    elif 40 <= avg < 50:
        return "D"
    else:
        return "F"


def student_details(
    name="Kavya",
    department="BCA",
    semester="3",
    m1=85,
    m2=78,
    m3=92
):
    avg = (m1 + m2 + m3) / 3
    grade = calculate_grade(avg)

    return (
        f"Name       : {name}\n"
        f"Department : {department}\n"
        f"Semester   : {semester}\n"
        f"Marks      : {m1}, {m2}, {m3}\n"
        f"Average    : {avg:.2f}\n"
        f"Grade      : {grade}"
    )


if __name__ == "__main__":
    print(student_details())
