
def backward(s,i=0):
    if i < len(s):
        print(s[0:i+1])
        backward(s,i+1)


# backward('abcdef')



def forward(s,j=0):
    if j > -len(s):
        print(s[j-1:])
        forward(s,j-1)

forward('abcdef')