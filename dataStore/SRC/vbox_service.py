import re
import os
import pandas as pd
from matplotlib import pyplot as plt
from dataStore.SRC.SR import create_sr

class VboxDataStore:

    def __init__(self,filename) -> None:
        self.filename = filename
        self.store = []
        self.data = pd.DataFrame()
        self.get_data()

    def get_data(self) -> pd.DataFrame:
        section = None
        column_names = None

        column_name_mapping = {
            'Vbat': 'battery vo',
        }

        with open(self.filename) as raw:
            for line in (line.strip() for line in raw):
                m = re.match(r'\[([\w ]+)\]', line)
                if m:
                    section = m.group(1)

                elif section == 'column names':
                    column_names = [column_name_mapping.get(col, col) for col in line.strip().split()]
                    column_names = [col.replace('-', '_').replace('.', '_') for col in column_names]
                    if column_names[11] == 'vo':
                        column_names.remove('vo')
                    column_names += ['time_of_day', 'lat_deg', 'long_deg', 'split_d']
                    self.data = pd.DataFrame(columns=column_names)
                    #print(column_names)

                elif section == 'data':
                    bits = line.split()
                    fields = list(map(float, line.split()))
                    tstamp = bits[1]
                    (hrs, mins, secs) = int(tstamp[0:2]), int(tstamp[2:4]), float(tstamp[4:])
                    # Add a new field with the time in seconds from midnight
                    time_of_day = 3600 * hrs + 60 * mins + secs
                    fields.append(time_of_day)
                    lat_deg = fields[2] / 60
                    long_deg = -fields[3] / 60
                    split_d = fields[4] / 3.6 * 0.05
                    self.data = self.data.append({
                        'time_of_day': time_of_day,
                        'lat_deg': lat_deg,
                        'long_deg': long_deg,
                        'split_d': split_d,
                        **dict(zip(column_names[:-4], fields))
                    }, ignore_index=True)
            self.data['distance'] = self.data.split_d.cumsum()
            self.data['SplitTime'] = self.data.time_of_day.diff()
            self.data['SessionTime'] = self.data.SplitTime.cumsum()
            #print(self.data.head)
            return self.data
        
    def add_sr(self):
        
        self.get_data()
        data = self.data
        #self.dataframe = pd.DataFrame(data)
        dff = pd.DataFrame(data)
        #df = butterworth(self.dataframe)  
        df = create_sr(dff)
        return df

            
    def get_graph(self):
        #print('we\'ve started')
        self.get_data()
        
        
        x = self.data.SessionTime
        y = self.data.velocity
        d = self.data.distance
        fig, (ax1, ax2) = plt.subplots(2,1)
        ax1.plot(x,y)
        ax1.set_xlabel('T.O.D', fontsize=15)
        ax1.set_ylabel('Velocity (Km/h)', fontsize=15)
        ax2.plot(d,y)
        # get dynamic title set to uploaded csv
        t = self.filename
        ax1.set_title('%s'%t, fontsize=15)

        #plt.scatter(x,y)
        #plt.show()

    def get_csv(self, name):
        os.makedirs('folder/subfolder', exist_ok=True)
        df = self.add_sr()
        df.to_csv(f'folder//subfolder//{name}.csv')


    def reset(self) -> None:
        self.data = []

