/*
Tek bir parametre bekliyoruz o da String türünde ve name sahipliğinde.
daha sonra bu gelen parametrenin sonuna yeni bir değer ekliyoruz ardından
Tekrar geri döndürüyoruz.
*/
fn add_suffix(mut name: String) -> String {
    name.push_str(" Jr.");
    name
}


/*
Sahiplikte eğer bir heap'i başka bir sahip'e aktarırsanız eski sahip yok edilir.
bu örnekte "t", "e", "s", "t" bitlerinden oluşan bir heap String'i oluşturmuşuz. 
Ardından bu oluşturduğumuz değerleri bir sahip'e yani bir değişkene aktarıyoruz.
Bir sonraki satırda heap'ı yeni bir sahip'e(değişkene) bağlıyoruz.
Bunu yaptığımız anda eski sahip bellekten silinecektir. Yani serbest bırakılacaktır.
*/
fn moved_heap() {
    let a = String::from("test");
    let b = a; // a artık drop edildi yani serbest bırakıldı yani artık kullanılamaz. Taşındıktan sonra kullanılamaz.

    // b a'nın heap('test') üzerindeki sahipliğini aldı. Bu yüzden a artık kullanımdan kaldırıldı.
    println!("{b}")
}


/*
Yukarıdaki fonksiyon içerisinde bir heap'in yeni bir sahip'e aktarılmasının ardından eski sahip'in serbest kaldığını söylemiştik.
Eğer Eski heap değerlerini kaybetmek istemiyorsak bunu bir clone üzerinden de yapabiliriz.
ilk satırda "F", "e", "r", "r", "i", "s" bitlerinden oluşan String türünde bir heap oluşturup sahipliğini first değişkenine veriyoruz.
Daha sonra bir klonunu(kopyasını) oluşturup sahipliğini first_clone'a veriyoruz.
Bir sonraki satırda ise add_suffix() fonksiyonuna parametre olarak first_clone'u veriyoruz artık first_clone'un sahip olduğu heap başka bir sahip'e aktarıldı
bu yüzden first_clone bellekten serbest bırakıldı. Ancak bu işlemleri klon üzerinden yaptığımız için first değişkeninin sahip olduğu heap'e herhangi bir işlem
uygulanmadı.
*/
fn clone_heap() {
    let first: String = String::from("Ferris");
    let first_clone = first.clone();
    let full = add_suffix(first_clone);

    println!("{full} originally {first}");
}


fn referanced_owners(g1: &String, g2: &String) {
    println!("{} {}", g1, g2);
}


fn hello_world() {
    let m1 = String::from("Hello");
    let m2 = String::from("world");

    referanced_owners(&m1, &m2);
    let s = format!("{} {}", m1, m2);
    println!("{s}");
}


fn referances() {

    // Eğer x değişkenini tamamen heap ile oluşturulmuş bir değişkeni herhangi bir değere aktarmak istersek. o zaman * kullanmalıyız.
    let mut x: Box<i32> = Box::new(1);
    let a: i32 = *x;
    *x += 1;

    let r1: &Box<i32> = &x;
    let b: i32 = **r1;

    let r2: &i32 = &*x;
    let c: i32 = *r2;

    println!("{a} {b} {c}");
}


fn abs_referance() {
    let x: Box<i32> = Box::new(1);
    let x_abs1 = i32::abs(*x);
    let x_abs2 = x.abs();
    assert_eq!(x_abs1, x_abs2);

    let r: &Box<i32> = &x;
    let r_abs1 = i32::abs(**r);
    let r_abs2 = r.abs();
    assert_eq!(r_abs1, r_abs2);

    let s = String::from("hello");
    let s_len1 = str::len(&s);
    let s_len2 = s.len();
    assert_eq!(s_len1, s_len2);
}


fn first_word(s: &str) -> &str {
    let bytes = s.as_bytes();

    for (i, &item) in bytes.iter().enumerate() {
        if item == b' ' {
            return &s[0..i];
        }
    }

    &s[..]
} 


fn second_word(s: &str) -> &str {
    let bytes = s.as_bytes();
    let len = bytes.len();

    for (i, &item) in bytes.iter().enumerate() {
        if item == b' ' {
            return &s[i..len].trim()
        }
    }
    &s[..]
}


type Document = Vec<String>;

fn new_document(words: Vec<String>) -> Document {
    words
}

fn add_word(this: &mut Document, word: String) {
    this.push(word);
}

fn get_words(this: &Document) -> &[String] {
    this.as_slice()
}

fn create_document() {
    let words = vec!["hello".to_string()];
    let d = new_document(words);

    let words_copy = get_words(&d).to_vec();
    let mut d2 = new_document(words_copy);
    add_word(&mut d2, "world".to_string());

    assert!(!get_words(&d).contains(&"world".into()));
}

fn inner(x: &mut i32) {
    let another_num = 1;
    let _a_stack_ref = &another_num;

    let _a_box = Box::new(2);
    let _a_box_stack_ref = &_a_box;
    let _a_box_heap_ref = &*_a_box;

    *x += 5
}

fn round_all(list: &mut Vec<f32>) -> Vec<f32> {
    let mut c = list.clone();
    for (i, &item) in list.iter().enumerate() {
        c[i] = item.round();       
    }
    c
}

fn main() {
    moved_heap();
    clone_heap();
    hello_world();
    referances();
    abs_referance();
    
    let b = String::from("Hello, World!");

    println!("{}", first_word(&b));
    println!("{}", second_word(&b));

    create_document();

    let mut a_num = 0;
    inner(&mut a_num);

    println!("{:?}", round_all(&mut vec![3.12, 5.12, 7.99]));
}