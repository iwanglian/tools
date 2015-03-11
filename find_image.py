from PIL import Image
import imagehash
import pickle

def is_image(filename):
	f = filename.lower()
	return f.endswith(".png")

def create_index(rootDir):
	import os
	images = {}
	for root,dirs,files in os.walk(rootDir):
		for filespath in files:
			if(is_image(filespath)):
				fullpath = os.path.join(root,filespath)
				img = Image.open(fullpath)
				if(img.format=='PNG'):
					pichash = imagehash.phash(img)
					images[pichash]=fullpath
					print pichash,fullpath
		dumpfile = open('index.pickle', 'wb')
		pickle.dump(images, dumpfile)

if __name__ == '__main__':
	import sys, os
	if(sys.argv[1]=='i'):
		create_index(sys.argv[2])
	else:
		if(not os.path.exists("index.pickle")):
			print("index file not exists,please run fi_index.py first")
			sys.exit(1)
		picpath = sys.argv[1]
		if(not os.path.exists(picpath)):
			print("image not exists")
			sys.exit(1)
		pichash = imagehash.phash(Image.open(picpath))
		dumpfile = open('index.pickle', 'rb')
		images = pickle.load(dumpfile)
		for key, value in images.iteritems():
			if(pichash - key <5):
				print(pichash - key),key,value

