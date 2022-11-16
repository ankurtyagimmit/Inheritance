class Base: # This is a base class
    def cal_sum(self,a,b):
        return a+b
class Derived(Base):# derived class
    def cal_mul(self,a,b):
        return a*b

n1=int(input("Enter 1st number:"))
n2=int(input("Enter 2nd number:"))

d=Derived()

print("(From basic class) Addition is:",d.cal_sum(n1,n2))
print("(From basic class) Multiplication is:",d.cal_mul(n1,n2))

