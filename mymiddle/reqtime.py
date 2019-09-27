from django.utils.deprecation import MiddlewareMixin
from datetime import datetime
from influxdb import InfluxDBClient


class GetReqTime(MiddlewareMixin):
    dtm_start = 0
    dtm_end = 0
    client = InfluxDBClient(database="otus")
    request_type = ''

    def process_request(self, request):
        self.dtm_start = datetime.now().timestamp()
        self.request_type = str(request)
        print('Middle ware request', self.dtm_start, 'RequesT', self.request_type)
        return None

    def process_response(self, request, response):
        self.dtm_end = datetime.now().timestamp()
        print('Middle ware response', self.dtm_end)
        json_data = []
        json_data.append({
            'measurement': 'reqtime',
            'fields': {
                'value': self.dtm_end-self.dtm_start,
                'reqtype': self.request_type,
            }
        })
        record = self.client.write_points(json_data)
        return response
