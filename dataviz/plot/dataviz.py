import os
import sys
import json


PATH_OUT = os.path.join(os.getcwd(), "html")

PATH_DATA = os.path.join(os.getcwd(), "../data/data.json")
assert os.path.isfile(PATH_DATA), \
    f"File {PATH_DATA} doesn't exist"


PATH_TEMPLATE_HTML = os.path.join(os.getcwd(), "template.html")
assert os.path.isfile(PATH_TEMPLATE_HTML), \
    f"Template {PATH_TEMPLATE_HTML} doesn't exist"

HTML_TAG = "##body##"

PATH_TEMPLATE_JS = os.path.join(os.getcwd(), "template.js")
assert os.path.isfile(PATH_TEMPLATE_JS), \
    f"Template {PATH_TEMPLATE_JS} doesn't exist"

if __name__ == "__main__":
    try:
        with open(PATH_DATA, 'r') as f:
            data = json.load(f)
    except Exception as e:
        print(e)
        sys.exit(1)

    if len(data.keys()) == 0:
        print(f"Empty data set in {PATH_DATA}")
        sys.exit(1)

    try:
        with open(PATH_TEMPLATE_HTML, 'r') as f:
            html = f.read()
    except Exception as e:
        print(e)
        sys.exit(1)

    insert_tag = '\n'.join(
        [f"""\t<div id="fig_{plot.lower().replace(' ', '_')}"></div>""" for plot in data.keys()])

    html = html.replace(HTML_TAG, insert_tag)
    
    try:
        with open(PATH_TEMPLATE_JS, 'r') as f:
            js = f.read()
    except Exception as e:
        print(e)
        sys.exit(1)

    js = f"var data = {json.dumps(data)};\n{js}"
    
    if not os.path.isdir(PATH_OUT):
        os.makedirs(PATH_OUT)
    
    with open(os.path.join(PATH_OUT, "index.html"), 'w') as f:
        f.write(html)
    
    with open(os.path.join(PATH_OUT, "graph.js"), 'w') as f:
        f.write(js)
