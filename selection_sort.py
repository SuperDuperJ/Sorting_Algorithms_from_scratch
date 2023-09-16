def minimum_index(X):
    """
    in: list X of orderable elements
    out: the index of the smallest element in X
    """
    min_index=0
    for i in range(len(X)):
        if X[i]<X[min_index]:
            min_index=i
    return min_index

def selection_sort(X):
    for i in range(len(X)-1):
        min_index=minimum_index(X[i:])+i
        X[i], X[min_index] = X[min_index], X[i]
    return X


