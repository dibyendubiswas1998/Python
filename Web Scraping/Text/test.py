import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq

product_name = "samsung"
flipkartUrl = "https://www.flipkart.com/search?q=samsung"
# print(flipkartUrl)

uClients = uReq(flipkartUrl)
flipkartPage = uClients.read()
# print(flipkartPage) # return huge information

flipkart_html = bs(flipkartPage, 'html.parser')
# print(flipkart_html)

bigboxes = flipkart_html.findAll("div", {"class": "_1AtVbE col-12-12"})
# seacrhing for appropriate tag (div) to redirect to the product link
# print(bigboxes)
del bigboxes[0:3]
box = bigboxes[0]

# print(box)
# print(box.div.div.div.a['href'])


productLink = "https://www.flipkart.com" + box.div.div.div.a['href']
# print(productLink)

prodRes = requests.get(productLink)
# print(prodRes)

prod_html = bs(prodRes.text, "html.parser")
# print(prod_html)

# Showing the Customer comment
commentboxes = prod_html.find_all('div', {'class': "col _2wzgFH"})
# print(commentboxes)


# get the product review
review = prod_html.find_all('p', {'class': "_2-N8zT"})
# print(review)


review_list = []
customer_name_list = []
rating_list = []
comments_list = []

for commentbox in commentboxes:
    try:
        reviews = commentbox.div.find_all('p', {'class': "_2-N8zT"})[0].text
    except:
        reviews = "No reviews"

    try:
        cname = commentbox.find_all('p', {'class': "_2sc7ZR"})[0].text
    except:
        cname = "No name"

    try:
        rating = commentbox.find_all('div', {'class': "_3LWZlK _1BLPMq"})[0].text
    except:
        rating = "No rating"

    try:
        comnts = commentbox.find_all('div', {'class': ""})[0].text
    except:
        comnts = "No Comments"

    print(cname)
    print(reviews)
    print(rating)
    print(comnts)
    print()

    review_list.append(reviews)
    customer_name_list.append(cname)
    rating_list.append(rating)
    comments_list.append(comnts)

mydct = {"Review": review_list, "Customer_Name": customer_name_list,
         "Rating": rating_list, "Customer_Comments": comments_list}

# print(mydct)
