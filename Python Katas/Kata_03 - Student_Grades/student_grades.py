
def add_student(students: dict,  name: str, student_id: str, grade: list[int, int, int])-> str:
    """Adds a new student to the dictionary"""
    
    if student_id in students.keys():
        raise ValueError("Student_id already in use")
    
    for item in grade:
        if not isinstance(item, int) or item < 0:
            raise ValueError("List items should be positive int type")
    
    students[student_id] = {"name": name, "grade": grade}


def calculate_average(students: dict, student_id: str) -> float:
    """Computes the average grade of a student"""
    
    return sum(students[student_id]["grade"])/ len(students[student_id]["grade"])
    

def has_passed(students: dict, student_id: str)-> bool:
    """Checks is a student passed based on their average grade"""
    
    return True if calculate_average(students, student_id) > 40 else False

