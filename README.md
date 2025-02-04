# 🚀 CourseGen - Udemy Course Management CLI

`coursegen` is a **developer-friendly CLI tool** for quickly generating Udemy course project structures. It automates the creation of **Sections and Lectures**, following Udemy's recommended structure.

## **✨ Features**
✅ **Generate Udemy course structures** effortlessly  
✅ **Customizable folder structure** (Sections & Lectures)  
✅ **Global installation support (`pip install coursegen`)**  
✅ **Progress bar & interactive CLI** for a smooth user experience**  

---

## **📥 Installation**
### **🔹 1. Install via `pip` (Recommended)**
Ensure you have **Python 3.8+** installed, then run:
```sh
pip install coursegen
```

### **🔹 2. Install from Source (Development Mode)**
If you want to modify `coursegen`, install it from source:
```sh
git clone https://github.com/yourusername/coursegen.git
cd coursegen
pip install -e .
```

---

## **🚀 Usage**
### **🔹 1. Create a New Udemy Course Structure**
```sh
coursegen create "MyUdemyCourse"
```
📂 **Expected Output**
```
🎯 Generating Udemy Course: MyUdemyCourse
✅ Course structure created successfully!
📂 Open your course folder: file:///C:/Users/sgari/Documents/UdemyCourses/MyUdemyCourse

📎 Sections & Lectures Created:
📁 Section01
   📄 Lecture01
```

### **🔹 2. List Available Courses**
```sh
coursegen list
```

### **🔹 3. Delete a Course**
```sh
coursegen delete "MyUdemyCourse"
```

---

## **🛠 Configuration**
By default, `coursegen` creates courses in:
```
C:\Users\sgari\Documents\UdemyCourses
```
You can change this in `settings.json`:
```json
{
    "course_directory": "C:\\Custom\\Path\\To\\UdemyCourses"
}
```

---

## **🛠 Development & Contribution**
### **🔹 1. Set Up a Local Development Environment**
```sh
git clone https://github.com/yourusername/coursegen.git
cd coursegen
pip install -r requirements.txt
```

### **🔹 2. Running Tests**
```sh
pytest tests/
```

### **🔹 3. Follow Conventional Commits**
```sh
git commit -m "feat(cli): added progress bar for course creation"
```

### **🔹 4. Create a Feature Branch**
```sh
git checkout -b feat/your-feature
```
Then push it to GitHub and create a Pull Request (PR).

---

## **📜 License**
This project is licensed under the **MIT License** – see the [`LICENSE`](LICENSE) file for details.

---

## **📞 Support & Feedback**
📩 **Found an issue?** Submit a [GitHub Issue](https://github.com/yourusername/coursegen/issues).  
💡 **Have a feature request?** Create a new [Discussion](https://github.com/yourusername/coursegen/discussions).  
🫶 **Want to contribute?** Fork the repo and open a Pull Request!  

---

