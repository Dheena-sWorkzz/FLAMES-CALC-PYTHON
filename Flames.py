a=input("enter your name: ")
b=input("enter your partner name: ")
different_letters=set(a+b)
same_letters=set(a)&set(b)
different_letters -= same_letters
count=len(different_letters)
result=["Friendship","love","Affection","Marriage","Enemy","Siblings"][count%6]
print("your relationship status: ",result)
