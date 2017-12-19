import math

password_list = []

def brute_force(word, password_length):
	counter = 0
	total_word = ""
	#print word
	#print password_length

	number_combinations = ""

	remaining_length = int(password_length) - len(word) 


	#print 10**remaining_length


	#10 to the power of the remaining length - 1
	#if it's 3, its 10^3, which is 1000-1=999- maximum amount of digits
	if len(word) > int(password_length):
		password_list.append(word) 
		return password_list
	while (counter < (10**remaining_length - 1)):
		counter += 1
		total_word = word + str(counter)
		#print total_word
		password_list.append(total_word) 

	return password_list	
	


def input_function():
	password_length = 0
	new_phrase = ""
	new_words_and_phrases = ""
	checking = True
	asking_provided_answers = True

	print ""
	print "******************************************"
	print "Welcome to *Little Hacker* Version 1.0" 
	print "******************************************"
	print ""
	print "First Please provide all possible words and/or phrases that may be included in your password"
	print ""
	print "			!!!!!!!WARNING!!!!!!!!"
	print ""
	print " -Each word or phrase must seperated by a space in provided formatting"
	print " -Case matters in all provided words and/or phrases"    
	print ""


	while(asking_provided_answers):
		provided_words_and_phrases = raw_input("Provided Answers: ")

		if provided_words_and_phrases == "":
			print "No Guesses?"
			no_guesses_check = raw_input("(ENTER/N): ")
			if no_guesses_check == "":
				asking_provided_answers = False
			elif no_guesses_check == "N":
				asking_provided_answers = True
			else:
				asking_provided_answers = True		
		else:
			asking_provided_answers = False	



	print ""
	print "#Please Check Answers#"

	provided_words_and_phrases += " "

	for i in range(len(provided_words_and_phrases)):

	    if (provided_words_and_phrases[i] == " "):
	    	checking = True

	    	while(checking):
		    	print ""
		    	print "Confrim This Answer:", new_phrase
		    	words_and_phrases_checker = raw_input("(ENTER/N): ")

		    	if words_and_phrases_checker.upper() == "":
		    		new_words_and_phrases += new_phrase  + " "
		    		new_phrase = ""
		    		checking = False
		    	elif words_and_phrases_checker.upper() == "N":
		    		changed_word_or_phrase = raw_input("New word/phrase: ")
		    		new_words_and_phrases += changed_word_or_phrase + " " 
		    		new_phrase = ""
		    		checking = False
		    	else:	    	
		    		print "*PLEASE PROVIDE A VALID ANSWER*"	
		    		checking = True
	    			

	    else:
	      new_phrase += provided_words_and_phrases[i]

	print ""
	print "##################################################################"
	print "Now Please Provide the maximum character length of your password"
	print "##################################################################"
	print ""
	password_length = raw_input("Maximum Amount of Characters: ")

	#print new_words_and_phrases   

	common_passwords = ["passw0rd","monkey","sunshine","master","letmein","dragon","login", "123456","123456789", "querty", "12345678", "111111", "1234567890","1234567", "password", "123123", "qwertyuiop", "mynoob", "666666", "7777777", "555555", "google"]
	
	for i in range(len(new_words_and_phrases)):
	    if new_words_and_phrases[i] == " ":
	    	password_list.append(new_phrase) 
	    	print brute_force(new_phrase, password_length)
	    	new_phrase = ""
	    else:

	      new_phrase += new_words_and_phrases[i]


	for i in range(len(common_passwords)):   
		password_list.append(common_passwords[i])    
		print brute_force(common_passwords[i], password_length)      

	
  
	


input_function()	


