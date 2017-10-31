import os
 
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
 
Base = declarative_base()
class Department(Base):
    __tablename__ = 'department'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    employees = relationship(
        'Employee',
        secondary='department_employee_link'
    )
 
class Employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    hired_on = Column(
        DateTime,
        default=func.now())
    departments = relationship(
        Department,
        secondary='department_employee_link'
    )
 
class DepartmentEmployeeLink(Base):
    __tablename__ = 'department_employee_link'
    department_id = Column(Integer, ForeignKey('department.id'), primary_key=True)
    employee_id = Column(Integer, ForeignKey('employee.id'), primary_key=True)

# Exemplo de script com relaiconamento N x N
fp = 'orm_in_detail.sqlite'
# Remove the existing orm_in_detail.sqlite file
if os.path.exists(fp):
    os.remove(fp)

from sqlalchemy import create_engine
engine = create_engine('sqlite:///orm_in_detail.sqlite')

from sqlalchemy.orm import sessionmaker
session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)

s = session()

IT = Department(name="IT")
Financial = Department(name="Financial")

cathy = Employee(name="Cathy")
marry = Employee(name="Marry")
john = Employee(name="John")

cathy.departments.append(Financial)
Financial.employees.append(marry)

john.departments.append(IT)

s.add(IT)
s.add(Financial)
s.add(cathy)
s.add(marry)
s.add(john)

s.commit()

print(cathy.departments[0].name)
print(marry.departments[0].name)
print(john.departments[0].name)
print(IT.employees[0].name)

# Recupera empregado do departamento especifico independente se o mesmo esta associado a outro departamento
empl = s.query(Employee).filter(Employee.departments.any(Department.name == 'IT')).all()[0].name
print(empl)

# Recupera o departamento que possua o empregado especifico
depart = s.query(Department).filter(Department.employees.any(Employee.name == 'John')).all()[0].name
print(depart)