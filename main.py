from stats import get_num_words, get_characters, sort_characters

import sys

def get_book_text(filepath, mode='r', encoding='utf-8-sig'):
	with open(filepath) as f:
		filetext = f.read()
		return filetext

def main():
	if (len(sys.argv) != 2):
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	else:
		file = sys.argv[1]

	txt = get_book_text(file)
	num_words = get_num_words(txt)
	charcount = get_characters(txt)
	sorted_list = sort_characters(charcount)

	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {file}...")
	print("----------- Word Count ----------")
	print(f"Found {num_words} total words")
	print("--------- Character Count -------")

	for x in sorted_list:
		print(f"{x}: {sorted_list[x]}")

if __name__ == "__main__":
	main()
