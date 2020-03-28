'''
Given the names and grades for each student in a Physics class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

Input Format:

The first line contains an integer,N , the number of students. 
The  2N subsequent lines describe each student over 2  lines; the first line contains a student's name, and the second line contains their grade.

Output Format:

Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, order their names alphabetically and print each one on a new line.

'''

N = int(raw_input())

students = list()
for i in range(N):
    students.append([raw_input(), float(raw_input())])

scores = set([students[x][1] for x in range(N)])
scores = list(scores)
scores.sort()

students = [x[0] for x in students if x[1] == scores[1]]
students.sort()

for s in students:
    print s
