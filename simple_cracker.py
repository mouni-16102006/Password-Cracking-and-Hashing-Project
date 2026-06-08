import hashlib

# Step 1: Let's automatically grab whatever hash your generator actually wrote to targets.txt
with open("targets.txt", "r") as target_file:
    target_hash = target_file.readline().strip()

print(f"Targeting the actual system hash: {target_hash}")
print("Starting dictionary attack simulation...")

# Step 2: Run the attack
with open("wordlist.txt", "r") as file:
    for line in file:
        guessed_word = line.strip()
        guessed_hash = hashlib.md5(guessed_word.encode()).hexdigest().strip()
        
        print(f"Testing word: {guessed_word} -> Hash: {guessed_hash}")
        
        if guessed_hash == target_hash:
            print("\n==========================================")
            print(f"[SUCCESS] Password Cracked! The password is: {guessed_word}")
            print("==========================================")
            break
