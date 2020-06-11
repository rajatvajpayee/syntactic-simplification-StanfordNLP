import json
try:
    from stanfordcorenlp import StanfordCoreNLP
except:
    print('Install stanfordcorenlp !!!')
from time import time

props = {'annotators': 'coref', 'pipelineLanguage': 'en'}

start = time()
print('>>> Loading ....')
nlp = StanfordCoreNLP(r'stanford-corenlp-full-2018-10-05')
print('>>> Loaded stanford model in {:.2f} seconds'.format(time()-start))


def sentence_former(tokens ,parsed ,rem_dep):
  sentences = []
  dependencies = [x for x in parsed if x[0] not in rem_dep]
  pos_nsubjs = [[x[1],x[2]] for i,x in enumerate(dependencies) if x[0] == 'nsubj' or x[0] == 'nsubjpass']
    
  def find_tails(number,dependencies = dependencies):
    n_ = [[x[1],x[2]] for x in dependencies if x[1]==number]
    return(n_)

  def make_one(ls):
    temp = ls[0]
    for y in ls[1:]:
      temp.append(y[0])
      temp.append(y[1])
    return(temp) 

  for x in pos_nsubjs:
    tail,head = x[0],x[1]
    ls_1 = find_tails(x[0])
    if len(ls_1)!= 0:
      ls_1 = make_one(ls_1)
    
    ls_2 = find_tails(x[1])
    
    if len(ls_2) != 0:
      ls_2 = make_one(ls_2)
    if len(ls_1)!=0 and len(ls_2)==0:
      n_ls_1 = sorted([y for y in {x for x in ls_1}])
      ds_1 = [tokens[int(i)-1] for i in n_ls_1]
      sentences.append(' '.join(ds_1))
    elif len(ls_2)!=0 and len(ls_1)==0:
      n_ls_2 = sorted([y for y in {x for x in ls_2}])
      ds_1 = [tokens[int(i)-1] for i in n_ls_2]
      sentences.append(' '.join(ds_1))
    elif len(ls_2)!=0 and len(ls_1)!=0:
      for x in ls_2:
        ls_1.append(x)
      ds_1 = [y for y in {x for x in ls_1}]
      ds_1 = sorted(ds_1)
      ds_1 = [tokens[int(i)-1] for i in ds_1]
      sentences.append(' '.join(ds_1))

  temp = dependencies[0]
  head_temp = temp[2]
  N_tails_head = find_tails(head_temp)
  nodes = make_one(N_tails_head)
  nodes = sorted([y for y in {x for x in nodes}])
  ds_1 = [tokens[int(i)-1] for i in nodes]
  sentences.append(' '.join(ds_1))
  new_sen = []

  return(sentences)


intt = int(input('Type 0 for default text and 1 for different text : '))
if intt == 0:
  sentence = 'Do not drive faster if objects are closer than 5m.'
else: sentence = input('Enter a text to check : ')
sentences = [sentence]
start = time()
for sentence in sentences:
  print('-----------------------------'*3)
  print('Original Sentence : \n{}'.format(sentence))
  print('-----------------------------'*3)
  rem_dep = ['acl', 'appos', 'advcl', 'cc', 'ccomp', 'conj', 'dep', 'mark', 'parataxis','ref']
  tokens = nlp.word_tokenize(sentence)
  dep_parser = nlp.dependency_parse(sentence)
  
  text = sentence
  result = json.loads(nlp.annotate(text, properties=props))
  arr = [];

  mentions = result['corefs']
  print(dep_parser)
  simpli_sentences =sentence_former(tokens = tokens,parsed = dep_parser,rem_dep = rem_dep) 
  print(simpli_sentences)


print('Time Taken {:.2f} sec'.format(time() - start))


