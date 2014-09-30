import sys
import os
import subprocess

#to run python createJava.py fileNamehere
if(len(sys.argv)<2):
	print ("Usage: createJava.py fileName")
	sys.exit(0)
fName = sys.argv[1]

def compile(fName):
    print ("Compiling")
    subprocess.call("javac " + fName, shell=True)
    print ("Output below\n")
    subprocess.call("java " + fName.split('.java')[0] +" ", shell=True)


def main():
	if(os.path.isfile(fName+".java")):
		compile(fName+".java")
	elif (os.path.isfile(fName)):
		compile(fName)
	else:
	    print ("New file created")
	    file = open(fName + ".java", 'w+')
	    file.write("public class " + fName + " {\n    public static void main(String[] args) {\n        \n        \n    }\n}")
    

if __name__ == '__main__':
	main()

