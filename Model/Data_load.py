import glob


def load_data(location):
    data = []
    for name in glob.glob(location):
        file = open(name, encoding="utf8", errors='ignore')
        s = file.read()
        data.append([s, location])
    return data