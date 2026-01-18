
from semantic_router import Route,RouteLayer
from semantic_router.encoders import HuggingFaceEncoder

encoder = HuggingFaceEncoder(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
)

faq = Route(
    name="faq",
    utterances=[
        "What is the return policy of the products?",
        "Do I get discount with the HDFC credit card?",
        "How can I track my order?",
        "What payment methods are accepted?",
        "How long does it take to process a refund?",
        "Are there any ongoing sales or promotions?",
        "Can I cancel or modify my order after placing it?",
        "Do you offer international shipping?",
        "What should I do if I receive a damaged product?",
        "How do I use a promo code during checkout?",
    ],
)

sql = Route(
    name="sql",
    utterances=[
        "I want to buy nike shoes that have 50% discount.",
        "Are there any shoes under Rs. 3000?",
        "Do you have formal shoes in size 9?",
        "Are there any Puma shoes on sale?",
        "What is the price of puma running shoes?",
    ],
)

talk = Route(
    name="talk",
    utterances=[
        "Hi",
        "Hello",
        "Hey there",
        "Good morning",
        "Good evening",
        "How are you?",
        "How's it going?",
        "What's up?",
        "How are you doing today?",
        "Nice to meet you",
        "Thanks",
        "Thank you so much",
        "Okay",
        "Alright",
        "Bye",
        "Goodbye",
        "See you later",
        "Have a nice day",
    ],
)

router = RouteLayer(routes=[faq, sql,talk],encoder=encoder)

if __name__ == "__main__":
    print(router("See you later").name)
