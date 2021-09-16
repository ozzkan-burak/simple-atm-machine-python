
Account01 = {
  'Fullname' : 'Ali Veli',
  'AccountNo': '87654321',
  'Balance' : 3000,
  'AdditionalAccount': 2000,
}

Account02 = {
  'Fullname' : 'Veli Derin',
  'AccountNo': '12345678',
  'Balance' : 2000,
  'AdditionalAccount': 1000
}

def Withdraw(account, amount):
  # print(f"Merhaba {account['Fullname']}")

  if account["Balance"] >= amount:
    account["Balance"] -= amount
    print("Paranizi alabilirsiniz.")
    BalanceInquiry(account)
 
  else:
    totalAmount = account['Balance'] + account['AdditionalAccount']
   
    if totalAmount >= amount:
      additionalAccountUsage = input('Ek hesabinizdan kullanmak istermisiniz? e = Evet, h = Hayir')
   
      if additionalAccountUsage == 'e':
        account['Balance'] = 0 
        account['AdditionalAccount'] = totalAmount - amount
        print('Paranizi alabilirsiniz.')
        BalanceInquiry(account)
      else:
        print("{account['AccountNo']} nolu hesabinizda {account['Balance']} Tl paraniz bulunmakta. Ek hesabinizda {account['AdditionalAccount']} TL bulunmaktadir")
    else:
      print('Hesabinizda yeterli bakiye bulunmamaktadir.')
      BalanceInquiry(account)





    
def BalanceInquiry(account):
  print(f"{account['AccountNo']} nolu hesabinizda {account['Balance']} Tl paraniz bulunmakta. Ek hesabinizda {account['AdditionalAccount']} TL bulunmaktadir")


Withdraw('Veli Derin', 2500)