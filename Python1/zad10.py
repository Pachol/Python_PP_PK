import os

dict = {"i" : "oraz","oraz" : "i","nigdy" : "prawie nigdy","dlaczego" : "czemu"}

dir = "C:\Users\Przemek\PycharmProjects\Python\Python1"
list = os.listdir(dir)
print(list)

for file in list:
    fin=open(dir+file)
    file2 = dir+file + "_changed.txt"
    fout=open(file2, 'w+')

    for line in fin:
        for word in dict:
            line = line.replace(word, dict[word])
        fout.write(line)
    fin.close()
    fout.close()