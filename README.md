# PySpace
PySpace is a python program that looks for duplicate files on your computer and deletes them to save space

Looking for duplicate files and then removing them manually proved annoying and boring to me, plus you might have 2 different files in 2 different directories with the same name, leading to confusion. So I wrote this program to automate the boring stuff, and because it relies on calculating md5 hash codes of the files (something humans can't do) rather than just reading their names, it's less likely to make a mistake.

Big thanks to the guys at codereview.stackexchange.com for great suggestions.

Hope you find it useful.

Update: Because 2 different files of different lengths (i.e size) can yield the same md5 checksum, I added file size checking to the program. The odds of 2 different files of different sizes generating the same md5 hash code are negligibly small. You'd need 2^64 files before there's a 50% chance. Even if those were 1KB text files they'd need a couple servers to house them.

Update: Added a new feature; now the user can choose to ignore certain file extensions (.rar .py ...etc).

# Usage:

python pyspace.py -p [target path to clean] -e [(optional) file extensions to ignore separated by a -..

eg: python pyspace.py -p d:\ or /user/ -e .py-.doc-.pdf

for more details python pyspace.py -h
