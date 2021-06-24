def DT_accuracy(features_train, labels_train, features_test, labels_test):
    # import the sklearn module for tree
    from sklearn import tree
    from sklearn.metrics import accuracy_score

    # create classifier
    clfTwo = tree.DecisionTreeClassifier(min_samples_split=2)
    clfFifty = tree.DecisionTreeClassifier(min_samples_split=50)

    # fit the classifier on the training features and labels
    clfTwo.fit(features_train, labels_train)
    clfFifty.fit(features_train, labels_train)

    # make predictions
    predTwo = clfTwo.predict(features_test)
    predFifty = clfFifty.predict(features_test)

    acc_min_samples_split_2 = accuracy_score(predTwo, labels_test)

    acc_min_samples_split_50 = accuracy_score(predFifty, labels_test)


