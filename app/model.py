def load_model():
    # dummy model
    return {"coef": 2}

def predict(model, x: float):
    return model["coef"] * x
