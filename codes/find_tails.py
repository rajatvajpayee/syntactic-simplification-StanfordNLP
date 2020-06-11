## @package find_tails
# Function to find out all the tokens which have same tail index numbers

def find_tails(number,dependencies):
    """
    Args : 
        1. number : Index number 
        2. dependencies : List of all tokens with their index numbers
    
    Returns:
        A 2D list of tokens with same tail index
    """ 
    n_ = [[x[1],x[2]] for x in dependencies if x[1]==number]
    return(n_)