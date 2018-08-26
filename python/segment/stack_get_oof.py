from sklearn.tree import DecisionTreeClassifier, ExtraTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, BaggingClassifier, GradientBoostingClassifier
from sklearn.linear_model import RidgeClassifier,SGDClassifier,LogisticRegression
from sklearn.svm import SVC
from sklearn.model_selection import KFold
import pickle
import pandas as pd
import numpy as np
feature_cols = ['wc_diff', 'char_diff', 'total_unique_words', 'total_unq_words_stop', 'wc_diff_unique',\
 'common_words', 'same_start_word', 'word_match', 'tfidf_word_match', 'cosine_distance', 'cityblock_distance', \
 'jaccard_distance', 'shingle_similarity', 'canberra_distance', 'euclidean_distance', 'minkowski_distance', \
 'braycurtis_distance', 'skew_q1vec', 'skew_q1vec', 'skew_q2vec', 'kur_q1vec', 'kur_q2vec']

def get_oof(train, labels, test, clf, save_path, n_splits=5):
    kf = KFold(n_splits=n_splits, shuffle=True, random_state=2017)
    kfs = list(kf.split(train))
    ntrain = train.shape[0]
    ntest = test.shape[0]
    oof_train = np.zeros((ntrain,))
    oof_test = np.zeros((ntest,))
    oof_test_skf = np.zeros((n_splits, ntest))
    for i, (train_index, test_index) in enumerate(kfs):
        x_tr = train[train_index]
        y_tr = labels[train_index]
        x_te = train[test_index]
        y_te = labels[test_index]

        clf.fit(x_tr, y_tr)
        tmp = clf.predict_proba(x_te)
        oof_train[test_index] = tmp[:,1]
        oof_test_skf[i, :] = clf.predict_proba(test)[:,1]
        #pickle.dump(clf, open(save_path + clf.__class__.__name__ + str(i) + '.pkl','wb'))

        # xgb
        #clf.train(x_tr, y_tr, x_te, y_te)
        #oof_train[test_index] = clf.predict(x_te)
        #oof_test_skf[i, :] = clf.predict(test)

    oof_test[:] = oof_test_skf.mean(axis=0)
    return oof_train.reshape(-1), oof_test.reshape(-1)
clfs = []
clfs.append(DecisionTreeClassifier())
clfs.append(ExtraTreeClassifier())
clfs.append(AdaBoostClassifier())
clfs.append(BaggingClassifier())
clfs.append(LogisticRegression(solver='sag',
                            penalty='l2',
                            class_weight=None,
                            C=1.2))
clfs.append(RandomForestClassifier(max_features='auto',
                                 max_depth=10,
                                 min_samples_split=10,
                                 min_samples_leaf=20,
                                 random_state=10,
                                 n_estimators=100,
                                 class_weight='balanced'))

clfs.append(GradientBoostingClassifier())
clfs_len = len(clfs)
train = df1[feature_cols].values
train_label = df1['label'].values
test = df2[feature_cols].values
test_label = df2['label'].values
model_2_train = np.empty((train.shape[0], clfs_len))
model_2_test = np.empty(( test.shape[0], clfs_len))
save_path = model_dir + '0822_classical_'
for i,clf in enumerate(clfs):
    model_2_train[:,i], model_2_test[:,i] = get_oof(train, train_label, test, clf, save_path)

topai(1,pd.DataFrame(model_2_train))
topai(2,pd.DataFrame(model_2_test))