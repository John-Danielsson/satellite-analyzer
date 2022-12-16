class ImageGatherer:


# https://maps.googleapis.com/maps/api/staticmap?center=40.714728,-73.998672&zoom=12&size=400x400&key=YOUR_API_KEY&signature=YOUR_SIGNATURE
n_requests = 100
apiRequestStart = 'https://maps.googleapis.com/maps/api/staticmap?'
centerLat = 40.714728
centerLon = -73.998672
latDelta = []
lonDelta = []
# for i in range(n_requests):
requests = []
for dx in latDelta:
    for dy in lonDelta:
        requests.append(
            makeRequest(
                apiRequestStart + 
                f'center={centerLat+dx},{centerLon+dy}'
                'size=200x200' +
                '&zoom=20'
            )
        )

def makeRequest(apiRequest):
    return ''