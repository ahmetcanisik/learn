
const objemiz = {
    objeElemani: "bu elemanın görevi buraya yazacağın değeri aklında tutmak."
}


Objelerin elemanlarına şu şekilde ulaşıyoruz: ⁠ objemiz.objeElemani ⁠

Dizilerde birer objedir. Sen dizinin içine değerler aktarırsın bu gider önceden oluşan objenin içine atar.

⁠ const dizimiz = ["eleman1", 3, 50.1] ⁠

bu dizimiz arka planda objeye dönüştürülüyor ve önceden hazırlanmış metodlarda bu sürece dahil ediliyor;


const ornekDizi = {
    0: "eleman1",
    1: 3,
    2: 50.1,
    sort: function() {...},
    reverse: function() {...}
}


Sonra bu objeyle dizimizle yer değiştiriyor.

⁠ sort ⁠, bu metod alfabetik olarak değerleri sıralar


const wtkOgrencileri = ["emre", "veysel", "bayram", "ahmet"];

console.log(wtkOgrencileri); // ["emre", "veysel", "bayram", "ahmet"]

wtkOgrencileri.sort();

console.log(wtkOgrencileri); // ["ahmet", "bayram", "emre", "veysel"] 


⁠ reverse ⁠ ise en sondaki elemanların sırasını değiştiriyor aynı bi kelimeyi tersten okumak gibi (emre -> erme)


console.log(dizimiz); // ["eleman1", 3, 50.1]

dizimiz.reverse();

console.log(dizimiz); // [50.1, 3, "eleman1"];
