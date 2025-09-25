def make_cars(name:str, model:str, **kwargs):
    car_info:dict = {"name": name, "model": model}
    car_info.update(kwargs)
    return car_info



car = make_cars("Stelvio", "Alfa Romeo", color="red", fxf=False)

print(car)