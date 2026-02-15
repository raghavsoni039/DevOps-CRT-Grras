 How to Start Backend

uvicorn app.main:app --host 127.0.0.1 --port 8000

 Nginx

Nginx reverse proxies port 80 to FastAPI on port 8000 using a symlinked config.

 Firewall

INBOUND zone allows only TCP port 80. Backend port is not externally accessible.

