def nthFibonacci(nthTerm):
    termOne = 0
    termTwo = 1

    if(nthTerm == 0):
        print("The first term in Fibonacci Sequence is: ", termOne)
    elif(nthTerm == 1):
        print("The second term in Fibonacci Sequence is: ", termTwo)
    else:
        for counter in range(nthTerm):
            print("Term #", counter, " :", termOne)
            nthNumber = termOne + termTwo
            termOne= termTwo
            termTwo = nthNumber 

if __name__ == "__main__":

    while True:
     try:
        nthTerm = int(input("Which nth term would you like to compute? "))
        nthFibonacci(nthTerm)
        break
     except:
        print("Invalid input. Please try again. ")