# alice_in_wonderland.txt dosyasını okuyoruz
with open('alice_in_wonderland.txt', 'r') as f:
    text = f.read()
    
# Shift-Or algoritması
def shift_or(text, pattern):
    m = len(pattern) # pattern uzunluğu
    mask = [1 << i for i in range(m)] # öntanımlı maske oluşturma
    P = [0] * 128 # 128 bitlik karakter kodları için maske
    for i in range(m):
        P[ord(pattern[i])] |= mask[i] # pattern'in karakterleri ile eşleştirme yapıyoruz
    result = 0 # eşleşmelerin sayısını tutmak için değişken
    state = 0 # bit durumunu takip etmek için değişken
    for c in text:
        state = ((state << 1) | 1) & P[ord(c)] # bit durumunu güncelleme
        result += state >> (m-1) # eşleşme durumunu kontrol etme ve sonuç değişkenini artırma
    return result

# Kelimelerimiz
word1 = 'upon'
word2 = 'sigh'
word3 = 'Dormouse'
word4 = 'jury-box'
word5 = 'swim'

# Shift-Or algoritmasını kullanarak kelime sayısını hesapla
count1 = shift_or(text, word1)
count2 = shift_or(text, word2)
count3 = shift_or(text, word3)
count4 = shift_or(text, word4)
count5 = shift_or(text, word5)

# Sonuçları ekrana yazdır
print(f"'{word1}' kelimesi {count1} kez tekrar etmiştir.")
print(f"'{word2}' kelimesi {count2} kez tekrar etmiştir.")
print(f"'{word3}' kelimesi {count3} kez tekrar etmiştir.")
print(f"'{word4}' kelimesi {count4} kez tekrar etmiştir.")
print(f"'{word5}' kelimesi {count5} kez tekrar etmiştir.")
