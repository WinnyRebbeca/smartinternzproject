from flask import Flask,render_template,request 
import pickle
import numpy as np

app=Flask(__name__) #your application
rfr=pickle.load(open('CC_Strength.pkl','rb'))


@app.route('/') # default route
def home():
    return render_template("ccstr_demo.html")

@app.route('/ccstr')
def ccstr():
    return render_template('ccsrt1.html')
@app.route('/predict',methods=['post'])
def predict():
    cement=float(request.form['Cement'])
    black=float(request.form['BlastFurnaceSlag'])
    fly=float(request.form['FlyAsh'])
    wat=float(request.form['Water'])
    sup=float(request.form['Superplasticizer'])
    cg=float(request.form['CoarseAggregate'])
    fg=float(request.form['FineAggregate'])
    ag=float(request.form['Age'])
    
    print(cement,black,fly,wat,sup,cg,fg,ag)
    a=np.array([[cement,black,fly,wat,sup,cg,fg,ag]])
    
    result=rfr.predict(a)
    x=result
    return render_template('ccsrt1.html',x='Predicted Concrete Strenght is {}'.format(*x))

if __name__ == '__main__':
    app.run() # you are running your app