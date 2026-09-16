print("Analisis Persamaan Kuadrat")

a = float(input("Koefisien a: "))
b = float(input("Koefisien b: "))
c = float(input("Koefisien c: "))

if a == 0:
    print("Bukan persamaan kuadrat.")
else:
    diskriminan = b ** 2 - 4 * a * c
    print(f"Diskriminan = {diskriminan:.2f}")

    if diskriminan > 0:
        akar_1 = (-b + diskriminan ** 0.5) / (2 * a)
        akar_2 = (-b - diskriminan ** 0.5) / (2 * a)
        print("Dua akar real berbeda.")
        print(f"Akar pertama = {akar_1:.2f}")
        print(f"Akar kedua = {akar_2:.2f}")
    else:
        if diskriminan == 0:
            akar = -b / (2 * a)
            print("Akar kembar.")
            print(f"Akar = {akar:.2f}")
        else:
            print("Tidak ada akar real.")