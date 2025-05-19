"""
Paroles Ģenerators
------------------

Šī Python lietotne ģenerē drošas paroles, ņemot vērā lietotāja norādītās prasības:
- Paroles garums
- Vai iekļaut lielos burtus
- Vai iekļaut ciparus
- Vai iekļaut speciālās rakstzīmes

Autors: [Tavs vārds]
Licence: MIT
"""

import random
import string


def generate_password(length=12, use_uppercase=True, use_digits=True, use_specials=True):
    """
    Ģenerē paroli ar norādītajām īpašībām.

    :param length: Paroles garums (noklusējums: 12)
    :param use_uppercase: Vai iekļaut lielos burtus (noklusējums: True)
    :param use_digits: Vai iekļaut ciparus (noklusējums: True)
    :param use_specials: Vai iekļaut speciālās rakstzīmes (noklusējums: True)
    :return: Ģenerēta parole kā virkne
    """
    if length < 4:
        raise ValueError("Paroles garumam jābūt vismaz 4 rakstzīmēm.")

    characters = list(string.ascii_lowercase)

    if use_uppercase:
        characters += list(string.ascii_uppercase)
    if use_digits:
        characters += list(string.digits)
    if use_specials:
        characters += list("!@#$%^&*()-_=+[]{}|;:,.<>?/")

    if not characters:
        raise ValueError("Jāizvēlas vismaz viens rakstzīmju tips.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


# Lietošanas piemērs
if __name__ == "__main__":
    print("Ģenerēta parole:")
    parole = generate_password(length=16, use_uppercase=True, use_digits=True, use_specials=True)
    print(parole)
