from random import randrange

lFiftyMostCommonWords = [
    "the", "be", "to", "of", "and", "a", "in", "that", "have", "I",
    "it", "for", "not", "on", "with", "he", "as", "you", "do", "at",
    "this", "but", "his", "by", "from", "they", "we", "say", "her",
    "she", "or", "an", "will", "my", "one", "all", "would", "there",
    "their", "what", "so", "up", "out", "if", "about", "who", "get",
    "which", "go", "me"
]

def _generateContent(wordCount: int) -> str:
    return ' '.join([ lFiftyMostCommonWords[randrange(len(lFiftyMostCommonWords))]
                      for _ in range(wordCount) ])

def _writeContentToLocalFile(content: str, filename: str) -> None:
    with open(filename, 'w') as f: f.write(content)

def generateFile(wordCount: int, filename: str) -> None:
    content = _generateContent(wordCount)
    _writeContentToLocalFile(content, filename)


if __name__ == '__main__':

    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('-w', '--wordcount', type=int, default=100)
    parser.add_argument('-f', '--filename', default='testfile.txt')

    args = parser.parse_args()
    generateFile(args.wordcount, args.filename)
    print(f'Content written to {args.filename}')
