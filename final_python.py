from flask import Flask

from temperature import temp_check

app = Flask(__name__)

app.config["DEBUG"] = True

@app.route('/')
def home_page():
    return '''
        <html>
            <body>
                <p>Enter your Temperature:</p>
                <form>
                    <p><input name="temp" /></p>
                    <p><input type="submit" value="Submit" /></p>
                </form>
            </body>
        </html>
    '''
if __name__=='__main__':
    app.run()


    
