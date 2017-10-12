from flask import Flask, url_for, render_template

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main()
    return render_template('home.html')

@app.route("/p1")
def render_page1():
    celcius = ((float(request.args['color']))-32)*5/9 
    return render_template('home.html', response = "the temp in celcius is" + celcius)

@app.route("/response")
def render_response():
    color = request.args['color']
    #The request object stores information about the request sent to the server.
    #args is a MultiDict (like a dictionary but can have muiltiple values for the same key)
    if color == 'purple':
        reply = "That's my favorite color, too!"
    else:
        reply = "My favorite color is purple."
    return render_template('response.html', response = reply)

@app.route("/p2")
def render_page2():
     return render_template('page2.html')
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
            

