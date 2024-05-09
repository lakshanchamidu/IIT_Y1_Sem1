import w2052950_part1A       #import hte marks chart for this code
import w2052950_part_1D          # import the graph code for this code
import os               #import the os module
Graph_list = []      #define the list(this list used for create the graph)
first = ["Start"]
new = [" "]
count = 0            #Define the variables 

print("\n")
s = ("Student Result Check Programme")
print(s.center(100))
print("\n~ Student Version")
print("Student Version only display Result")
print("\n~ Staff Version")
print("Staff Version create extention text file, Histrogram and user input display according to list\n")

def student_input():
        try:
            Pass_credit = int(input("Enter the Pass mark: "))
            if Pass_credit not in range(0,140,20):
                    print("Out of range")# This is a main part of the code. when this paet is run get pass,defer 
                    raise SystemExit    
            else:                                                                   #and fail credits,check the if enter input is integer, total credit equal to 120, 
                Defer_credit = int(input("Enter the Defer Credit: "))               #pass,defer and fail credit in marks range.
                if Defer_credit not in range(0,140,20):
                    print("Out of Range")
                    raise SystemExit
                else:
                    fail_credit = int(input("Enter the fail credit: "))
                    if fail_credit not in range(0,140,20):
                        print("Out of range")
                        raise SystemExit
        except ValueError:
            print("Enter the integer value")
            raise SystemExit
        if (Pass_credit + Defer_credit + fail_credit) != 120:
            print("Toatal incorrect")
            raise SystemExit
        outcomes = w2052950_part1A.outcomes[Pass_credit,Defer_credit,fail_credit]
        print(outcomes)
        print("Thank You!")
    
def previous_text_file():
    new = input("if you want or not previous text file then enter Yes(y) or No(n): ").lower()
    print("\n")
    if new == "y":       #This part is a if already have text file delet or not 
        pass
    else:
        if os.path.exists("marks.txt"):     #delete previous text file using os module
              os.remove("marks.txt")
            
def loop():
    for i in first:             #This part used for loop the code
        Again = input("\nWould you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: ").lower()
        print("\n")
        if Again == "y" or Again != "q":             
            staff_inputs()                    #when user enter y then continue the code 
            continue
            count+= 1
        if Again == "q":
            w2052950_part_1D.Graph(Graph_list)
            text = open("marks.txt","r")         #when user enter the q then create the graph and print the lists exit the code 
            cont = text.read()
            text.close()
            print(cont)
            raise SystemExit
    
def staff_inputs():
        Pass_credit = int(input("Enter the Pass mark: "))
        try:
                if Pass_credit not in range(0,140,20):
                    print("Out of range")
                    loop()                                                              # This is a main part of the code. when this paet is run get pass,defer 
                else:                                                                   #and fail credits,check the if enter input is integer, total credit equal to 120, 
                    Defer_credit = int(input("Enter the Defer Credit: "))               #pass,defer and fail credit in marks range.
                    if Defer_credit not in range(0,140,20):
                        print("Out of Range")
                        loop()
                    else:
                        fail_credit = int(input("Enter the fail credit: "))
                        if fail_credit not in range(0,140,20):
                            print("Out of range")
                            loop()
        except ValueError:
                print("Enter the integer value")
                loop()    
        if (Pass_credit + Defer_credit + fail_credit) != 120:
                print("Toatal incorrect")
                loop()
        print(w2052950_part1A.outcomes[Pass_credit,Defer_credit,fail_credit])
        outcomes = w2052950_part1A.outcomes[Pass_credit,Defer_credit,fail_credit]
        Graph_list.append(outcomes)                          #append the result for graph list
        file = open("marks.txt","a")                    #Text file handling
        file.write(f"\n{w2052950_part1A.outcomes[Pass_credit,Defer_credit,fail_credit]} - {Pass_credit},{Defer_credit},{fail_credit}")
        file.close()
        loop()            # loop the code
        return markschart.outcomes[Pass_credit,Defer_credit,fail_credit],Pass_credit,Defer_credit,fail_credit        #return the values

for a in new:
        print("Student: 1 | Staff: 2 ")
        person = input("Enter the 1 or 2: ").lower()  # rhis part is a if user choose student or staff part then run the its own functions
        print('\n')
        if person == "1":
            student_input()
            raise SystemExit
        else:
            previous_text_file()
            staff_inputs()
    

    




