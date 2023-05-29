skaitli = []

summa = 0
skaits = 0 

while True:
    ievads=(int(input("Ievadi skaitļus lai pabeigtu ievadi 0 :")))

    if ievads==0:
         break
    skaitli.append(ievads)

for skaitlis in range(len(skaitli)):
    if skaitli[skaitlis] % 2 == 0:
        summa = summa + skaitli[skaitlis]
        skaits = skaits + 1
   
rezultats = summa / skaits
print(f"Pāra skaitļu vidējais aritmētiskais ir: {rezultats}")