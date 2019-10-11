# Hacky script to compute stats
import json
import sys
import os

for n in os.listdir("."):
    try:
        with open(os.path.join(".", n, "data.json")) as f:
            data = json.load(f)
            items = len(data)
            props = len(data[0])
            total = items * props
            print("items = {a:08}, properties = {b:02}, total = {c:09} ({d})".format(d=n, a=items, b=props, c=total))
    except:
        pass