def solution(arr, flag):
    X = []
    
    for i in range(len(arr)):
        arr_i = arr[i]
        if flag[i]:
            X += [arr_i] * arr_i * 2
        else:
            X = X[:len(X) - arr_i]
        
    return X
