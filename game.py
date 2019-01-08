'''

Game runtime 
- 1. config from yaml or json: 
- 2. Types of game: 
    - Interactive
    - Quiz
- 3. Select words based on 
        - random (query can be a join - like select  random words where toughIndex is low or frequency is high)
        - frequency
        - toughIndex
        - partsofspeech
        - meaning

'''

from word import get_wordpairs_from_file
from cass_db_talker import CassandraConnection, get_wordpairs_from_db, update_word_toughness_freq




#ToDo: import 'difflib' to accept close matches
def compare_text(first,second):
    ''' works for unicode chars too'''
    return first.casefold().strip() == second.casefold().strip()

# interactive mode - choose "german" or "english"
def interactive_console_app(num_of_questions=10,guess="german"):
    # runtime_wordlist = get_wordpairs_from_file(num_of_questions)

    runtime_wordlist = get_wordpairs_from_db(num_of_questions)

    question_number = 0
    results = {}
    if(compare_text(guess,"german")):
        for word in runtime_wordlist:
            question_number = question_number+1    
            print("{0}: {1}".format(question_number,word.english),end=" ")
            answer = str(input(" = "))
            # compare with nearest matches
            if(compare_text(word.german, answer)):
                results[word.german]=1
            elif (compare_text(answer, "")):
                results[word.german] = 0
                print("pass: {0}".format(word.german)) 
            else:
                results[word.german]=-1
                print("correct ans:{0}".format(word.german))  
    else:
        for word in runtime_wordlist:
            question_number = question_number+1    
            print("{0}: {1}".format(question_number,word.german),end=" ")
            answer = str(input(" = "))
            if (compare_text(word.english,answer)):
                results[word.german]= 1
            elif compare_text(answer,""):
                results[word.german] = 0
                print("pass: {0}".format(word.english)) 
            else:
                results[word.german]= -1
                print("correct ans:{0}".format(word.english))  
    report_card_app(results)


# conduct the game as a quiz & evaluate


''' ToDo: Needs improvement w.r.t report card & two way quiz'''
def run_quiz_app(num_of_questions = 10, guess="german"):

    # runtime_wordlist = get_wordpairs_from_file(num_of_questions)
    runtime_wordlist = get_wordpairs_from_db(num_of_questions)

    question_number = 0    
    # current_dictionary={}
    results = {}
    if(compare_text(guess,"german")):
        for word in runtime_wordlist:
            question_number = question_number+1
            
            print("{0}: {1}".format(question_number,word.english),end=" ")

            answer = str(input(" = "))
            #ToDo: write a method to compare with nearest matches
            if compare_text(word.german, answer):
                # results["rights"].append(word.german)
                results[word.german]= 1
            elif compare_text(answer,""):
                results[word.german] = 0
                print("pass: {0}".format(word.german)) 
            else:
                results[word.german]= -1
                print("correct ans: {0}".format(word.german)) 
    else:
        for word in runtime_wordlist:
            question_number = question_number+1
            
            print("{0}: {1}".format(question_number,word.german),end=" ")

            answer = str(input(" = "))
            #ToDo: write a method to compare with nearest matches
            if compare_text(word.english, answer):
                # results["rights"].append(word.german)
                results[word.german]= 1
            elif compare_text(answer,""):
                results[word.german] = 0
                print("pass: {0}".format(word.english)) 
            else:
                results[word.german]= -1
                print("correct ans: {0}".format(word.english)) 

    report_card_app(results)

def report_card_app(results):
    '''
    displays results & writes back to db for analytics
    '''

    wrongs = [i for i in results.values() if i==-1]
    print("wrong answers:{0}/{1}".format(len(wrongs),len(results)))
    update_word_toughness_freq(results)


if __name__ == "__main__":
    interactive_console_app(3,"english")
    # run_quiz_app(3,"german")
    # print(compare_text("baße ","Basse"))