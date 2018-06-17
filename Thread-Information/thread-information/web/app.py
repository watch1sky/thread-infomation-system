# -*- coding:utf-8 -*-
from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap
from pymongo import MongoClient
from OTXv2 import OTXv2
import IndicatorTypes
import ip
import predictions

conn = MongoClient('127.0.0.1', 27017)
db = conn.mydb
ip_info = db.info

API_KEY = '0b357b5832ee35374dd4b6b959a730c3208ec2cfd5ccb00c4ac96b88efcd61a5'
OTX_SERVER = 'https://otx.alienvault.com/'
otx = OTXv2(API_KEY, server=OTX_SERVER)

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html',name='index')

@app.route('/query/',methods=['GET'])
def query():
    if request.method == 'GET':
        error = 0
        error_msg = ''
        q = request.args.get('q')
        if q:
            result = ip_info.find_one({'ip':q})
            if result:
                results = {'ip':result['ip'], 'country':result['country'], 'city':result['city'], 'country_id':result['country_id']}
            else:
                result = otx.get_indicator_details_full(IndicatorTypes.IPv4, q)
                if result:
                    results = {'ip':result['general']['indicator'],'country':result['general']['country_name'], 'city':result['general']['city']}
                    ip.search_ip(q)
                else:
                    results = {}
                    error = 1
            if error:
                city_pre = ''
            else:
                city_pre = predictions.predict(results['city'])
                city_pre = city_pre[0:2]
                result = []
                for cp in city_pre:
                    r = ip_info.find({'city':cp[0]})
                    for rs in r[0:10]:
                        result.append(rs)
            return render_template('index.html', q=q, error=error, error_msg=error_msg, results=results, pre=result, city_pre=city_pre)
        else:
            return render_template('index.html')



@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug = True)
