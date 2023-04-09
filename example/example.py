import bugs

if __name__ == "__main__":
    chart = bugs.ChartData()
    print(chart.date)
    for entry in chart:
        print(entry)
