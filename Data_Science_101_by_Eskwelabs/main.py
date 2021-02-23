import spacy
from spacy import displacy
from IPython.core.display import display, HTML

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
phrase = ''
for token in doc:
    if token.tag_ == '$':
        phrase = token.text
        i = token.i+1
        while doc[i].tag_ == 'CD':
            phrase += doc[i].text + ''
            i += 1
        phrase = phrase[:-1]
        print(phrase)
print('='*30)

print(spacy.explain('CD'))
print('='*30)

doc = nlp('I want to fly to Manila.')
html = displacy.render(doc, style='ent', page=True)
display(HTML(html))
print('='*30)

print(spacy.explain('GPE'))
print(spacy.explain('ORG'))
print(nlp('apple').similarity(nlp('banana')))
print(nlp('king').similarity(nlp('queen')))
print('='*30)

displacy.serve(doc, style='dep')