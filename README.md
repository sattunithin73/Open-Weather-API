# 🌦️ Django Weather App

A simple weather application built using Django that fetches real-time weather data using the OpenWeather API.

## 🚀 Features

- Search weather by city name
- Displays temperature, humidity, and weather conditions
- Clean and simple UI
- API integration with OpenWeather

## 🛠️ Tech Stack

- Python
- Django
- HTML, CSS
- OpenWeather API

## 📂 Project Structure

```
weather_project/
│── weather_app/
│── templates/
│── static/
│── db.sqlite3
│── manage.py
```

## ⚙️ Installation & Setup

1. Clone the repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

2. Create virtual environment
```bash
python -m venv env
source env/bin/activate   # Windows: env\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Add your OpenWeather API key

Go to:
```
weather_app/views.py
```
Replace:
```python
api_key = "YOUR_API_KEY"
```

5. Run server
```bash
python manage.py runserver
```

6. Open in browser
```
http://127.0.0.1:8000/
```

## 🔑 API Used

- OpenWeather API (https://openweathermap.org/api)

## 📸 Screenshots

(Add screenshots here if you want)

## 📌 Future Improvements

- Add 5-day forecast
- Improve UI design
- Add location-based weather (GPS)
- Deploy to cloud (Render / AWS)

## 🌐 Live Demo

(Add your deployed link here if available)

## 🤝 Contributing

Feel free to fork this repo and improve it.

## 📄 License

This project is open-source and available under the MIT License.

---

💡 Built as part of learning Django and API integration.
