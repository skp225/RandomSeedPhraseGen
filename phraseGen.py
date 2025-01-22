import random
import pathlib
import pandas as pd

def generate_seed_phrases(wordlist_path, num_seed_lines):
    # Load wordlist
    with open(wordlist_path) as f:
        wordlist = [line.strip() for line in f.readlines()]
    
    # Check if there are enough words to generate seed phrases
    if len(wordlist) < 12 or num_seed_lines <= 0:
        raise ValueError("Not enough words in the wordlist to generate seed phrases.")

    seeds = []
    for _ in range(num_seed_lines):
        combination = random.sample(wordlist, k=12)
        seeds.append(' '.join(combination))
    
    return seeds

def write_to_csv(seeds, output_path):
    # Create CSV file
    df = pd.DataFrame({'Seed Phrase': seeds})
    df.to_csv(output_path, index=False, header=False)

# Main function to execute the script
def main():
    wordlist_path = pathlib.Path("bip39wordlist.txt")
    output_path = pathlib.Path("bip39_seed_phrases.csv")
    try:
        # Get number of seed phrases from user input
        num_seed_lines = int(input("Enter the number of seed phrases to generate: "))
        # Generate seed phrases and save them to CSV
        seeds = generate_seed_phrases(wordlist_path, num_seed_lines)
        write_to_csv(seeds, output_path)
        print(f"CSV file with {num_seed_lines} seed phrases generated.")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()