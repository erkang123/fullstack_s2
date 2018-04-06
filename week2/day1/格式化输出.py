#__author:"HYK"
#DATE:2018/4/5

name = input('Name:')
age = input('Age:')
job = input('Job:')
salary = input('Salary:')

if salary.isdigit():
    salary = int(salary)
else:
    exit('must input digit')
msg = '''
-----------info of %s-------
name:%s
age:%s
job:%s
salary:%d
-----------end----------------
'''%(name,name,age,job,salary)
print(msg)
