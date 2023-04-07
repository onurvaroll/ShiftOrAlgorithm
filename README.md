# ShiftOrAlgorithm

Nasıl Çalışır?
Öncelikle kesinlikle txt dosyası ile python dosyası aynı klasör ya dizin içinde olmalıdır. Bazen VSCode txt dosyasını okumuyor bu durumda da klasör ile açıp
klasör içinden python dosyasını açtığımda bir sorun yaşamadım. Programın ne yaptığı yorum satırlarında yazılı olup çalıştırıldğında terminalde direkt sonuçlar yazmaktadır.


Açıklaması:

Shift-Or algoritması, bir örüntüyü bir metinde aramak için kullanılan bir bit maskeleme algoritmasıdır. Algoritma, öntanımlı maske oluşturma, bit durumu güncelleme ve eşleşme durumunu kontrol etme adımlarını içerir.

Örneğin, bu program bir metin dosyası olan "alice_in_wonderland.txt" dosyasını açar ve içindeki kelime sayısını hesaplamak için Shift-Or algoritmasını kullanır. Algoritma, kelime örüntülerini maskeleyerek, metindeki her karakteri örüntü ile karşılaştırır ve eşleşme durumunu takip eder.

Değişkenler:

Programda tanımlanan değişkenler şunlardır:

text: "alice_in_wonderland.txt" dosyasından okunan metni tutar. Bu değişken, Shift-Or algoritması tarafından örüntü aramak için kullanılır.

pattern: örüntüyü temsil eden bir karakter dizisidir. Bu değişken, Shift-Or algoritması tarafından metinde aranacak olan örüntüyü temsil eder.

m: pattern değişkeninin uzunluğunu tutar. Bu değişken, Shift-Or algoritması tarafından örüntüyü aramak için kullanılır.

mask: örüntüdeki her karakterin bit maskelemesi için kullanılan bir liste. Bu değişken, Shift-Or algoritması tarafından bit maskeleri oluşturmak için kullanılır.

P: her karakterin bit maskelemesi için kullanılan bir sözlük. Bu değişken, Shift-Or algoritması tarafından bit maskelemeleri oluşturmak ve karakterlerin bit durumunu takip etmek için kullanılır.

result: eşleşmelerin sayısını tutan bir değişken. Bu değişken, Shift-Or algoritması tarafından eşleşmeleri saymak için kullanılır.

state: bit durumunu takip eden bir değişken. Bu değişken, Shift-Or algoritması tarafından bit durumunu güncellemek ve eşleşmeleri saymak için kullanılır.

count1, count2, count3, count4, count5: her kelimenin sayısını tutan değişkenler. Bu değişkenler, Shift-Or algoritması tarafından her kelimenin sayısını hesaplamak için kullanılır.


Çalışma Analizi:

Programın çalışma zamanı analizi, algoritmanın en iyi, en kötü ve ortalama sınırlarını belirlemek için kullanılır. Shift-Or algoritması, örüntü uzunluğu m ve metin uzunluğu n için O(nm) çalışma zamanına sahiptir. En iyi durumda, algoritma O(m) çalışma zamanına sahip olabilir, yani örüntü bulunursa ilk karakterden başlayarak tek bir karakteri karşılaştırarak arama yapabilir. En kötü durumda, algoritma O(nm) çalışma zamanına sahip olabilir, yani örüntü metinde hiç bulunmazsa her karakter için tüm örüntüyü karşılaştırmak zorunda kalır. Ortalama durumda, algoritma O(n) çalışma zamanına sahiptir, yani örüntü metinde ortalama bir sayıda kez bulunursa.

Bu örnek programda, Shift-Or algoritması kullanılarak beş kelime için kelime sayısı hesaplanır ve sonuçlar ekrana yazdırılır. Programın çalışma zamanı, örüntü ve metin uzunluğuna bağlı olarak değişebilir, ancak ortalama durumda O(n) çalışma zamanı beklenir.
