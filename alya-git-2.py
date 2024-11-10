# Ananda Alya P.M
# 2403506
# RPL 1A

def deret_fibonacci(n):
    if n <= 1:
        return n
    else:
        return deret_fibonacci(n - 1) + deret_fibonacci(n - 2)

angka = int(input("Masukkan angka : "))

print("Deret : ")
for i in range(angka):
    print(deret_fibonacci(i), end= " ")

def login():
    password_yang_benar = "Latihan"
    kesempatan = 3

    while kesempatan > 0:
        username = input("Masukkan username Anda : ")
        password = input("Masukkan password Anda : ")

        if password == password_yang_benar:
            print("Selamat! Anda berhasil Login!")
        else:
            kesempatan -= 1
            print("Password salah!")
            
            if kesempatan > 0:
                print(f"Anda masih memiliki {kesempatan} kesempatan.")
            else:
                print("Akses Anda ditolak!")

login()

def waktu_lari(jam_mulai, menit_mulai, detik_mulai, jam_selesai, menit_selesai, detik_selesai):
    total_detik_mulai = (jam_mulai * 3600) + (menit_mulai * 60) + detik_mulai
    total_detik_selesai = (jam_selesai * 3600) + (menit_selesai * 60) + detik_selesai
    selisih = total_detik_selesai - total_detik_mulai
    jam = selisih / 3600
    menit = selisih % 3600 / 60
    detik = selisih % 60
    return jam, menit, detik

jam_mulai = int(input("Jam mulai : "))
menit_mulai = int(input("Menit mulai : "))
detik_mulai = int(input("Detik mulai : "))

jam_selesai = int(input("Jam selesai : "))
menit_selesai = int(input("Menit selesai : "))
detik_selesai = int(input("Detik selesai : "))

jam, menit, detik = waktu_lari(jam_mulai, menit_mulai, detik_mulai, jam_selesai, menit_selesai, detik_selesai)
print(f"{jam} jam, {menit} menit, {detik} detik")