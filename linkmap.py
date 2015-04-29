if __name__ == '__main__':
    import sys, os

    filenameArray = []
    no_dir = 1
    if len(sys.argv) > 1:
        # walk around
        no_dir = 0
        rootDir = sys.argv[2]
        for root, dirs, files in os.walk(rootDir):
            for filespath in files:
                if filespath.endswith(".m") or filespath.endswith(".mm") or filespath.endswith(".cpp"):
                    # print(filespath)
                    file_parts = os.path.splitext(filespath)
                    filenameArray.append(file_parts[0])
    parseState = 0
    oDict = {}
    sizeDict = {}
    for line in open(sys.argv[1]):
        if line.startswith(r"# Object files:"):
            parseState = 1
        elif line.startswith(r"# Address	Size    	File  Name"):
            parseState = 2
        elif line.startswith("#"):
            parseState = 0
        elif parseState == 1:
            parts = line.split("] /")
            if len(parts) > 1:
                filename = os.path.basename(parts[1])
                file_parts = os.path.splitext(filename)
                if no_dir == 1:
                    oDict[parts[0]] = file_parts[0]
                else:
                    if file_parts[0] in filenameArray:
                        oDict[parts[0]] = file_parts[0]
        elif parseState == 2:
            parts = line.split("\t")
            if len(parts) < 3:
                continue
            fileno = parts[2].split("] ")[0]
            if oDict.has_key(fileno):
                filename = oDict[fileno]
                size = int(parts[1], 0)
                if sizeDict.has_key(filename):
                    sizeDict[filename] += size
                else:
                    sizeDict[filename] = size

    import operator

    sorted_sizeDict = sorted(sizeDict.items(), key=operator.itemgetter(1), reverse=True)
    for item in sorted_sizeDict:
        print item


