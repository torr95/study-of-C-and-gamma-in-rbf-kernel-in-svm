def classify(features_train, labels_train):   
    from sklearn.svm import SVC
    clf= SVC(kernel="rbf",C=100,gamma=1/10/100/1000)
    clf=clf.fit(features_train, labels_train)
    
    
    return clf
    
    
