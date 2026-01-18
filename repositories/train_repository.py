class TrainRepository:
    def __init__(self, schedules):
        self.schedules = schedules
        self.trains = {}
        self.stations = {}
        self._build_trains()
        self._build_stations()

    def _build_trains(self):
        for train in self.schedules:
            self.trains[train['trainNumber']] = {
                'trainName': train['trainName'],
                'route': train['route'],
                'routes': [],
                'runningDays': train['runningDays']
            }
    
    def _build_stations(self):
        for train in self.schedules:
            train_no = train['trainNumber']

            for stop in train['trainRoute']:
                    
                if stop['arrives'] == 'Source':
                    self.trains[train_no]['start'] = [
                        stop['day'], stop['departs']
                    ]

                if stop['departs'] == 'Destination':
                    self.trains[train_no]['end'] = [
                        stop['day'], stop['arrives']
                    ]

                self.trains[train_no]['routes'].append(
                    {stop['stationName']: stop['distance']}
                )

                station_name = stop['stationName']
                station_data = {
                    train_no: {
                        'arrives': stop['arrives'],
                        'departs': stop['departs'],
                        'day': stop['day']
                    }
                }

                self.stations.setdefault(station_name, []).append(station_data)

    def get_trains(self):
        return self.trains

    def get_stations(self):
        return self.stations
