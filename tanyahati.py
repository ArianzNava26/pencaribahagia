namamu = str(input("\nSiapa Nama Anda?\n>> "))
print("\nSebutkan 3 Hal yang POSITIF dan Paling Kamu Sukai dalam Hidup!\n")
sebut1 = str(input("\nYang Pertama\n>> "))
sebut2 = str(input("\nYang Kedua\n>> "))
sebut3 = str(input("\nYang Ketiga\n>> "))
kesukaan = [sebut1, sebut2, sebut3]
print()
print(f"Sahabatku {namamu} bahagia versi Kamu adalah: ")
for permata in kesukaan:
    hakikat = "Menolong Orang dengan "
    bijaksana = "Bahagiamu itu adalah " + hakikat + permata
    print()
    print(bijaksana)
print()
bahagia = "*** Selalu Bahagia Terus Ya! *** ~ Arian S"
print(bahagia.center(80))
print(end="\n")
