from generate_schema import *

d = Department(name="IT")
emp1 = Employee(name="John", department=d)
s = session()
s.add(d)
s.add(emp1)
s.commit()

select_john = s.query(Employee).filter(Employee.name == "John").all()
print("select_john:", select_john)

s.delete(d)  # Deleting the department also deletes all of its employees.
s.commit()
all = s.query(Employee).all()
print("all:", all)

select_john = s.query(Employee).filter(Employee.name == "John").all()
print("select_john:", select_john)

emp2 = Employee(name = "Marry")
print(emp2.hired_on)
s.add(emp2)
print(emp2.hired_on)
s.commit()
print(emp2.hired_on)

'''
Remover todos os registros de departamento
dessa forma todos os empregados associados também serão removidos
'''
all = s.query(Department).all()
for dept in  all:
    s.delete(dept)

all = s.query(Employee).all()
for empl in  all:
    s.delete(empl)
    
s.commit()

total_dept = s.query(Department).count()
total_empl = s.query(Employee).count()

print("Total de registros departamento {0} empregados {1}".format(total_dept, total_empl))