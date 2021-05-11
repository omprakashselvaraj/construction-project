from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/input',methods=['GET','POST'])
def input():
    if request.method=="POST":
        detail=request.form
        print('1')
        builtup=detail['builtup']
        print('2')
        cost=detail['cost']
        print(builtup,cost)
        return "success"

if __name__=='__main__':
    app.run(debug=True)