vertejums = int(input("Ievadi vērtējumu programmēšana no 1 līdz 10:"))
if vertejums < 1 or vertejums > 10:
    print("vērtējums nevar būt mazāks par 1 vai lielāks 10 ")
if vertejums >=1 and vertejums <=3:
    print("Zems")
elif vertejums >=4 and vertejums <=6:
    print("Vidējs")
elif vertejums >=7 and vertejums <=8:
    print("Augsts")
elif vertejums >=9 and vertejums <=10:
    print("Ļoti augsts")
