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

                };

majorDict = {
                'Finance': 0,


                };


biasDict = {'fatherhood': 'parenthood', 'goddess': 'god', 'manhandle': 'rough up', 'hostess': 'host', 'manlike': 'humanlike', 'mankind': 'humankind', 'maintenance man': 'janitor', 'flagman': 'flagger', 'copy girl': 'copy clerk',
 'to a man': 'to a person', 'spaceman': 'astronaut', 'masterpiece': 'great work of art', 'lookout man': 'lookout', "gentlemen's agreement": 'unwritten agreement', 'journeyman': 'experienced tradesperson', 'ranchman': 'rancher', 'elder statesman': 'senior statesperson', "master's degree": 'graduate degree', 'temptress': 'tempter',
  'newsman': 'reporter', 'enlisted man': 'enlistee', 'young man': 'youth', 'number-two-man': 'second in command', 'mother country': 'homeland', 'housewife': 'homemaker', 'spokeswoman': 'spokesperson', 'Englishman': 'Englander', 'prodigal son': 'returning child', 'medicine man': 'spirit healer',
   'man of letters': 'scholar', 'toastmistress': 'toast maker', 'manhole': 'utility access hole', 'cowgirl': 'cowhand', 'councilman': 'council member', 'manageress': 'manager', 'johnny-come-lately': 'newcomer', 'craftsman': 'artisan', 'lineman': 'football player', 'mechanical man': 'robot',
   'maiden name': 'family name', 'choir girl': 'choir member', 'odd-man-out': 'person not included', 'outdoorsman': 'outdoors person', 'man about town': 'bon vivant', 'tribesman': 'tribe member', 'stewardess': 'flight attendant', 'bridesmaid': "bride's attendant", 'headmaster': 'principal', 'governess': 'child caretaker',
   'forefathers': 'ancestors', "king's ransom": 'valuable', 'legman': 'runner', 'Renaissance man': 'Renaissance person', 'bondsman': 'bondsperson', 'manpower': 'workers', 'chorus girl': 'chorus member', 'man': 'operate', 'fireman': 'firefighter', 'cabin boy': 'cabin attendant',
    'murderess': 'murderer', 'lumberjack': 'logger', 'yes-man': 'avid follower', 'patrolman': 'police officer', 'Mother Earth': 'earth', 'heiress': 'heir', 'heroine': 'hero', 'man-sized': 'large', 'pressman': 'press operator', 'flyboy': 'pilot',
     'mailman': 'letter carrier', 'juryman': 'juror', 'oilman': 'oil executive', 'airwoman': 'pilot', 'Scotsman': 'Scot', 'newspaperman': 'reporter', 'paperboy': 'paper carrier', 'funnyman': 'comedian', 'insurance man': 'insurance agent', 'modern man': 'modern people',
     'drum majorette': 'drum major', 'cavemen': 'cave dwellers', 'maiden': 'first', 'priestess': 'priest', 'frog man': 'diver', 'fighting man': 'fighter', 'maid': 'house cleaner', 'waitress': 'server', 'letterman': 'achiever', 'master': 'expert',
      'man of distinction': 'person of distinction', 'learned man': 'learned person', 'starlet': 'star young actor', 'masculine': 'male', 'common man': 'commoner', 'contact man': 'contact person', 'men working': 'people working', 'brew master': 'brew director', 'Norseman': 'Norse person', 'master plan': 'main plan',
      'anchorwoman': 'anchor', 'publicity man': 'publicist', 'brotherly': 'kind', 'marked man': 'targeted person', 'mother tongue': 'native language', 'helmsman': 'coxswain', 'longshoreman': 'stevedore', 'triggerman': 'shooter', 'maid-of-honor': 'honored attendant', 'dairyman': 'dairy farmer',
      'Uncle Sam': 'United States', 'doorman': 'doorkeeper', 'fall guy': 'scapegoat', 'Frenchmen': 'French people', 'male nurse': 'nurse', 'marksman': 'sharpshooter', 'forewoman': 'supervisor', 'showman': 'actor', 'statesman': 'senior politician', 'Mother Nature': 'nature',
       'Welshman': 'Welsh person', 'alderman': 'council member/person', 'bus boy': "server's helper", 'organization man': 'team player', 'workman': 'worker', 'businesswoman': 'businessperson', 'meter maid': 'parking enforcement officer', 'majorette': 'drum major', 'crewman': 'crew member', 'newsboy': 'news deliverer',
       'guardsman': 'soldier', 'conductress': 'conductor', 'pitchman': 'promoter', 'straw man': 'test theory', 'matron of honor': 'honored attendant', 'boss lady': 'supervisor', 'infantryman': 'infantry soldier', 'chambermaid': 'housekeeper', 'congressman': 'member of congress', 'chairwoman': 'chair person',
       'weatherman': 'weathercaster', 'clergy women': 'clergy', 'brakeman ': 'brake operator', 'switchman': 'switch operator', 'sorceress': 'sorcerer', 'signalman': 'signaler', 'fatherland': 'homeland', 'prehistoric man': 'prehistoric person', 'sculptress': 'sculptor', 'cattlemen': 'cattle owners',
       'night watchman': 'night security guard', 'horsewoman': 'rider', 'alumna': 'graduates', 'manmade': 'hand made', 'shipmaster': 'captain', 'idea man': 'idea person', 'motherhood': 'parenthood', 'favorite son': 'favorite candidate', 'deliveryman': 'deliverer', 'grandfather clause': 'pre-existing condition',
       'countryman': 'compatriot', 'blind man': 'blind person', 'man of the year': 'newsmaker of the year', "old wives' tale": 'superstition', 'midshipman': 'sailor', 'middleman': 'go-between', 'office boy': 'messenger', 'rifleman': 'shooter', 'layman': 'layperson', 'brakeman': "conductor's assistant",
       'song-and-dance-man': 'singer and dancer', 'snowman': 'snow person', 'man of the house': 'husband', 'mother lode': 'main vein', 'king-size': 'huge', 'taskmaster': 'supervisor', 'henchman': 'partner in crime', 'showmanship': 'stage presence', 'radioman': 'radio broadcaster', 'Miss': 'Ms.',
       'seductress': 'seducer', 'seamstress': 'tailor', 'penmanship': 'handwriting', "workmen's compensation": "workers' compensation", 'nobleman': 'noble person', 'sportsmanlike': 'sporting', 'Irishmen': 'Irish people', 'founding father': 'founder', 'front man': 'representative', 'freshman': 'first year students',
       'masseuse': 'massage therapist', 'postmistress': 'postal worker', 'man on the street': 'average person', 'serviceman': 'maintenance person', 'headman': 'boss', 'gamesmanship': 'game playing', 'actress': 'actor', 'jazz man': 'jazz player', 'fraternal twins': 'non-identical twins', 'man among men': 'outstanding person',
       'bagboy': 'bagger', 'master key': 'passkey', 'right-hand man': 'main assistant', 'Dutchman': 'Dutch person', 'key man': 'key person', 'man-eater': 'flesh eater', 'repairman': 'repairer', 'seaman': 'sailor', 'gateman': 'gate keeper', 'playboy': 'pleasure seeker',
       'career woman': 'career professional', 'assemblyman': 'assemblyperson', 'gunman': 'shooter', 'man-hours': 'work hours', 'comedienne': 'comedian', 'saleslady': 'sales person', 'brethren': 'laity', 'brotherhood': 'fellowship', 'brotherly love': 'charity', 'watchman': 'security guard',
        'handyman': 'maintenance person', 'man of action': 'go-getter', 'oarsman': 'rower', 'camerawoman': 'camera operator', 'masterful': 'skillful', 'airline stewardess': 'flight attendant', "man's work": 'work', 'John Q. Public': 'the public', 'johnny-on-the-spot': 'prompt person', 'man-to-man': 'face-to-face',
        'coed': 'student', 'inside man': 'insider', 'number-one-man': 'head', 'workmanlike': 'skillful', 'trash man': 'trash collector', 'sister ship': 'partner ship', 'postman': 'letter carrier', 'weak sister': 'weak', 'girl Friday': 'aide', 'confidence man': 'swindler',
        'Mrs. ': 'Ms.', 'jack-of-all-trades': 'handyperson', "man's best friend": 'dog', 'city fathers': 'city leaders', 'songstress': 'singer', 'floor man': 'floorwalker', "no-man's-land": 'uninhabited land', 'usherette': 'usher'}

skillsDict = {'sqlite': '', 'linux': '', 'node.js': '', 'objective-c': '', 'mysql': '', 'angular js': '', 'java': '', 'opengl': '', 'ruby': '',
'unix': '', 'shell script': '', 'heroku': '', 'perl': '', 'c#': '', 'unity': '', 'html': '', 'matlab': '', 'android': '', 'css3': '', 'python': '',
'mongodb': '', 'javascript': '', 'aws': '', 'ajax': '', 'php': '', 'swift': '', 'jquery': '', 'c': '', 'express.js': '', 'windows': '',
'ruby on rails': '', 'c++': '', 'r': '', 'html/css': '', 'azure': ''}
