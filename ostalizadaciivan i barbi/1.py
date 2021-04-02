# class ParserError (Exception):
# 	pass
	
	
# class Sentence (object):
# 	def __init__(self , subject, verb, obj):
# 		#we take ('noun', 'princesse') tuple and convert them
# 		self.subject = subject[1]
# 		self.verb = verb[1]
# 		self.object = obj[1]
		
		
# 	def peek(word_list):
# 		if word_list:
# 			word = word_list[0]
# 			return word[0]
# 		else:
# 			return None
			
	
	
# 	def mach(word_list, expecting):
# 		if word_list:
# 			word = word_list.pop(0)
			
# 			if word[0] == expecting:
# 				return word
# 			else:
# 				return None
# 		else:
# 			return None
			
		
		
# 	def skip(word_list,word_type):
# 		while peek (word_list) == word_type:
# 			mach(word_list, word_type)
			
			
			
# 	def parse_verb(word_list):
# 		skip(word_list, 'stop')
		
# 		if peek (word_list) == 'verb':
# 			return match(word_list, 'verb')
# 		else:
# 			ParserError("Expected a verb next.")
			
			
# 	def parse_object(word_list):
# 		skip (word_list, 'stop')
# 		next_word = peek(word_list)

# 		if next_word == 'noun':
# 			return mach(word_list, 'noun')
# 		elif next_word == 'direction':
# 			return match(word_list, 'diretion')
# 		else:
# 			raise ParserError("Expected a noun or direction next.")
			
# 	def parse_subject(word_list):
# 		skip(word_list, 'stop')
# 		next_word = peek(word_list)

# 		if next_word == 'noun':
# 			return match(word_list, 'noun')
# 		elif next_word == 'verb':
# 			return ('noun', 'player')
# 		else:
# 			raise ParserError("Expected a verb next.")
		
# 	def parse_sentence(word_list):
# 		subj = parse_subject(word_list)
# 		verb = parse_verb(word_list)
# 		obj = parse_object(word_list)

# 		return Sentence(subj, verb, obj)


# x = Sentence()
# x = parse_sentence([('verb','run'), ('direction','north')])


from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	greeting = "World"
	return f'Hello, {greeting}!'
	
@app.route('/ivan')
def metoda_ivan():
	greeting = "World"
	return 'Hello, iv!'
	
if __name__=="__main__":
	app.run()
	