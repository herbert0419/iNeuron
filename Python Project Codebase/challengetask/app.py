from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from urllib.request import urlopen as uReq

app = Flask(__name__)


@app.route('/', methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")


# route to show the review comments in a web UI
@app.route('/review', methods=['POST', 'GET'])
@cross_origin()
def index():
    if request.method == 'POST':
    try:

        driver = webdriver.Chrome()
        for url in urls:
        driver.get('{}'.format(url))
        content = driver.page_source.encode('utf-8').strip()
        soup = BeautifulSoup(content, 'lxml')
        titles = soup.findAll('a', id='video-title')
        views = soup.findAll(
            'span', class_='style-scope ytd-grid-video-renderer')
        video_urls = soup.findAll('a', id='video-title')
        print('Channel: {}'.format(url))
        i = 0  # views and time
        j = 0  # urls
        for title in titles[:50]:
            print('\n{}\t{}\t{}\thttps://www.youtube.com{}'.format(title.text,
                  views[i].text, views[i+1].text, video_urls[j].get('href')))
            i += 2
            j += 1

        filename = searchString + ".csv"
        fw = open(filename, "w")
        headers = "Product, Customer Name, Rating, Heading, Comment \n"
        fw.write(headers)
        reviews = []
        for commentbox in commentboxes:
            try:
                    # name.encode(encoding='utf-8')
                    name = commentbox.div.div.find_all(
                        'p', {'class': '_2sc7ZR _2V5EHH'})[0].text

                except:
                    name = 'No Name'

                try:
                    # rating.encode(encoding='utf-8')
                    rating = commentbox.div.div.div.div.text

                except:
                    rating = 'No Rating'

                try:
                    # commentHead.encode(encoding='utf-8')
                    commentHead = commentbox.div.div.div.p.text

                except:
                    commentHead = 'No Comment Heading'
                try:
                    comtag = commentbox.div.div.find_all('div', {'class': ''})
                    # custComment.encode(encoding='utf-8')
                    custComment = comtag[0].div.text
                except Exception as e:
                    print("Exception while creating dictionary: ", e)

                mydict = {"Product": searchString, "Name": name, "Rating": rating, "CommentHead": commentHead,
                          "Comment": custComment}
                reviews.append(mydict)
            return render_template('results.html', reviews=reviews[0:(len(reviews)-1)])
        except Exception as e:
            print('The Exception message is: ', e)
            return 'something is wrong'
    # return render_template('results.html')

    else:
        return render_template('index.html')


if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=8001, debug=True)
    app.run(debug=True)
