
def add_student(students: dict,  name: str, student_id: str, grade: list[int, int, int])-> str:
    """Adds a new student to the dictionary"""
    
    if student_id in students.keys():
        raise ValueError("Student_id already in use")
    
    for item in grade:
        if not isinstance(item, int) or item < 0:
            raise ValueError("List items should be positive int type")
    
    students[student_id] = {"name": name}
    students[student_id][name] = grade



def calculate_average(students: dict, student_id: str) -> float:
    """Computes the average grade of a student"""
    
    name = students[student_id]['name']
    grades = students[student_id][name]
    return sum(grades)/ len(grades)
    

def has_passed(students: dict, student_id: str)-> bool:
    """Checks is a student passed based on their average grade"""
    
    

