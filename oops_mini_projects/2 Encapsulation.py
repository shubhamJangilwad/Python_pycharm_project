class Result:
    def __init__(self,name,sir_name):
        self.name = name
        self.sir_name = sir_name
        self.__mark = 0
        self.__percentage = 0

    def add_marks(self,marks):
        if marks >= 0 and  marks <= 100:
            self.__marks = marks
            print("marks added successfully")

    def update_marks(self,new_marks):
        if new_marks >= 0  and new_marks <= 100:
            self.__marks += new_marks
            print("update the marks")
        else:
            print("not updated the marks")


    def calculate_percentage(self):
        self.__percentage = self.__marks   # out of 100

    def show_result(self):
        self.calculate_percentage()
        print("Marks:", self.__marks)
        print("Percentage:", self.__percentage, "%")



student = Result("shubham","Jangilwad")
student.add_marks(82)
student.show_result()
student.update_marks(10)
student.show_result()