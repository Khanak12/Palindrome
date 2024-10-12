def func1(r):
    length=len(r)-1
    s=0
    while (s<length):
        if (r[s]!=r[length]):
            return False
    
        s=s+1
        length=length-1
    
    return True
r=(1,2,3,3,2,1)
if func1(r):
    print("Its a palindrome")
else:
    print("ITS NOT A PALINDROME")
