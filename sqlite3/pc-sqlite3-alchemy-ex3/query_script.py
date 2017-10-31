from schema_script import *
from datetime import datetime

s = session()

'''
 Para cada departamento removido, remove tambem
 os empregados associados
'''
for department in s.query(Department).all():
    s.delete(department)
    
s.commit()

# Define departamentos
IT = Department(name="IT")
Financial = Department(name="Financial")

# Define empregados e associacao com os departamentos
john = Employee(name="John", department=IT)
marry = Employee(name="marry", department=Financial)

s.add(IT)
s.add(Financial)
s.add(john)
s.add(marry)

s.commit()

cathy = Employee(name="Cathy", department=Financial)
s.add(cathy)

s.commit()

# Recupera empregado de acordo com o seguinte filtro
print(s.query(Employee).filter(Employee.name.startswith("C")).one().name)

empl = s.query(Employee).join(Employee.department).filter(Employee.name.startswith('C'), Department.name == 'Financial').all()[0].name
print("join Employee x Department:", empl)

future_empl = s.query(Employee).filter(Employee.hired_on > func.now()).count()
print("total de registros futuro:", future_empl)

past_empl = s.query(Employee).filter(Employee.hired_on <= func.now())
print("total de registros passado:", past_empl.count())

for empl in past_empl.all():
    print(empl.name, empl.hired_on)