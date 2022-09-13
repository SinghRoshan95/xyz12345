#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, render_template,request
app=Flask(__name__)
@app.route('/')
def fhhggh():
    return render_template('deploy.html')
@app.route('/info',methods=['POST'])
def hdgggdh():
    if (request.method=='POST'):
        num1=float(request.form['a'])
        num2=float(request.form['b'])
        result=num1+num2
        return render_template('deploy.html', answer=result)
if __name__=='__main__':
    app.run()


# In[12]:


pwd


# In[ ]:





# In[ ]:





# In[ ]:




