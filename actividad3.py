#!/usr/bin/env python3
from scapy.all import rdpcap, ICMP, IP

def extract_message_from_pcap(pcap_file, src_ip="192.168.0.16", dst_ip="8.8.8.8"):
    """
    Extrae el primer caracter de cada payload ICMP desde src_ip hacia dst_ip
    """
    packets = rdpcap(pcap_file)
    message = ""

    for pkt in packets:
        if IP in pkt and ICMP in pkt:
            if pkt[IP].src == src_ip and pkt[IP].dst == dst_ip:
                data = bytes(pkt[ICMP].payload)
                if len(data) > 0:
                    message += chr(data[0])  # primer caracter del payload

    return message

def caesar_decrypt(ciphertext, shift):
    """
    Descifra un texto usando el cifrado César con shift dado
    """
    decrypted = ""
    for c in ciphertext:
        if c.isupper():
            decrypted += chr((ord(c) - 65 - shift) % 26 + 65)
        elif c.islower():
            decrypted += chr((ord(c) - 97 - shift) % 26 + 97)
        else:
            decrypted += c
    return decrypted

if __name__ == "__main__":
    archivo = "cesar.pcapng"

    mensaje_cifrado = extract_message_from_pcap(archivo)
    print(f"Mensaje cifrado extraído: {mensaje_cifrado}\n")

    print("Intentando fuerza bruta del cifrado César (clave 0-25):\n")
    for clave in range(26):
        descifrado = caesar_decrypt(mensaje_cifrado, clave)
        print(f"Clave {clave}: {descifrado}")
