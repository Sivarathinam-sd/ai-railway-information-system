class TrainQueryService:
    def __init__(self, trains, stations):
        self.trains = trains
        self.stations = stations

    def get_trains_between(self, origin, destination):
        origin_trains = self.stations.get(origin)
        destination_trains = self.stations.get(destination)

        if not origin_trains or not destination_trains:
            return f"There are no Trains running between {origin} and {destination}"

        trains_from_origin = {list(t.keys())[0] for t in origin_trains}
        trains_from_destination = {list(t.keys())[0] for t in destination_trains}

        common_trains = trains_from_origin & trains_from_destination
        valid_trains = []
        
        for train in common_trains:
            d1, d2 = 0, 0
            for route in self.trains[train]['routes']:
                if origin in route:
                    d1 = route[origin].split()[0]
                if destination in route:
                    d2 = route[destination].split()[0]
            if int(d1) < int(d2):
                # Extract departure and arrival times for this train from all origin_trains
                
                start = [i.get(train, {}).get('departs') for i in self.stations[origin] if i.get(train)]
                stop  = [i.get(train, {}).get('arrives') for i in self.stations[destination] if i.get(train)]

                # Get train name safely
                train_name = self.trains.get(train, {}).get('trainName')

                # Append valid train details with start/stop times
                if train_name:
                    valid_trains.append({
                        'trainNumber': train,
                        'trainName': train_name,
                        'startTimes': start[0],
                        'stopTimes': stop[0]
                    })


        return valid_trains
    
    def get_train_schedule(self, train_number, origin=None):
        if self.trains.get(train_number, None):
            train_name = self.trains.get(train_number, {}).get('trainName')
            if not origin:
                return {'trainNumber' : train_number,
                        'trainName' : train_name,
                        'trainTimings' : [
                            { 'start' : f"Day {self.trains[train_number]['start'][0]} - {self.trains[train_number]['start'][1]}",
                            'end' : f"Day {self.trains[train_number]['end'][0]} - {self.trains[train_number]['end'][1]} "
                            }
                            ]
                ,
                'route' : self.trains[train_number]['route']
                }
            
            else:
                if self.stations.get(origin, None):
                    return {'trainNumber' : train_number,
                            'trainName' : train_name,
                            'trainTimings' : [

                        i[train_number]
                        for i in self.stations[origin]
                        if train_number in i
                    ],
                    'station' : origin
                    }
                else:
                    return "Station Not Found"
        else:
            return 'Train Not Found'
        
    def get_running_days(self, train_number):
        if self.trains.get(train_number, None):
            days_dict = {'SUN': True, 'MON': True, 'TUE': False, 'WED': True, 'THU': True, 'FRI': False, 'SAT': True}
            days_list = [day for day, is_available in days_dict.items() if is_available]
            return {'trainNumber': train_number, 'trainName': self.trains[train_number]['trainName'], 'runningDays' : days_list, 'route' : self.trains[train_number]['route']  }
        else:
            return 'Train Not Found'

    def get_train_routes(self, train_number):
        if self.trains.get(train_number, None):
            return {'trainNumber': train_number, 'trainName': self.trains[train_number]['trainName'], 'routes': self.trains[train_number]['routes'], 'route' : self.trains[train_number]['route']}
        else:
            return 'Train Not Found'
        
    def get_all_stations(self):
        return ", ".join(list(self.stations.keys()))