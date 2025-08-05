# Pure-Random-Search-Puzzle-71-
This script performs a brute-force key search to find a Bitcoin private key whose public key hash matches a target RIPEMD-160 value. It does this by:  Randomly generating private keys in a given range.  Converting each private key to a public key.  Hashing the public key (SHA-256 → RIPEMD-160).  Comparing the result to a known target hash.
