glucose_yesterday = 0
glucose_today = 0
glucose_today = int(input("Enter the amount of glucose from today: "))
glucose_yesterday = int(input("Enter the amount of glucose from yesterday: "))
if glucose_today > glucose_yesterday:
    print("Great! Your reading improved!")
    glucose_today + 1
else:
    print("No change")
    glucose_yesterday + 1
print("glucose today = " , glucose_today )
print("glucose yesterday = ", glucose_yesterday)
