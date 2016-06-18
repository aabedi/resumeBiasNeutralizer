from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
import unicodedata, codecs
from cStringIO import StringIO
import os
import json

def getPDFText(pdfFilenamePath):
    retstr = StringIO()
    parser = PDFParser(open(pdfFilenamePath,'r'))
    try:
        document = PDFDocument(parser)
    except Exception as e:
        print(pdfFilenamePath,'is not a readable pdf')
        return ''
    if document.is_extractable:
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr,retstr, codec='ascii' , laparams = LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(document):
            interpreter.process_page(page)
        return retstr.getvalue()
    else:
        print(pdfFilenamePath,"Warning: could not extract text from pdf file.")
        return ''

def mapColleges(text_file):
    text_file = text_file.split(',')
    return (text_file[1], text_file[2])

def getUniversities():
    universities = {}
    collegeFile = open('resources/collegeRank.txt', 'r')
    for line in collegeFile:
        line = line.lower()
        pair = mapColleges(line)
        universities[pair[1]] = pair[0]
    return universities

companyDict = {
                'goldman sachs': 10,
                'morgan stanley': 10,
                'jp morgan': 10,
                'jp': 10,
                'blackstone': 9,
                'bloomberg': 8,
                'credit suisse': 7,
                'barclays': 7,
                'mckinsey': 10,
                'boston consulting group': 10,
                'bain company': 10,
                'pricewaterhouseCoopers advisory': 8,
                'deloitte': 7,
                'accenture': 7,
                'kpmg': 7,
                'palantir': 10,
                'uber': 10,
                'airbnb': 10,
                'google': 10,
                'microsoft': 9,
                'apple': 9,
                'facebook': 10,
                'amazon': 9,
                'pinterest': 9,
                'tesla': 9,
                'spacex': 9,
                'square': 9,
                'intel': 8,
                'yahoo': 8,
                'yahoo!': 8,
                'twilio': 8,
                'yelp': 8,
                'paypal': 7,
                'disney': 8,
                'pebble': 7,
                'northrup grumman': 8,
                'lockheed martin': 8
                };

majorDict = {
                'Finance': 0,
                'Business': 0,
                'Economics': 0,
                'Management': 0,
                'Economics': 0,
                'Accounting': 0,
                'Biology': 'STEM',
                'Physics': 'STEM',
                'Chemistry': 'STEM',
                'Math': 'STEM',
                'Computer Science': 'STEM',
                'Computer Engineering': 'STEM',
                'Software Engineering': 'STEM',
                'Mechanical Engineering': 'STEM',
                'Electrical Engineering': 'STEM',
                'Biomedical Engineering': 'STEM',
                'Chemical Engineering': 'STEM',

                };

skillsDict = {'sqlite': '', 'linux': '', 'node.js': '', 'objective-c': '', 'mysql': '', 'angular js': '', 'java': '', 'opengl': '', 'ruby': '',
'unix': '', 'shell script': '', 'heroku': '', 'perl': '', 'c#': '', 'unity': '', 'html': '', 'matlab': '', 'android': '', 'css3': '', 'python': '',
'mongodb': '', 'javascript': '', 'aws': '', 'ajax': '', 'php': '', 'swift': '', 'jquery': '', 'c': '', 'express.js': '', 'windows': '',
'ruby on rails': '', 'c++': '', 'r': '', 'html/css': '', 'azure': ''}
