import os
import sys
import hashlib

def hashFile(path, blockSize= 65536):
    aFile = open(path, 'rb')
    hasher = hashlib.md5()
    buf = aFile.read(blockSize)
    aFile.close()
    return hasher.hexdigest()

def findDup(parentFolder):
    dups = []
    for dirName, subDirs, fileList in os.walk(parentFolder):
        print ("Scanning %s.." % dirName)
        for fileName in fileList:
            #get the path to the file
            path = os.path.join(dirName, fileName)
            #calculate hash
            file_hash = hashFile(path)

            #add or append the file path
            if file_hash in dups:
                dups[file_hash].append(path)
            else:
                dups[file_hash] = [path]
    return dups
def joinDicts(dict1, dict2):
    for key in dict2.keys():
        if key in dict1:
            dict1[key] = dict1[key] + dict2[key]
        else:
            dict1[key] = dict2[key]


def printResults(dict1):
    results = list(filter(lambda x: len(x) > 1, dict1.values()))
    if len(results) > 0:
        print ('Duplicates Found!:')
        print ('The following files are identical. the name could differ, but the content is identical')
        print ('-----------------')
        for result in results:
            for subresult in result:
                print ('\t\t%s' %subresult)
        print ('-----------------')
    else:
        print ('No dublicates found.')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        dups = []
        folders = sys.argv[1:]

        for i in folders:
            #iterate the folders given
            if os.path.exists(i):
                #find the duplicated files and append them to dups
                joinDicts(dups, findDup(i))
            else:
                print("%s is not a valid path, please verify.. haah verify!!" % i)
                sys.exit()
        printResults(dups)
    else:
        print('Usage: python dupHELL.py folder or python dupHELL.py folder1 folder2 folder3')


