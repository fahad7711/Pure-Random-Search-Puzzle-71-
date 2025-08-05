import os
import random
import hashlib
from bit import Key
from tqdm import tqdm
from colorama import Fore, Style

def public_key_to_rmd160(public_key):
    """Generate RIPEMD-160 hash from a public key."""
    return hashlib.new('ripemd160', hashlib.sha256(bytes.fromhex(public_key)).digest()).hexdigest()

def private_key_to_public_key(private_key):
    """Convert a private key to its corresponding public key."""
    key = Key.from_int(private_key)
    return key.public_key.hex()

def generate_random_keys(lower_bound, upper_bound, count=100000):
    """Generate completely random private keys within the given range."""
    return [random.randint(lower_bound, upper_bound) for _ in range(count)]

def generate_and_compare_keys():
    """Generate and compare public key hashes until a match is found."""
    folder_path = os.path.dirname(os.path.abspath(__file__))
    target_rmd160 = "f6f5431d25bbf7b12e8add9af5e3475c44a0a5b8"
    user_lower_bound = 1331198259382744477091
    user_upper_bound = 2353518513036786330335
    
    print(Fore.CYAN + "Starting search for matching RIPEMD-160 hash..." + Style.RESET_ALL)
    iteration_count = 0
    sampled_keys = []
    
    while True:
        print(Fore.BLUE + f"Using random search in range: {user_lower_bound} to {user_upper_bound}" + Style.RESET_ALL)
        
        private_keys = generate_random_keys(user_lower_bound, user_upper_bound)
        
        for private_key in tqdm(private_keys, desc=Fore.GREEN + "Generating and checking keys" + Style.RESET_ALL):
            public_key = private_key_to_public_key(private_key)
            public_key_hash = public_key_to_rmd160(public_key)
            iteration_count += 1
            
            if iteration_count % 300000 == 0:
                sampled_keys.append((private_key, public_key, public_key_hash))
                if len(sampled_keys) > 15:
                    sampled_keys.pop(0)
            
            if public_key_hash == target_rmd160:
                match_file_path = os.path.join(folder_path, "matching_keys.txt")
                with open(match_file_path, "w") as match_file:
                    match_file.write(f"Private Key: {private_key}\nPublic Key: {public_key}\nRIPEMD-160: {public_key_hash}\n")
                print(Fore.GREEN + "Match found! Saved to matching_keys.txt. Stopping search." + Style.RESET_ALL)
                return
        
        if sampled_keys:
            print(Fore.YELLOW + "Sampled private-public key pairs after 3,00,000 iterations:" + Style.RESET_ALL)
            for priv, pub, hash_val in sampled_keys:
                print(f"Private Key: {priv}, Public Key: {pub}, RIPEMD-160: {hash_val}")
        
        print(Fore.RED + "No matches found in this round. Retrying with new random keys..." + Style.RESET_ALL)

if __name__ == "__main__":
    generate_and_compare_keys()
