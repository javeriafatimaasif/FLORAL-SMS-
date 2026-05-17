# 🌸 Student Management System

A beautiful, full-stack **Student Management System** built with **Python Flask** and **JSON-based storage**. Manage student records through an elegant, petal-themed web interface featuring real-time search, GPA tracking, department filtering, and full CRUD operations.

---

## ✨ Features

- 📋 **Add, Edit, View & Delete** student records
- 🔍 **Live Search** by name, department, or student ID
- 📊 **Dashboard Stats** — total students, average GPA, department breakdown
- 🎨 **Custom Avatar Colors** per student profile
- 🏷️ **Student Status** — Active, On Leave, Graduated
- 💾 **JSON File Storage** — no database setup required
- 📱 **Responsive UI** with animated floral background and glassmorphism design
- 🔗 **REST API Endpoints** for stats and search

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python, Flask |
| Templating | Jinja2 |
| Storage | JSON file (`students.json`) |
| Frontend | HTML, CSS, Font Awesome |
| Fonts | Playfair Display, DM Sans, Cormorant Garamond |

---

## 📁 Project Structure

```
student_mgmt/
├── app.py                  # Main Flask application
├── students.json           # Data storage file
├── requirements.txt        # Python dependencies
└── templates/
    ├── base.html           # Base layout with navigation & styles
    ├── index.html          # Dashboard & student list
    ├── add_student.html    # Add new student form
    ├── edit_student.html   # Edit student form
    └── view_student.html   # Student profile view
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/student-management-system.git
   cd student-management-system/student_mgmt
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**
   ```bash
   python app.py
   ```

4. **Open in browser**
   ```
   http://127.0.0.1:5000
   ```

> The app comes pre-loaded with 4 sample students so you can explore right away!

---

## 🔗 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Dashboard with student list |
| GET | `/add` | Add student form |
| POST | `/add` | Submit new student |
| GET | `/view/<id>` | View student profile |
| GET | `/edit/<id>` | Edit student form |
| POST | `/edit/<id>` | Update student record |
| POST | `/delete/<id>` | Delete student |
| GET | `/search?q=` | Search students (JSON) |
| GET | `/api/stats` | Department stats (JSON) |

---

## 📸 Sample Data

The app includes 4 pre-loaded students across departments:

| Name | Department | Year | GPA |
|------|-----------|------|-----|
| Ayesha Malik | Computer Science | 3rd | 3.8 |
| Sara Ahmed | Software Engineering | 2nd | 3.5 |
| Zara Khan | Data Science | 4th | 3.2 |
| Hina Fatima | Artificial Intelligence | 1st | 3.9 |

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to open a pull request or file an issue.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

<p align="center">Made with 🌸 by <a href="https://github.com/javeriafatimaasif">Javeria Fatima Asif</a></p>
