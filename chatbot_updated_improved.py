print('Hello! I am Milo')
print('I will be assisting you today!')
name = str(input("What is your name? "))
print("Hello " + name)
subject = str(input("Maths or Science? "))

if subject.upper() == "MATH" or subject.upper() == "MATHS" or subject.upper() == "MATHEMATICS":
    question = input("Which question do you need help in?(a,b,c) ")
    if question.lower() == "a":
        print('For question a. let the number be x and then rearrange the equation as x*6=66 so 6x=66 so x=66/6 x=11')
    elif question.lower() == "b":
        print('x+28/4=50 so x+28=50*4 then 50*4 =200 then =200-28 = 178')
    elif question.lower() == "c":
        print('In this question, we use prime factorization to attain 52 as root of 2704, since root of 2704 = root of 2*2*2*2*13*13 = 2*2*13 =52.')
    else:
        print("!error! : please enter either a, b, or c. Thank you!")

elif subject.upper() == "SCIENCE":
    question = input("Which question do you need help in?(a,b,c) ")
    if question.lower() == "a":
        print("for question a the answers are nostrils as they are the openings in our noses that help us breath freely")
    elif question.lower() == "b":
        print("this is direct answer 32 ,16 present in the upper jaw and 16 in the lower jaw not even close to the mighty shark :p ")
    elif question.lower() == "c":
        print('Our body does this by using platelets which repair our skin')
    else:
        print("!error! : please enter either a, b, or c. Thank you!")

else:
    print("!error! : please follow instruction")


calculator = input("Do you want to use my bonus calculator feature?(yes/no) ")

if calculator.lower() == "yes":
  operator = input("Do you want to (A)dd, (S)ubtract, (M)ultiply, or (D)ivide? ")

  if operator.upper() == "A":
    i = int(input("How many numbers do you want to add? "))
    n = 0
    s = 0

    if i==1:
        print("!error! : You cannot enter 1.")
    else:
        while n<i:
            ig = float(input("Enter a number: "))
            s = s + ig
            n = n + 1
        print("The sum: " + str(s))
        print("Hope I was helpful!")

  elif operator.upper() == "M":
    i = int(input("How many numbers do you want to multiply? "))
    n = 0
    s = 1

    if i==1:
        print("!error! : You cannot enter 1.")
    else:
        while n<i:
            ig = float(input("Enter a number: "))
            s = s * ig
            n = n + 1
        print("The product: " + str(s))
        print("Hope I was helpful!")

  elif operator.upper() == "D":
    i = int(input("How many numbers do you want to divide by each other, in order? "))
    n = 0

    if i==1:
        print("!error! : You cannot enter 1.")
    else:
        ig = float(input("Enter your first number: "))
        s = ig
        n = n + 1
        while n<i:
            ig = float(input("Enter another number: "))
            s = s / ig
            n = n + 1
        print("The quotient: " + str(s))
        print("Hope I was helpful!")

  elif operator.upper() == "S":
    i = int(input("How many numbers do you want to subtract, in order? "))
    n = 0

    if i==1:
        print("!error! : You cannot enter 1.")
    else:
        ig = float(input("Enter your first number: "))
        s = ig
        n = n + 1
        while n<i:
            ig = float(input("Enter another number: "))
            s = s - ig
            n = n + 1
        print("The difference: " + str(s))
        print("Hope I was helpful!")

  else:
    print("!error!")
    print("Kindly rerun and follow instructions.")

elif calculator.lower() == "no":
  print("Hope I was helpful!")

else:
    print("!error!")
    print("Kindly rerun and follow instructions.")
