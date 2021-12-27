
shema = """
-------------------
|  {}  |  {}  |  {}  |
|  {}  |  {}  |  {}  |
|  {}  |  {}  |  {}  |
-------------------
"""

print("""
---------------------------------
|           Tik-Tac-Toe         |
---------------------------------
| Yapımcı : Beetlejuicetr (MID) |
| Dil     : Python 3.9.7        |
| Sürüm   : v1.0                |
---------------------------------


{}
""".format(shema.format(" "," "," "," "," "," "," "," "," ")))

slots="         "

newslot = ""

while True:
	
	birinciOyuncu = input("Birinci oyuncu (1-9) : ") # Birinci oyuncudan bir yer seçmesini istiyorum


	try: # her hangi bir hata olursa bunu idare edelim diye try kullanıyorum
		
		newslot = "" # yeni olusturulacak slotu temizliyorum bir birini kopyalama olmasın

		birinciOyuncu = int(birinciOyuncu) # oyuncudan aldığım değeri sayıya çeviriyorum

		if birinciOyuncu <= 9 and birinciOyuncu >= 0: # Oyuncunun girdiği değeri kontrol ediyorum 0-9 arasında girmesi gerekli!
			
			
			for i in range(0,9): # oyuncunun seçtiği yere işaret koymak için for döngüsüyle 
				#print("newslot",newslot)
				if i == birinciOyuncu -1: # oyuncunun girdiği sayı mı değil mi? kontrol ediyorum
					if slots[i] != "O" and slots[i] != "X": # oyuncunun sayısı her hangi bir işaretle çakışıyor mu?
						newslot = newslot + "X" # Hiç bir karakterle çakışmıyorsa karakterimizi ekliyorum

					# Seçimimiz başka bir karakterle çakışırsa gösterilecek mesaj
					else:
						print("\nBurası zaten dolu!")
						print("Üzgünüm fakat artık sıran 2.oyuncuya geçti :/ \n")
						newslot = newslot + slots[i]

				else: # oyuncumuzun girdiği sayı değilse yapılacak işlem
					newslot = newslot + slots[i]
			
			slots = newslot # Yukarıda oyuncumuzun girdisiyle oluşan yeni tabloyu kullanıdığımız tabloya aktarıyorum

			print(shema.format(slots[0],slots[1],slots[2],slots[3],slots[4],slots[5],slots[6],slots[7],slots[8])) # tabloyu gösterir

			# Başarım durumları

			# Soldaçn - Sağa
			if slots[0] == slots[1] == slots[2] == "X":
				print("Birinci oyuncu kazandı!")
				break
			elif slots[3] == slots[4] == slots[5] == "X":
				print("Birinci oyuncu kazandı!")
				break
			elif slots[6] == slots[7] == slots[8] == "X":
				print("Birinci oyuncu kazandı!")
				break


			# Yukarıdan - Aşağıya
			elif slots[0] == slots[3] == slots[6] == "X":
				print("Birinci oyuncu kazandı!")
				break
			elif slots[1] == slots[4] == slots[7] == "X":
				print("Birinci oyuncu kazandı!")
				break
			elif slots[2] == slots[5] == slots[8] == "X":
				print("Birinci oyuncu kazandı!")
				break

			# Çapraz
			elif slots[0] == slots[4] == slots[8] == "X":
				print("Birinci oyuncu kazandı!")
				break
			elif slots[2] == slots[4] == slots[6] == "X":
				print("Birinci oyuncu kazandı!")
				break
			
			pass

		else: # oyuncunun girdiği sayı istediğimiz sayı aralığının dışındaysa
			print("Sadece 1 ve 9 arasında sayı giriniz!")
			break

		#------------------------------------------------------------------------#
		# ---------- Üstteki Aynı Açıklamalar 2. Oyuncu içinde Geçerli ----------#
		#------------------------------------------------------------------------#

		newslot = "" 
		
		ikinciOyuncu = input("İkinci oyuncu (1-9) : ") 

		ikinciOyuncu = int(ikinciOyuncu)
		if ikinciOyuncu <= 9 and ikinciOyuncu >= 0:
			
			
			for i in range(0,9):
				#print("newslot",newslot)
				if i == ikinciOyuncu -1:
					if slots[i] != "X" and slots[i] != "O":
						newslot = newslot + "O"
					else:
						print("\nBurası zaten dolu!")
						print("Üzgünüm fakat artık sıran 1.oyuncuya geçti :/ \n")
						newslot = newslot + slots[i]
					
				else:
					newslot = newslot + slots[i]
		
			slots = newslot

			print(shema.format(slots[0],slots[1],slots[2],slots[3],slots[4],slots[5],slots[6],slots[7],slots[8]))
			


			# Soldan - Sağa
			if slots[0] == slots[1] == slots[2] == "O":
				print("İkinci oyuncu kazandı!")
				break
			elif slots[3] == slots[4] == slots[5] == "O":
				print("İkinci oyuncu kazandı!")
				break
			elif slots[6] == slots[7] == slots[8] == "O":
				print("İkinci oyuncu kazandı!")
				break


			# Yukarıdan - Aşağıya
			elif slots[0] == slots[3] == slots[6] == "O":
				print("İkinci oyuncu kazandı!")
				break
			elif slots[1] == slots[4] == slots[7] == "O":
				print("İkinci oyuncu kazandı!")
				break
			elif slots[2] == slots[5] == slots[8] == "O":
				print("İkinci oyuncu kazandı!")
				break

			# Çapraz
			elif slots[0] == slots[4] == slots[8] == "O":
				print("İkinci oyuncu kazandı!")
				break
			elif slots[2] == slots[4] == slots[6] == "O":
				print("İkinci oyuncu kazandı!")
				break

			pass

		else:
			print("Sadece 1 ve 9 arasında sayı giriniz!")
			break
	except ValueError: # sayı dışında bir karakter girildiğinde çıkarılacak hata
		print("Hata! Sadece sayı giriniz.")
		break
	
	
	pass
