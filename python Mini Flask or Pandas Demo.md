Code: 
Text file: teest27.py

from flask import Flask, jsonify, request

  

app = Flask(__name__)

  

weather_data = {

"kyiv": {"temp": 15, "condition": "cloudy"},

"san francisco": {"temp": 18, "condition": "foggy"},

"berlin": {"temp": 12, "condition": "rainy"}

}

  

@app.route("/")

def home():

return jsonify({"message": "Hello, would you like to know today's weather forecast?"})

  

@app.route("/weather")

def get_weather():

city = request.args.get("city")

if not city:

return jsonify({"error": "City parameter is missing"}), 400

city = city.lower()

if city in weather_data:

return jsonify({"city": city, "weather": weather_data[city]})

else:

return jsonify({"error": "City not found"}), 404

  

if __name__ == "__main__":

app.run(debug=True)

Разбор:
1. from flask import Flask, jsonify, request
app = Flask(__name__) - импорт модулей flask 
2. weather_data = {
    "kyiv": {"temp": 15, "condition": "cloudy"},
    "san francisco": {"temp": 18, "condition": "foggy"},
    "berlin": {"temp": 12, "condition": "rainy"}
} - словарь с погодой для трёх городов
3. @app.route("/")
def home():
    return jsonify({"message": "Hello, would you like to know today's weather forecast?"}) - декоратор создаёт маршрут, home возвращает с приветствием, message имеет ключ с текстом
4. @app.route("/weather")
def get_weather():
    city = request.args.get("city")
    if not city:
        return jsonify({"error": "City parameter is missing"}), 400
    city = city.lower()
    if city in weather_data:
        return jsonify({"city": city, "weather": weather_data[city]})
    else:
        return jsonify({"error": "City not found"}), 404 - получение параметров города из url сайта, если параметра нету даём ошибку 400, приводим город к нижнему регистру, если город есть в реестре возвращаем данные JSON о погоде, если нет даём ошибку 404
5. if __name__ == "__main__":
    app.run(debug=True) - скрипт запускается напрямую 