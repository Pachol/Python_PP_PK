File = open("somedata", "r")
print File.read()

new_data = raw_input("Put new data: ")

File.close()
File = open("somedata", "w")

File.write(new_data)

File.close()