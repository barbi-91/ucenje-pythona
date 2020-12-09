def caesar_enkripcija(kod,korak):
  output=[]
  kod1=[]
  velika = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  mala = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  for slovo in kod:
    if slovo in velika:
      index=velika.index(slovo)
      kodiranje=(index + korak)%26
      kod1.append(kodiranje)
      slovo1=velika[kodiranje]
      output.append(slovo1)

    elif slovo in mala:
      index=mala.index(slovo)
      kodiranje=(index + korak) %26
      kod1.append(kodiranje)
      slovo1=mala[kodiranje]
      output.append(slovo1)
  return output

print(caesar_enkripcija("„Na svijetu uvijek postoji jedna osoba koja čeka onu drugu, bilo da je nasred pustinje ili usred velikog grada. A kad se te osobe sretnu i njihovi se pogledi ukrste, prošlost i budućnost gube svako značenje. Postoji taj trenutak i nevjerojatna sigurnost da je sve stvari pod suncem ispisala jedna ista ruka, ruka koja je stvorila po jednu dušu, blizanku za svaku osobu.-P.C.", 28))
