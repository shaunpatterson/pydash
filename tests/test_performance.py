# -*- coding: utf-8 -*-

import pickle
import pydash as _

import time


def test_get():

    with open('product.pkl', 'rb') as f:
        product = pickle.load(f)

    start = time.time()
    count = 10000 * 10
    #for i in range(count):
    #    for test in tests:
    #       _.get(*test[0])

    for i in range(count):
        productSlug = _.get(product, 'allMeta.tile.product.productSlug')

    end = time.time()

    total = end - start
    avg = total / count

    print("Time: %s. Avg: %s" % (total, avg))

if __name__ == "__main__":
    test_get()
