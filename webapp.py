from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('index.html')

@app.route("/moon")
def render_page1():
    return render_template('moon.html')

@app.route("/mars")
def render_page2():
    return render_template('mars.html')

@app.route("/venus")
def render_page3():
    return render_template('venus.html')
    
@app.route("/titan")
def render_page4():
    return render_template('titan.html')

@app.route("/responseMoon")
def render_responseMoon():
    weight = request.args['weight']
    #The request object stores infor about the request sent to the server
    #args is a "MultiDict" - a dictionary that can hold more than one value per key
    #The information in args is visible in the url for the page being requested (ex. .../response?color=blue)
    
    reply = "Your weight is " + weight*0.177 + " on this planet."
    return render_template('response.html', response = reply)

@app.route("/responseMars")
def render_responseMars():
    weight = request.args['weight']
    #The request object stores infor about the request sent to the server
    #args is a "MultiDict" - a dictionary that can hold more than one value per key
    #The information in args is visible in the url for the page being requested (ex. .../response?color=blue)
    
    reply = "Your weight is " + weight*0.38 + " on this planet."
    return render_template('response.html', response = reply)

@app.route("/responseTitan")
def render_responseTitan():
    weight = request.args['weight']
    #The request object stores infor about the request sent to the server
    #args is a "MultiDict" - a dictionary that can hold more than one value per key
    #The information in args is visible in the url for the page being requested (ex. .../response?color=blue)
    
    reply = "Your weight is " + weight*0.14 + " on this planet."
    return render_template('response.html', response = reply)

@app.route("/responseVenus")
def render_responseVenus():
    weight = request.args['weight']
    #The request object stores infor about the request sent to the server
    #args is a "MultiDict" - a dictionary that can hold more than one value per key
    #The information in args is visible in the url for the page being requested (ex. .../response?color=blue)
    
    reply = "Your weight is " + weight*0.91 + " on this planet."
    return render_template('response.html', response = reply)

    
if __name__=="__main__":
    app.run(debug=False, port=54321)
