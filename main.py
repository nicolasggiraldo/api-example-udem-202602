import uvicorn

from fastapi import FastAPI
from src.load_model import load_model
from src.input_data import InputData
from conf.parameters import VERSION, HOST, PORT


model = load_model('model.pickle')

app = FastAPI(
    title='FastAPI Example',
    description='This is a simple FastAPI example',
    version=VERSION
)

@app.get("/health")
async def health_check():
    return {
        'status': 'healthy',
        'version': VERSION
    }

@app.post("/predict")
async def predict(input_data: InputData):

    if (input_data.lot_size <= 0) or (input_data.bedrooms <= 0):
        return {
            "error": "Invalid input values. Lot size and bedrooms must be greater than 0",
            "message": "Please provide valid input values"
        }

    X_input = [[input_data.lot_size, input_data.bedrooms]]
    result = model.predict(X_input)[0]
    result = round(result, 0)

    return {
        'result': result
    }


if __name__ == "__main__":
    uvicorn.run(app, host=HOST, port=PORT)
