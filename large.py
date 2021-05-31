import numpy as np
def multmatrix():
    
    X = np.random.rand(1000,1000)
    Y = np.random.rand(1000,1000)
    result = np.zeros((1000,1000))
    for i in range(len(X)):
   # iterate through columns of Y
        for j in range(len(Y[0])):
       # iterate through rows of Y
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]
                

    for r in result:
        print(r)

if __name__ == "__main__":
    #solver()
    multmatrix()