def product(inputs):
    for i in range(len(inputs)):
        for j in range(len(inputs)):
            if(i!=j):
                reqprod = inputs[i]*inputs[j]
                if(reqprod%2 < 2):
                    print(inputs[i], inputs[j])
set1 = [1, 6, 5, 7, 3]
product(set1)