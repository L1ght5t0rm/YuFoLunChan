#!/usr/bin/env python3
#https://github.com/L1ght5t0rm/YuFoLunChan
#Credit:
#    https://github.com/lersh/TudouCode/
#    https://gist.github.com/qinmenghua/7538e1888764587c914f2413ec299935
#        nianfo.py - TudouCode Demo in Python 3
#        Note:
#            This is the first version('佛曰') of TudouCode('与佛论禅').
#            The second version('如是我闻') needs compression and I can't debug.
#            Dependency: pycrypto

from Crypto.Cipher import AES
from random import choice
import argparse
KEY = b'XDXDtudou@KeyFansClub^_^Encode!!'
IV = b'Potato@Key@_@=_='
TUDOU = [
    '滅', '苦', '婆', '娑', '耶', '陀', '跋', '多', '漫', '都', '殿', '悉', '夜', '爍', '帝', '吉',
    '利', '阿', '無', '南', '那', '怛', '喝', '羯', '勝', '摩', '伽', '謹', '波', '者', '穆', '僧',
    '室', '藝', '尼', '瑟', '地', '彌', '菩', '提', '蘇', '醯', '盧', '呼', '舍', '佛', '參', '沙',
    '伊', '隸', '麼', '遮', '闍', '度', '蒙', '孕', '薩', '夷', '迦', '他', '姪', '豆', '特', '逝',
    '朋', '輸', '楞', '栗', '寫', '數', '曳', '諦', '羅', '曰', '咒', '即', '密', '若', '般', '故',
    '不', '實', '真', '訶', '切', '一', '除', '能', '等', '是', '上', '明', '大', '神', '知', '三',
    '藐', '耨', '得', '依', '諸', '世', '槃', '涅', '竟', '究', '想', '夢', '倒', '顛', '離', '遠',
    '怖', '恐', '有', '礙', '心', '所', '以', '亦', '智', '道', '。', '集', '盡', '死', '老', '至']
BYTEMARK = ['冥', '奢', '梵', '呐', '俱', '哆', '怯', '諳', '罰', '侄', '缽', '皤']

def Encrypt(plaintext):
    data = plaintext.encode('utf-16le')
    pads = (- len(data)) % 16
    data += bytes(pads * [pads])
    cryptor = AES.new(KEY, AES.MODE_CBC, IV)
    result = cryptor.encrypt(data)
    return '佛曰：' + ''.join([TUDOU[i] if i < 128 else choice(BYTEMARK) + TUDOU[i-128] for i in result])

def Decrypt(ciphertext):
    if ciphertext.startswith('佛曰：'):
        ciphertext = ciphertext[3:]
    data = bytearray()
    i = 0
    while i < len(ciphertext):
        if ciphertext[i] in BYTEMARK:
            i += 1
            data = data + bytes([TUDOU.index(ciphertext[i]) + 128])
        else:
            data = data + bytes([TUDOU.index(ciphertext[i])])
        i += 1
    cryptor = AES.new(KEY, AES.MODE_CBC, IV)
    result = cryptor.decrypt(data)
    flag = result[-1]
    if flag < 16 and result[-flag] == flag:
        result = result[:-flag]
    return result.decode('utf-16le')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-e', type=str, metavar='String', help='Plaintext encryption')
    group.add_argument('-d', type=str, metavar='String', help='Decryption of ciphertext')
    args = parser.parse_args()

    if args.e:
        print(Encrypt(args.e))
    elif args.d:
        print(Decrypt(args.d))







