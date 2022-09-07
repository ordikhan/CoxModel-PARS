import matplotlib.pyplot as plt
import pandas as pd
from lifelines import CoxPHFitter
import numpy as np

class LifeLine:
    def __init__(self, FileAddress):
        self.dataframe = pd.read_excel(FileAddress,
                                       names=["IHHPCode", "sex", "whr", "smoker", "family_history", "diabetes", "age",
                                              "cholesterol", "blood_pressure", "dbp", "hdl", "ldl", "tg", "htn",
                                              "sbp_cat", "sbp1", "sbp2", "sbp3", "sbp4", "tchcat", "tch1", "tch2",
                                              "tch3", "tch4", "tch5",
                                              "FollowDu5th", "label"], header=0)

    def Beta4(self):
        self.dataframe_r = self.dataframe.loc[:,
                           {"sex", "age", "tch2", "tch3", "tch4", "tch5", "sbp2", "sbp3", "sbp4", "FollowDu5th",
                            "label"}]
        self.cph = CoxPHFitter()
        self.cph.fit(self.dataframe_r, duration_col='FollowDu5th', event_col='label')
        self.Beta = self.cph.hazards_.iloc[0].to_dict()
        return self.Beta

    def BaselineSurvival4(self):
        self.dataframe_r = self.dataframe.loc[:,
                           {"sex", "age", "tch2", "tch3", "tch4", "tch5", "sbp2", "sbp3", "sbp4", "FollowDu5th",
                            "label"}]
        self.cph = CoxPHFitter()
        self.cph.fit(self.dataframe_r, duration_col='FollowDu5th', event_col='label')
        BaselineS = self.cph.baseline_survival_
        return BaselineS
        # return float(BaselineS.loc[144])

    def Beta5(self):
        self.dataframe_r = self.dataframe.loc[:,
                           {"sex", "whr", "age", "tch2", "tch3", "tch4", "tch5", "sbp2", "sbp3", "sbp4", "FollowDu5th",
                            "label"}]
        self.cph = CoxPHFitter()
        self.cph.fit(self.dataframe_r, duration_col='FollowDu5th', event_col='label')
        self.Beta = self.cph.hazards_.iloc[0].to_dict()
        return self.Beta

    def BaselineSurvival5(self):
        self.dataframe_r = self.dataframe.loc[:,
                           {"sex", "whr", "age", "tch2", "tch3", "tch4", "tch5", "sbp2", "sbp3", "sbp4", "FollowDu5th",
                            "label"}]
        self.cph = CoxPHFitter()
        self.cph.fit(self.dataframe_r, duration_col='FollowDu5th', event_col='label')
        BaselineS = self.cph.baseline_survival_
        return BaselineS
        # return float(BaselineS.loc[144])

    def Beta6(self):
        self.dataframe_r = self.dataframe.loc[:,
                           {"sex", "whr", "smoker", "age", "tch2", "tch3", "tch4", "tch5", "sbp2", "sbp3", "sbp4",
                            "FollowDu5th", "label"}]
        self.cph = CoxPHFitter()
        self.cph.fit(self.dataframe_r, duration_col='FollowDu5th', event_col='label')
        self.Beta = self.cph.hazards_.iloc[0].to_dict()
        return self.Beta

    def BaselineSurvival6(self):
        self.dataframe_r = self.dataframe.loc[:,
                           {"sex", "whr", "smoker", "age", "tch2", "tch3", "tch4", "tch5", "sbp2", "sbp3", "sbp4",
                            "FollowDu5th", "label"}]
        self.cph = CoxPHFitter()
        self.cph.fit(self.dataframe_r, duration_col='FollowDu5th', event_col='label')
        BaselineS = self.cph.baseline_survival_
        return BaselineS
        # return float(BaselineS.loc[144])

    def Beta7(self):
        self.dataframe_r = self.dataframe.loc[:,
                           {"sex", "whr", "smoker", "family_history", "age", "tch2", "tch3", "tch4", "tch5", "sbp2",
                            "sbp3", "sbp4",
                            "FollowDu5th", "label"}]
        self.cph = CoxPHFitter()
        self.cph.fit(self.dataframe_r, duration_col='FollowDu5th', event_col='label')
        self.Beta = self.cph.hazards_.iloc[0].to_dict()
        return self.Beta

    def BaselineSurvival7(self):
        self.dataframe_r = self.dataframe.loc[:,
                           {"sex", "whr", "smoker", "family_history", "age", "tch2", "tch3", "tch4", "tch5", "sbp2",
                            "sbp3", "sbp4",
                            "FollowDu5th", "label"}]
        self.cph = CoxPHFitter()
        self.cph.fit(self.dataframe_r, duration_col='FollowDu5th', event_col='label')
        BaselineS = self.cph.baseline_survival_
        # p=[]
        # for i in range(100):
        #     p.append(BaselineS.loc[i][0])
        return BaselineS

    def Beta8(self):
        self.dataframe_r = self.dataframe.loc[:,
                           {"sex", "whr", "smoker", "family_history", "diabetes", "age", "sbp2", "sbp3", "sbp4", "tch2",
                            "tch3", "tch4", "tch5", "FollowDu5th", "label"}]
        self.cph = CoxPHFitter()
        self.cph.fit(self.dataframe_r, duration_col='FollowDu5th', event_col='label')
        self.Beta = self.cph.hazards_.iloc[0].to_dict()
        return self.Beta

    def BaselineSurvival8(self):
        self.dataframe_r = self.dataframe.loc[:,
                           {"sex", "whr", "smoker", "family_history", "diabetes", "age", "sbp2", "sbp3", "sbp4", "tch2",
                            "tch3", "tch4", "tch5", "FollowDu5th", "label"}]
        self.cph = CoxPHFitter()
        self.cph.fit(self.dataframe_r, duration_col='FollowDu5th', event_col='label')
        BaselineS = self.cph.baseline_survival_
        # print(BaselineS)
        # p=[]
        # for i in range(100):
        #     p.append(BaselineS.loc[i])
        # print(BaselineS.loc[1][0])
        p = BaselineS.to_numpy().reshape(-1)
        avrg= np.mean(p)
        # print(avrg)
        return avrg

#
# a = LifeLine('ParsDataSet7.xlsx')
#
# print(a.BaselineSurvival8())