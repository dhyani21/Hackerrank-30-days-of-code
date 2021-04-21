# Given a base-10 integer,n , convert it to binary (base-2). Then find and print the base-10 integer denoting the maximum number of consecutive !'s in n's binary representation. 
# When working with different bases, it is common to show the base as a subscript.

print(len(max(bin(int(input().strip()))[2:].split('0'))))
