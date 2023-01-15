######## Probability of landing a coin heads n times in a row out of n tosses
def head_tails(p, n):
    probability = p**n
    return probability


p = 0.5
n = 500

print(head_tails(p, n))