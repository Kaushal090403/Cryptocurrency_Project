from django.shortcuts import render
import requests
def home(request):
    def home(request):
        if request.method == "GET" and request.GET.get("coin"):
            coin = request.GET.get("coin")
            try:
                access_key = "a71df52581b33e8fc0b25a85f7ed6489"
                url = f"https://api.coinlayer.com/live?access_key={access_key}"
                response = requests.get(url)
                data = response.json()

                if coin in data["rates"]:
                    price = data["rates"][coin]
                    msg = f"Currency: {coin}, Price: {price}"
                else:
                    msg = f"Currency '{coin}' not found"

                return render(request, "home.html", {"msg": msg})

            except Exception as e:
                msg = f"Error: {str(e)}"
                return render(request, "home.html", {"msg": msg})
        else:
            return render(request, "home.html")

# Create your views here.
