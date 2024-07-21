import openai
import os
import string
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to normalize text by removing punctuation and extra spaces
def normalize_text(text):
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = ' '.join(text.split())
    return text.lower()

# Expanded corpus with more questions and answers
corpus = {
    normalize_text("What is your best red wine?"): "Our best red wine is the 2018 Merlot. It's a full-bodied wine with notes of blackberry and plum.",
    normalize_text("Tell me more about the 2018 Merlot."): "The 2018 Merlot is aged for 18 months in French oak barrels, giving it a smooth finish with hints of vanilla and spice. It's perfect for pairing with red meats and hearty pasta dishes.",
    normalize_text("What are your hours of operation?"): "We are open from 10 AM to 6 PM, Monday through Saturday.",
    normalize_text("Do you offer wine tasting events?"): "Yes, we offer wine tasting events every Friday and Saturday from 2 PM to 5 PM. You can try a selection of our best wines and learn more about the winemaking process.",
    normalize_text("How can I book a wine tasting event?"): "You can book a wine tasting event by visiting our website and filling out the booking form, or by calling our customer service at (555) 123-4567.",
    normalize_text("What is the price range of your wines?"): "Our wines range from $20 to $150 per bottle, depending on the variety and vintage.",
    normalize_text("Do you offer any discounts?"): "Yes, we offer a 10% discount on purchases of 12 bottles or more. We also have seasonal promotions and special discounts for members of our wine club.",
    normalize_text("How can I join the wine club?"): "You can join our wine club by signing up on our website. Membership includes exclusive discounts, invitations to special events, and access to limited edition wines.",
    normalize_text("Can I order wine online?"): "Yes, you can order wine directly from our website. We offer shipping to most states in the US.",
    normalize_text("What are your shipping policies?"): "We offer standard and expedited shipping options. Standard shipping usually takes 5-7 business days, while expedited shipping takes 2-3 business days. Shipping rates vary based on the destination and the number of bottles ordered.",
    normalize_text("Do you ship internationally?"): "Currently, we only ship within the United States. We hope to offer international shipping in the near future.",
    normalize_text("What is your return policy?"): "If you are not satisfied with your purchase, you can return the unopened bottles within 30 days for a full refund. Please contact our customer service for assistance with returns.",
    normalize_text("Do you offer gift cards?"): "Yes, we offer gift cards in various denominations. They can be purchased on our website and are perfect for any wine lover.",
    normalize_text("What are your most popular wines?"): "Our most popular wines include the 2018 Merlot, the 2020 Chardonnay, and the 2019 Cabernet Sauvignon.",
    normalize_text("Tell me more about the 2020 Chardonnay."): "The 2020 Chardonnay is a crisp and refreshing wine with notes of green apple and citrus. It's aged in stainless steel tanks, which preserves its bright acidity and clean finish. It's great with seafood and light pasta dishes.",
    normalize_text("Tell me more about the 2019 Cabernet Sauvignon."): "The 2019 Cabernet Sauvignon is a robust wine with flavors of dark cherry, chocolate, and a hint of oak. It's aged for 24 months in American oak barrels, giving it a rich and complex profile. It pairs well with steak, lamb, and aged cheeses.",
    normalize_text("Do you offer tours of your vineyard?"): "Yes, we offer guided tours of our vineyard. Tours are available by appointment and include a walk through the vineyard, a visit to the winery, and a tasting of our current releases.",
    normalize_text("How can I book a vineyard tour?"): "You can book a vineyard tour by visiting our website and filling out the tour booking form, or by calling our customer service at (555) 123-4567.",
    normalize_text("Where are you located?"): "We are located at 123 Vine Street, Wine Country, CA 98765.",
    normalize_text("Do you have a physical store?"): "Yes, we have a tasting room and store at our vineyard where you can sample and purchase our wines.",
    normalize_text("What safety measures are you taking due to COVID-19?"): "We are following all recommended health guidelines, including social distancing, regular sanitization of our facilities, and limiting the number of guests in our tasting room and on tours. Masks are required for all guests and staff.",
    normalize_text("Can I host a private event at your vineyard?"): "Yes, we offer facilities for private events such as weddings, corporate events, and family gatherings. Please contact our events coordinator for more information and availability.",
    normalize_text("How can I contact customer service?"): "You can contact our customer service by calling (555) 123-4567, or by emailing us at support@winebusiness.com.",
    normalize_text("Do you have any organic wines?"): "Yes, we offer a selection of organic wines that are made from grapes grown without synthetic pesticides or fertilizers. Look for the organic label on our website or in our store.",
    normalize_text("What are the benefits of joining your wine club?"): "Members of our wine club receive exclusive discounts, early access to new releases, invitations to members-only events, and a quarterly shipment of selected wines.",
    normalize_text("Can I customize my wine club shipments?"): "Yes, you can customize your wine club shipments by selecting your preferred wines from our current offerings. You can also choose the frequency of your shipments.",
    normalize_text("Do you have a loyalty program?"): "Yes, we have a loyalty program where you earn points for every purchase. Points can be redeemed for discounts on future orders.",
    normalize_text("What types of wines do you produce?"): "We produce a variety of wines including red, white, rosé, and sparkling wines. Our most popular varieties are Merlot, Cabernet Sauvignon, Chardonnay, and Pinot Noir.",
    normalize_text("Do you have any vegan wines?"): "Yes, we offer a selection of vegan wines that are made without any animal-derived fining agents. Look for the vegan label on our website or in our store.",
}

def generate_response(user_message, context):
    print(f"User message: {user_message}")
    normalized_message = normalize_text(user_message)
    print(f"Normalized message: {normalized_message}")
    
    # Find the best matching response
    response = "Please contact the business directly for more information."
    for key in corpus:
        if key in normalized_message:
            response = corpus[key]
            break
    
    print(f"Response: {response}")
    return response

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    context = request.json.get('context', [])
    bot_response = generate_response(user_message, context)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
