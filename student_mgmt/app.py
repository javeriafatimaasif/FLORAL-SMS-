from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import json, os, uuid
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'javyriyah_secret_garden_2024'

DATA_FILE = 'students.json'

def load_students():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []

def save_students(students):
    with open(DATA_FILE, 'w') as f:
        json.dump(students, f, indent=2)

@app.route('/')
def index():
    students = load_students()
    total = len(students)
    avg_gpa = round(sum(float(s.get('gpa', 0)) for s in students) / total, 2) if total else 0
    departments = list(set(s.get('department', '') for s in students))
    return render_template('index.html', students=students, total=total, avg_gpa=avg_gpa, departments=departments)

@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        students = load_students()
        student = {
            'id': str(uuid.uuid4())[:8].upper(),
            'name': request.form['name'],
            'email': request.form['email'],
            'age': request.form['age'],
            'department': request.form['department'],
            'year': request.form['year'],
            'gpa': request.form['gpa'],
            'phone': request.form['phone'],
            'status': request.form.get('status', 'Active'),
            'enrolled': datetime.now().strftime('%B %d, %Y'),
            'avatar_color': request.form.get('avatar_color', '#f9a8d4'),
        }
        students.append(student)
        save_students(students)
        flash('🌸 Student added to the garden successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('add_student.html')

@app.route('/edit/<student_id>', methods=['GET', 'POST'])
def edit_student(student_id):
    students = load_students()
    student = next((s for s in students if s['id'] == student_id), None)
    if not student:
        flash('Student not found 🌷', 'error')
        return redirect(url_for('index'))
    if request.method == 'POST':
        idx = next(i for i, s in enumerate(students) if s['id'] == student_id)
        students[idx].update({
            'name': request.form['name'],
            'email': request.form['email'],
            'age': request.form['age'],
            'department': request.form['department'],
            'year': request.form['year'],
            'gpa': request.form['gpa'],
            'phone': request.form['phone'],
            'status': request.form.get('status', 'Active'),
            'avatar_color': request.form.get('avatar_color', '#f9a8d4'),
        })
        save_students(students)
        flash('🌼 Student details updated beautifully!', 'success')
        return redirect(url_for('index'))
    return render_template('edit_student.html', student=student)

@app.route('/delete/<student_id>', methods=['POST'])
def delete_student(student_id):
    students = load_students()
    students = [s for s in students if s['id'] != student_id]
    save_students(students)
    flash('🍂 Student removed from the garden.', 'info')
    return redirect(url_for('index'))

@app.route('/view/<student_id>')
def view_student(student_id):
    students = load_students()
    student = next((s for s in students if s['id'] == student_id), None)
    if not student:
        flash('Student not found 🌷', 'error')
        return redirect(url_for('index'))
    return render_template('view_student.html', student=student)

@app.route('/search')
def search():
    query = request.args.get('q', '').lower()
    students = load_students()
    results = [s for s in students if query in s['name'].lower() or query in s['department'].lower() or query in s['id'].lower()]
    return jsonify(results)

@app.route('/api/stats')
def stats():
    students = load_students()
    dept_counts = {}
    for s in students:
        d = s.get('department', 'Unknown')
        dept_counts[d] = dept_counts.get(d, 0) + 1
    return jsonify({'total': len(students), 'departments': dept_counts})

if __name__ == '__main__':
    app.run(debug=True)
