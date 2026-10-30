# 🔄 Unit Converter

A simple full-stack Unit Converter application built using **React, TypeScript, and FastAPI**. Convert values between different units of length, weight, and temperature through a clean and interactive interface.

## 🚀 Features

- **Length Conversion:** Meters, Kilometers, Centimeters, Millimeters, Miles, Yards, Feet, and Inches.
- **Weight Conversion:** Kilograms, Grams, Milligrams, Pounds, and Ounces.
- **Temperature Conversion:** Celsius, Fahrenheit, and Kelvin.
- Interactive tabs to switch between conversion categories.
- Real-time API communication between frontend and backend.
- Results displayed with up to 2 decimal places.
- Responsive user interface.

## 🛠️ Tech Stack

### Frontend
- React
- TypeScript
- Vite
- CSS
- Fetch API

### Backend
- Python
- FastAPI
- Uvicorn

## 📁 Project Structure

```text
unit-converter/
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── App.tsx
│   │   ├── App.css
│   │   ├── index.css
│   │   └── main.tsx
│   ├── index.html
│   ├── package.json
│   ├── package-lock.json
│   └── vite.config.ts
│
├── main.py
├── .gitignore
└── README.md
```

## ⚙️ Installation and Setup

### Prerequisites

- Python 3.10+
- Node.js and npm
- Git

### 1. Clone the repository

```bash
git clone https://github.com/bharath200578/unit-converter.git
```

```bash
cd unit-converter
```

### 2. Start the Backend

Install Python dependencies:

```bash
pip install fastapi uvicorn
```

Run the FastAPI server:

```bash
uvicorn main:app --reload
```

Backend runs at:

`http://127.0.0.1:8000`

API documentation:

`http://127.0.0.1:8000/docs`

### 3. Start the Frontend

Open another terminal:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the React development server:

```bash
npm run dev
```

Frontend runs at:

`http://localhost:5173`

## 🔌 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/length` | Convert length units |
| GET | `/weight` | Convert weight units |
| GET | `/temperature` | Convert temperature units |

### Example API Request

```http
GET /length?length=100&unit1=meters&unit2=kilometers
```

Example response:

```json
{
  "original_length": 100,
  "original_unit": "meters",
  "converted_length": 0.1,
  "converted_unit": "kilometers"
}
```

## 📸 Application Preview

Add your application screenshots here as the project develops.

## 🎯 Learning Objectives

This project helped me practice:

- Building a frontend using React and TypeScript.
- Managing component state using React Hooks.
- Creating REST API endpoints using FastAPI.
- Connecting React with a Python backend.
- Handling HTTP requests and JSON responses.
- Using Git and GitHub for version control.

## 👨‍💻 Author

**Bharath**

GitHub: [@bharath200578](https://github.com/bharath200578)
https://roadmap.sh/projects/unit-converter
---

⭐ If you find this project useful, consider giving it a star!
