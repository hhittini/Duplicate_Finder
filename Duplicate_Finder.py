from hashlib import sha256
from os import listdir,walk,mkdir
from os.path import isfile,join,exists
from shutil import copy2,move
File_Hash_DB={}

def FillNCheck(file_name,full_name,Instance_Counter,Action,FID):
	if file_name!='.DS_Store':			#Ignore .DS_Store file
		if isfile(full_name)==True:
			HASH=sha256(open(full_name).read()).hexdigest()	#Calculate the hash
			if HASH in File_Hash_DB:						#Check if the same hash exists
				Instance_Counter+=1
				if Action==1:
					FID.write('{}\n{}\n\n'.format(full_name,File_Hash_DB[HASH]))
				elif Action==2:
					FID.write('{}\n{}\n\n'.format(full_name,File_Hash_DB[HASH]))
					copy2(full_name,'Duplicate_Output/')
				elif Action==3:
					FID.write('{}\n{}\n\n'.format(full_name,File_Hash_DB[HASH]))
					move(full_name,'Duplicate_Output/')

			elif HASH not in File_Hash_DB:		#Append hash to dictonary if it's the first occurance
				File_Hash_DB[HASH]=full_name		
	return Instance_Counter;

def main():
	# 1- List in a file
	# 2- List and copy to a new folder
	# 3- List and move to a new folder
	Action=1
	Target_DIR=('/Users/user/Pictures/')
	Instance_Counter=0

	if not exists('Duplicate_Output') and Action!=1:
		mkdir('Duplicate_Output')

	FID=open('find_Duplicate_log.txt','w')

	for root, dirs, files in walk(Target_DIR):
		for name in files:
			Instance_Counter= FillNCheck(name,join(root, name),Instance_Counter,Action,FID)
		for name in dirs:
			Instance_Counter= FillNCheck(name,join(root, name),Instance_Counter,Action,FID)
	FID.write('Number of duplicate instances: {}' .format(Instance_Counter))
	print('Number of duplicate instances: {}' .format(Instance_Counter))
main()