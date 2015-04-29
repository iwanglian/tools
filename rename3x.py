if __name__ == '__main__':
    import sys, os

    root = sys.argv[1]
    for filename in os.listdir(root):
        if filename.endswith(".png") and not filename.endswith("@3x.png"):
            # print filename[:-4]
            fullpath = os.path.join(root, filename)
            fullpath2 = os.path.join(root, "@3x".join([filename[:-4], ".png"]))
            os.rename(fullpath, fullpath2)