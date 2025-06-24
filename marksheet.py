def fun():
    sub1=int(input("enter marks for sub1:"))
    sub2=int(input("enter marks for sub2:"))
    sub3=int(input("enter marks for sub3:"))

    total_marks= sub1+sub2+sub3

    max_marks=300
    percentage=(total_marks/max_marks)*100

    print("subject 1:", sub1)
    print("subject 2:",sub2)
    print("subject 3:",sub3)

    print("Total marks:",total_marks)
    print("percentage",percentage)

    if percentage >= 90:
     grade ="A+"
    elif percentage >= 80:
     grade ='A'
    elif percentage >= 70:
     grade ='B'    
    elif percentage >= 60:
     grade ='C'
    elif percentage >= 50:
     grade ='D'
    else:
     grade ='F'

    print("Grade:",grade)

fun()