def gcd(a, b):
    """
    Calculates the greatest common divisor of two numbers a and b.
    Uses the Euclidean algorithm to compute this.
    """
    while b != 0:
        a, b = b, a % b
    return a

def multiplicative_inverse(e, phi):
    """
    Finds the multiplicative inverse of e modulo phi.
    This function uses the extended Euclidean algorithm to find the inverse.
    """
    d = 0
    x1, x2, y1 = 0, 1, 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi // e
        temp2 = temp_phi - temp1 * e
        temp_phi, e = e, temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2, x1 = x1, x
        d, y1 = y1, y

    if temp_phi == 1:
        return d + phi

def decrypt(ciphertext, n, d):
    """
    Decrypts an encrypted message using the private key (n, d).
    The message is decrypted using the formula m = c^d mod n, where c is the encrypted text.
    """
    try:
        return [pow(c, d, n) for c in ciphertext]
    except TypeError:
        return pow(ciphertext, d, n)

# Given values
p = 11
q = 3
e = 65537
ciphertext = [21, 5, 3, 22, 26, 24, 28, 3, 14, 16]

# Calculating n and φ(n)
n = p * q
phi = (p - 1) * (q - 1)

# Choosing e such that it is coprime with φ(n) and 1 < e < φ(n)
# Need to find the smallest value of e that is coprime with φ
e = next(e for e in range(3, phi, 2) if gcd(e, phi) == 1)

# Calculating d, the multiplicative inverse of e modulo φ
d = multiplicative_inverse(e, phi)

# Decrypting the message
decrypted_message = decrypt(ciphertext, n, d)

# Displaying the private key (d), public key (e) and the decrypted message
print(f"Private key d: {d}\nPublic key e: {e}\nDecrypted message: {''.join(chr(m + 96) for m in decrypted_message)}")
