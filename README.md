# AI Document Knowledge Assistant

Django portfolio project: upload PDF -> extract text -> AI summary -> ask questions.

Stack: Python, Django, HTML, CSS, JavaScript, SQLite, PyPDF2, Google Gemini API.

## Windows setup
py -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

Create `.env` from `.env.example`, add GEMINI_API_KEY, then:
python manage.py migrate
python manage.py runserver


