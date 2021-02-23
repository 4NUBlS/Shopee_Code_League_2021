import spacy
nlp = spacy.load('en_core_web_lg')
doc = nlp('I am flying to Manila.')
print([w.text for w in doc])
