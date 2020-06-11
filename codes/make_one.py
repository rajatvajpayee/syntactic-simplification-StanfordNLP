## @package make_one
# Function to prepare a unique list of token indexes of simplified sentence obtained from MSD

def make_one(ls):
  """
  Args : 
      ls : 2-D list of token indexes of sentences simp
  Returns:
      A 1D list of indexes of tokens
  """
    temp = ls[0]
    for y in ls[1:]:
        temp.append(y[0])
        temp.append(y[1])
    return(temp) 