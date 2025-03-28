<?php
function CheckUser($school_number) {
    try {
        // secrets.php dosyasında tanımladığımız gizli değişkenleri dahil ediyoruz
        require_once 'secrets.php';
        
        // PDO ile bağlantı
        $conn = new PDO("mysql:host=".DB_SERVER.";dbname=".DB_NAME, DB_USERNAME, DB_PASSWORD);
        
        // Hata modunu ayarla
        $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        
        // Sorgu - sadece kontrol için COUNT kullanıyoruz
        $stmt = $conn->prepare("SELECT COUNT(*) AS count FROM Student WHERE school_number = :school_number");
        $stmt->bindParam(':school_number', $school_number);
        $stmt->execute();
        
        // Sonucu al
        $result = $stmt->fetch(PDO::FETCH_ASSOC);
        
        // Bağlantıyı kapat
        $conn = null;
        
        // Kullanıcı var mı yok mu kontrol et (0 = yok, 1 = var)
        return ($result['count'] > 0);
        
    } catch(PDOException $e) {
        // Hata durumunda false döndür
        return false;
    }
}

// register.php sayfasının geri kalanı

// POST isteği geldiğinde
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Form verilerini al
    $name = $_POST['name'] ?? '';
    $school_number = $_POST['username'] ?? '';
    $password = $_POST['passwords'] ?? '';
    
    // Boş alan kontrolü
    if (empty($name) || empty($school_number) || empty($password)) {
        echo "Lütfen tüm alanları doldurun!";
    } else {
        // Kullanıcı var mı kontrol et
        if (CheckUser($school_number)) {
            echo "Bu okul numarası zaten kayıtlı!";
        } else {
            // Kullanıcıyı kaydet
            try {
                require_once 'secrets.php';
                $conn = new PDO("mysql:host=".DB_SERVER.";dbname=".DB_NAME, DB_USERNAME, DB_PASSWORD);
                $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
                
                // Şifreyi güvenli şekilde hashle
                $hashed_password = password_hash($password, PASSWORD_DEFAULT);
                
                // Yeni kullanıcı ekle
                $stmt = $conn->prepare("INSERT INTO Student (name, school_number, password) VALUES (:name, :school_number, :password)");
                $stmt->bindParam(':name', $name);
                $stmt->bindParam(':school_number', $school_number);
                $stmt->bindParam(':password', $hashed_password);
                $stmt->execute();
                
                echo "Kayıt başarılı! Giriş yapabilirsiniz.";
                
            } catch(PDOException $e) {
                echo "Kayıt hatası: " . $e->getMessage();
            }
            
            $conn = null;
        }
    }
}
?>