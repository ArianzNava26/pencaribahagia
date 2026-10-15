namamu = str(input("\nWhat is your name?\n>> "))
print("\nName 3 POSITIVE things you love most in life!\n")
sebut1 = str(input("\nThe First\n>> "))
sebut2 = str(input("\nThe Second\n>> "))
sebut3 = str(input("\nThe Third\n>> "))
kesukaan = [sebut1, sebut2, sebut3]
print()
print(f"My friend {namamu}, your version of happiness is: ")
for permata in kesukaan:
    hakikat = "Helping people with "
    bijaksana = "Your happiness is " + hakikat + permata
    print()
    print(bijaksana)
print()
bahagia = "*** Always Stay Happy! *** ~ Arian S"
print(bahagia.center(80))
print(end="\n")
