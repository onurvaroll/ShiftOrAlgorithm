# ShiftOrAlgorithm
Shift Or algoritması, bir metinde belirli bir kelime veya kelime grubunun olup olmadığını kontrol etmek için kullanılır. Bu algoritma, kelime uzunluğuna bağlı olarak lineer zaman karmaşıklığına sahip bir algoritmadır.

Algoritmanın çalışma şekli şu şekildedir:

Kelimenin karakterlerini bit vektörüne dönüştürün. Her karakter, bit vektöründeki belirli bir bit konumuna atanır.
Bit vektöründe belirli bir aralığı arayın, bu aralık kelimenin bit vektörüyle karşılaştırılacak olan metnin bit vektöründeki konumunu gösterir.
Karşılaştırma işlemi, bitwise OR işlemi ile gerçekleştirilir. Eğer eşleşme olursa, OR işlemi sonucu sıfır olmayan bir bit elde edilir.
Shift Or algoritması, en kötü durumda tamamen eşleşmeyen bir kelime için bile O(nm) zamanda çalışır. Burada n, metnin uzunluğu ve m, kelimenin uzunluğudur. Ancak, iyi tasarlanmış bir bit vektörü ile Shift Or algoritması, genellikle diğer kelime arama algoritmalarından daha hızlı çalışır.
