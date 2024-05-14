import requests
from colorama import Fore, Style, init
import socket
import sys

# Inisialisasi Colorama dengan autoreset
init(autoreset=True)

def cetak_teks_berwarna(teks):
    teks_berwarna = Fore.RED + teks + Style.RESET_ALL
    print(teks_berwarna)

def print_info_geo(ip):
    url = f"https://ipinfo.io/{ip}/json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print("\nInformasi Geografis untuk IP {}:".format(ip))
        print("IP Address     : {}".format(data.get('ip', 'N/A')))
        print("Hostname       : {}".format(data.get('hostname', 'N/A')))
        print("Lokasi         : {}, {}, {}, {}".format(data.get('city', 'N/A'), data.get('region', 'N/A'), data.get('country', 'N/A'), data.get('postal', 'N/A')))
        print("Koordinat      : {}".format(data.get('loc', 'N/A')))
        print("Penyedia Layanan Internet : {}".format(data.get('org', 'N/A')))
    else:
        print("Gagal mendapatkan informasi geografis.")

def scan_port(target_host, target_ports):
    hasil_pemindaian = []
    for port, service in target_ports.items():
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target_host, port))
            if result == 0:
                hasil_pemindaian.append(f"Port {port} ({service}): Open")
            else:
                hasil_pemindaian.append(f"Port {port} ({service}): Closed")
            sock.close()
        except KeyboardInterrupt:
            print("KeyboardInterrupt")
            sys.exit()
        except socket.error:
            print("Tidak bisa terhubung ke server")
            sys.exit()
    return hasil_pemindaian

def print_selamat():
    target_host = input("\nEnter hostname/domain/sub-domain: ")

    try:
        ip = socket.gethostbyname(target_host)
        print_info_geo(ip)
    except socket.gaierror:
        print("Maaf, IP tidak ditemukan. Mohon periksa kembali domain atau koneksi internet Anda.")

    pilihan_lanjut = input("Apakah Anda ingin melanjutkan? (y/n): ")
    if pilihan_lanjut.lower() != 'y':
        print("Perintah selesai.")
        sys.exit()

# Teks yang ingin diberi warna
teks = """
         ..................
                           ...$$$..
                             ....
                        .....    ..1x$.
                  ......         ...1$.
         .........    ...............$.
                          ........
                        ..  .........x.
                      ...             0Xx0c:..  ...
                    ..   .          .0n%,:&0Xx0c:..,,
                 ....             .0n%             :00;
                .               .0n%                 :00;
                                .0n%                  ':00;.
                                 .0n%                    .0;.
                                   .0n
                                    .0n;
                                      oodl0n;...   ...
                                         ..'.;;oodl0n;...
                                                   ..'.;;...
                                                        ..'...
                                                         .d   .;.
                                                          .d   ;: .
                                                           .l
                                                            .l
                                                            .o ngintip V1.0
        Information Gathering\n1. Informasi Geografis IP Address\n2. Scan Port\n3. Exit
"""

while True:
    # Memanggil fungsi dengan teks yang diinginkan
    cetak_teks_berwarna(teks)

    # Menanyakan pengguna apakah ingin menjalankan fungsi lain
    jawaban = input("(1/2/3): ")

    if jawaban == '1':
        print_selamat()
    elif jawaban == '2':
        target_host = input("\nEnter hostname/domain/sub-domain: ")
        target_ports = {
            21: "FTP (File Transfer Protocol)",
            22: "SSH (Secure Shell)",
            23: "Telnet",
            25: "SMTP (Simple Mail Transfer Protocol)",
            80: "HTTP (Hypertext Transfer Protocol)",
            110: "POP3 (Post Office Protocol version 3)",
            143: "IMAP (Internet Message Access Protocol)",
            443: "HTTPS (Hypertext Transfer Protocol Secure)",
            3306: "MySQL Database",
            3389: "Remote Desktop Protocol (RDP)"
        }
        hasil_pemindaian = scan_port(target_host, target_ports)
        for hasil in hasil_pemindaian:
            print(hasil)

        pilihan_lanjut = input("Apakah Anda ingin melanjutkan? (y/n): ")
        if pilihan_lanjut.lower() != 'y':
            print("Perintah selesai.")
            sys.exit()
    elif jawaban == '3':
        print("Perintah selesai.")
        break
    else:
        print("Opsi tidak dikenali. Silakan coba lagi.")
