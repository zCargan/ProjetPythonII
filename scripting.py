import argparse
if __name__ == "__main__":
    max = -float('inf')
    parser = argparse.ArgumentParser(description="Trouver le plus grand nombre d'un fichier.")
    parser.add_argument('file', help='fichier pour chercher le plus grand nombre')
    args = parser.parse_args()
    data = open(args.file).read()
    for i in data.split():
        try:
            i = float(i)
            max = i if i > max else max
        except:
            pass

    print(max)