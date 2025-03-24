import sys


def load_charset(file_path: str) -> set:
    """
    Load characters from a charset file.
    """
    with open(file_path, 'r') as file:
        charset_content = file.read()

    charset = set(charset_content.strip())
    return charset


def validate_corpus(charset: set, corpus_file: str):
    """
    Check if all characters in the corpus are present in the charset.
    """
    with open(corpus_file, 'r') as file:
        corpus_content = file.read()

    missing_chars = set(corpus_content) - charset

    if missing_chars:
        print(f"Characters present in corpus but not in charset: {missing_chars}")
    else:
        print("All characters in the corpus are present in the charset.")


def main(charset_file: str, corpus_file: str):
    charset = load_charset(charset_file)
    validate_corpus(charset, corpus_file)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python Charset_Corpus_Validation.py <charset_file> <corpus_file>")
        sys.exit(1)

    charset_file = sys.argv[1]
    corpus_file = sys.argv[2]
    main(charset_file, corpus_file)
