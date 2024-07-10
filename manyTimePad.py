import binascii

def hex_xor(hex_str1, hex_str2): #ascii string
    l = min(len(hex_str1), len(hex_str2))
    a = int(hex_str1[:l], 16)
    b = int(hex_str2[:l], 16)
    c = hex(a ^ b)[2:]
    return ''.join(['0' for i in range(len(c), l)]) + c

def ascii_to_hex(s):
    return str(binascii.hexlify(s.encode()), 'ascii')

def hex_to_ascii(hex_string):
    unhex_string = binascii.unhexlify(hex_string.encode())
    return str(unhex_string, 'ascii')

def fix_view(s):
    l = []
    i = 0
    while i <= len(s)-2:
        l.append(s[i:i+2])
        i += 2
    return l

def over_views(ciphertexts_file):
    with open(ciphertexts_file, 'r') as f:
        ciphertexts = f.read().split('\n')
    l = min([len(i) for i in ciphertexts])
    views = []
    for ciphertext in ciphertexts:
        list_xored = [fix_view(hex_xor(cipher[:l], ciphertext[:l])) for cipher in ciphertexts]
        view = []
        for i in range(l//2):
            b = 0
            for xored in list_xored:
                c = int(xored[i], 16)
                if c >= 127 or c in range(32, 64):
                    b = 1000
                    break
                if c >= 1 and c <= 31:
                    b += 1
            view.append('\s' if b < 2 else '__')
        views.append((fix_view(ciphertext[:l]), view))
    with open('over_view.txt', 'w') as f:
        for v in views:
            print('{}\n{}\n'.format('.'.join(v[0]), '.'.join(v[1])), file= f)
    return views

def encrypt_view(ciphertexts_file, decrypt_text):
    with open(ciphertexts_file, 'r') as f:
        ciphertexts = f.read().split('\n')
    l = min([len(i) for i in ciphertexts])
    list_xored = [fix_view(hex_xor(cipher[:l], decrypt_text[:l])) for cipher in ciphertexts]
    with open('result.txt', 'w') as f:
        for xored in list_xored:
            print('.'.join(xored), file= f)
        print('.'.join(fix_view(decrypt_text)), file= f)
        view = []
        for i in range(l//2):
            b = 0
            for xored in list_xored:
                c = int(xored[i], 16)
                if c >= 127 or c in range(32, 64):
                    b = 1000
                    break
                if c >= 1 and c <= 31:
                    b += 1
            view.append('\s' if b < 2 else '__')
        print('.'.join(view), file= f)
        
def decrypt(decrypt_text):
    ov = over_views('ciphertexts.txt')
    encrypt_view('ciphertexts.txt', decrypt_text)
    strong_view = ''
    l = len(ov[0][0])
    decrypt_text = fix_view(decrypt_text)[:l]
    for t in ov:
        if t[0] == decrypt_text:
            decrypt_text = t
            break
    for i in range(len(decrypt_text[1])):
        if decrypt_text[1][i] == '\s':
            strong_view += ' '
            continue
        b = True
        strong_view += '('

        for cipher in ov:
            if cipher[1][i] == '\s':
                b = False
                h = hex_xor(hex_xor(cipher[0][i], decrypt_text[0][i]), ascii_to_hex(' '))
                if int(h, 16) in range(33, 128):
                    strong_view += hex_to_ascii(h)
                if int(h, 16) == 32:
                    b = True
        strong_view += '_' if b else ''
        strong_view += ')'
    with open('result.txt', 'a') as f:
        print(strong_view, file= f)

def main():
    with open('decrypt.txt', 'r') as f:
        decrypt_text = f.read()
    decrypt(decrypt_text)



if __name__ == '__main__':
    main()

