import spacy
from spacy import displacy

nlp = spacy.load('en_core_web_lg')

doc = nlp('I am flying to Manila.')
for token in doc:
    print(token.text)
print('='*30)

doc = nlp('this product integrates both libraries for downloading and applying patches')
for token in doc:
    print(token.text, token.lemma_)
print('='*30)

doc = nlp('I have flown to Singapore. I am flying to Manila.')
for token in doc:
    print(token.text, token.pos_, token.tag_)
print('='*30)

print(spacy.explain('AUX'))
print(spacy.explain('VBG'))
print('='*30)

print([w.text for w in doc if w.tag_=='VBG' or w.tag_=='VB'])
print('='*30)

for sent in doc.sents:
    print([sent[i] for i in range(len(sent))])
print('='*30)

doc = nlp('The Golden Gate Bridge is an iconic landmark in San Francisco.')
print([w.text for w in doc])
print('='*30)

with doc.retokenize() as retokenizer:
    retokenizer.merge(doc[1:4])
with doc.retokenize() as retokenizer:
    retokenizer.merge(doc[7:9])
for token in doc:
    print(token.text, token.lemma_, token.pos_)
print('='*30)

doc = nlp('I want a green apple.')
for token in doc:
    print(token.text, token.pos_, token.dep_, spacy.explain(token.dep_))
print('='*30)

doc = nlp('The firm earned $1.5 million in 2017.')
displacy.serve(doc, style='dep')