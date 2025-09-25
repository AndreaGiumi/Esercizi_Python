from my_project.weather import check_weather
# importare pytest

#passed
# def test_check_weather1():
#     assert check_weather(21.00) == "hot", "temperatures greater than 20 degree \
#         must be considered as hot"
    

# #failed
# def test_check_weather2():
#     assert check_weather(5.00) == "average", "temperature between 10 and 20 degree \
#         must be considered as average temperature"


# #passed
# def test_check_weather3():
#     assert check_weather(5.00) == "cold", "temperatures lower than 10 degree must be considered as cold"


# #passed
# def test_check_weather4():
#     assert check_weather(13.00) == "averege", "temperatures  between 10 and 20 degree  must be conidered as average temperature"


# #failed because every def test_function() is considered as a single test
# def test_check_wether5():
#     assert check_weather(30.00) == "hot", "temperatures greater then 20 degree must be considered as hot"
#     assert check_weather(11.00) == "cold", "temperatures lower then 10 degree must be considered as cold"


@pytest.mark.parametrize("temperature", "expected", [
    (21.00, "hot")
    (13.00, "average")
    (0.00, "cold")
    (15.00, "cold")
])
def test_check_weather(temperature, expected):
    assert check_weather(temperature) == expected