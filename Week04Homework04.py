vowel = 'aeiouöü'
inputFile = open("futbolcularTurkce.txt", "r", encoding='cp1254')
file = inputFile.read().split('\n')

with open("FootbollerVowel.txt", 'w+', encoding='cp1254') as fnew:
    for name in file:
        if name[0].lower() in vowel:
            print(name)
            fnew.write(name.split(",")[0] + "\n")