def classify(features_train, labels_train):
    # import the sklearn module for SVM - Support Vector Classifier
    from sklearn.svm import SVC

    # create classifier
    clf = SVC(kernel="linear") # can change type of kernel here

    # fit the classifier on the training features and labels
    clf.fit(features_train, labels_train)
    
    return clf

