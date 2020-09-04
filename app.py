from flask import Flask, jsonify,make_response,abort
from flask import request

app = Flask(__name__)

formulas=[
    {
        "name": 'Simple Interest',
        "SI": "PTR/100",
    },
    {
        "name": 'Compound Interest',
        "If interst is calculated annually": "Amount=p(1+R/100)^n",
        "If interst is calculated half-yearly": "Amount=p(1+(R/2)/100)^2n",
        "If interst is calculated quarterly": "Amount=p(1+(R/4)/100)^4n",
    },
    {
        "name": 'Profit and Loss',
        "p": "sp-cp",
        "p%": "((sp-cp)/cp)*100",
        "p": "(p%/100)*cp",
        "sp": "((100+p%)/100)/cp",
        "cp": "(100/(100+p%))*sp",
        "l": "cp-sp",
        "l%": "((cp-sp)/cp)*100",
        "l": "(l%/100)*cp",
        "sp": "((100-l%)/100)/cp",
        "cp": "(100/(100-l%))*sp",
    },
    {
        "name": 'Marked Price',
        "D": "mp-sp",
        "d%": "((mp-sp)/mp)*100",
        "D": "(d%/100)*mp",
    },
    {
        "name": 'Discount',
        "D": "mp-sp",
        "d%": "((mp-sp)/mp)*100",
        "D": "(d%/100)*mp",
    },
    {
        "name": 'Time,Speed,Distance',
        "D": "s*t",
        "s": "d/t",
        "t": "d/s",
        "if 2 distances are same": "d1=d2 and s1t1=s2t2",
        "if time is same": "t1=t2 and d1/s1=d2/s2",
        "if speed is same": "s1=s2 and d1/t1=d2/t2",
    },
    {
        "name": 'algebra',
        "(a+b)^2": "a^2+b^2+2ab",
        "(a-b)^2": "a^2+b^2-2ab",
        "(a+b+c)^3": "a^3+b^3+c^3+2ab+2ac+2bc",
        "a^2-b^2": "(a+b)(a-b)",
        "(a+b)^2+(a-b)^2": "2(a^2+b^2)",
        "(a+b)^2-(a-b)^2": "4ab",
    },
    {
        "name": 'Probability',
        "probability": "no of favourble outcomes / no of possible outcomes",
        "probablity which is certain to happen": "p(s)=1",
        "probablity which is impossible to happen": "0",
        "probablity which something not happening": "p(b)=1-p(a)",
        "p(aUb)": "p(a)+p(b)-p(aUb)",
        "p(aUbUc)": "p(a)+p(b)+p(c)-p(a inst b)-p(b inst c)-p(c inst a)+p(a inst b inst c)",
    },
    {
        "name": 'Permutation',
        "nPr": "n!/(n-r)!",
        "nP0": "1",
        "nP1": "n",
    },
    {
        "name": 'Combiation',
        "nCr": "n!/r!(n-r)!",
        "nCr": "nC(n-r)",
        "nCn": "1",
        "nC0": "1",
        "nC1": "n",
    },
]
#returns all
@app.route('/formulas',methods=['GET'])
def get_fs():
    return jsonify({'All formulas':formulas})

#return specified one
@app.route('/formulas/<string:name>', methods=['GET'])
def formula(name):
	requestedfs = [fs for fs in formulas if fs['name'] == name]
	if len(requestedfs) == 0:
		abort(404)
	return jsonify(requestedfs[0])

#delete
@app.route('/formulas/<string:name>', methods=['DELETE'])
def removeformula(name):
	fetch_fs = [fs for fs in formulas if fs['name'] == name]
	if len(fetch_fs) == 0:
		abort(404)
	formulas.remove(fetch_fs[0])
	return jsonify({'deletedStatus': True})

if __name__ == '__main__':
    app.run(debug=True)
