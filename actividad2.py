#!/usr/bin/env python3
from scapy.all import IP, ICMP, send
import time
import random

# Lista de caracteres especiales para el padding
PADDING_CHARS = list("+.!.-,0,3,2,&%$#@*?;:<>[]{}~")

def generate_padding(length):
    """Genera un padding de longitud `length` con caracteres aleatorios."""
    return ''.join(random.choice(PADDING_CHARS) for _ in range(length)).encode('utf-8')

def send_text_via_ping(text, target="8.8.8.8", payload_size=40, delay=0.2):
    """
    Envía cada caracter de `text` en un paquete ICMP Echo Request.
    
    :param text: Texto a enviar
    :param target: IP destino
    :param payload_size: Tamaño del payload ICMP en bytes (40 recomendado)
    :param delay: Tiempo entre pings (segundos)
    """
    # Identificador inicial aleatorio
    icmp_id = random.randint(0, 0xFFFF)
    seq_num = 0  # Número de secuencia inicial

    for char in text:
        # Convertir carácter a byte
        char_byte = char.encode('utf-8')

        if len(char_byte) > payload_size:
            raise ValueError("El payload_size es menor que 1 byte del caracter")

        padding = generate_padding(payload_size - len(char_byte))
        payload = char_byte + padding

        # Crear paquete ICMP
        pkt = IP(dst=target)/ICMP(id=icmp_id, seq=seq_num)/payload

        # Enviar paquete
        send(pkt, verbose=False)

        print(f"Enviado: '{char}' -> ID={icmp_id}, Seq={seq_num}, Payload={payload}")

        # Incrementar número de secuencia
        seq_num += 1

        # Espera para mantener un patrón coherente
        time.sleep(delay)

if __name__ == "__main__":
    texto = input("Ingrese el texto a enviar por ICMP: ")
    
    # Tamaño del payload
    payload_bytes = 40  # simula un ping real
    
    # Retraso entre pings
    delay_sec = 0.2

    send_text_via_ping(texto, payload_size=payload_bytes, delay=delay_sec)
