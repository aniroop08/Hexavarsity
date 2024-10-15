class DuplicateEnrollmentException(Exception):
    def __init__(self, message="Duplicate enrollment detected"):
        self.message = message
        super().__init__(self.message)


class CourseNotFoundException(Exception):
    def __init__(self, message="Course not found"):
        self.message = message
        super().__init__(self.message)


class StudentNotFoundException(Exception):
    def __init__(self, message="Student not found"):
        self.message = message
        super().__init__(self.message)


class TeacherNotFoundException(Exception):
    def __init__(self, message="Teacher not found"):
        self.message = message
        super().__init__(self.message)


class PaymentValidationException(Exception):
    def __init__(self, message="Payment validation failed"):
        self.message = message
        super().__init__(self.message)


class InvalidDataException(Exception):
    def __init__(self, message="Invalid data provided"):
        self.message = message
        super().__init__(self.message)


class InvalidStudentDataException(Exception):
    def __init__(self, message="Invalid student data"):
        self.message = message
        super().__init__(self.message)


class InvalidCourseDataException(Exception):
    def __init__(self, message="Invalid course data"):
        self.message = message
        super().__init__(self.message)


class InvalidEnrollmentDataException(Exception):
    def __init__(self, message="Invalid enrollment data"):
        self.message = message
        super().__init__(self.message)


class InvalidTeacherDataException(Exception):
    def __init__(self, message="Invalid teacher data"):
        self.message = message
        super().__init__(self.message)


class InsufficientFundsException(Exception):
    def __init__(self, message="Insufficient funds for the transaction"):
        self.message = message
        super().__init__(self.message)
