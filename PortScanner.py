
import socket

def port_scan(target_ip, start_port, end_port):
    print(f"Port taraması başlatıldı: {target_ip}")

    for port in range(start_port, end_port + 1):
        try:
            # Yeni bir soket oluştur
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)  # Bağlantı zaman aşımını 1 saniye olarak ayarla

            # Hedef IP adresi ve port numarasıyla bağlantı kurmaya çalış
            result = s.connect_ex((target_ip, port))

            # Bağlantı başarılı ise port açık demektir
            if result == 0:
                print(f"Port {port} açık")
            
            # Soketi kapat
            s.close()

        except socket.error:
            print("Bağlantı hatası. Port taraması tamamlanamadı.")

    print("Port taraması tamamlandı.")

# Kullanım örneği
target_ip = input(“Hedef siteyi girin”);  # Taranacak IP adresi
start_port = 1  # Taramanın başlayacağı port numarası
end_port = 100  # Taramanın biteceği port numarası

port_scan(target_ip, start_port, end_port)

