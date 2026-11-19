<div align="center">

![Series Sentinel banner](https://capsule-render.vercel.app/api?type=waving&color=0:#854d0e,100:#0f766e&height=170&section=header&text=Series%20Sentinel&fontSize=34&fontColor=ffffff)

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=18&pause=1000&color=0f766e&center=true&vCenter=true&width=720&lines=Spot%20unusual%20data%20points%20early%3BRobust%20rolling%20anomaly%20detection" alt="Typing SVG" />

[![MIT](https://img.shields.io/badge/license-MIT-0f766e.svg)](LICENSE)
[![Python](https://img.shields.io/badge/language-Python-blue.svg)](https://www.python.org/)
[![Stars](https://img.shields.io/github/stars/CyberLoop-dev/series-sentinel?style=flat)](https://github.com/CyberLoop-dev/series-sentinel/stargazers)
[![Last commit](https://img.shields.io/github/last-commit/CyberLoop-dev/series-sentinel)](https://github.com/CyberLoop-dev/series-sentinel/commits/main)

**A small, explainable anomaly detector for CSV time series.**

<img src="assets/illustration.svg" alt="Series Sentinel illustration" width="560" />

</div>

## 🧭 Overview

Series Sentinel scans a numeric CSV column in row order and compares each value with a rolling window of previous observations. It uses the median and median absolute deviation (MAD), making the baseline less sensitive to earlier outliers.

## ✨ Features

- 📈 Reads timestamped or plain numeric CSV series.
- 🧮 Uses rolling median and median absolute deviation.
- 🚩 Reports anomaly rows with baseline and score details.
- 📄 Exports JSON or CSV reports.
- 🐍 Uses only the Python standard library.

## 🖥️ Demo

```bash
python main.py examples/series.csv --value-column value --time-column timestamp --window 5
```
The included sample has one intentionally unusual final observation.

## 🚀 Quick Start

```bash
git clone https://github.com/CyberLoop-dev/series-sentinel.git
cd series-sentinel
python main.py examples/series.csv --value-column value --window 5
```

## 🧱 Tech Stack

- 🐍 Python 3.10+
- 📦 Standard library: argparse, csv, json, statistics

## 🗂️ Folder Structure

```text
series-sentinel/
├── main.py
├── examples/series.csv
├── tests/test_main.py
├── pyproject.toml
├── assets/illustration.svg
├── .gitignore
└── README.md
```

## 🛣️ Roadmap

- [x] Rolling median/MAD detection
- [x] JSON and CSV reports
- [ ] Optional rolling IQR detector

## 🤝 Contributing

Issues and pull requests are welcome. Please include a clear reproduction or sample input and keep changes focused.

## 📄 License

Released under the [MIT License](LICENSE).

<div align="center">

![Footer](https://capsule-render.vercel.app/api?type=waving&color=0:#0f766e,100:#854d0e&height=100&section=footer)

</div>
