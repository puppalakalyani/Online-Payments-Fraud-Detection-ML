# Online Payments Fraud Detection - Setup Guide

## Windows Setup Instructions

### 1. Install Python
1. Download Python from [python.org](https://www.python.org/downloads/)
   - Choose Python 3.10 or later
   - During installation, check "Add Python to PATH"
2. Verify installation by opening Command Prompt and typing:
   ```
   python --version
   ```

### 2. Install Git (Optional, for version control)
1. Download Git from [git-scm.com](https://git-scm.com/download/win)
2. Install with default options
3. Verify installation:
   ```
   git --version
   ```

### 3. Project Setup
1. Create a project directory:
   ```
   mkdir fraud_detection
   cd fraud_detection
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   ```
   venv\Scripts\activate
   ```

4. Install required packages:
   ```
   pip install flask numpy pandas scikit-learn
   ```

### 4. Project Files
Create the following directory structure:
```
fraud_detection/
├── app.py
├── static/
│   ├── style.css
│   └── model.pkl
├── templates/
│   └── index.html
└── predictions/
    └── transaction_predictions.json
```

## Sharing the Project

### Method 1: ZIP File
1. Compress the entire project folder:
   - Right-click the folder
   - Select "Send to" → "Compressed (zipped) folder"
2. Share the ZIP file

### Method 2: GitHub (Recommended)
1. Create a GitHub account
2. Create a new repository
3. Push your code:
   ```
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin <your-repository-url>
   git push -u origin main
   ```

## Running the Project (For Recipients)

1. Download/clone the project
2. Open Command Prompt in the project directory
3. Create and activate virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate
   ```
4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
5. Run the application:
   ```
   python app.py
   ```
6. Open browser and go to: http://localhost:8080

## Project Structure Explanation

- `app.py`: Main Flask application
- `static/model.pkl`: Trained machine learning model
- `static/style.css`: CSS styling
- `templates/index.html`: HTML template
- `predictions/`: Directory for storing prediction results
- `requirements.txt`: List of Python dependencies

## Troubleshooting

1. Port Issues:
   - If port 8080 is in use, modify the port in `app.py`:
     ```python
     app.run(debug=True, port=<different-port>)
     ```

2. Package Installation Issues:
   - Try updating pip:
     ```
     python -m pip install --upgrade pip
     ```
   - Install packages one by one:
     ```
     pip install flask
     pip install numpy
     pip install pandas
     pip install scikit-learn
     ```

3. Permission Issues:
   - Run Command Prompt as Administrator
   - Check antivirus settings

## Additional Notes

- Keep the virtual environment (`venv` folder) in `.gitignore` when sharing via GitHub
- Include a `requirements.txt` file:
  ```
  pip freeze > requirements.txt
  ```
- For large files (>100MB), use Git LFS or share separately

For any issues or questions, please create an issue on the GitHub repository.
