from random import randrange

lFiftyMostCommonWords = [
    "the", "be", "to", "of", "and", "a", "in", "that", "have", "I",
    "it", "for", "not", "on", "with", "he", "as", "you", "do", "at",
    "this", "but", "his", "by", "from", "they", "we", "say", "her",
    "she", "or", "an", "will", "my", "one", "all", "would", "there",
    "their", "what", "so", "up", "out", "if", "about", "who", "get",
    "which", "go", "me"
]

def _getLocalFileContent(filename: str) -> str:
    with open(filename, 'r') as f: return f.read()

def _updateContent(content: str, numberOfUpdates: int) -> str:
    lContent = content.split()

    for _ in range(numberOfUpdates):
        lContent[randrange(len(lContent))] = \
            lFiftyMostCommonWords[randrange(len(lFiftyMostCommonWords))]

    return ' '.join(lContent)

def _writeContentToLocalFile(content: str, filename: str) -> None:
    with open(filename, 'w') as f: f.write(content)

def updateFile(filename: str, numberOfUpdates: int) -> None:
    content = _getLocalFileContent(filename)
    updatedContent = _updateContent(content, numberOfUpdates)
    _writeContentToLocalFile(updatedContent, filename)

if __name__ == '__main__':

        from argparse import ArgumentParser
        parser = ArgumentParser()
        parser.add_argument('-f', '--filename', default='testfile.txt')
        parser.add_argument('-u', '--updates', type=int, default=10)

        args = parser.parse_args()
        updateFile(args.filename, args.updates)
        print(f'Content updated in {args.filename}')
