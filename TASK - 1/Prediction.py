import numpy as np, joblib as jb

def pred(sl, sw, pl, pw):
    m = jb.load("KNN.sav")
    inp = np.array([[sl,sw,pl,pw]])
    return "".join(m.predict(inp))