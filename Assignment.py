import requests
from bs4 import BeautifulSoup

# Make a request to the URL

url = "https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_1"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the product information
    products = soup.find_all("div", class_="aok-relative")
    for product in products:
        # Get the product URL
        product_url = product.find("a-page")["href"]

        # Get the product name
        product_name = product.find("h3").text

        # Get the product price
        product_price = product.find("span", class_="a-price").text

        # Get the rating
        rating = product.find("span", class_="a-icon").text

        # Get the number of reviews
        num_reviews = product.find("span", class_="review-count").text

        # Print the information
        print("Product URL:", product_url)
        print("Product Name:", product_name)
        print("Product Price:", product_price)
        print("Rating:", rating)
        print("Number of Reviews:", num_reviews)
else:
    print("Request failed")