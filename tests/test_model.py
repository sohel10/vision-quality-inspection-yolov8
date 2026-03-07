def test_model_loading():
    # simple sanity test
    from api.model_loader import load_model
    assert callable(load_model)