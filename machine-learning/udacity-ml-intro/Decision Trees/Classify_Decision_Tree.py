def classify(features_train, labels_train):
    # import the sklearn module for tree
    from sklearn import tree

    # create classifier
    clf = tree.DecisionTreeClassifier() # can change type of kernel here

    # fit the classifier on the training features and labels
    clf.fit(features_train, labels_train)
    
    return clf

