import os

def enter_folder(directory):
    for root, dirs, files in os.walk(directory):
        for i in dirs:
            print(i)

enter_folder("C:/Users/Przemek/PycharmProjects")