from sklearn import tree

X = [[1,1,1,0],
     [0,0,1,0],
     [1,1,0,1],
     [1,1,1,1],
     [1,0,1,1]]

Y = [1,0,0,1,1]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)

clf.predict([[0,1,1,0]])

tree.plot_tree(clf)