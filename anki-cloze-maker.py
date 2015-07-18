#!venv/bin python2.7
import time
import os
import sys

ANSWER_SPLITTER = ' '
CLOZE_SPLITTER = '_'

notes_cloze = []

question_parts = []
list_questions = []

args = sys.argv

def evalListQuestions():
	"""THIS LOOKS LIKE A JOB FOR ME"""
	

today = time.strftime("%Y-%m-%d")
#only opens one file at a time for now
#TODO support multiple file conversion
if len(args) == 2:
	file_name = args[1]
else:
	print "Thank you for using the Anki Cloze Maker!"
	file_name = raw_input("What should be opened? ")

file_to_open = open(file_name, 'r')

text_lines = file_to_open.readlines()

file_name_mod = file_name.split("_")
file_name_mod.pop(0)
file_name_mod = "_".join(file_name_mod)
if "." in file_name_mod:
	#removes the extension
	file_name_mod = file_name_mod[:file_name_mod.index(".")]

csv_cloze_name = today + "_" + file_name_mod + "_notes_cloze" + ".csv"

if os.path.isfile(csv_cloze_name):
	os.remove(csv_cloze_name)

csv_cloze = open(csv_cloze_name, 'w')

csv_cloze.write("tags:" + text_lines[0])



for line in text_lines[1:]:
	if list_questions != []:

		if line[0:3] == "###":
			#evaluate the entire list
			#write into csv_cloze
			print list_questions
			list_questions = []

		elif line[0:2] == "##":
			list_questions.append(line[2:].rstrip())

		else:
			print list_questions
			raise ValueError("can't find the ## sign")

	else:
		line = line.rstrip()
		if line[0:2] == "//":
		#comment
			pass
		
		elif line[0:3] == "###":
			list_questions.append(line[3:].rstrip())

		elif line[0:2] == "##":
			raise ValueError("why is there a ## sign")

		elif line:
		#cloze 
			cloze_answers = line.split(ANSWER_SPLITTER)
			lineup = ""
			x = 0
			for i in xrange (len(cloze_answers)):
				if cloze_answers[i][0] == "@":
					x = x + 1
					cloze_answers[i] = cloze_answers[i][1:] #removes @
					cloze_answers[i] = cloze_answers[i].replace(CLOZE_SPLITTER, ANSWER_SPLITTER)
					cloze_answers[i] = r"{{c" + str(x) + r"::" + cloze_answers[i] + r"}}" #adds cloze wrapper
				if i != 0:
					cloze_answers[i] = " " + cloze_answers[i]
			for i in xrange (len(cloze_answers)):
				lineup = lineup + cloze_answers[i]
			lineup = lineup + "\n"
			csv_cloze.write(lineup)


file_to_open.close()

csv_cloze.close()

print "Note-making complete! This program may now be closed."
