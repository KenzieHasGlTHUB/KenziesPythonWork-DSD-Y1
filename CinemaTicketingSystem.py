# Task 2: Cinema Ticketing System


cinema = {
    "Wonka": {"Time": "17:45", "Seats": 45,},
    "Dune 2": {"Time": "19:00", "Seats": 30,},
}
print("What would you like to do?")

print("1) View all movies")
print("2) Add a new film with seats and times")
print("3) Book Tickets")
print("4) Delete a film")
print("5) Validate Seat Counts")
option=input("Please select now: ")

if option == "1":
    print(cinema)

elif option == "2":
    Movie3=input("Enter the new film you would like to watch: ")
    Time3 = input("Enter the time that this movie will be broadcasted: ")
    Seats3 = input("How many seats will be taken?: ")
    cinema =  {"Wonka": {"Time": "17:45", "Seats": 45},
               "Dune 2": {"Time": "19:00", "Seats": 30}
               movie3: {"Time": Time3, "Seats": Seats3}
    }   
elif option == "3":
    Tickets = input("Enter what movie you would to see?: ")
    Amount = input("How many people will be coming with you?: ")