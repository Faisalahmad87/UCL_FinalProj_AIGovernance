# FairC.py

import pandas as pd
import numpy as np
import time, copy
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

import sys, os
sys.path.append(os.path.abspath('..'))
from Measure import measure_final_score

def FairC(df, base_clf, keyword, ratio=0.2, rep=10):
    dataset_orig = df.dropna()
    scaler = MinMaxScaler()
    dataset_orig = pd.DataFrame(scaler.fit_transform(dataset_orig), columns=dataset_orig.columns)

    acc, pre, recall, f1 = [], [], [], []
    aod, eod, spd, di = [], [], [], []
    eopd = []

    for i in range(rep):
        start = time.time()
        dataset_orig_train, dataset_orig_test = train_test_split(dataset_orig, test_size=ratio, random_state=i)
        X_train = dataset_orig_train.loc[:, dataset_orig_train.columns != 'Probability'].copy()
        y_train = dataset_orig_train['Probability'].copy()
        X_test = dataset_orig_test.loc[:, dataset_orig_test.columns != 'Probability'].copy()
        y_test = dataset_orig_test['Probability'].copy()

        # Step 1: Train base model on training data
        clf = copy.deepcopy(base_clf)
        clf.fit(X_train, y_train)

        # Step 2: Flip sensitive attribute
        X_flip = X_train.copy()
        X_flip[keyword] = np.where(X_flip[keyword] == 1, 0, 1)

        # Step 3: Identify fair-consistent examples
        y_pred_orig = clf.predict(X_train)
        y_pred_flip = clf.predict(X_flip)
        consistent_mask = (y_pred_orig == y_pred_flip)

        X_train_filtered = X_train[consistent_mask].copy()
        y_train_filtered = y_train[consistent_mask].copy()

        # Step 4: Retrain on fair-consistent data
        clf_fair = copy.deepcopy(base_clf)
        clf_fair.fit(X_train_filtered, y_train_filtered)

        # Step 5: Evaluate
        y_pred = clf_fair.predict(X_test)
        cm = confusion_matrix(y_test, y_pred)

        acc.append(accuracy_score(y_test, y_pred))
        pre.append(precision_score(y_test, y_pred))
        recall.append(recall_score(y_test, y_pred))
        f1.append(f1_score(y_test, y_pred))
        aod.append(measure_final_score(dataset_orig_test, y_pred, cm, X_train_filtered, y_train_filtered, X_test, y_test, keyword, 'aod'))
        eod.append(measure_final_score(dataset_orig_test, y_pred, cm, X_train_filtered, y_train_filtered, X_test, y_test, keyword, 'eod'))
        spd.append(measure_final_score(dataset_orig_test, y_pred, cm, X_train_filtered, y_train_filtered, X_test, y_test, keyword, 'SPD'))
        di.append(measure_final_score(dataset_orig_test, y_pred, cm, X_train_filtered, y_train_filtered, X_test, y_test, keyword, 'DI'))
        eopd.append(measure_final_score(dataset_orig_test, y_pred, cm, X_train_filtered, y_train_filtered, X_test, y_test, keyword, 'eopd'))
        print(f"Round {i+1} finished. Time: {time.time() - start:.2f} sec")

    res = [acc, pre, recall, f1, aod, eod, spd, di,eopd]
    return res
