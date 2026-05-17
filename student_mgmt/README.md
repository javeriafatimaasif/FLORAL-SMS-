# 🌸 Student Management System
### Designed by Javyriyah Fatima

A dreamy, garden-themed Flask web application for managing students beautifully.

---

## ✨ Features

- 🌸 **Dashboard** — Stats overview, live search, filter by department & status
- 🌱 **Add Students** — Full form with avatar color picker
- ✏️ **Edit Students** — Update any detail seamlessly
- 👁 **View Profile** — Elegant student profile with GPA circle visualization
- 🗑 **Delete** — Remove students with confirmation
- 🔍 **Live Search** — Real-time search dropdown as you type
- 💾 **JSON Storage** — No database needed, data stored in `students.json`

---

## 🚀 Setup & Run

```bash
# 1. Navigate to the project folder
cd student_mgmt

# 2. Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python app.py
```

Then open your browser at: **http://127.0.0.1:5000**

---

## 📁 Project Structure

```
student_mgmt/
├── app.py               # Flask application
├── students.json        # Data storage (auto-created)
├── requirements.txt     # Python dependencies
└── templates/
    ├── base.html        # Base layout (navbar, footer, petals)
    ├── index.html       # Dashboard
    ├── add_student.html # Add student form
    ├── edit_student.html# Edit student form
    └── view_student.html# Student profile page
```

---

## 🎨 Theme

Dreamy pastel pink garden aesthetic with:
- Floating flower petals animation
- Glassmorphism cards
- Playfair Display serif typography
- Soft blush & lavender color palette
- Smooth hover & transition animations

---

*Crafted with 🌸 by Javyriyah Fatima*
