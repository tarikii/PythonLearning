import os

source = 'C:\\Users\\beryp\\PycharmProjects\\PythonLearning\\files\\move.txt'
destination = 'C:\\Users\\beryp\\Desktop\\move.txt'

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source, destination)
        print(source + " was moved")
except FileNotFoundError:
    print(source + " was not found")












