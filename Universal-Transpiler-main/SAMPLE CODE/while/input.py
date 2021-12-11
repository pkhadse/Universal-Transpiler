print "How many fibonacci numbers do you want?"
input nums

float a = 0
float b = 1
while nums > 0:
    print a
    float c = a + b
    a = b
    b = c
    nums = nums - 1



