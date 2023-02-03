def get_from_file():
    result = []
    with open('cities.csv') as file:
        for line in file:
            result.append(line.replace("\n", "").split(';'))

    return result

