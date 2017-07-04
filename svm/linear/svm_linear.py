def classify(features_train, labels_train):   
    from sklearn.svm import SVC
    clf= SVC(kernel="linear")
    clf=clf.fit(features_train, labels_train)
    
    return clf
    
    
