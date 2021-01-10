#web: gunicorn --bind 0.0.0.0:$PORT -k uvicorn.workers.UvicornWorker app.main:app
web: uvicorn app.main:app --host=0.0.0.0 --port=${PORT:-5000} --workers 4