#Add the missing items to the file


checklist = ["Portugal", "Germany", "Spain"]

fhand = open ('../inputs&outputs/countries_missing.txt')
inp = fhand.read().split('\n')

inp.extend(checklist)
FinalFile = [newf for newf in inp if newf] # to remove whitespaces
FinalFile.sort()
# print len(FinalFile)
# print (FinalFile)

with open('../inputs&outputs/AllCountries_Ex87.txt', 'w') as file:
	for i in FinalFile:
		file.write(i+'\n')
