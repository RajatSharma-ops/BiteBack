# 🥫 Bite Back

**Bite Back** is a food donation and redistribution platform built using **Flask**. It bridges the gap between food donors and receivers to reduce food waste and help those in need. Developed during **Code Cubicles 3.0 Hackathon**, the project focuses on impact, simplicity, and accessibility.

---

## 🌟 Features

- 📝 **Donor Form** – Submit food donations with quantity, pickup location, and contact.
- 🍽️ **Receiver Form** – NGOs or individuals can request food donations.
- 📬 **Contact Us** – Users can reach out to the Bite Back team.
- 🔐 Authentication-ready structure for future security enhancements.
- 💡 Modular Flask backend and scalable project layout.

---

## 🧰 Tech Stack

| Layer       | Technology      |
|-------------|-----------------|
| **Frontend** | HTML/CSS (custom UI, ongoing updates) |
| **Backend**  | Python with Flask |
| **Database** | SQLite (easy to upgrade to PostgreSQL/MySQL) |
| **Versioning** | Git & GitHub |
| **Deployment** | Docker-ready + CI/CD potential (Render, Railway, etc.) |

---

# 🥫 Bite Back

**Bite Back** is a community-driven food donation platform that connects food donors with people in need. Built during the Code Cubicles 3.0 Hackathon, the project promotes food sharing and minimizes waste through a clean and functional web interface.

## 🌐 Overview

The platform provides:
- A **Donor Form** to submit food donation details.
- A **Receiver Page** to view and claim available donations.
- A **Contact Page** for communication and feedback.
- Backend support for managing submissions, with SQLite database storage.

## 🔧 Tech Stack

| Layer        | Technology           |
|--------------|----------------------|
| Frontend     | HTML, CSS            |
| Backend      | Python, Flask        |
| Database     | SQLite               |
| Deployment   | Docker, Gunicorn     |
| Dev Tools    | Git, GitHub, VS Code |

## 📦 Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/BiteBack.git
   cd BiteBack
   ```

2. Copy the environment file:
   ```bash
   cp .env.example .env
   ```

3. Run the app with Docker Compose:
   ```bash
   docker-compose up -d --build
   ```

4. Access the app at [http://localhost:5050](http://localhost:5050)

## 🔐 Environment Variables

The app requires a `.env` file with:
```
SECRET_KEY=your_secret_key_here
```

## 📁 Project Structure

```
BiteBack/
├── firstapp/
│   ├── app.py
│   ├── models.py
│   ├── routes.py
│   ├── templates/
│   ├── static/
│   └── instance/
├── Dockerfile
├── docker-compose.yml
├── .env.example
└── README.md
```

## 📣 License

This project is open-source and available under the MIT License.