# url_shorter
FastApi service for creating shortened links

# Install

1. Create venv
    ```
    python -m venv .venv
    ```
2. Activate venv
3. Install requirements
    ```
    pip install -r requirements.txt
    ```
4. Create postgres database
5. Rename .env.example -> .env
5. Fill in the connection details and domain name in .env
6. Run server
    ```bash
    uvicorn main:app --reload
    ```