from flask import Flask,jsonify,json
import pickle
import numpy as np
from sklearn.linear_model import LinearRegression


app = Flask(__name__)


@app.route('/<int:year>')
def hello_world(year):
    #Load pickle file from the "sales_ml.ipynb"
    model = pickle.load(open('smodel.pkl', 'rb'))
    #Below are the predictions
    #x1-the year,x2-total_quantity,x3-total_stock,x4-total_product_sold,x5-avg_buying_price,x6-avg_selling_price
    var = [[year, 400, 500, 100, 150, 210]]
    #Convert the var to a Numpy array
    var = np.array(var)
    #This has the Y for the year
    prediction = round(model.predict(var)[0][0],2))
    print((prediction))
    #Render the template for the predictor chart template
    return render_template("predictor.html",y_sales=predictor)




if __name__ == '__main__':
    app.run()
