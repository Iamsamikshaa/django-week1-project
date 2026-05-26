# 📁 Django File Explorer

A modern Django-based File Explorer web application with dark mode, file upload, download, preview, delete functionality, search bar, breadcrumbs, and secure directory browsing.

---

## 🚀 Features

- ✅ File & Folder Explorer
- ✅ Folder Navigation
- ✅ Dynamic Breadcrumb Navigation
- ✅ Dark Mode UI
- ✅ Search Files/Folders
- ✅ File Upload
- ✅ File Download
- ✅ File Delete
- ✅ Image Preview
- ✅ File Type Icons
- ✅ Hover Effects
- ✅ Responsive UI
- ✅ Secure Base Directory Restriction
- ✅ Error Handling
- ✅ Hidden Files Protection

---

## 🛠️ Technologies Used

- Python
- Django
- HTML
- CSS
- JavaScript
- Font Awesome

---

## 📂 Project Structure

```bash
django-week1-project/
│
├── explorer/
│   ├── templates/
│   │   └── explorer/
│   │       ├── explore.html
│   │       └── error.html
│   │
│   ├── views.py
│   ├── apps.py
│   └── __init__.py
│
├── fileexplorer/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── __init__.py
│
├── public_files/
│   ├── demo.txt
│   ├── images/
│   └── videos/
│
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation Guide

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Iamsamikshaa/django-week1-project.git
```

### 2️⃣ Open Project Folder

```bash
cd django-week1-project
```

### 3️⃣ Install Required Packages

```bash
pip install -r requirements.txt
```

---

## ▶️ Run The Project

### Run Database Migration

```bash
python manage.py migrate
```

### Start Django Server

```bash
python manage.py runserver
```

### 🌐 Open In Browser

```
http://127.0.0.1:8000/
```

---

## 📸 Main Functionalities

### 📁 File Explorer
- Browse folders and files
- Open nested directories
- Breadcrumb navigation

### 🔍 Search Functionality
- Instant file filtering
- Dynamic table search

### 📤 File Upload
- Upload files directly from browser
- Save inside current directory

### ⬇️ File Download
- Download any uploaded file

### 🗑️ File Delete
- Delete files with confirmation

### 🖼️ Image Preview
- Preview JPG / PNG images in browser

### 🎨 Modern UI
- Dark mode interface
- Hover effects
- Font Awesome icons
- Responsive layout

---

## 🔐 Security Features

- ✅ Restricted to `public_files` directory only
- ✅ Hidden files blocked
- ✅ Path traversal protection
- ✅ Basic error handling implemented

---

## 📦 Python Modules Used

```python
os
datetime
django.shortcuts
django.http
django.conf
```

---

## 📌 Future Improvements

- Grid View
- Drag & Drop Upload
- File Rename
- Create Folder
- User Authentication
- Storage Statistics
- Mobile Optimization
- Video Player
- Audio Player

---

## 🧠 Learning Concepts Covered

- Django Routing
- Django Templates
- Python `os` Module
- Dynamic Path Handling
- File Handling
- File Uploads
- Django Views
- Static Styling
- Error Handling
- Secure Path Validation

---

## 👨‍💻 Author

**Samiksha Kakde**

## ⭐ GitHub Repository

[https://github.com/Iamsamikshaa/django-week1-project](https://github.com/Iamsamikshaa/django-week1-project)
