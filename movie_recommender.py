#Movie_Recommender
from csv import reader
from termcolor import colored


genres=['Action','Adventure','Animation','Crime','Comedy','Horror','Romance','sci-fi','thriller']

name=input("Please type your name - ")
print(f"\nHii {name} good to see you. I'm here to suggest you some best movies to watch")
print("\nOkayy....so tell me....on what basis you want to watch movies..??")
print("\n1. Rating\n2. Genre")

m=int(input("Enter your choice number - "))

if m==1:
    o=input("Enter your prefered rating on the scale of 1 to 9 (1 place after decimal) - ")

    with open("all_movies.csv",'r') as f:
        csv_reader=reader(f)
        for row in csv_reader:
            if(row[1]==o):
                print(f"{colored(row[0],'yellow',attrs=['bold'])},{colored(row[3],'blue',attrs=['bold'])}")

elif m==2:                
    print("\nPlease choose your preferred genre : ")
    print("\n0. Action\n1. Adventure\n2. Animation\n3. Crime\n4. Comedy\n5. Horror\n6. Romance\n7. Sci-fi\n8. Thriller")


    n=int(input("\nEnter your preferred genre number - "))

    print("\nHere are best movies from your chosen genre according to IMDB..")
    print("Fetching.......")


    with open("all_movies.csv",'r') as f:
        csv_reader=reader(f)
        for row in csv_reader:
            if(row[3]==genres[n]):
                print(f"{colored(row[0],'yellow',attrs=['bold'])},{colored(row[1],'blue',attrs=['bold'])},'\n'{colored(row[2],'white')}")

else:
    print("Oops...please input valid input..!!")

