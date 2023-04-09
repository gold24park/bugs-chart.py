# bugs-chart.py
bugs-chart.py is a Python API that retrieves the TOP 100 information from the 'Bugs'.

## Installation
```commandline
pip install bugs-chart.py
```

## Quickstart
The main usage of bugs-chart.py is similar to [billboard.py](https://github.com/guoguo12/billboard-chart).
```commandline
>>> from bugs import *
>>> chart = ChartData(chart_type=BugsChartType.Domestic)
>>> print(chart[0])
'Kitsch' by IVE (아이브)
```

### ChartData Arguments
- `chart_type`
  - BugsChartType.All – 전체
  - BugsChartType.Domestic – 국내
  - BugsChartType.International – 해외
- `chart_preiod`
  - BugsChartPeriod.Realtime – 실시간
  - BugsChartPeriod.Daily – 일간
  - BugsChartPeriod.Weekly – 주간
- `image_size` – The size of cover image for the track. (default: 256)
- `fetch` – A boolean value that indicates whether to retrieve the chart data immediately. If set to `False`, you can fetch the data later using the `fetchEntries()` method.

### Chart entry attributes
`ChartEntry` can be accessed using the `ChartData[index]` syntax. A `ChartEntry` instance has the following attributes:
- `title` – The title of the track
- `artist` – The name of the artist
- `image` – The URL of the cover image for the track
- `peakPos` - The track's peak position on the chart.
- `lastPos` - The track's last position on the previous period.
- `rank` – The track's current rank position on the chart.

## Dependencies
- [requests](https://requests.readthedocs.io/en/latest/)

## License
This project is licensed under the MIT License.