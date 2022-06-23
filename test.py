import pytest
from app import app

def setup():
    print("HELLO")

def test_main_page():
    response = app.test_client().get('/')
    assert response.status_code == 200
    print("Main page is accessable!")
    
