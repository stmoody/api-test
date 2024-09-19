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

def updatedFileContent(filename: str, numberOfUpdates: int) -> str:
    content = _getLocalFileContent(filename)
    return _updateContent(content, numberOfUpdates)

def generateContent(wordCount: int) -> str:
    return ' '.join([ lFiftyMostCommonWords[randrange(len(lFiftyMostCommonWords))]
                      for _ in range(wordCount) ])
