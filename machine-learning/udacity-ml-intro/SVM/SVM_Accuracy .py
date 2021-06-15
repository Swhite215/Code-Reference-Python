def SVM_Accuracy(features_train, labels_train, features_test, labels_test):
    # import the sklearn module for SVM - Support Vector Classifier
    from sklearn.svm import SVC
    from sklearn.metrics import accuracy_score

    # create classifier
    clf = SVC(kernel="linear") # can change type of kernel here

    # fit the classifier on the training features and labels
    clf.fit(features_train, labels_train)
    
    # make prediction
    pred = clf.predict(features_test)

    # calculate and return accuracy
    accuracy = accuracy_score(pred, labels_test)

    return accuracy

