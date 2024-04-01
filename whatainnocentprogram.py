from colorama import Fore
import sys
import os

#Kullanıcıya gösterilecek çıktıları bu fonksiyon ile daha kullanışlı bir biçimde verebiliyoruz
def print_message(msg_type, message):
    #Gelen msg_type stringine göre mesaj öncesine colorama kütüphanesi ile renklendirdiğim mesaj tipini ve sonrası için mesajı yazdırdığımız kod alttaki gibi
    if msg_type == "w":
        print(Fore.YELLOW + "[Warning] " + Fore.WHITE + message)
    elif msg_type == "i":
        print(Fore.LIGHTBLACK_EX + "[INFO] " + Fore.WHITE + message)
    elif msg_type == "s":
        print(Fore.GREEN + "[SUCCESSFULL] " + Fore.WHITE + message)
    elif msg_type == "e":
        print(Fore.RED + "[ERROR] " + Fore.WHITE + message)

def encrypt_file(path, key):
    try:
        print_message("i", "File Path: " + str(path))
        print_message("i", "Encryption Key: " + str(key))
        
        #sys kütüphanesi ile aldığım dosya yolunu 'rb' ile byte tipinde okumak istediğimi belirterek
        #open fonksiyonunu kullanıyorum dönen veriye fin değişkeni ile ulaşmak istediğimi belirtiyorum
        with open(path, 'rb') as fin:
            #dosya içeriğini okuduktan sonra bytearray tipine çevirip file değişkenine atıyorum
            file = bytearray(fin.read())

        #for döngüsü ile elimizdeki bytearray içeriğini enumerate ediyorum
        for i, value in enumerate(file):
            #i değeri her dönüşte artıyor ve bytearray içeriğimizin bir sonraki elemanını almamızı ve bu elemanı
            #file bytearray içeriğindeki byte verisinin key verisi ile XOR mantıksal işlecini (^) kullanarak dosyanın verilerini değiştiriyoruz
            #bu durumda dosya verileri bozulmuş olacaktır dolayısı ile key verinizi saklı tuttuğunuz sürece ulaşılmaz halde olacaktır 
            file[i] = value ^ key

        with open(path, 'wb') as fout:
            fout.write(file)
            #dosyayı yeni hali ile yazdık ve işlemin bittiğini yazdırdık

        print_message("s", "Encryption Done...")
        
    except Exception as e:
        print_message("e", 'Error caught: ' + str(e))

def decrypt_file(path, key):
    try:
        print_message("i", "File Path: " + str(path))
        print_message("i", "Decryption Key: " + str(key))
        
        #dosya yolumuzu aldık open ile rb read-byte şeklinde okuyacağımızı belirttik fin adı ile geri dönmesini istedik
        with open(path, 'rb') as fin:
            file = bytearray(fin.read())
            #aynı şekilde bytearray tipinde dosyayı okuduk array içerisine aktardık

        for i, value in enumerate(file):
            #key ile tekrar xor mantıksal işleç üzerinden geçirdik
            file[i] = value ^ key

        #verilen dosya yoluna bytearray içerisindeki key ile eski haline getirilmiş dosyamızı yazdırdık ve çıktı verdik
        with open(path, 'wb') as fout:
            fout.write(file)

        print_message("s", "Decryption Done...")

    except Exception as e:
        print_message("e", "Error caught: " + str(e))

#komut girişinde 4 input olması gerektiğini belirttim
if len(sys.argv) == 4:
    file_path = sys.argv[1] #dosya yolu 1.input
    operation = sys.argv[2] #şifreleme şifre çözümleme olarak yapılacak işlemi aldığımız input 2. inputumuz
    key = int(sys.argv[3]) #anahtar verimizi aldığımız input ise 3.input
    
    #verilen dosya yolunun kontrolünü sağladık
    if os.path.exists(file_path):
        if operation == "-d":
            #işlem -d olarak verildiyse şifre çözümleme fonksiyonumuzu çalıştırdık
            decrypt_file(file_path, key)
        elif operation == "-e":
            #işlem -e olarak verildiyse şifreleme fonksiyonumuzu çalıştırdık
            encrypt_file(file_path, key)
        else:
            print_message("w", "Invalid operation. Please use '-d' for decryption or '-e' for encryption.")
    else:
        print_message("w", "File not found.")
else:
    print_message("w", "imageCryptographer.py target_file_path operation(-d or -e) key(integer)")

#Ön Uyarı
    
#Ben bu programa bir for döngüsü ekleyeyimde tüm dosyaların içine erişsin hepsini rastgele key ile şifrelesin falan,
#yapmayalım böyle fidyeci hareketler önden uyarayım sorguda polislerimize bu vatandaş bana verdi demeyin sorumluluk kabul etmiyorum
#Fidye yazılım yapın diye vermiyorum saklamak istediğiniz fotoğraf olsun aman hocam şu gözükmesin diyorsanız onları şifrelersiniz yanlış yollara sapmayalım
#Umuyorum katkım olmuştur, iyi günler diliyorum
