def connect(host, *, port=5432, ssl=False):
    print(host, port, ssl)

connect("localhost", port=3306, ssl=True)
