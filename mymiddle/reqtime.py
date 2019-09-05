from django.utils.deprecation import MiddlewareMixin
from datetime import datetime
from influxdb import InfluxDBClient

class GetReqTime(MiddlewareMixin):
    dtm_start = 0
    dtm_end = 0
    client = InfluxDBClient(database="otus")

    def process_request(self, request):
        self.dtm_start = datetime.now().timestamp()
        print('Middle ware request', self.dtm_start)
        return None


    def process_response(self, request, response):
        self.dtm_end = datetime.now().timestamp()
        print('Middle ware response', self.dtm_end)
        json_data = []
        json_data.append({
            'measurement': 'reqtime',
            'fields': {
                'value': self.dtm_end-self.dtm_start,
            }
        })
        record = self.client.write_points(json_data)
        return response
