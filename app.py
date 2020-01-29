from flask import Flask,jsonify,json
import pickle
import numpy as np
from sklearn.linear_model import LinearRegression


app = Flask(__name__)


@app.route('/<int:year>')
def hello_world(year):
    model = pickle.load(open('smodel.pkl', 'rb'))
    var = [[year, 400, 500, 100, 150, 210]]
    var = np.array(var)
    result = {"year": str(year),"sales":str(round(model.predict(var)[0][0],2))}
    print((type(result)))
    return jsonify(result)




if __name__ == '__main__':
    app.run()
