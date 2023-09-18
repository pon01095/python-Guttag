# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 20:49:21 2021

@author: pon01
"""

# capitals = {'France': 'Paris', 'Italy': 'Rome', 'Japan':'Kyoto'}

# x = input('The capital of ' )

# if x in capitals.keys(): #x가 capitals의 key값중 하나라면
#     print('is ', capitals[x]) #capitals의 key x에 해당하는 value를 출력
# else:
#     print("")    
    
# number_to_word = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 10: 'ten'}
# word_to_number = {w: d for d, w in number_to_word.items()}
# word_to_number = {w: d for d, w in number_to_word.items() if d < 10}


gen_code_keys = (lambda book, plain_text:({c: str(book.find(c)) for c in plain_text}))
encoder = (lambda code_keys, plain_text: ''.join(['*' + code_keys[c] for c in plain_text])[1:])
encrypt = (lambda book, plain_text:encoder(gen_code_keys(book, plain_text), plain_text))


decoder = (lambda decode_keys, cipher_text: ''.join([decode_keys[i] for i in cipher_text.split('*')]))
gen_decode_keys = (lambda book, cipher_text: {s: book[int(s)] for s in cipher_text.split('*')})


book = 'In a village of La Mancha, the name of which I have no desire to call to mind, there lived not long since one of those gentlemen that keep a lance in the lance-rack, an old buckler, a lean hack, and a greyhound for coursing.jqxz'

plain_text = 'no is no'
code_keys = gen_code_keys(book, plain_text)
encoding = encoder(code_keys, plain_text)
encoding2 = encrypt(book, plain_text)
cipher_text = '22*13*33*137*59*11*23*11*1*57*6*13*1*2*6*57*2*6*1*22*13*33*137*59*11*23*11*1*57*6*173*7*11'
decode_keys = gen_decode_keys(book, cipher_text)
decoding = decoder(decode_keys, cipher_text)

x = []
for i in cipher_text.split('*'):
    x.append(decode_keys[i])    
x="".join(x)
                