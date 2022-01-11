class Student():
    
    student_ID = 221000
    
    uni_name = 'UEK Krakow'
    
    def __init__(self, name, surname, field):
        self.name = name
        self.surname = surname
        self.fieldofstudy = field

    def __str__(self):
        return '{} {} ({}), {}, {}'.format(self.name,self.surname, self.student_ID, self.fieldofstudy, self.uni_name)


print(Student('Anna', 'MAJ', 'Informatyka'))

Student.student_ID += 1

print(Student('Jakub', 'BOREK', 'Zarządzanie'))
        
Student.student_ID += 1

print(Student('Mikołaj', 'MAREK', 'Logistyka'))

