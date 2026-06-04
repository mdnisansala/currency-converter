from flask import Flask, render_template, request
import requests

app = Flask(__name__)

currencies = {
    "USD": "US Dollar",
    "EUR": "Euro",
    "GBP": "British Pound",
    "LKR": "Sri Lankan Rupee",
    "JPY": "Japanese Yen",
    "INR": "Indian Rupee",
    "AUD": "Australian Dollar",
    "CAD": "Canadian Dollar",
    "CNY": "Chinese Yuan"
}

@app.route("/", methods=["GET", "POST"])
def home():

    result = None
    amount = ""
    from_currency = "USD"
    to_currency = "LKR"

    if request.method == "POST":

        amount = float(request.form["amount"])
        from_currency = request.form["from_currency"]
        to_currency = request.form["to_currency"]

        url = f"https://open.er-api.com/v6/latest/{from_currency}"
        data = requests.get(url).json()

        rate = data["rates"][to_currency]
        result = amount * rate

    return render_template(
        "index.html",
        currencies=currencies,
        result=result,
        amount=amount,
        from_currency=from_currency,
        to_currency=to_currency
    )

if __name__ == "__main__":
    app.run(debug=True)