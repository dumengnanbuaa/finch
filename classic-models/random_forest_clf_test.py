from random_forest_clf import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


if __name__ == '__main__':
    X, y = make_classification(5000, flip_y=0.5)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)

    forest = RandomForestClassifier()
    forest.fit(X_train, y_train)

    tree = DecisionTreeClassifier()
    tree.fit(X_train, y_train)

    print("Tree | Test acc: %.3f" % tree.score(X_test, y_test))
    print("Random Forest | Test acc: %.3f" % forest.score(X_test, y_test))
