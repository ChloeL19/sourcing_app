# import stuff
import bcolz
import tensorflow as tf 
import numpy as np 
import pickle
import spacy

import requests 
import json

# create a Word class (phrase)
class Word:

	def __init__(self, phrase):
		self.phrase_1 = phrase
		self.phrase_2 = phrase


	def glove_replace(self, wordx):
		# define functions that take a string and replace each noun and verb with closest glove equivalent
		vocab_size = 400000
		embedding_size = 50

		graph = tf.Graph()
		with graph.as_default():
			embedding = tf.placeholder(tf.float32, [vocab_size, embedding_size])
		    # select a word of interest
			word = tf.placeholder(tf.float32, [1,embedding_size])
			normed_embedding = tf.nn.l2_normalize(embedding, axis=1)
			normed_word = tf.nn.l2_normalize(word, axis=1)
		    # find a list of the top 5 words closest to that word
			cosine_similarity = tf.matmul(normed_word, tf.transpose(normed_embedding, [1,0]))
			closest_5_words = tf.nn.top_k(cosine_similarity, k=5)


			# C://Users/chloeloughridge/littleApp/app
			vectors = bcolz.open('./app/6B.50.dat')[:]
			words = pickle.load(open('./app/6B.50_words.pkl', 'rb'))
			word2idx = pickle.load(open('./app/6B.50_idx.pkl', 'rb'))
			idx2word = {v: k for k, v in word2idx.items()}

			glove = {w: vectors[word2idx[w]] for w in words}

		with tf.Session(graph=graph) as sess:
			try: 
				w = np.expand_dims(np.asarray(glove[wordx]), axis=0)
				sim_scores = sess.run(cosine_similarity, feed_dict={embedding: vectors, word: w}).flatten()
				id3 = (-sim_scores).argsort()[:5][-1] #index of 5th largest value in array
				return idx2word[id3]
			except:
				return wordx

	def muse_replace(self, wordx):
		url = "https://api.datamuse.com/words?ml="+wordx
		response = requests.request("GET", url)
		res = json.loads(response.text)
		return res[0]['word']


	def replace(self):
		# find verbs and nouns and call glove_replace
		#self.phrase = phrase
		nlp = spacy.load('en_core_web_sm')
		doc = nlp(self.phrase_1)
		for token in doc:
			if token.pos_ == 'NOUN' or token.pos_ == 'VERB' or token.pos_ == 'ADJ' or token.pos_ == 'PROPN':
				self.phrase_1 = self.phrase_1.replace(token.text, self.glove_replace(token.text)) #glove version
				self.phrase_2 = self.phrase_2.replace(token.text, self.muse_replace(token.text)) #muse version

		# return modified phrase
		return [self.phrase_1, self.phrase_2]
	


	# def api_replace():
		# use api to replace verbs and nouns with closest equivalents
