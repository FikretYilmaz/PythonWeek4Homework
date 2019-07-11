"""Futfutbol dosyasındaki futbolcu isimlerini yazdığınız program ile Türkçe karakter içermeyecek bir hale getirip yeni bir dosyaya kaydediniz."""
with open("futfutbol.txt","r+") as file:
	file1 = file.read()
	file3 = open("englisCharacter.txt", "w+")
	file2=file1.replace("ş","s").replace("ç","c").replace("ö","o").replace("ğ","g").replace("ü","u").replace("ı","i").replace("Ş","S").replace("Ç","C").replace("Ö","O").replace("Ğ","G").replace("Ü","U").replace("İ","I")
	print(file2)
	print(file2,file=file3)
	file3.close()
	