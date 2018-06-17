# -*- coding:utf-8 -*-
import word2vec

model = word2vec.load('wiki.bin')

def predict(city):
    indexes, metrics = model.cosine(city)
    city_pre = model.generate_response(indexes, metrics)
    return city_pre

#a = u'上海'
#result = predict(a)
#print(result)