'''
Consider a list (list = []). You can perform the following commands:

1. insert i e: Insert integer e at position i.
2. print: Print the list.
3. remove e: Delete the first occurrence of integer e.
4. append e: Insert integer e at the end of the list.
5. sort: Sort the list.
6. pop: Pop the last element from the list.
7. reverse: Reverse the list.
Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above. Iterate through each command in order and perform the corresponding operation on your list.

Input Format:

The first line contains an integer,n , denoting the number of commands. 
Each line i of the n subsequent lines contains one of the commands described above.

Output Format:

For each command of type print, print the list on a new line.

'''

L = []

N = int(raw_input())

for i in range(0, N):
    tokens = raw_input().split()

    if tokens[0] == 'insert':
        L.insert(int(tokens[1]), int(tokens[2]))
    elif tokens[0] == 'print':
        print L
    elif tokens[0] == 'remove':
        L.remove(int(tokens[1]))
    elif tokens[0] == 'append':
        L.append(int(tokens[1]))
    elif tokens[0] == 'sort':
        L.sort()
    elif tokens[0] == 'pop':
        L.pop()
    elif tokens[0] == 'reverse':
        L.reverse()
