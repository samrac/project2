from myapp import app
import pytest

def test_myapp():
    response = app.test_client().get('/')

    assert response.status_code == 200
#    assert response.data == b'Hello, World!'

#def test_myapp_status():
    response = app.test_client().get('/status', follow_redirects=True)
    assert response.status_code == 200
