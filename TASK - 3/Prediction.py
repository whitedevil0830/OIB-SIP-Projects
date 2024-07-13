import joblib as jb

def pred(yr, pp, dkms, ft, st, tran, owner):
    model = jb.load("DT.sav")
    Driven_max = 99708.75
    Driven_min = 500.0
    Year_max = 2018
    Year_min = 2003
    yr = (yr - Year_min) / (Year_max- Year_min)
    dkms = (dkms - Driven_min) / (Driven_max- Driven_min)
    res = model.predict([[yr, pp, dkms, ft, st, tran, owner]])
    return res[0]