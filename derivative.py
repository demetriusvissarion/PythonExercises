######### Calculate the first derivative of f(x)=w1*x^3+w2*x^2+1
def derivative(w1, w2, x):
    if x == 0:
        return w2
    else:
        return 3 * w1 * x ** 2 + w2


print(derivative(1, 2, 3))