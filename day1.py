'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.
'''

x= '''9sixsevenz3
seven1cvdvnhpgthfhfljmnq
6tvxlgrsevenjvbxbfqrsk4seven
9zml
52sevenone'''
x = x.split('\n')
container = []
def find_first_num(number):
    for i in number:
        if (i.isdigit()):
            return str(i)
def find_last_num(number):
    for i in number[::-1]:
            if (i.isdigit()):
                return str(i)
def transform_int(number):
    return int(find_first_num(number) + find_last_num(number))

for i in x: 
    container.append(transform_int(i))
print(sum(container))

