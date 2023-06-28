try:
    with open('C:\\Users\\beryp\\PycharmProjects\\PythonLearning\\files\\prueba.txt') as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found :(")











