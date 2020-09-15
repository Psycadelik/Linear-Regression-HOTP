import pandas

def generate_csv():
    houses_dict = {
        'area': [1, 2, 3, 4],
        'price': [1, 2, 3, 4]
    }

    dataframe = pandas.DataFrame(houses_dict)

    return dataframe

if __name__ == "__main__":
    generate_csv()
