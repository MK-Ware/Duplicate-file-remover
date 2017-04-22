#!/usr/bin/env python
#A simple Python script to remove duplicate files...Coded by MCoury
import hashlib, os, optparse, sys

#define a function to calculate md5checksum for a given file:
def md5(f):
    """takes one file f as an argument and calculates md5checksum for that file"""
    md5Hash=hashlib.md5()
    with open(f,'rb') as f:
        for chunk in iter(lambda: f.read(4096),b""):
            md5Hash.update(chunk)
    return md5Hash.hexdigest()

#define our main function:
def rm_dup(path, exps):
    """relies on the md5 function above to remove duplicate files"""
    if not os.path.isdir(path):#make sure the given directory exists
        print('specified directory does not exist!')
    else:
        md5_dict={}
        if exps:
            exp_list=exps.split("-")
        else:
            exp_list = []
        print('Working...')
        print()
        for root, dirs, files in os.walk(path):#the os.walk function allows checking subdirectories too...
            for f in files:
                filePath=os.path.join(root,f)
                md5Hash=md5(filePath)
                size=os.path.getsize(filePath)
                fileComb=str(md5Hash)+str(size)
                if fileComb in md5_dict:
                    md5_dict[fileComb].append(filePath)
                else:
                    md5_dict.update({fileComb:[filePath]})
        ignore_list=[]
        for key in md5_dict:
            for item in md5_dict[key]:
                for p in exp_list:
                    if item.endswith(p):
                        ignore_list.append(item)
                        while md5_dict[key].count(item)>0:
                            md5_dict[key].remove(item)

        print("Done! Following files will be deleted:\n")
        for key in md5_dict:
            for item in md5_dict[key][:-1]:
                print(item)
        if input("\nEnter (y)es to confirm operation or anything else to abort: ").lower() not in ("y", "yes"):
            sys.exit("Operation cancelled by user. Exiting...")

        print("Deleting...")
        c=0
        for key in md5_dict:
            while len(md5_dict[key])>1:
                for item in md5_dict[key]:
                    os.remove(item)
                    md5_dict[key].remove(item)
                    c += 1
        if len(ignore_list)>0:
            print('Done! Found {} duplicate files, deleted {}, and ignored {} on user\'s request...'.format(c+len(ignore_list),c,len(ignore_list)))
        else:
            print('Done! Found and deleted {} files...'.format(c))

if __name__=='__main__':
    print('    ##########A simple Python script to remove duplicate files#########')
    print('    #                      Coded by monrocoury                        #')
    print('    #              The script relies on the fact the fact             #')
    print('    #        that if 2 files have the same md5checksum                #')
    print('    #                  they most likely have the same content         #')
    print('    ###################################################################')
    parser = optparse.OptionParser("usage: python %prog -p <target path> -e <file extensions to ignore separated by ->")
    parser.add_option("-p", dest="target_path", type="string", help="provide target path")
    parser.add_option("-e", dest="ext2ignore", type="string", help="(optional) provide file extensions to ignore separated by - eg: -e .py-.doc")
    (options, args) = parser.parse_args()
    p = options.target_path
    e = options.ext2ignore

    rm_dup(p, e)
