import json

hair_color = {'Black': 'CCAGCAATCGC', 'Brown': 'GCCAGTGCCG', 'Blonde': 'TTAGCTATCGC'}
face_shape = {'Square': 'GCCACGG', 'Round': 'ACCACAA', 'Oval': 'AGGCCTCA'}
eye_color = {'Blue': 'TTGTGGTGGC', 'Green': 'GGGAGGTGGC', 'Brown': 'AAGTAGTGAC'}
gender = {'Female': 'TGAAGGACCTTC', 'Male': 'TGCAGGAACTTC'}
race = {'White': 'AAAACCTCA', 'Black': 'CGACTACAG', 'Asian': 'CGCGGGCCG'}

accused = {'Eva': ['Female', 'White', 'Blonde', 'Blue', 'Oval'],
            'Larisa': ['Female', 'White', 'Brown', 'Brown', 'Oval'],
            'Matej': ['Male', 'White', 'Black', 'Blue', 'Oval'],
            'Miha': ['Male', 'White', 'Brown', 'Green', 'Square']}

with open("dna.txt", "r") as dna:
    dna = dna.read()

guessed_person = []

for x in hair_color:
    if hair_color[x] in dna:
        print(x)
        guessed_person.append(x)

for x in face_shape:
    if face_shape[x] in dna:
        print(x)
        guessed_person.append(x)

for x in eye_color:
    if eye_color[x] in dna:
        print(x)
        guessed_person.append(x)

for x in gender:
    if gender[x] in dna:
        print(x)
        guessed_person.append(x)

for x in race:
    if race[x] in dna:
        print(x)
        guessed_person.append(x)

for a in accused:
    if accused[a] == guessed_person:
        print("The person we're looking for is %s" % p.lower())
        break