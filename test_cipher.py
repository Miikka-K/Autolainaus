# CIPHER.PY -MODUULIN YKSIKKÖTESTIT
# =================================

import pytest # Järjestelmätason virheiden testaus
import cipher # Testattavan moduulin lataus

plainText = b'Selkokieliteksti'
key = cipher.newKey()
cipherEngine = cipher.createChipher(key)
cryptoText = cipher.encrypt(cipherEngine, plainText)


def test_decrypt():
    assert cipher.decrypt(cipherEngine, cryptoText, True) == plainText
     
def test_decryptString():
    cryptoText = cipher.encryptString('kahvi on hyvää')
    assert cipher.decryptString(cryptoText) == 'kahvi on hyvää'

