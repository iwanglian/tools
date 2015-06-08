__author__ = 'iwanglian'

from PIL import Image
import os, sys

if __name__ == '__main__':
    ####### add size here ######
    shot_sizes = {"35": (640, 960), "40": (640, 1136), "47": (750, 1334), "55": (1242, 2208)}
    icon_names = ["Icon.png", "Icon@2x.png", "Icon-72.png", "Icon-72@2x.png", "Icon-60@2x.png", "Icon-76.png",
                  "Icon-76@2x.png", "Icon-29@2x.png", "Icon-40@2x.png"
        , "Icon-40@2x.png", "Icon-60@3x.png"]
    #############################

    rootDir = sys.argv[1]
    iconDir = os.path.join(rootDir, "icons")

    if not os.path.isdir(iconDir):
        os.mkdir(iconDir)

    for key, value in shot_sizes.iteritems():
        out_path = os.path.join(rootDir, "shot_" + key)
        if not os.path.isdir(out_path):
            os.mkdir(out_path)

    import re

    for filename in os.listdir(rootDir):
        if filename.endswith(".png") or filename.endswith(".PNG"):
            fullpath = os.path.join(rootDir, filename)
            if os.path.isdir(fullpath):
                continue
            img = Image.open(fullpath)
            width, height = img.size
            size = (0, 0)
            if width == height:
                # this is icon
                for icon_name in icon_names:
                    pattern = re.compile(r'Icon\-(\d.*?)@(\d)x\.png')
                    match = pattern.match(icon_name)
                    if match:
                        w = int(match.group(1))
                        scale = int(match.group(2))
                        size = (w * scale, w * scale)
                    else:
                        pattern = re.compile(r'Icon\-(\d.*?)\.png')
                        match = pattern.match(icon_name)
                        if match:
                            w = int(match.group(1))
                            size = (w, w)
                        else:
                            pattern = re.compile(r'Icon@(\d)x\.png')
                            match = pattern.match(icon_name)
                            if match:
                                scale = int(match.group(1))
                                size = (57 * scale, 57 * scale)
                            elif icon_name == "Icon.png":
                                size = (57, 57)
                            else:
                                exit(0)

                    icon_path = os.path.join(iconDir, icon_name)
                    img.resize(size, Image.ANTIALIAS).save(icon_path)
            else:
                for key, value in shot_sizes.iteritems():
                    out_path = os.path.join(rootDir, "shot_" + key)
                    shot_path = os.path.join(out_path, filename)
                    img.resize(value, Image.ANTIALIAS).save(shot_path)

