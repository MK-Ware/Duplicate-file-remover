# PySpace
PySpace is a python program that looks for duplicate files on your computer and deletes them, saving space

# How it works:

Looking for duplicate files and then removing them manually proved annoying and boring to me, plus you might have 2 different files in 2 different directories with the same name, leading to confusion. So I wrote this program to automate the boring stuff, and because it relies on calculating md5 hash codes of the files (something humans can't do) rather than just reading their names, it's less likely to make a mistake.

Update: Because 2 different files of different lengths (i.e size) can yield the same md5 checksum, I added file size checking to the program. The odds of 2 different files of different sizes generating the same md5 hash code are? Negligibly small! md5 is a 128-bit hash, so the odds of 2 different files generating identical md5 sums are 1 / 2^128.. That's 1 / 340282366920938463463374607431768211456. In other words, you'd need 2^64 files before there's a 10% chance. Even if those were 1KB text files they would require 16384 Exabytes of storage capacity, which is unfathomably huge.

Update: Added a new feature; now the user can choose to ignore certain file extensions (.rar .py ...etc).

# Usage:

- python pyspace.py -p (target path to clean) -e (-optional- file extensions to ignore separated by a -). <br />
eg: python pyspace.py -p d:\ or /user/ -e .py-.doc-.pdf

- The script will display the duplicate files it detected and ask the user to confirm the deletion, if the user confirms, it will leave only one copy of each and every file and remove the rest.

for more details python pyspace.py -h

_______________________________________________________________________________________________________

* Kudos to the nice guys at codereview.stackexchange.com for their very helpful suggestions!
* Hope you find it useful! Don't forget to star the repo if you do..
