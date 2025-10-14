mark = int(input("Enter Your Marks: "))
if mark>90:
    print("You Achieved A+ As Your mark ",mark)
elif 80 < mark < 90:
    print("You Achieved A As Your mark ",mark)
elif 70 < mark < 80:
    print("You Achieved B+ As Your mark ",mark)
elif 60 < mark < 70:
    print("You Achieved B As Your mark ",mark)
else :
    print("You Failed As Your Mark ",mark)
