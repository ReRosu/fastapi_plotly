import uvicorn

if __name__ == '__main__':
    uvicorn.run('app.core.asgi:app', reload=False, workers=1, port=8081, host='127.0.0.1')

