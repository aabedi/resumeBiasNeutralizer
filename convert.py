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


scl1 = ['ABA Legal Opportunity Scholarship Fund', 'ACS Scholars Program', 'Advisors of American Scholarship', 'AGI Minority Geoscience Student Scholarship', 'AIChE Minority Scholarship Award', 'AICPA Scholarship', 'Allison E. Fisher Scholarship', 'Alphonso Deal Scholarship Award', 'American Dental Association Scholarships', 'Anthony A. Welmas Scholarship', 'APALA Scholarship', 'Arizona Public Service Navajo Scholars Program', 'Asian Pacific Islander Organization Scholarships', 'Blacks at Microsoft Scholarship', 'Boeing IET Minority Enhancement Scholarship', 'Carole Simpson Scholarship', "Denny's Hungry for Education Scholarship", 'Diamond Wipes Scholarship', 'Dowers Family Scholarship',
'Erie Insurance Scholarship', 'Esperanza Scholarship', 'Eugene Moore Memorial Scholarships', 'Frederick and Demi Seguritan Scholarship', 'Gamma Mu Foundation Scholarship', 'Gates Millennium Scholars Program', 'GE Funds LULAC Scholarship Program', 'Generation Google Scholarship', 'Golden Gate Section Scholarship of the Society of Women Engineers', 'Google Anita Borg Memorial Scholarship', 'Harriet Evelyn Wallace Scholarship', 'Hawaii Community Foundation Scholarships', 'Hsiao Memorial Economics Scholarship', 'Institute of Management Accountants Scholarship', 'Irene and Daisy MacGregor Memorial Scholarship', 'Islamic Scholarship Fund Scholarships', 'Jack Tuckfield Memorial Graduate Business Scholarship Fund', 'Japanese American Citizen League Scholarships', "Jeannette Rankin Women's Scholarship Fund", 'Judy Mann DiStefano Memorial Scholarship', 'Kay Longcope Scholarship Program', 'Lapiz Family Scholarship', 'League Foundation Student Scholarship', 'LGBT Heart Scholarship', 'MALDEF Law School Scholarship',
'Margaret R. Brewster Scholarship', 'Maria Elena Yuchengco Memorial Journalism Scholarship', 'Marsha D. Roberts Scholarship', 'Martin Luther King Jr. Scholarship Program', 'Michael Jackson Scholarship for the Communication Arts', 'Minorities in Government Finance Scholarship', 'Minorities in Government Scholarship', 'Minority Teacher Education Scholarship', 'MnACC Student of Color Scholarship', 'Monsignor Philip Kenney Scholarship', 'Mothers Pursuing Dreams', 'Mutual of Omaha Actuarial Scholarship for Minority Students', 'NACME Scholarships', 'Nashville Alumni Chapter of Kappa Alpha Psi Fraternity, Inc. Scholarship', 'National Association of Hispanic Journalists Scholarship', 'Palantir Scholarship for Women in Technology', 'PFLAG National Scholarship', 'Point Foundation Scholarships', 'Pride Foundation Scholarships', 'Quincy Sharpe Mills Scholarships', 'Rising Star Scholarship', 'Samuel Schulman Memorial Scholarship', 'Sia Yang Memorial Scholarship', 'Simmons Scholarship for Unitarian Universalist Women', 'Sisters in Solidary to Educate, Respond and Serve Scholarship',
'Society of Women Engineers Lehigh Valley Section Scholarship', 'Sophie Greenstadt Scholarship for Mid-Life Women', 'South Asian Journalist Association Scholarship', 'South Ohio Science Fair Scholarship', 'Sovereign Nations Scholarship Fund', 'TCU Scholarship Program', 'Tony and Cindi Williams Political Science Scholarship', 'United Way EMS Minority Scholarship', 'University of Connecticut Actuarial Diversity Scholarship', 'Vine Deloria Jr. Memorial Scholarship', 'Wally Davis Scholarship', 'Whitney M. Young, Jr. Memorial Scholarship', 'William Randolph Hearst Scholarship for Minorities', 'William Randolph Hearst Scholarship for Minorities', 'Worldstudio Foundation AIGA Scholarships']


women = ["girl's", "girl", "women", "women's", "grace hopper", "ghc", "girls who code"]

minority = ["minority", "hispanic", "black", "asian", "indian", "native american", "pacific islander", "middle eastern", "african american", "lgbtq", "lgbt", "lgb", "queer", "glaad", "black student union", "national society of black engineers", "society of hispanic professional engineers", "women in computing", "society of asian scientists and engineers",
"nsbe", "sase", "shpe", "society of women in engineering", "swe" ]

scl2 = ["O Wines Opportunity for Success Scholarship", "Gals Go Fish Scholarship","Slaymaker- Kinsey Academic Achievement Award","Citizens Bank Womens Athletic Scholarship","Association for Women in Sports Media Intern/Scholarship","Women and Leadership Program, Panama City","P.E.O. Program for Continuing Education","Lifetime Adoption Foundation Scholarship","Madeline P. Peterson Scholarship for American Indian Women","Burlingame/Gerrity Horticultural Therapy Scholarship", "Women in Wireless Communications Scholarship", "Anarcha, Betsy, and Lucy Memorial Scholarship Award", "O Wines Opportunity for Success Scholarship"]




skillsDict = {'sqlite': '', 'linux': '', 'node.js': '', 'objective-c': '', 'mysql': '', 'angular js': '', 'java': '', 'opengl': '', 'ruby': '',
'unix': '', 'shell script': '', 'heroku': '', 'perl': '', 'c#': '', 'unity': '', 'html': '', 'matlab': '', 'android': '', 'css3': '', 'python': '',
'mongodb': '', 'javascript': '', 'aws': '', 'ajax': '', 'php': '', 'swift': '', 'jquery': '', 'c': '', 'express.js': '', 'windows': '',
'ruby on rails': '', 'c++': '', 'r': '', 'html/css': '', 'azure': ''}
