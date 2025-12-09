from basic import main

def test_get_weather():
    assert main.get_weather(21) == "hot"
    assert main.get_weather(19) == "cold"
    assert main.get_weather(20) == "cold"