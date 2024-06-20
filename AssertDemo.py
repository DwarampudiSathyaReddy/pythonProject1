def avg(marks):
    assert len(marks) !=0,"The List is empty"
    return sum(marks)/len(marks)
mark1=[34,45,6,64,33]
print("the average of marks1:",avg(mark1))
mark2=[1,33,45,56,77]
print("The average of marks2:",avg(mark2))

list123=[1,2,33,4,5]
x=6
assert x not in list123,"x is not in list"
assert x in list123,"x is not in list"