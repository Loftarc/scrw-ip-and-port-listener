import socket
import subprocess

def main():
    host = '127.0.0.1'  # dinlenicek ip ve port
    port = 8080

    # Soket oluştur
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"Dinleniyor: {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Bağlantı alındı: {client_address[0]}:{client_address[1]}")

        try:
            data = client_socket.recv(1024).decode('utf-8')
            print(f"Gelen veri: {data}")

            # Olası saldırıyı tespit etmek için burada gereken kontrolleri yapabilirsiniz.

            
            if "saldırı" in data.lower():
                subprocess.run(["cmd.exe", "/c", "echo UYARI: Olası  dos saldırısı algılandı!"], shell=True)

        except Exception as e:
            print(f"Hata: {e}")
        finally:
            client_socket.close()

if __name__ == "__main__":
    main()