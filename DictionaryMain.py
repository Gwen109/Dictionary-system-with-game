from bs4 import BeautifulSoup #parsing(converting to python format) 
import requests #module for sending http request
import time
import pandas as pd
import playsound

global Tim
 
#SEARCHING THE WORD
def dic(Tim):
    global  m,word
    word=input("\nEnter the word: ")
#scraping english meaning
    url='https://www.oxfordlearnersdictionaries.com/definition/english/'+str(word)+'?q='+str(word)
    page=requests.get(url)#getting the content of the url
    soup=BeautifulSoup(page.text,'html.parser') #parsing(converting to python format)
    m=soup.find('span',attrs={'class':'def'}) # find where <span> is there with class name as 'def' and get the information(data) given inside that <span> 
    e=soup.find('span',attrs={'class':'x'})

    try:
        print("\nMEANING: ",m.get_text())
        
    except:
        playsound.playsound('incorrect.mp3')
        print("Ooops !! Incorrect spelling , Plz check :)")
        time.sleep(2)
        dic(Tim)
    
    try:
        print("\nEXAMPLE: ",e.get_text())
    except:
        print("")
    Tim=False

print("WELCOME TO LEARN WORDS ^_^")
playsound.playsound("welcome.mp3")
wish=int(input("Dictionary=1\nGuessMeGame=2\nFindMeGame=3\nGiveMeExamplesGame=4\nENTER UR CHOICE: "))
Tim=True
if wish==1:
    playsound.playsound('enterword.mp3')
    if Tim:
        dic(Tim)
#storing it in csv file
    existingwords=pd.read_csv('dictionary.csv',usecols=['WORD'])
    data=[word,m.get_text()]
    r=pd.DataFrame([data])
    if word in list(existingwords['WORD']):
        playsound.playsound('already.mp3')
        print('\nThe word was searched already,seems that you gorget the meaning :( Its ok ,learn it this time ')
    else:
        with open('dictionary.csv','a') as f:
            r.to_csv('dictionary.csv',mode='a',header=False,index=False)
        playsound.playsound('newword1.mp3')
        print("\nHurray!! We've learnt a new word today :) ")

#GuessMeGame
elif wish==2:
    playsound.playsound('guessme.mp3')
    print("Press 'q' to exit ..Lets Begin ^_^")
    score=0
    existingwords=pd.read_csv('dictionary.csv',usecols=['WORD'])
    allmeanings=list(pd.read_csv('dictionary.csv',usecols=['MEANING'])['MEANING'])
    
    for i in list(existingwords['WORD']):
        indexw=list(existingwords['WORD']).index(i)
        print("\n WORD: "+i)
        print('guess the meaning :).......')
        response=input('wanna confirm ? press [y/n] :')
        if response=='y':
            print('lets see ...\n\n'+allmeanings[indexw])
            point=input('Was it correct ? press[y/n] :')
            if point=="y":
                score=score+1
            playsound.playsound('nextword.mp3')
            print("Lets go for next word")
            print("____________________________")    
            
                
        elif response=='n':
            playsound.playsound('awesome.mp3')
            print("Awesome! u learnt it :)")
            score=score+1
            playsound.playsound('nextword.mp3')
            print("Lets go for next word")
            print("____________________________")
        else:
            print("the game is finished in between")
            break
    playsound.playsound('score.mp3')
    print("HERE IS YOUR SCORE :) = "+str(score)+"/"+str(len(list(existingwords['WORD']))))
#FindMeGame
elif wish==3:
    playsound.playsound('findme.mp3')
    print("\nWelcome to FINDME game ^_^\nIf you dont know the word plz press 'n',if want to quit,press'q'\nLets begin....")
    score=0
    existingwords=pd.read_csv('dictionary.csv',usecols=['WORD'])
    for i in list(existingwords['WORD']):
        evenind=0
        print("findme : ",end="")
        while (evenind <len(i)):
            print(i[evenind],end="")
            evenind+=2
        answer=input("\nEnter the word : ")
        if answer == i:
            score+=1
        if answer == 'q':
            break 
    playsound.playsound('score.mp3')
    print("lets check the score :) \n SCORE= "+str(score)+"/"+str(len(list(existingwords['WORD']))))
    
#GiveMeExamplesGame
else:
    playsound.playsound('useme.mp3')
    print("Welcome to EXAMPLES game ^_^ , give an example to the following words,to end the game press'q'")
    print("\nThe existing examples are given below ")
    df=pd.read_csv('examples.csv')
    df.sort_values(by=['WORD'], inplace=True)
    print("\n",df)
    score=0
    existingwords=pd.read_csv('dictionary.csv',usecols=['WORD'])
    #giving example for each word in dictionary
    for i in list(existingwords['WORD']):
        print("\nWord : "+i)
        ex=input("EXAMPLE : ")
        if ex!='q':
            data=[i,ex]
            r=pd.DataFrame([data])
            with open('examples.csv','a') as f:
                r.to_csv('examples.csv',mode='a',header=False,index=False)
            score+=1
        if ex=='q':
            break
    playsound.playsound('score.mp3')
    print("lets check the score :) \n SCORE= "+str(score))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
