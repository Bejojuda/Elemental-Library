class Gender:
    GENDER_CHAR_LENGTH = 1
    MALE = 'M'
    FEMALE = 'F'

    GENDER_CHOICES =[
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]


class Type:
    TYPE_CHAR_LENGTH = 2
    STUDENT = 'ST'
    TEACHER = 'TE'
    VISITOR = 'VI'

    TYPE_CHOICES = [
        (STUDENT, 'Student'),
        (TEACHER, 'Teacher'),
        (VISITOR, 'Visitor'),
    ]