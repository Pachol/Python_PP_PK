root_file = open("text9.1.txt").readlines()
new_file = open("text9.2.txt",'w')

for s in root_file:
     s = s.replace("sie", "")
     s = s.replace("i ", " ")
     s = s.replace("oraz", "")
     s = s.replace("nigdy", "")
     s = s.replace("dlaczego", "")
     new_file.write(s)
new_file.close()