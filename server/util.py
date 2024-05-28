# All the functions are located here
import json
import pickle
import numpy as np
__area_types = None  # variable to store the area_types
__locations = None  # variable to store the locations
__data_columns = None  # variable to store the data_columns from json
__model = None  # variable to store the model
def get_location_names():
    return [location.title() for location in __locations]  # returns all the location names and capitalizes them
def get_area_types():
    return [area_type.title() for area_type in __area_types]  # returns all the area types
def get_estimated_price(location,area_type,size,total_sqft,bath,balcony):
    try:
        loc_index = __data_columns.index(location.lower())
        loc_index1 = __data_columns.index(area_type.lower())
    except:
        loc_index = -1
        loc_index1 = -1
    x = np.zeros(len(__data_columns))
    x[0] = size
    x[1] = total_sqft
    x[2] = bath
    x[3] = balcony
    if loc_index >= 0:
        x[loc_index] = 1
    if loc_index1 >= 0:
        x[loc_index1] = 1
    return round(__model.predict([x])[0], 2)
def load_saved_artifacts():  # load all the artifacts
    print('Loading the saved artifacts..')
    global __data_columns  # declare the variables as global otherwise they are treated as local variables
    global __locations
    global __model
    global __area_types

    with open("./artifacts/columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[8:]
        __area_types = [area_type.replace("  ", " ") for area_type in __data_columns[4:8]]

    with open("./artifacts/pune_house_data_model_pickle", 'rb') as f:
        __model = pickle.load(f)
    print('Successfully loaded the saved artifacts..')

if __name__ == "__main__":
    load_saved_artifacts()
    print(get_area_types())
    # print(get_location_names())
    print(get_estimated_price('Anandnagar', 'Built-up Area', 3, 1440, 2, 3))

