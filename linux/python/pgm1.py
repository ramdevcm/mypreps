
# Write a program to read a text file, and print out every line that contains the word "error".
from os import linesep

def main():
    f = open(r"C:\Users\workstation\Desktop\mypreps\src\linux\python\file1.txt", "r")
    lines = f.readlines() 
    count = 0
    for line in lines:
        if 'error' in line:
           count += 1
           print(line)
    print("The total number of lines printed holding a word \'error\' is : ",count)
    

if __name__== '__main__':
     main()

