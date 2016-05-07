
class Lexicon:
	def __init__(self):
		self.lex = {}
		self.load()

class SubjLexicon(Lexicon):
	def load(self):
		with open('../lexicons/subjectivity_clues_hltemnlp05/subjclueslen1-HLTEMNLP05.tff', 'r') as f:
			read_data = f.readlines()
			for line in read_data:
				parts = line.split()
				word = parts[2].split('=')[1]
				self.lex[word] = {}
				for p in parts:
					key,val = p.split('=')
					if key=='len' or key=='word1':
						continue
					else:
						self.lex[word][key] = val

	def getFeatures(self, words):
		#call before converting word to number
		subj = []
		pola = []
		for w in words:
			if w in self.lex:
				if self.lex[w]['type']=='strongsubj':
					subj.append(1)
				else:
					subj.append(0.5)

				pol = self.lex[w]['priorpolarity']
				if pol=='negative':
					pola.append(-1)
				elif pol=='positive':
					pola.append(1)
				else:
					pola.append(0)
			else:
				subj.append(0)
				pola.append(0)
		return subj+pola

class LiuLexicon(Lexicon):
	def load(self):
		with open('../lexicons/liu/negative-words.txt', 'r') as f:
			read_data = f.readlines()
			for line in read_data:
				lin = line.strip()
				if lin and lin[0]!=';':
					self.lex[lin] = -1
		with open('../lexicons/liu/positive-words.txt', 'r') as f:
			read_data = f.readlines()
			for line in read_data:
				lin = line.strip()
				if lin and lin[0]!=';':
					self.lex[lin] = 1

	def getFeatures(self, words):
		#call before converting word to number
		sent = []
		for w in words:
			if w in self.lex:
				sent.append(self.lex[w])
			else:
				sent.append(0)
		return sent

if __name__ == '__main__':
	s = LiuLexicon()
	print s.getFeatures(['He','is','hack'])
