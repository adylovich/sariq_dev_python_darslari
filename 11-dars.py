# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 14:49:12 2023

@author: @adylovich
"""

# yosh = int(input('Yoshingiz nechchida? '))
# if yosh<=4:
#     narh = 0
# elif yosh<=12:
#     narh = 5000
# elif yosh<=18:
#     narh = 7500
# else:
#     narh = 10000
# print(f"Sizga kirish {narh} so'm")

# kun = input("Bugun nima kun? >>>")
# harorat = float(input("Havo harorati qanday? "))

# if kun.lower()=='yakshanba' or kun.lower()=='shanba' and harorat>=30:
#     print("Cho'milgani kettik! ")
# elif kun.lower()=='yakshanba' or kun.lower()=='shanba' and harorat<30:
#     print('Uyda dam olamiz. ')

# narh = 15000
# choy = True
# salat = True

# if choy and salat:
#     narh = narh + 10000
# elif choy or salat:
#     narh = narh + 5000
    
# print(f"Jami {narh} so'm")


# narh = 15000
# choy = 1
# salat = 0
# non = 1
# kompot = 1
# assorti = 1
# if choy:
#     print("Mijoz choy oldi.")
#     narh = narh + 3000
# if salat:
#     print("Mijoz salat oldi.")
#     narh = narh +5000
# if non:
#     print("Mijoz non oldi.")
#     narh = narh + 2000
# if kompot:
#     print("Mijoz kompot oldi.")
#     narh - narh + 5000
# if assorti:
#     print("Mijoz assorti oldi.")
#     narh = narh + 15000
# print(F"Jami {narh} so'm.")

# menu = ['osh', 'qazonkabob', 'shashlik', 'norin', 'somsa']
# ovqat = input('Nima ovqat yeysiz?>>> ')
# if ovqat.lower() in menu:
#     print('Buyurtma qabul qilindi.')
# else:
#     print("Afsuski, bizda bunday ovqat yo'q.")
# ------------------------------------------------

# son = int(input("Istalgan juft sonni kiriting: \n>>> "))
# if son % 2 == 0:
#     print("Rahmat!")
# else:
#     print(f"{son} soni juft son emas! Iltimos, qaytadan urinib ko'ring... ")    
# --------------------------------------------------

# yosh = int(input("Chipta narhini bilish uchun yoshingizni kiriting: \n>>> "))
# if  yosh<=4 or yosh>=60:
#     print("Siz uchun chipta tekin!")
# elif yosh<18:
#     narh = 10000
# elif yosh>=18:
#     narh = 20000
#     print(f"Siz uchun chipta {narh} so'm.")         
# --------------------------------------------------

# x = int(input("Birinchi sonni kiriting: \n>>> "))
# y = int(input("Ikkinchi sonni kiriting: \n>>> "))
# if x > y: 
#     print(f"{x} soni {y} sonidan Katta")
# elif x < y:
#     print(f"{x} soni {y} sonidan Kichik")
# elif x == y:
#     print("Bu sonlar o'zaro teng!")
# ---------------------------------------------------

# mahsulotlar = ['anor', 'uzum', 'olma', 'shaftoli', 'olcha', 'xurmo', 'qulupnay', 
#                'nok', "gaynoli", 'qovun', 'tarvuz']

# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))
    
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         print(f"Do'konimizda {mahsulot} mahsuloti bor.")
#     else:
#         print(f"Do'konimizda {mahsulot} mahsuloti yo'q.")
# -----------------------------------------------------

# tovary = ['un', "yog'", 'sut', 'non', 'bulichka', 'qalam', 'sochiq']

# korzinka = []
# for n in range(3):
#     korzinka.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

# bor_tovary = []
# yoq_tovary = []

# for tovar in korzinka:
#     if tovar in tovary:
#         bor_tovary.append(tovar)
#     else:
#         yoq_tovary.append(tovar)
        
# if yoq_tovary:
#     print("Do'konimizda quyidagi mahsulotlar yo'q: ")
#     for tovar in yoq_tovary:
#         print(tovar)
# else:
#     print("Bizda so'ralgan barcha mahsulotlar bor")    

# --------------------------------------------------------

# users = ['sarvar', 'ali', 'vali', 'anvar', 'aliyor', 'aziz', 'doston']
# login = []

# login = input("Foydalanuvchi uchun yangi nom tanglang: ")
# if login in users:
#     print("Login band, boshqa login tanglang!")
     
# else:
#     print(f"Xush kelibsiz, {login.title()}!")

# --------------------------------------------------------

number = int(input("Butun son kiriting: "))

for n in range(2,11):
    if not (number%n):
        print(f"{number} soni {n} soniga qoldiqsiz bo'linadi")


    