class Course:
    def __init__(self, course_id, course_name, teacher_id, credits):
        self.course_id = course_id
        self.course_name = course_name
        self.teacher_id = teacher_id
        self.credits = credits

        self.enrollments = []

    def Get_course_id(self):
        return self.__course_id

    def Get_course_name(self):
        return self.__course_name

    def set_course_id(self, course_id):
        self.__course_id = course_id

    def set_course_name(self, course_name):
        self.__course_name = course_name






