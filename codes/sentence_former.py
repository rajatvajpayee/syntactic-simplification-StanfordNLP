## @package sentence_former
# Main function to join the simplified tokens according to the given conditions to make simple sentences

def sentence_former(tokens ,parsed ,rem_dep):
    """
    Args : 
        1. tokens : Tokens of a sentence
        2. parsed : Dependencies obtained from dependency parser
        3. rem_dep : dependencies which do not effect meaning of simple sentence

    Returns:
        A list of simple sentences 
    """
    sentences = []
    dependencies = [x for x in parsed if x[0] not in rem_dep]
    pos_nsubjs = [[x[1],x[2]] for i,x in enumerate(dependencies) if x[0] == 'nsubj' or x[0] == 'nsubjpass']
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