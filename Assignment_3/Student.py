class StudentInfo:
    name: str
    roll_no: int
    marks: float

    def __init__(self, name, roll_no, marks) -> None:
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
def averageMarks(obj1, obj2, obj3, obj4, obj5):
    return (
        (
            obj1.marks +
            obj2.marks +
            obj3.marks +
            obj4.marks +
            obj5.marks
        ) / 5
    )
obj1 = StudentInfo("abc", 10, 100)
obj2 = StudentInfo("def", 20, 200)
obj3 = StudentInfo("ghi", 30, 300)
obj4 = StudentInfo("jkl", 40, 400)
obj5 = StudentInfo("mno", 50, 500)
print("Average Marks of 5 Students is:\t", averageMarks(obj1, obj2, obj3, obj4, obj5))