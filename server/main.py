import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# origins = [
#     "http://localhost",
#     "http://localhost:3000",
# ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"data": "this is from backend fastapi"}

@app.get("/cash")
def read_root():
    return {"data":"12/04/2556","Num":"1","Description":"ค่ารถ","Transfer":"Car","R":"n","Receive":"1500","Spend":"0","Balance":"1500"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)