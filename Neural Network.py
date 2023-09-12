x1=eval(input("Enter First Number"))
x2=eval(input("Enter Second Number"))
w11=0.4
w12=0.45
w21=0.8
w22=0.9
w01=0.6
w02=0.7
def sigmoid(a):
    return(1/(1+2.71**(0-a)))
h1=w11*x1 + w21*x2
h2=w12*x1 + w22*x2
z1=sigmoid(h1)
print(z1)
z2=sigmoid(h2)
print(z2)
o1=w01*z1 + w02*z2
print(sigmoid(o1))