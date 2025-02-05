# 🏦 Budgeting App

## **📌 Project Overview**
This **Budgeting App** is designed to help users track their financial transactions, including **income** and **expenses**. The app provides a simple interface for adding transactions and viewing them in an organized list. Future enhancements will include **data visualization**, **account-based access**, and **better UI/UX**.

---

## **⚙️ Project Management with Poetry**
This project is managed using **Poetry**, which simplifies dependency management and virtual environments.

### **🔧 Setting Up the Project**
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/budgeting_app.git
   cd budgeting_app
2. **Install Dependencies Using Poetry**:
   ```bash
   poetry install
3. **Activate the Virtual Environment**:
   ```bash
   poetry shell
4. **Run the Application**:
   ```bash
   python manage.py runserver

## **📦 Dependencies**
The following dependencies are managed using Poetry and are listed in pyproject.toml:

| Package |	Purpose |
| ------- | ------- |
| Django |	Web framework for building the backend |
| Graphene-Django |	Enables GraphQL functionality |
| Firebase Admin SDK |	Integrates Firebase Firestore for data storage |
| Python-Dotenv |	Loads environment variables from a .env file |
| Google Cloud Firestore | 	Firestore NoSQL database support |
| Urllib3 |	Manages HTTP requests |
| Poetry |	Dependency management and virtual environment control |


**To see all installed dependencies, run**:
   ```bash
   poetry show
```

## **🚀 Future Enhancements**
- Improve UI/UX for a more user-friendly experience.
- Add visual data representations (charts, graphs).
- Implement transaction deletion functionality.
- Introduce user authentication so users only see their own transactions.

## **📝 Notes**
- The .venv/ directory is ignored using .gitignore, as Poetry manages the virtual environment.
- Firebase keys and other sensitive data are stored securely in a .env file and not committed to Git.
