'''
Given an integer,n , and n space-separated integers as input, create a tuple,t , of those n integers. Then compute and print the result of hash(t) .

Input Format:

The first line contains an integer, n, denoting the number of elements in the tuple. 
The second line contains n space-separated integers describing the elements in tuple t.

Output Format:

Print the result of hash(t).



'''
n = int(raw_input())
t = tuple(map(int, raw_input().split()))

print hash(t)
