def addition():
    n1=int(input("Enter English mark:- "))
    n2=int(input("Enter Maths mark:- "))
    n3=int(input("Enter Physic mark:- "))
    n4=int(input("Enter Chemistry mark:- "))
    n5=int(input("Enter Computer Science mark:- "))
    n6=int(input("Enter PD mark:- "))
    n7=n1+n2+n3+n4+n5+n6
    print("Total score:- ",n7)
    Percentage=(n7/600)*100
    print("Congrulation You got",Percentage,"%")
    
