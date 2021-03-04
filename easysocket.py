#!/usr/bin/python3

import socket
def recv_exactly (s, taille_exacte):
    res = b''
    while len(res) < taille_exacte:
        morceau = s.recv (taille_exacte -len(res))
        res = res + morceau
    return res
nbr_octet_entete = 10
def make_client_socket(server_host, server_port):
    s = socket.socket()
    s.connect((server_host, server_port))
    return s
def make_server_socket(server_port):
    s = socket.socket()
    s.bind(('', server_port))
    s.listen()
    return s
def int_to_bytes(i):
    res = str (i).encode()
    while len(res) < nbr_octet_entete:
        res = b'0' + res
    return res
def bytes_to_int(bb):
    return int(bb)
def send_header (s, nbr_octet_contenu):
    header = int_to_bytes(nbr_octet_contenu)
    s.sendall(header)
def receive_header(s):
    header = recv_exactly (s, nbr_octet_entete)
    return bytes_to_int (header)
def send(s, contenu):
    nbr_octet_contenu = len(contenu)
    send_header (s, nbr_octet_contenu)
    s.sendall(contenu)
def receive (s):
    nbr_octet_contenu = receive_header(s) 
    return recv_exactly (s, nbr_octet_contenu)