# Lesson 13 Tasks

#Task 1

songs = str(input("Create a list of your 5 favourite songs"))
print("So heres your list of 5 songs: ")
print(songs)

q = input("Would you like to enter any other songs?")
if q == "yes":
    newsong = input("Enter a new song into the list: ")
    newlist = (songs, newsong)
    print(newlist)
else:
    print()

q2 = input("Would you like to remove any song from the list?")
if q2 == "yes":
    newsongs = input("Re-enter the same songs again however remove the song you did not want in the list: ")
    print(newsongs,newsong)

songs.sort()
songs