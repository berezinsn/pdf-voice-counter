#!/usr/bin/env python3
import PyPDF2
from gtts import gTTS
import os

# TODO: write the pdf file opening function
# TODO: need to change hardcoded input file to a link as a param
file = open('doc-name.pdf', "rb")  # rb means read binary mode

# TODO: count pages from the file
readerObj = PyPDF2.PdfFileReader(file)
outputToVoice = readerObj.numPages

# print(type(outputToVoice))  # debug string

# TODO: Research how to connect voice generator
# gTTS lib is used to include voice gen

# TODO: Connect the generator, say how many pages in PDF
language = 'en'
voice = gTTS(text=("This file contains " + str(outputToVoice) + " pages"), lang=language)
voice.save("page-count.mp3")
play = "page-count.mp3"
os.system("afplay " + play)  # afplay used for Mac only
