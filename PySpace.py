#A simple Python script to remove duplicate files...Coded by MCoury AKA python-scripter
import hashlib
import os

#define a function to calculate md5checksum for a given file:
def md5(f):
    """takes one file f as an argument and calculates md5checksum for that file"""
    md5Hash=hashlib.md5()
    with open(f,'rb') as f:
        for chunk in iter(lambda: f.read(4096),b""):
            md5Hash.update(chunk)
    return md5Hash.hexdigest()

#define our main function:
def rm_dup(path):
    """relies on the md5 function above to remove duplicate files"""
    if not os.path.isdir(path):#make sure the given directory exists
        print('specified directory does not exist!')
    else:
        md5_dict={}
        exp_list=[]
        if input('Would you like to ignore a certain file-type (y)es or (n)o? ')[0].lower()=='y':
            exp_list=input(r'''Please enter the file extension, eg: .doc or .py.
To ignore more than one type, use spaces to separate the extensions''').split(' ')
        print()
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
        c=0
        for key in md5_dict:
            while len(md5_dict[key])>1:
                for item in md5_dict[key]:
                    os.remove(item)
                    md5_dict[key].remove(item)
                    c+=1
        if len(ignore_list)>0:
            print('Done! Found {} duplicate files, deleted {}, and ignored {} on user\'s request...'.format(c+len(ignore_list),c,len(ignore_list)))
        else:
            print('Done! Found and deleted {} files...'.format(c))

if __name__=='__main__':
    print('=======A simple Python script to remove duplicate files===========')
    print()
    print('============Coded by MCoury AKA python-scripter===================')
    print()
    print('===========The script counts on the fact the fact=================')
    print('=========that if 2 files have the same md5checksum================')
    print('==========they most likely have the same content==================')
    print()
    path=input('Please provide the target path\directory... for example: c: or c:\directory...')
    print()
    rm_dup(path)
