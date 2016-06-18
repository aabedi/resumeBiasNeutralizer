import convert
import os
import json
import ast
import re
from pymongo import MongoClient

try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse


client = MongoClient()

universities = {}

def parse(fname, lname, text):
    text = text.lower()
    text = text.replace('\n', ' ')
    text = text.replace(',', '')
    text_array = text.split(' ')
    text_array = filter(None, text_array)
    candidate = {}
    candidate['first_name'] = fname
    candidate['last_name'] = lname
    candidate['college'] = parseForEducation(text_array)
    candidate['major'] = parseForMajor(text_array)
    candidate['gpa'] = parseForGPA(text_array)
    candidate['experience'] = parseForExperience(text_array)
    candidate['skills'] = parseForSkills(text_array)
    candidate['score'] = calculateResumeScore(candidate, text)
    print candidate
    return candidate

def parseForEducation(text_array):
    try:
        index_education = text_array.index('education')
        college = ""
        for i in range(index_education + 1 , index_education + 7 + 1):
            college = college + text_array[i] + ' '
            if college[0:len(college)-1] in universities:
                print 'found college: ' +  college[0:len(college)-1]
                return college[0:len(college)-1]
    except ValueError:
        print 'parse for education error'

def minorityScore(text_array):
    score = 0
    txt = text_array.lower()
    for scl in convert.scl1:
        if scl.lower() in txt:
            score += 1
            print(scl)
    for wm in convert.women:
        if wm.lower() in txt:
            score += 1
            print(wm)
    for mn in convert.minority:
        if mn.lower() in txt:
            score +=1
            print(mn)
    for scl in convert.scl1:
        if scl.lower() in txt:
            score +=1
            print(scl)
    print("SCORE IS", score)
    return score


def parseForGPA(text_array):
    try:
        index_GPA = text_array.index('gpa:')
        gpa = ''
        if '/' in text_array[index_GPA + 1]:
            temp = text_array[index_GPA + 1]
            print temp[0:temp.index('/')]
            return temp[0:temp.index('/')]
        print text_array[index_GPA + 1]
        return text_array[index_GPA + 1]
    except ValueError:
        print 'parsing for gpa error'
        return None

def parseForMajor(text_array):
    try:
        for word in text_array:
            if word in convert.majorDict:
                print word
                return word
            elif word == 'computer':
                index = text_array.index(word)
                print word  + ' ' + text_array[index+1]
                return word + ' ' + text_array[index+1]
            elif word == 'engineering':
                index = text_array.index(word)
                if len(text_array[index - 1]) > 5:
                    print text_array[index - 1] + ' ' + word
                    return text_array[index - 1] + ' ' + word
    except ValueError:
        print 'parse for major error'

def parseForExperience(text_array):
    try:
        for word in text_array:
            if word in convert.skillsDict:
                print word
                return word
    except ValueError:
        print 'parse for Experience error'



# def parseForSkills(text_array):
def parseForSkills(text_array):
    skills = []
    for word in text_array:
        if word in convert.skillsDict:
            skills.append(word)
    print 'skills : ' + str(skills)
    return skills

def calculateResumeScore(candidate, text_array):
    schoolScore = ((280-int(universities.get(candidate['college'])))/280)*25
    if candidate['gpa'] != None:
        gpaScore = (float(candidate['gpa'])/4.0)*25
    else:
        gpaScore = 0
    try:
        expScore = ((convert.companyDict.get(candidate['experience']))/10)*25
    except:
        expScore = 0
    skillsScore = 25
    ms = minorityScore(text_array)*10
    score = (schoolScore) + (gpaScore) + (skillsScore) + (expScore) + ms
    return score

if __name__ == '__main__':
    universities = convert.getUniversities()
    list_files = os.listdir('pdf_files')
    list_json = []
    for fp in list_files:
        data = {}
        if(fp != '.DS_Store'):
            data['name'] = fp;
            data['text'] = convert.getPDFText('pdf_files/' + fp);
            json_data = json.dumps(data)
            list_json.append(json_data)

    for resume in list_json:
        resume_dict = ast.literal_eval(resume)
        fullName = resume_dict['name']
        fname = fullName[0:fullName.index('_')]
        lname = fullName[fullName.index('_') + 1: len(fullName)-4] # - 4 for .pdf
        print 'parsing ' + fname + ' ' + lname + '\'s resume'
        candidate = parse(fname, lname, resume_dict['text'])

        client = MongoClient('mongodb://user:password@ds019054.mlab.com:19054/biasneutralizer')
        db = client.biasneutralizer
        db = client['biasneutralizer']
        # print(candidate)
        # db.Candidate.ensureIndex({ first_name: 1, last_name: 1}, {unique:true})
        result = db.Candidate.insert_one(candidate)

    # topCandidates = db.Candidate.find()._addSpecial({ score: -1 })
    # db.collection.find()._addSpecial( "$orderby", { age : -1 } )
    # print(topCandidates)
        # from above: .inserted_id
        # result = db.Candidate.update(candidate)
        # print(db.inventory.find( { type: "first_name" } ))
