# 🏋️ Workout Tracker using Nutritionix API & Sheety API

A Python-based Workout Tracker that accepts natural language exercise input, calculates calories burned using the Nutritionix API, and automatically stores workout history in Google Sheets using the Sheety API.

---

## 🚀 Features

- 🏃 Accepts workout input in natural language
- 🔥 Calculates calories burned automatically
- ⏱ Tracks exercise duration
- 📅 Stores workout history with date and time
- 📊 Saves data directly into Google Sheets
- 🔐 Secure API key management using `.env`
- 🔑 Supports both Bearer Token and Basic Authentication for Sheety API

---

## 🛠 Technologies Used

- Python
- Requests
- Nutritionix API
- Sheety API
- Google Sheets
- python-dotenv

---

## 📂 Project Structure

```
Workout-Tracker/
│
├── screenshots/
│   ├── terminal-output.png
│   └── workout-sheet.png
│
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Workout-Tracker.git
```

Move into the project folder

```bash
cd Workout-Tracker
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file and add your credentials.

Run the project

```bash
python main.py
```

---

## 📸 Screenshots

### Terminal Output

![Terminal Output](screenshots/terminal-output.png)

### Google Sheets Output

![Google Sheets Output](screenshots/workout-sheet.png)

---

## 💻 Example Input

```
cycled for 45 minutes
```

---

## ✅ Example Output

```
Tell me which exercise you did: cycled for 45 minutes

✅ Cycling added successfully!

🎉 Workout data saved successfully!
```

---

## 🔐 Environment Variables

Create a `.env` file and configure the following variables:

```
APP_ID=YOUR_APP_ID
API_KEY=YOUR_API_KEY
EXERCISE_ENDPOINT=YOUR_EXERCISE_ENDPOINT

SHEETY_ENDPOINT=YOUR_SHEETY_ENDPOINT

# Choose ONE authentication method

# Option 1
SHEETY_TOKEN=YOUR_BEARER_TOKEN

# Option 2
SHEETY_USERNAME=YOUR_USERNAME
SHEETY_PASSWORD=YOUR_PASSWORD
```

---

## 📌 Future Improvements

- GUI using Tkinter or CustomTkinter
- Daily workout summary
- Weekly statistics
- Monthly progress report
- BMI calculator
- Data visualization using Matplotlib

---

## 👨‍💻 Author

**Pratik Prajapati**

GitHub: https://github.com/pratikxdev

---

⭐ If you found this project helpful, consider giving it a Star!
