from flask import Flask,render_template,request,send_file
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
import jinja2
plt.style.use('ggplot')

msg=[]
    


app=Flask(__name__)


@app.route('/')
def main():
    return render_template('main.html')

@app.route('/input',methods=['GET','POST'])
def input():
    if request.method=="POST":
        detail=request.form
        builtup=int(detail['builtup'])
        cost=int(detail['cost'])
        print(builtup,cost)
        msg.append(builtup)
        msg.append(cost)
        tot=cost*builtup
        msg.append(tot)
        msg.append(0.164*tot)
        msg.append(0.123*tot)
        msg.append(0.0742*tot)
        msg.append(0.246*tot)
        msg.append(0.165*tot)
        msg.append(0.228*tot)
        msg.append(0.4*builtup)
        msg.append(0.816*builtup)
        msg.append(0.608*builtup)
        msg.append(4*builtup)
        msg.append(0.18*builtup)
        msg.append(8*builtup)
        msg.append(1.3*builtup)

        return render_template('output.html', msg=msg)

@app.route('/plotcall')
def plotcall():
    x=np.array(msg[3:9])
    mylabels=['cement(16.4%)','sand(12.3%)','aggregate(7.4%)','steel(24.6%)','finitures(16.5%)','fittings(22.8%']
    plt.title('Approx. cost on various work of materials')
    plt.pie(x,labels=mylabels)
    figfile = BytesIO()
    plt.savefig(figfile, format='png')
    figfile.seek(0)  # rewind to beginning of file
    import base64
    figdata_png = base64.b64encode(figfile.getvalue())
    return figdata_png


if __name__=='__main__':
    app.run(debug=True)