from flask import Flask, render_template, request
from src.tweet_fetcher import query_tweets_db

# Flask server for handling HTTP requests
app = Flask(__name__, template_folder="templates")


@app.route('/', methods=['GET', 'POST'])
def website():
    if request.method == 'POST':
        tweet = request.form['keywords']
        print("<h2>" + tweet + " </h2>")
        return render_template('index.html', tweet=query_tweets_db(tweet, "Danickyflash"))

    return render_template('index.html')


# TODO:
# - Fix 500 HTTP error with app in JS
# - Fix path so that it prints out correctly! (might be solved if we fix first one)
# - make this work for linda time

if __name__ == '__main__':
    app.run(debug=True)
