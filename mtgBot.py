import praw
import json
import time

#Assembles a list of consecutive strings in array stringy of length 'length'
def assembleStrings(stringy, length):
	base = []
	for i in range(0, len(stringy)-length+1):
		base.append(stringy[i])
		for num in range(1, length):
			base[i] = base[i] + " " + (stringy[i+num])
	#print base
	return base

#Given a string "messager", find and return all URLs of magic cards referenced in the list
def searchForCards(message):
	ret = []
	#strip out all keyboard punctuation
	messager = message.replace('`','').replace('~','').replace('!','').replace('@','').replace('#','').replace('$','').replace('%','').replace('^','').replace('&','').replace('*','').replace('(','').replace(')','').replace('-','').replace('+','').replace('=','').replace('{','').replace('[','').replace('}','').replace(']','').replace(':','').replace(';','').replace('\"','').replace('\'','').replace('<','').replace(',','').replace('>','').replace('.','').replace('?','').replace('/','').replace('|','').replace('\\','').lower()

	#Special case for card name _____
	if "_____" in messager:
		ret.append(data["_____"])

	messager = messager.replace('_','')

	#special case for an absurdly long name also, I typed it in with caps, so the .lower their is at the end for that reason
	if "Our Market Research Shows That Players Like Really Long Card Names So We Made this Card to Have the Absolute Longest Card Name Ever Elemental".lower() in messager:
		ret.append(data["Our Market Research Shows That Players Like Really Long Card Names So We Made this Card to Have the Absolute Longest Card Name Ever Elemental"])


	messagy = messager.split()
#print messager
	#There is one card that I know of that is longer than 6 words, and I don;t think anyone will mind if it does not support the card:
	#Our market research showsthat players like really long names so we made this card to have the absolute longest card name ever elemental
	for wordLen in range(1,7):
		searchableWords = assembleStrings(messagy, wordLen)
		#print assembleStrings(messagy,wordLen)
		for x in data:
			qq = data[x]['name'].lower()
			zz = qq.replace('`','').replace('~','').replace('!','').replace('@','').replace('#','').replace('$','').replace('%','').replace('^','').replace('&','').replace('*','').replace('(','').replace(')','').replace('_','').replace('-','').replace('+','').replace('=','').replace('{','').replace('[','').replace('}','').replace(']','').replace(':','').replace(';','').replace('\"','').replace('\'','').replace('<','').replace(',','').replace('>','').replace('.','').replace('?','').replace('/','').replace('|','').replace('\\','')
			#print ">>>>" + zz
			#print assembleStrings(messagy,1)
			if zz in searchableWords:
				#print "Found:"
				#print zz
				#print data[x]['name']
				#print data[x]['imageName']
				if zz not in ret:
					ret.append(data[x])
				#print " "
	return ret


########################################START#######################

f = open("AllCards-x.json","r")
data = json.load(f)



#Reddit bt framework based heavily on supplied python example code
userAgent = "python:MTGcourtesy v0.5 by emorelleum"
reddy = praw.Reddit(user_agent = userAgent)

#setups for lists to keep track of what we have seen
postFile = open("postFile.txt",'r')
repliedPosts = []

for lines in postFile:
	#apparently the new lines stay on, according to the python api
	repliedPosts.append(lines.strip('\n'))

postFile.flush()
postFile.close()

commentFile = open("commentFile.txt",'r')
repliedComments = []

for lines in commentFile:
	repliedComments.append(lines.strip('\n'))

commentFile.flush()
commentFile.close()

credFile = open("info.txt",'r')
namey = credFile.readline().strip('\n')
wordy = credFile.readline().strip('\n')
reddy.login(namey,wordy)

#infinite loop via python wrapper
while True:
	submissions = reddy.get_subreddit("UMW_CPSC470Z").get_hot(limit=None)

	for submission in submissions:
	#	print submission.selftext
		if "MTG_LINK" in submission.selftext and submission.id not in repliedPosts:
	
			vals = searchForCards(submission.selftext)
			#construct the text of the post
			post = "Courtesy Links for the post:\n\n"
			for cards in vals:
				post += "[" + cards['name'] + "](http://mtgimage.com/card/" + cards['imageName'] + ".jpg)\n\n"
			print post
			#if there were no characters added to the string, no cards were found
			if len(post) > 30:
				submission.add_comment(post)
			else:
				submission.add_comment("There were no MTG cards found in this submission")
			repliedPosts.append(submission.id)
		#get all the comments (from praw framework explanation)	
		comment_list = praw.helpers.flatten_tree(submission.comments)
		for g in comment_list:
			#print g.body
			if "MTG_LINK" in g.body and g.id not in repliedComments:
				#print g.body
				print " "
				vals = searchForCards(g.body)
				#construct the text of the post
				post = "Courtesy Links:\n\n"
				for cards in vals:
					post += "[" + cards['name'] + "](http://mtgimage.com/card/" + cards['imageName'] + ".jpg)\n\n"
				print post
				#If we did not find any cards to link to, then post an error
				if len(post) > 20:
					g.reply(post)
				else:
					g.reply("There were no MTG cards found in this comment")
				repliedComments.append(g.id)
	print "Saving....Do not turn off the power"
	#write the contents of the arrays to their appropriate files. Not 100% sure what will happen if the program is interrupted here (I am no python guru), so hopefully it won;t be!
	#mostly here so I can stop and start the bot without reposting a bunch of comments
	postFile = open("postFile.txt",'w')
	for records in repliedPosts:
		postFile.write(records+'\n')

	postFile.flush()
	postFile.close()

	commentFile = open("commentFile.txt",'w')
	for records in repliedComments:
		commentFile.write(records+'\n')

	commentFile.flush()
	commentFile.close()
	
	print "sleeping"
	time.sleep(30)
	print "Woke Up!"
	print ""
