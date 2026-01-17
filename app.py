#frankfurter uygulamasında open source ve açık euro bazlı kurları alarak döviz çevirici yapımı

#Dış kaynaklı api kullanarak kullanıcı isteklerine yanıt vermek hedeflenmektedir

from flask import Flask, render_template, request,flash,redirect,url_for
import os
import requests

app = Flask(__name__)
app.secret_key = app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "dev-secret-key")


# kur bilgilerini kullanmak üzere formata sokma kur kısaltması ülke para birimi ülke kısaltması sözlüğü
CURRENCY_DATA = {
    'EUR': {'name': 'Euro', 'country': 'eu'},
    'USD': {'name': 'Amerikan Doları', 'country': 'us'},
    'GBP': {'name': 'İngiliz Sterlini', 'country': 'gb'},
    'JPY': {'name': 'Japon Yeni', 'country': 'jp'},
    'TRY': {'name': 'Türk Lirası', 'country': 'tr'},
    'AUD': {'name': 'Avustralya Doları', 'country': 'au'},
    'CAD': {'name': 'Kanada Doları', 'country': 'ca'},
    'CHF': {'name': 'İsviçre Frangı', 'country': 'ch'},
    'CNY': {'name': 'Çin Yuanı', 'country': 'cn'},
    'SEK': {'name': 'İsveç Kronu', 'country': 'se'},
    'NZD': {'name': 'Yeni Zelanda Doları', 'country': 'nz'},
    'MXN': {'name': 'Meksika Pesosu', 'country': 'mx'},
    'SGD': {'name': 'Singapur Doları', 'country': 'sg'},
    'HKD': {'name': 'Hong Kong Doları', 'country': 'hk'},
    'NOK': {'name': 'Norveç Kronu', 'country': 'no'},
    'KRW': {'name': 'Güney Kore Wonu', 'country': 'kr'},
    'INR': {'name': 'Hindistan Rupisi', 'country': 'in'},
    'RUB': {'name': 'Rus Rublesi', 'country': 'ru'},
    'BRL': {'name': 'Brezilya Reali', 'country': 'br'},
    'ZAR': {'name': 'Güney Afrika Randı', 'country': 'za'},
    'DKK': {'name': 'Danimarka Kronu', 'country': 'dk'},
    'PLN': {'name': 'Polonya Zlotisi', 'country': 'pl'},
    'THB': {'name': 'Tayland Bahtı', 'country': 'th'},
    'MYR': {'name': 'Malezya Ringiti', 'country': 'my'},
    'HUF': {'name': 'Macar Forinti', 'country': 'hu'},
    'CZK': {'name': 'Çek Kronu', 'country': 'cz'},
    'ILS': {'name': 'İsrail Şekeli', 'country': 'il'},
    'CLP': {'name': 'Şili Pesosu', 'country': 'cl'},
    'PHP': {'name': 'Filipin Pesosu', 'country': 'ph'},
    'AED': {'name': 'BAE Dirhemi', 'country': 'ae'},
    'SAR': {'name': 'Suudi Riyali', 'country': 'sa'},
    'IDR': {'name': 'Endonezya Rupisi', 'country': 'id'},
    'RON': {'name': 'Rumen Leyi', 'country': 'ro'},
    'BGN': {'name': 'Bulgar Levası', 'country': 'bg'},
    'HRK': {'name': 'Hırvat Kunası', 'country': 'hr'},
    'ISK': {'name': 'İzlanda Kronu', 'country': 'is'}
}

# Yardımcı fonksiyonlar
def get_currency_name(code): #para biriminin tamamını alan fonksiyon
    
    return CURRENCY_DATA.get(code, {}).get('name', code)

def get_country_code(code):
    #ülke kısaltması alan fonksiyon
    return CURRENCY_DATA.get(code, {}).get('country', code.lower()[:2])

def get_currency_flag(code):
   #ülke bayrağo kodu alan fonksiyon
    country_code = CURRENCY_DATA.get(code, {}).get('country', code[:2])
    if not country_code:
        return '🏴'
    
    # ülke kodunda ülke bayrağını bulup gönderir
    country_code = country_code.upper()
    flag = ''.join(chr(127397 + ord(char)) for char in country_code)
    return flag


app.jinja_env.globals.update( #global şekilde tmeplate a gönderilmesi
    get_currency_name=get_currency_name,
    get_country_code=get_country_code,
    get_currency_flag=get_currency_flag
)

API_URL = "https://api.frankfurter.app/latest"

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    # API'den kurları çekme
    response = requests.get(API_URL)
    data = response.json()

    rates = data["rates"]
    rates["EUR"] = 1.0  # Euro'yu base olarak ekle

    if request.method == "POST":
        
        try:

            # Form doldurulup çeviri yapılmıştır
            amount = float(request.form["amount"])
            from_currency = request.form["from_currency"]
            to_currency = request.form["to_currency"]

            if amount <= 0:
                flash("Girilen Miktar 0'dan Büyük Olmalıdır !!!","danger")

                return redirect(url_for("index"))
            
            elif from_currency == to_currency:

                flash("Hesaplanacak Para Birimleri Aynı Olamaz !","warning")

                return redirect(url_for("index"))
            
            else:
                # Çapraz kur hesabı
                result = amount * (rates[to_currency] / rates[from_currency])
                flash("Döviz Çevirme İşlemi Başarılı !","success")

        except Exception:
            flash("Bir Hata Oluştu Lütfen Tekrar Deneyin !!!","danger")
            return redirect(url_for("index"))
        

    return render_template("index.html", rates=rates, result=result)


if __name__ == "__main__":
    app.run(debug=True)