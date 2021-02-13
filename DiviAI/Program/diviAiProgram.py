import spacy
import csv
import pandas as pd
import json

frame = pd.read_csv("aapl-10k.txt", delimiter= "\t")
frame.to_csv("aapl-10k.csv", encoding='utf-8', index=False)

with open("aapl-10k.csv", "r", encoding = 'utf-8') as file:
    file_reader = csv.reader(file)
    info = [row for row in file_reader]
    for row in info:
        row[1] = row[1].split('.')
        row[1].pop()
    for i in range(0, len(info)):
        info[i] = [info[i][0]] + info[i][1]

nlp = spacy.load("en_core_web_sm")
    
for record in info:
    header = nlp(record[0])    
    for phrases in record[1:]:
        sentence = nlp(phrases)   
        if len(sentence.ents) > 0:
            data = {str(header) : {"text" : str(sentence), "entities" : [{"text" : word.text , "start" : word.start_char , "end" : word.end_char , "label" : word.label_} for word in sentence.ents]}}
            with open('result.txt', 'a') as result:
                json.dump(data, result, indent = 4) 


            
            
                


        

        
            






