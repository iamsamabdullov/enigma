#This program is a fairly simple enigma with 3 rotors and one reflector.
def enigma(text, ref, rot1, rot2, rot3):

    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    rot1 =     'EKMFLGDQVZNTOWYHXUSPAIBRCJ'
    if rot2 == 2:
        rot2 = 'AJDKSIRUXBLHWTMCQGZNPYFVOE'
    else:
        rot2 = alphabet
    if rot3 == 3:
        rot3 = 'BDFHJLCPRTXVZNYEIWGAKMUSQO'
    else:
        rot3 = alphabet
    ref = 'YRUHQSLDPXNGOKMIEBFZCWVJAT'

    txt = ''.join([t for t in text.upper() if t in alphabet])
    trantab = txt.maketrans(alphabet, rot3)
    x = str(txt.translate(trantab))
    trantab1 = x.maketrans(alphabet, rot2)
    x1 = x.translate(trantab1)
    trantab2 = x1.maketrans(alphabet,rot1)
    x2 = x1.translate(trantab2)
    trantab3 = x2.maketrans(alphabet,ref)
    x3 = x2.translate(trantab3)
    trantab4 = x3.maketrans(rot1, alphabet)
    x4 = x3.translate(trantab4)
    trantab5 = x4.maketrans(rot2, alphabet)
    x5 = x4.translate(trantab5)
    trantab6 = x5.maketrans(rot3, alphabet)
    x6 = x5.translate(trantab6)

    return x6
