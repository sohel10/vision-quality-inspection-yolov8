from api.model_loader import load_model

def test_model_loading():
    model = load_model()
    assert model is not None