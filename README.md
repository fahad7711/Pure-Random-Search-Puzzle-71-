# Pure-Random-Search-Puzzle-71-
This script performs a brute-force key search to find a Bitcoin private key whose public key hash matches a target RIPEMD-160 value. It does this by:  Randomly generating private keys in a given range.  Converting each private key to a public key.  Hashing the public key (SHA-256 → RIPEMD-160).  Comparing the result to a known target hash.
📦 Requirements
🐍 Python Version
Python 3.8+ is recommended (for full bit library compatibility and tqdm/colorama formatting).

🔗 Python Libraries
Install dependencies with:

pip install bit tqdm colorama

🔹 Required Libraries:
Library	Purpose
bit	Bitcoin key generation & manipulation 
tqdm	
colorama	.
hashlib

# 🔐 RIPEMD-160 Bitcoin Key Matcher

A powerful, educational Python script that attempts to find a Bitcoin private key whose public key hash matches a given RIPEMD-160 value.

---

## 🚀 Overview

This script simulates a **random brute-force attack** to reverse a RIPEMD-160 public key hash. It generates random private keys in a specified range, converts them to public keys, and hashes them to check for a match.

It uses:
- ✅ `bit` for Bitcoin key management
- ✅ `hashlib` for SHA-256 + RIPEMD-160 hashing
- ✅ `tqdm` for smooth progress bars
- ✅ `colorama` for styled CLI output

> ⚠️ **Educational Use Only** — This tool is for cryptographic research, keyspace learning, and developer curiosity. Brute-forcing Bitcoin addresses is computationally impractical due to the enormous keyspace.

---

## 🔧 Features

- Generate **random private keys** in a custom range
- Convert private keys to **public keys**
- Generate **RIPEMD-160 hash** from public keys
- Detect and store matches to a target hash
- Color-coded output and real-time progress
- Stores sampled keys every 300,000 iterations for review

---

## 🧰 Requirements

- Python 3.8 or later

Install dependencies:

```bash
pip install -r requirements.txt

⚙️ Usage
Run the script from the terminal:

python main.py

You can customize:

The target RIPEMD-160 hash

The private key range

Change them directly in 71.py:

The Program is under liscened MIT.
⚠️ **Educational Use Only** — This tool is for cryptographic research, keyspace learning, and developer curiosity. Brute-forcing Bitcoin addresses is computationally impractical due to the enormous keyspace.
