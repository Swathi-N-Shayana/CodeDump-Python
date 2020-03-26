''' 
You are given three integers X,Y  and Z representing the dimensions of a cuboid along with an integer N. You have to print a list of all possible coordinates given by (i,j,k)  on a 3D grid where the sum of i+j+k is not equal to N. Here, 0<=i<=X, 0<=j<=Y, 0<=k<=Z
'''


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    N = int(input())
    arr = [[X, Y, Z] for X in range(x+1) for Y in range(y+1) for Z in range(z+1) if X + Y + Z != N]
    print(arr) 
