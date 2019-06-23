def huffman_decode():
    k, l = (int(x) for x in input().split())
    code = {}
    for el in range(0, k):
        letter, value = input().split(': ')
        code[letter] = value
    encoded = input()
    decoded = ""
    k = 1
    while encoded:
        for k in code:
            posl = code[k]
            if encoded.startswith(posl):
                decoded += k
                encoded = encoded[len(posl):]
    print(decoded)

huffman_decode()
