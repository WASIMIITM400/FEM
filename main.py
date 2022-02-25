#connectivity
string1 = '$Elements'
# yodleyo
# opening a text file
file = open("assignment_star.msh", "r")

# setting flag and index to 0
flag = 0
index = 0

# Loop through the file line by line
for line in file:
    index += 1

    # checking string is present in line or not
    if string1 in line:

        flag = 1
        break

# checking condition for string found or not
if flag == 0:
    print('String', string1, 'Not Found')
else:
    print('String', string1, 'Found In Line', index)


#num = int(file.readline())  # number of lines to read for Physical Names
#print(num)
num = int(file.readline())  # number of lines to read for elements
connectivity = {} # Initialising an empty dictionary
for j in range(num):
                k = file.readline().split()
                print(k)
                if int(k[1])==1:
                    connectivity.update({int(k[0]): [int(k[-2]),int(k[-1])]})  # Updating the dictionary
                elif int(k[1])==2:
                    connectivity.update({int(k[0]): [int(k[-3]),int(k[-2]), int(k[-1])]})  # Updating the dictionary
                elif int(k[1])==3:
                    connectivity.update({int(k[0]): [int(k[-4]),int(k[-3]), int(k[-2]), int(k[-1])]})  # Updating the dictionary
                else:
                    print("higher oreder elements found")
print(connectivity)