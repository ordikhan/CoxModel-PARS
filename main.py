import pandas as pd
from allsurval import LifeLine
from ChartStatisticalCalculations import df_generator
from sklearn.model_selection import StratifiedKFold as KFold
import numpy as np
from calcu import *

kfold_n_split = 10
kf = KFold(n_splits=kfold_n_split, shuffle=True, random_state=6)
kfole_train = 'kfold_train.xlsx'
kfole_test = 'kfoldtest.xlsx'
file_name = 'ParsDataSet7.xlsx'
main_file = pd.read_excel(file_name)
y = main_file["label"]
kfold_get = kf.split(main_file, y)
test_fpr = []
test_tpr = []
test_auc = []
for j in range(kfold_n_split):
    print("\nstart kfold : ", j)
    result = next(kfold_get)
    train = main_file.iloc[result[0]]
    test = main_file.iloc[result[1]]

    train.to_excel(kfole_train, header=True, index=False)
    test.to_excel(kfole_test, header=True, index=False)
    del test, train

    pool = LifeLine(kfole_train)
    beta = pool.Beta8()
    age = [40, 50, 60, 70, 78]
    PREMIURE = [1, 2, 3, 4]
    s = ["sex", "whr", "smoker", "family_history", "diabetes"]
    DL = [1, 2, 3, 4, 5]
    S0=pool.BaselineSurvival8()
    dataframe = pd.read_excel(kfole_train,
                              names=["IHHPCode", "sex", "whr", "smoker", "family_history", "diabetes",
                                     "age",
                                     "cholesterol", "blood_preMIure", "dbp", "hdl", "ldl", "tg", "htn",
                                     "sbp_cat", "sbp1", "sbp2", "sbp3", "sbp4", "tchcat", "tch1", "tch2",
                                     "tch3", "tch4",
                                     "tch5", "FollowDu5th", "label"], header=0)

    a = df_generator(dataframe=dataframe, S0=S0, Beta=beta, Dual_RF=s, AGE=age, SBP=PREMIURE, DL=True,
                     List_DL=DL)

    #eval
    ev=aaa(a, kfole_test )
    test_auc.append(ev)

print(test_auc)

