import hashlib

# 1. Choose a target password to encrypt
password = "secret123"

# 2. Convert the password into an MD5 hash
md5_hash = hashlib.md5(password.encode()).hexdigest()

# 3. Convert the password into a SHA-256 hash
sha256_hash = hashlib.sha256(password.encode()).hexdigest()

# 4. Print the results to your screen
print("--- GENERATED HASHES ---")
print(f"MD5 Hash: {md5_hash}")
print(f"SHA-256 Hash: {sha256_hash}")
print("------------------------")

# 5. Automatically create a file named targets.txt and save the hashes inside it
with open("targets.txt", "w") as f:
    f.write(f"{md5_hash}\n")
    f.write(f"{sha256_hash}\n")
print("Hashes successfully saved to targets.txt!")