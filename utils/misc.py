#! /usr/bin/env python3

import socket

'''
Fonctions diverses de vérification
'''

'''
is_valid_ipv4_address: vérifie qu'une adresse IPv4 passée en paramètres est valide
entrée: adresse IPv4
sortie: retourne True si l'IP est valide, False sinon
'''
def is_valid_ipv4_address(address):
    try:
        socket.inet_pton(socket.AF_INET, address)
    except AttributeError:  # no inet_pton here, sorry
        try:
            socket.inet_aton(address)
        except socket.error:
            return False
        return address.count('.') == 3
    except socket.error:  # not a valid address
        return False

    return True


'''
is_valid_ipv6_address: vérifie qu'une adresse IPv6 passée en paramètres est valide
entrée: adresse IPv6
sortie: retourne True si l'IP est valide, False sinon
'''
def is_valid_ipv6_address(address):
    try:
        socket.inet_pton(socket.AF_INET6, address)
    except socket.error:  # not a valid address
        return False
    return True
