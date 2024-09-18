from os import remove

def deleteLocalFile(filename: str) -> None: remove(filename)

if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('-f', '--filename', default='testfile.txt')

    args = parser.parse_args()
    deleteLocalFile(args.filename)
    print(f'File {args.filename} deleted')
