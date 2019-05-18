import sys
import chilkat

crypt = chilkat.CkCrypt2()
success = crypt.UnlockComponent("1")
crypt.put_CryptAlgorithm("aes")
crypt.put_CipherMode("gcm")
crypt.put_KeyLength(128)
key = "7bde18701ac252b9a9b68a088c9a8f82"
iv = "65185e96595a97b07ef1b9f9"
src = "03"
crypt.put_EncodingMode("hex")
crypt.SetEncodedIV(iv,"hex")
crypt.SetEncodedKey(key,"hex")
ctResult = crypt.encryptEncoded(src)
print("computed result: " + ctResult)
tResult = crypt.getEncodedAuthTag("hex")
print("computed authTag: " + tResult)