def dekripsi_chat(chat_terenkripsi):
    alfabet = 'abcdefghijklmnopqrstuvwxyz'
    chat_didekripsi = ''

    for huruf in chat_terenkripsi:
        if huruf in alfabet:
            posisi_lama = alfabet.find(huruf)
            posisi_baru = (posisi_lama - 5) % len(alfabet)
            chat_didekripsi += alfabet[posisi_baru]
        else:
            chat_didekripsi += huruf

    return chat_didekripsi

chat_terenkripsi = """
xfqfr bfmdz
gjxtp lzj rfz ifkyfw jxi snm
gwt, gjxtp qz rfz rfpfs in bfwlty lfp?
fpz xfdfsl pfrz, rfz lfp ofin ufhfwpz
dfsl pnwnr xynhpjw otrtp pz pnhp ifwn lwzu
"""

chat_didekripsi = dekripsi_chat(chat_terenkripsi)
print(chat_didekripsi)