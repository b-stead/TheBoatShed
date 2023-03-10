from dataStore.SRC.vbox_service import VboxDataStore

class VBoxController(object):

    def __init__(self,filename):
        self.data_store: VboxDataStore = VboxDataStore(filename)
        self.dataframe  = None

    def get_data(self):
        self.dataframe = self.data_store.get_data()
        return self.dataframe

    def get_graph(self):
        self.data_store.get_graph()

    def add_sr(self):
        self.data_store.add_sr()

    def get_csv(self):
        name = input("enter file name: ")
        self.data_store.get_csv(name)
        

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='VBox Controller')
    parser.add_argument('command', type=str, help='Enter a command: get_graph')
    parser.add_argument('filename', type=str, help='Enter the filename')
    args = parser.parse_args()
    
    a = VBoxController(args.filename)
    if args.command == 'graph':
        a.get_graph()

    elif args.command == 'SR':
        a.add_sr()

    elif args.command == 'csv':
        a.get_csv()