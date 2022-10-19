# ATM Program#
import random


def main():
    total_money = {200: 100, 100: 100, 50: 100, 20: 100, 10: 100} # Atm içindeki tüm paraları temsil eden Dictionary
    hour = 8 # Saat
    minute = 0 # Dakika
    loop_counter = 0 # Para çekme/yatırma döngü işlemini kontrol eden değişken
    total_counter = 0 # Toplam müşteri
    counter = random.randint(0, 9) # Random para yatırma sırasını belirleyen değişken
    remain_money = left_behind_money(total_money) # Tüm paraların toplam değeri

    while (remain_money != 0): # Atm'de para bitene kadar döngü devam etsin
        loop_counter += 1
        total_counter += 1
        if loop_counter == 10: # Her 10 kişide sıfırlanan para random yatırma kontrolü
            loop_counter = 0
            counter = random.randint(0, 9)

        hour, minute = random_time_split(hour, minute) # Random işlem saati belirlenir.

        if counter == total_counter % 10:  # Para yatırma
            total_money =  deposit_money(total_money, hour, minute, total_counter)
        else:  # Para çekme
            total_money = withdraw_money(total_money, hour, minute, total_counter)
        remain_money = left_behind_money(total_money)
    print("\n--- para bitti ---")



def random_time_split(hour, minute):
    temp_min = random.randint(1, 15) # 15 dakika içerisinde random gerçekleşen işlem saatine göre saat ilerler.
    minute += temp_min
    if minute > 60:
        minute -= 60
        hour += 1
    return hour, minute  # Saat ve dakika bilgisi döndürür.


def withdraw_money(total_money, hour, minute, total_counter):
    money = random.randrange(10, 2000,10)# 10-2000 arasında 10'un katları şekilde random belirlenen işlem tutarı
    last_process = left_behind_money(total_money)
    if money > last_process:
        money = last_process
    flag = False #para cektiğini doğrulayan boolean değişken
    cash200, cash100, cash50, cash20, cash10 = split_money(money, total_money,flag)  # İşlem sırasında kullanılan para adetleri belirlendi

    cash_list = [cash200, cash100, cash50, cash20, cash10]

    #Yazdırma işlemleri
    print("{}. kişi {} TL çekecek (saat: {:02d}:{:02d})".format(total_counter, money,(hour),minute))
    print("verilen   :",end=" ")
    for i in cash_list:
        if i != 0:
            if cash_list.index(i) == 0:
                print("{} adet 200,".format(i),end = " ")
            elif cash_list.index(i)==1:
                print("{} adet 100,".format(i),end = " ")
            elif cash_list.index(i)==2:
               print("{} adet 50,".format(i),end = " ")
            elif cash_list.index(i)==3:
                print("{} adet 20,".format(i),end = " ")
            else:
                print("{} adet 10.".format(i),end=" ")
    print("")
    print("kalan     : {} adet iki yüz, {} adet yüz, {} adet elli, {} adet yirmi, {} adet on.\n"
          .format(total_money[200],total_money[100], total_money[50], total_money[20], total_money[10]))
    return total_money


def deposit_money(total_money, hour, minute, total_counter):
    flag = True #para yatırdığını doğrulayan boolean değişken
    money = random.randrange(10, 2000,10) # 10-2000 arasında 10'un katları şekilde random belirlenen işlem tutarı
    cash200, cash100, cash50, cash20, cash10 = split_money(money, total_money, flag) # İşlem sırasında kullanılan para adetleri belirlendi
    cash_list = [cash200, cash100, cash50, cash20, cash10]

    #Yazdırma işlemleri
    print("{}. kişi {} TL yatıracak (saat: {:02d}:{:02d})".format(total_counter, money, hour,minute))
    print("alınan    :",end=" ")
    for i in cash_list:
        if i != 0:
            if cash_list.index(i) == 0:
                print("{} adet 200,".format(i),end = " ")
            elif cash_list.index(i)==1:
                print("{} adet 100,".format(i),end = " ")
            elif cash_list.index(i)==2:
               print("{} adet 50,".format(i),end = " ")
            elif cash_list.index(i)==3:
                print("{} adet 20,".format(i),end = " ")
            else:
                print("{} adet 10.".format(i),end=" ")
    print("")
    print("kalan     : {} adet iki yüz, {} adet yüz, {} adet elli, {} adet yirmi, {} adet on.\n"
          .format(total_money[200],total_money[100], total_money[50], total_money[20], total_money[10]))

    return total_money


def split_money(money, total_money,flag): # Kullanılan para miktarlarını belirleyip doğru banknotlara ayıran ve Atm'deki para miktarlarını düzenleyen metod.
    remainder = money # İşlemlerde kalan para değeri
    cash200 = 0
    cash100 = 0
    cash50 = 0
    cash20 = 0
    cash10 = 0
    while remainder != 0: # İşlem tutarı bitene kadar döngü devam etsin.
        if remainder > 4 * 100 and total_money[200] != 0: #İşlem tutarı 4 banknot değerinden büyükse ve ATM'de banknot bitmemişse DOĞRU
            if total_money[200]*200>remainder:
                cash200 = remainder // 200
            else:
                cash200 = total_money[200]
            remainder -= (cash200 * 200)

            if flag: #Para yatırma
                total_money[200] += cash200
            else: #Para çekme
                total_money[200] -= cash200

        elif remainder > 4 * 50 and total_money[100] != 0: #İşlem tutarı 4 banknot değerinden büyükse ve ATM'de banknot bitmemişse DOĞRU
            if total_money[100]*100>remainder:
                cash100 = remainder // 100
            else:
                cash100 = total_money[100]

            remainder -= (cash100 * 100)
            if flag:#Para yatırma
                total_money[100] += cash100
            else: #Para çekme
                total_money[100] -= cash100

        elif remainder > 4 * 20 and total_money[50] != 0: #İşlem tutarı 4 banknot değerinden büyükse ve ATM'de banknot bitmemişse DOĞRU
            if total_money[50]*50>remainder:
                cash50 = remainder // 50

            else:
                cash50 = total_money[50]

            remainder -= (cash50 * 50)
            if flag:#Para yatırma
                total_money[50] += cash50
            else: #Para çekme
                total_money[50] -= cash50

        elif remainder > 4 * 10 and total_money[20] != 0: #İşlem tutarı 4 banknot değerinden büyükse ve ATM'de banknot bitmemişse DOĞRU
            if total_money[20]*20>remainder:
                cash20 = remainder // 20

            else:
                cash20 = total_money[20]
            remainder -= (cash20 * 20)
            if flag:#Para yatırma
                total_money[20] += cash20
            else: #Para çekme
                total_money[20] -= cash20

        else:

            cash10 = remainder//10
            remainder -= cash10*10
            if flag:#Para yatırma
                total_money[10] += cash10
            else: #Para çekme
                total_money[10] -= cash10

    return cash200, cash100, cash50, cash20, cash10


def print_left_behind_money(total_money):
    print("Kalan :", total_money[200], "adet iki yüz,", total_money[100], "adet yüz,",
          total_money[50], "adet elli,", total_money[20], "adet yirmi,", total_money[10], "adet on.")


def left_behind_money(total_money):
    return total_money[200]*200 + total_money[100]*100 + total_money[50]*50 + total_money[20]*20 + total_money[10]*10


main()
