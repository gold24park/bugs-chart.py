# 🅱️ 벅스차트 API : bugs-chart.py
![bugs](./image.png)

bugs-chart.py is a Python API that retrieves the TOP 100 information from the [Bugs](https://music.bugs.co.kr/).

## Installation
```commandline
pip install bugs-chart.py
```

## Quickstart
The main usage of bugs-chart.py is similar to [billboard.py](https://github.com/guoguo12/billboard-charts).
```commandline
>>> from bugs import *
>>> chart = ChartData(chartType=BugsChartType.Domestic)
>>> print(chart[0].json())
{
    "artist": "IVE (아이브)",
    "image": "https://image.bugsm.co.kr/album/images/256/40849/4084947.jpg",
    "lastPos": 1,
    "peakPos": 1,
    "rank": 1,
    "title": "Kitsch"
}
>>> print(chart.date)
2023-04-09 12:00:00
```

### ChartData Arguments
- `date` – The chart date
- `chartType`
  - BugsChartType.All – 전체
  - BugsChartType.Domestic – 국내
  - BugsChartType.International – 해외
- `chartPeriod`
  - BugsChartPeriod.Realtime – 실시간
  - BugsChartPeriod.Daily – 일간
  - BugsChartPeriod.Weekly – 주간
- `imageSize` – The size of cover image for the track. (default: 256)
- `fetch` – A boolean value that indicates whether to retrieve the chart data immediately. If set to `False`, you can fetch the data later using the `fetchEntries()` method.

### Chart entry attributes
`ChartEntry` can be accessed using the `ChartData[index]` syntax. A `ChartEntry` instance has the following attributes:
- `title` – The title of the track
- `artist` – The name of the artist
- `image` – The URL of the cover image for the track
- `peakPos` - The track's peak position on the chart.
- `lastPos` - The track's last position on the previous period.
- `rank` – The track's current rank position on the chart.

### K-Pop music chart Python APIs
- [Melon | melon-chart.py](https://github.com/gold24park/melon-chart.py)
- [Bugs | bugs-chart.py](https://github.com/gold24park/bugs-chart.py)
- [Genie | genie-chart.py](https://github.com/gold24park/genie-chart.py)
- [Vibe | vibe-chart.py](https://github.com/gold24park/vibe-chart.py)
- [Flo | flo-chart.py](https://github.com/gold24park/flo-chart.py)

## Dependencies
- [requests](https://requests.readthedocs.io/en/latest/)

## License
This project is licensed under the MIT License.
