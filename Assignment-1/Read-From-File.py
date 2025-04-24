#read() : Reads the entire line of the file
#readline (): Reads one line from the file at a time.
#readlines(): reads all line into a list.

#Reading the entire file.
# Open the file
file = open('example.txt', 'r')
#read
content = file.read() #read entire data
print(content)
file.close()

#read-line -- reads first line
file = open('example.txt', 'r')
content = file.readline()
print(content)
file.close()

#read -lines -- reads all lines into a list


file = open('example.txt', 'r')
content = file.readlines()
print(content)
file.close()