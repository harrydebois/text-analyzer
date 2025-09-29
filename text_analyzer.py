def analyze_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    lines = text.splitlines()
    words = text.split()
    characters = list(text)
    return len(lines), len(words), len(characters)


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Analyze a text file')
    parser.add_argument('file', help='Path to the text file')
    args = parser.parse_args()
    lines, words, chars = analyze_file(args.file)
    print(f'Lines: {lines}, Words: {words}, Characters: {chars}')


if __name__ == '__main__':
    main()
