try:
    while(True):
        print("1.Insert data")
        print("2.List the students")
        print("3.Retrieve data")
        print("4.Exit")
        n=int(input())
        if(n==1):
            filename="swati.txt"
            file=open(filename,"w")
            print("Enter student Name")
            file.write(input())
            print(" ",end="")
            print("Enter the age")
            file.write(int(input()))
            print(" ",end="")
            print("Enter the branch")
            file.write(input())
            print(" ",end="")
            print("Enter the year")
            file.write(int(input()))
            print(" ",end="")
            print("Enter the semester")
            file.write(int(input()))
            print(" ",end="")
            print("Enter previous sem %")
            file.write(marks.Insert(int(input())))
            print()
            file.close()
        elif(n==2):
            print("List students data who are having marks less than")
            a=int(input())
            file=open("swati.txt","r")
            for line in file():
                if(marks[line]<a):
                    print(line)
        elif(n==3):
            print("List of all the Student data")
            file=open("swati.txt","r")
            for line in file():
                print(line)
            file.close()
        elif(n==4):
            break
        else:
            print("Incorrect input")
            break
except:
    print("Error")
