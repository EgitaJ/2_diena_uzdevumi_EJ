start = 1
stop = 100

for skaitlis in range(start, stop):
    if skaitlis % 3 == 0 and skaitlis % 5 == 0:
        print("BumRum")
    elif skaitlis % 5 == 0:
        print("Rum")
    elif skaitlis % 3 == 0:
        print("Bum")
    print(skaitlis)