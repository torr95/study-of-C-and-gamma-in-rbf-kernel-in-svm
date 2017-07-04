def classify(features_train, labels_train):
    from sklearn.svm import SVC
    clf= SVC(kernel="linear",C=0.1/1/10/100/1000/10000)
    clf=clf.fit(features_train, labels_train)
    
    
    return clf
