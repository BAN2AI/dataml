#using stopwords
from nltk import word_tokenize, SnowballStemmer, ngrams, pos_tag

from collections import Counter
from nltk.corpus import stopwords

fbooktokenfutaa = "EAAJYXY2apSsBABfkNOsI01qb2jqXXBMhkvOVSCPKk4qUMN7qxkIWhNwpgZBvqTgPJ9aLgGrwZBXzaByubpaORZC9Hwf84xZAaaif6BvzecxP1MYnNe53wrMjdZC8omRn7N4nnDwrxpxaiQYTa72OWakNESzW2d0LHoZCJX1vbLAgZDZD"

stopwords = stopwords.words('french')
print("stopwords")
print(stopwords)
print("=======")
ex_sentence = "Dans le cadre d’une démarche pour une instruction personnalisée et centrée sur les élèves, l’administration scolaire du comté de Howard dans le Maryland utilise  le Design Thinking pour s’atteler à la refonte des programmes de la prochaine génération en y intégrant les compétences du XXIe siècle. Actuellement, il y a un décalage entre les programmes existants, qui s’appuient sur des documents imprimés, et les ressources numériques interactives disponibles pour les enseignants et les élèves à tout moment et depuis n’importe où. En observant les comportements des enseignants, des parents et des élèves à l’intérieur et à l’extérieur de l’école, l’équipe du projet s’est inspirée des façons dont ces derniers accèdent à l’information et la traitent, et utilisent les contenus pédagogiques. Une meilleure compréhension des souhaits des enseignants, des élèves, des parents et des administrateurs a permis à l’équipe de repenser les manières d’enseigner et de développer de nouvelles ressources pour remplacer, augmenter et améliorer les contenus existants. Le comté de Howard utilise le Design Thinking pour reconceptualiser la création des programmes et leur enseignement afi n de répondre aux besoins de l’ensemble des élèves."

stemmer = SnowballStemmer('french')

tokens = word_tokenize(ex_sentence)	
#print(tokens)
#bigrams are used to see the frequency of somme words used separately he firts parameter is a words and the second is th number of words found when used the same time

bigrams = list(ngrams(tokens, 3))
frequencies = Counter(tokens)
tags = pos_tag(tokens)

print ("words frequencies and tokens and tags")
for token,count in frequencies.most_common(25) :
	if token in stopwords or len(token) < 2 :
		continue
	print (token + " : " + str(count))
	print ("stemmed words : " + stemmer.stem(token))

print("=======================")
#bigrams
print("words list of bigrams")
frequencies = Counter(bigrams)
for token,count in frequencies.most_common(25) :
	print (token ,count)

print (tags)


