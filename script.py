import codecs, os, re
from shutil import copyfile

def isValidPath(path):
    for key, val in FILE_EXTENSIONS.items():
        for extension in FILE_EXTENSIONS[key]:
            if path.endswith("." + extension):
                return True
    return False

def getFilePathsFromLine(line):
    strs = re.findall('"([^"]*)"', line)

    returnStr = []

    for s in strs:
        if "'" in s:
            strings = re.findall("'([^']*)'", s)
            for st in strings:
                if isValidPath(st):
                    returnStr.append(st)
        else:
            if isValidPath(s):
                returnStr.append(s)

    return returnStr

def getFileNameFromPath(path):
    if "/" in path:
        return path.rsplit('/', 1)[-1]
    elif "\\" in path:
        return path.rsplit('\\', 1)[-1]
    else:
        return path

def replaceLineWithNewPaths(line, dir):
    paths = getFilePathsFromLine(line)
    returnLine = line

    for path in paths:
        if(isValidPath(path)):
            returnLine = returnLine.replace(path, dir + "/" + getFileNameFromPath(path))
            copyFileFromPath(path, dir)

    return returnLine

def copyFileFromPath(path, dir):
    src = HTML_PATH + "/../" + path
    dest = dir + "/" + getFileNameFromPath(path)

    if(isValidPath(path)):
        if not os.path.isfile(dest):
            copyfile(src, dest)

FILE_EXTENSIONS = {
    "styles": ["css"],
    "images": ["jpg", "jpeg", "png", "gif", "jif", "jfif", "tif", "tiff", "bmp", "ico"],
    "scripts": ["js", "php", "py"],
    "fonts": ["woff", "woff2", "ttf", "otf", "fnt", "fon"]
}

HTML_PATH = "PATH TO HTML FILE" # use forward slashes instead of backslashes, otherwise you'll get an error

f = codecs.open(HTML_PATH, "r")
n = codecs.open("index.html", "w")


for extensionsKey in FILE_EXTENSIONS.keys():
    if not os.path.exists(extensionsKey):
        os.makedirs(extensionsKey)

for line in f.readlines():
    replaceLine = line

    for extensionsKey, extensionsValue in FILE_EXTENSIONS.items():
        for extension in FILE_EXTENSIONS[extensionsKey]:
            if "." + extension in line:
                replaceLine = replaceLineWithNewPaths(line, extensionsKey)

    n.write(line.replace(line, replaceLine))