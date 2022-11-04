# Vite.js + React + Flask Example

## How to use

Install backend:

```sh
cd api
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Run backend server:
```sh
cd api
export FLASK_APP=app.py
export FLASK_DEBUG=true
cd ..
npm run dev-api
```

Run front-end server (in another terminal window):
```sh
npm run dev
```