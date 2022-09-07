import math


def df_generator(dataframe, S0, Beta, Dual_RF, AGE, SBP, DL=False, List_DL=[]):
    FeatureMean = dataframe.mean(axis=0)
    beta = Beta

    if DL:
        column = (2 ** len(Dual_RF)) * len(List_DL)
        row = len(SBP) * len(AGE)
        df = [[0 for col in range(column)] for row in range(row)]
        SS = (beta.get('age') * FeatureMean.age) + (beta.get("sex") * FeatureMean.sex) + (
                (beta.get("diabetes")) * FeatureMean.diabetes) + ((beta.get("whr")) * FeatureMean.whr) + (
                     (beta.get("smoker")) * FeatureMean.smoker) + (
                     (beta.get("family_history")) * FeatureMean.family_history) + (
                     (beta.get("sbp2")) * FeatureMean.sbp2) + ((beta.get("sbp3")) * FeatureMean.sbp3) + (
                     (beta.get("sbp4")) * FeatureMean.sbp4) + ((beta.get("tch2")) * FeatureMean.tch2) + (
                     (beta.get("tch3")) * FeatureMean.tch3) + ((beta.get("tch4")) * FeatureMean.tch4) + (
                     (beta.get("tch5")) * FeatureMean.tch5)
        for i in range(row):
            FeatureAge = AGE[(len(AGE) - 1) - (i // len(SBP))]
            FeatureSBP = SBP[(len(SBP) - 1) - (i % len(SBP))]

            # print(FeatureSBP)

            for j in range(column):
                VV = 0

                FeatureDL = List_DL[(j % len(List_DL))]
                twoD_length = len(List_DL)

                # Age
                VV += (beta.get("age")) * FeatureAge

                # Sbp
                if FeatureSBP == 4:
                    VV += (beta.get("sbp4")) * 1
                elif FeatureSBP == 3:
                    VV += (beta.get("sbp3")) * 1
                elif FeatureSBP == 2:
                    VV += (beta.get("sbp2")) * 1
                else:
                    VV += 0

                    # total Cholesterol
                if FeatureDL == 5:
                    VV += (beta.get("tch5")) * 1
                elif FeatureDL == 4:
                    VV += (beta.get("tch4")) * 1
                elif FeatureDL == 3:
                    VV += (beta.get("tch3")) * 1
                elif FeatureDL == 2:
                    VV += (beta.get("tch2")) * 1
                else:
                    VV += 0

                # smoker
                if 0 <= j < 5 or 10 <= j < 15 or 20 <= j < 25 or 30 <= j < 35 or 40 <= j < 45 or 50 <= j < 55 or 60 <= j < 65 or 70 <= j < 75 or 80 <= j < 85 or 90 <= j < 95 or 100 <= j < 105 or 110 <= j < 115 or 120 <= j < 125 or 130 <= j < 135 or 140 <= j < 145 or 150 <= j < 155:
                    VV += 0
                else:
                    VV += (beta.get("smoker")) * 1

                # Diabetes
                if 0 <= j < 10 or 20 <= j < 30 or 40 <= j < 50 or 60 <= j < 70 or 80 <= j < 90 or 100 <= j < 110 or 120 <= j < 130 or 140 <= j < 150:
                    VV += 0
                else:
                    VV += (beta.get("diabetes")) * 1

                # sex
                if 0 <= j < 20 or 40 <= j < 60 or 80 <= j < 100 or 120 <= j < 140:
                    VV += 0

                else:
                    VV += beta.get("sex") * 1

                # whr
                if 0 <= j < twoD_length * 8 or 80 <= j < 120:
                    VV += 0
                else:
                    VV += (beta.get("whr")) * 1

                # family_history
                if 0 <= j < 80:
                    VV += 0
                else:
                    VV += (beta.get("family_history")) * 1
                # round
                df[i][j] = round((1 - (S0 ** (math.exp(VV - SS)))) * 100)
                # df[i][j] = ((1 - (S0 ** (math.exp(VV - SS)))) * 100)

        return df

    else:
        column = 2 ** len(Dual_RF)
        row = len(SBP) * len(AGE)
        df = [[0 for col in range(column)] for row in range(row)]
        SS = (beta.get('age') * FeatureMean.age) + (beta.get("sex") * FeatureMean.sex) + (
                (beta.get("diabetes")) * FeatureMean.diabetes) + ((beta.get("whr")) * FeatureMean.whr) + (
                     (beta.get("smoker")) * FeatureMean.smoker) + (
                     (beta.get("family_history")) * FeatureMean.family_history) + (
                     (beta.get("sbp2")) * FeatureMean.sbp2) + ((beta.get("sbp3")) * FeatureMean.sbp3) + (
                     (beta.get("sbp4")) * FeatureMean.sbp4)

        for i in range(row):
            for j in range(column):
                FeatureAge = AGE[(len(AGE) - 1) - (i // len(SBP))]
                FeatureSBP = SBP[(len(SBP) - 1) - (i % len(SBP))]
                VV = 0
                SS = 0
                # Age
                VV += (beta.get("age")) * FeatureAge

                # Sbp
                if FeatureSBP == 4:
                    VV += (beta.get("sbp4")) * 1
                elif FeatureSBP == 3:
                    VV += (beta.get("sbp3")) * 1
                elif FeatureSBP == 2:
                    VV += (beta.get("sbp2")) * 1
                else:
                    VV += 0

                # smoker
                if 0 <= j < 1 or 2 <= j < 3 or 4 <= j < 5 or 6 <= j < 7:
                    VV += 0
                else:
                    VV += (beta.get("smoker")) * 1

                # Diabetes
                if 0 <= j < 10 or 20 <= j < 30 or 40 <= j < 50 or 60 <= j < 70 or 80 <= j < 90 or 100 <= j < 110 or 120 <= j < 130 or 140 <= j < 150:
                    VV += 0
                else:
                    VV += (beta.get("diabetes")) * 1

                # sex
                if 0 <= j < 2 or 4 <= j < 6:
                    VV += 0

                else:
                    VV += beta.get("sex") * 1

                # whr
                if 0 <= j < 4:
                    VV += 0
                else:
                    VV += (beta.get("whr")) * 1

                # family_history
                if 0 <= j < 8:
                    VV += 0
                else:
                    VV += (beta.get("family_history")) * 1
                # round
                # df[i][j] = round((1 - (S0 ** (math.exp(VV - SS)))) * 100)
                df[i][j] = ((1 - (S0 ** (math.exp(VV - SS)))) * 100)


            return df






