#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, request, render_template
import json,time
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        q = request.form.get("question")
        body = json.dumps(
            {
                "version"  :  "db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf",
                "input"  :  {"prompt":q}
            }
        )
        headers = {
            "Authorization"  :  "Token r8_VphYxkWPuCKzI5OBHGoXA0LLmV5VP901JQaYn",
            "Content-Type"   :  "application/json"
        }        
        r = requests.post("https://api.replicate.com/v1/predictions", data=body, headers=headers)
        time.sleep(10)
        get_url = r.json()["urls"]["get"]
        get_result = requests.post(get_url,headers=headers).json()["output"]
        return(render_template("index.html", result=get_result[0]))
    else:
        return(render_template("index.html", result="waiting"))
    
if __name__ == "__main__":
    app.run()


# In[ ]:




