"""
cryptography library using pycryptodome
"""
import hashlib
from base64 import b64decode, b64encode, urlsafe_b64decode, urlsafe_b64encode
from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
from Crypto.Cipher import PKCS1_OAEP

BS = 16
# pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
pad = lambda s: (s + ((BS - len(s) % BS) * chr(BS - len(s) % BS))).encode(encoding="utf-8")

unpad = lambda s: s[:-ord(s[len(s)-1:])]


def gen_rsa_pem():
    """
    generate rsa key in .PEM format
    """
    random_generator = Random.new().read
    key = RSA.generate(1024, random_generator)
    s_k = key.exportKey('PEM').decode('utf-8')
    p_k = key.publickey().exportKey('PEM').decode('utf-8')
    return s_k, p_k


def gen_rsa_key():
    """
    generate rsa key in binary format
    """
    random_generator = Random.new().read
    key = RSA.generate(1024, random_generator)
    print(key.exportKey('PEM').decode('utf-8'))
    print(key.publickey().exportKey('PEM').decode('utf-8'))
    bin_priv_key = key.exportKey('DER')
    bin_pub_key = key.publickey().exportKey('DER')
    return b64encode(bin_priv_key), b64encode(bin_pub_key)


def enc_aes(key, msg):
    """
    encrypt message using AES key
    """
    key = hashlib.sha256(key.encode('utf-8')).hexdigest()[:BS]
    raw = pad(bytes(msg))
    # raw = pad(bytes(msg, encoding='utf8'))
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return b64encode(iv + cipher.encrypt(raw))


def dec_aes(key, hdn_msg):
    """
    decrypt chipper message using AES key
    """
    key = hashlib.sha256(key.encode('utf-8')).hexdigest()[:BS]
    enc = b64decode(hdn_msg.encode('utf-8'))
    iv = enc[:BS]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(enc[BS:]))


def enc_rsa(pubkey, msg):
    """
    encrypt message using RSA key
    """
    pub_key_obj = RSA.importKey(b64decode(pubkey))
    hdn_msg = pub_key_obj.encrypt(msg, 'x')[0]
    return b64encode(hdn_msg)


def dec_rsa(privkey, hdn_msg):
    """
    decrypt message using RSA key
    """
    priv_key_obj = RSA.importKey(b64decode(privkey))
    msg = priv_key_obj.decrypt(b64decode(hdn_msg))
    return msg


def gen_rsa_1():
    """
    generate RSA key in .PEM format
    """
    key = RSA.generate(1024)
    private_key = key.export_key('PEM')
    public_key = key.publickey().exportKey('PEM')
    # print(private_key, public_key)
    return private_key.decode("ascii"), public_key.decode("ascii")


def gen_rsa():
    """
    generate RSA key in binary format
    """
    key = RSA.generate(1024)
    private_key = key.export_key('PEM')
    public_key = key.publickey().exportKey('PEM')
    # print(private_key, public_key)
    return private_key.hex(), public_key.hex()


def encrypt_rsa_1(pk, message):
    """
    encrypt message using RSA key with .PEM key format
    """
    message = str.encode(message)
    rsa_public_key = RSA.importKey(pk.encode('ascii'))
    rsa_public_key = PKCS1_OAEP.new(rsa_public_key)
    encrypted_text = rsa_public_key.encrypt(message)
    return urlsafe_b64encode(encrypted_text).decode('ascii')


def encrypt_rsa(pk, message):
    """
    encrypt message using RSA key with binary key format
    """
    message = str.encode(message)
    rsa_public_key = RSA.importKey(bytearray.fromhex(pk))
    rsa_public_key = PKCS1_OAEP.new(rsa_public_key)
    encrypted_text = rsa_public_key.encrypt(message)
    return urlsafe_b64encode(encrypted_text).decode('ascii')


def decrypt_rsa(pv, encdata):
    """
    decrypt message using RSA key with binary key format
    """
    encrypted_text = urlsafe_b64decode(encdata.encode('ascii'))
    rsa_private_key = RSA.importKey(bytearray.fromhex(pv))
    rsa_private_key = PKCS1_OAEP.new(rsa_private_key)
    decrypted_text = rsa_private_key.decrypt(encrypted_text)
    return decrypted_text.decode('ascii')


class AESCipher():
    """
    AES chiper class for simple setup
    """
    def __init__(self, key, is_debug=False):
        """
        constructor class with secret key input
        """
        self.bs = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()
        if is_debug:
            print(hashlib.sha256(key.encode()).hexdigest())

    def encrypt(self, raw):
        """
        encrypt raw message using AES secret key
        """
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return urlsafe_b64encode(iv + cipher.encrypt(raw.encode())).decode('ascii')

    def decrypt(self, enc):
        """
        decrypt chipper message using AES secret key
        """
        enc = urlsafe_b64decode(enc.encode('ascii'))
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

    def _pad(self, s):
        """
        padding method
        """
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        """
        unpadding method
        """
        return s[:-ord(s[len(s)-1:])]


def test_polygon():
    """
    testing function using polygon network
    """
    pku = """"2d2d2d2d2d424547494e205055424c4943204b45592d2d2d2d2d0a4d4947664d413047435371475349623344514542415155414134474e4144434269514b426751444430356f6253465470496b3546385a2f6a43636959455078750a334d6268537865757442794b55396b487a49646964756268626c36316d744a5033566259367139584844626554566b2b54394b3361434e5671796b73426533750a317a4651706b726e78666f6b616a572b534535363270527877336e6e4d656e2f376b4d6f5471475a5546512f7a5164436a70303475386370446639386c6a55300a55514c713962616b3634544e43796f3556774944415141420a2d2d2d2d2d454e44205055424c4943204b45592d2d2d2d2d"""
    pvu = """2d2d2d2d2d424547494e205253412050524956415445204b45592d2d2d2d2d0a4d4949435841494241414b426751444430356f6253465470496b3546385a2f6a4363695945507875334d6268537865757442794b55396b487a496469647562680a626c36316d744a5033566259367139584844626554566b2b54394b3361434e5671796b7342653375317a4651706b726e78666f6b616a572b53453536327052780a77336e6e4d656e2f376b4d6f5471475a5546512f7a5164436a70303475386370446639386c6a553055514c713962616b3634544e43796f3556774944415141420a416f4741454442734b786b3975394255504541506763754c513963547032366c476e63457a444b6a735750684b31336a533261644338482b486e46674e61344d0a77663455354e5332544961456644784a4a56523870315a784873643871744d7356774b4831575769643879376f4f716653435a4845675246326f3943505a444d0a664847524a4b5332497a4e383143354c585735716372584a4a77304f68734158584376326943445648354e4f2f774543515144526b664d755077547a476142580a6b39677666557a4c68506867764c64324d45683453436c4d5a6a4945505964676672336b5978445a6537686146566967794d43756767793234387a3469336b580a5a42516a70707042416b4541377a5972477a78344b784b714854734c4b43474c4c666346715a6f5a6c7268566e38764234304571374b716d782b734f75792b410a71415251597457546a73534a353641544b54426c373237554b61392b417250396c774a42414b75473059736765575366724f55425651684a66666c31732f55350a674d397a5a56314e63722f6452554c444f584a3553654d4d556c59764e5178475047776334396678435963486e4651786b384c5a58734a764d6745435146794e0a75393338356f3362326541586354696b7965494e2b71336c68744d5048576f486630773763613143566564794a692f387343335342587849494b43546f4c76790a377062344e2b694e48422f49323975563470384351434e434352654a6f79442b42492f492b366d41306753594c4a462f2b6f612b614e4453674c2f6e674c50360a78714d466b2b45444e67376d6e64463350656e4152507344356e693063733056524a58686a6377717565343d0a2d2d2d2d2d454e44205253412050524956415445204b45592d2d2d2d2d"""
    # enc_data = encrypt_rsa(pku,"1234567890")
    enc_data = encrypt_rsa(pku, "10.0.0.2:8000,abcdefghij")
    dec_data = decrypt_rsa(pvu, enc_data)
    print(dec_data)


# keystr = "abcdefghijklmnopabcdefghijklmnop"
# hello = "12345678901234567890123456789012345678901234567890"
# print "Plain:",hello
# enc1 = enc_aes(keystr,hello)
# print enc1
# dec1 = dec_aes(keystr,enc1)
# print "Decrypted:",dec1


if __name__ == "__main__":
    # gen_rsa_key()
    # sys.exit()
    # test_polygon()

    # sys.exit()
    MODE = 1
    if MODE == 0:
        aes = AESCipher("hello123")
        chiper = aes.encrypt("It is a hidden message")
        print(chiper)

        # print(chiper.decode('ascii'))
        # ascstr = chiper.decode('ascii')
        # byteval = ascstr.encode('ascii')
        aes2 = AESCipher("hello123")
        # plain = aes2.decrypt(byteval)
        plain = aes2.decrypt(chiper)
        print(plain)
    else:
        pv, pk = gen_rsa()
        print(pv, pk)
        MESSAGE = "hello there!"
        print(MESSAGE)
        chiper = encrypt_rsa(pk, MESSAGE)
        plain = decrypt_rsa(pv, chiper)
        print(chiper)
        print(plain)
