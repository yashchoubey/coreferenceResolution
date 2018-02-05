from neuralcoref import Coref

coref = Coref()
count=0
totalcount=0
with open('reviews.csv','r') as file :
	with open("corefs.txt",'a') as wfile:
		content=file.readlines()
		totalcount=len(content)

		for review in content:
			if review:
				count=count+1
				clusters = coref.one_shot_coref(utterances=review.decode('utf-8'))
				resolved_utterance_text = coref.get_most_representative()
				if 	resolved_utterance_text:
					#print "=========================="
					#print review
					print "=========================="
					wfile.write(str(resolved_utterance_text))
					wfile.write('\n')
					print "------",count," of ",totalcount
					print "=========================="


# print(clusters)
# print "=========================="
# mentions = coref.get_mentions()
# print(mentions)
# print "=========================="
# utterances = coref.get_utterances()
# print(utterances)
# print "=========================="
# resolved_utterance_text = coref.get_resolved_utterances()
# print(resolved_utterance_text)
# print "=========================="
# resolved_utterance_text = coref.get_clusters()
# print(resolved_utterance_text)
# print "=========================="
# resolved_utterance_text = coref.get_most_representative()
# print(resolved_utterance_text)