import unittest
from main import detect
class SeriesTests(unittest.TestCase):
    def test_detects_spike(self):
        rows=[{"v":str(x),"t":str(i)} for i,x in enumerate([10,11,10,12,11,10,92])]
        report=detect(rows,"v","t",window=5,threshold=3.5)
        self.assertEqual(report["anomaly_count"],1)
        self.assertEqual(report["anomalies"][0]["row"],8)
    def test_constant_baseline(self):
        rows=[{"v":str(x)} for x in [5,5,5,5,5,20]]
        self.assertEqual(detect(rows,"v",window=5)["anomaly_count"],1)
    def test_skips_invalid_values(self):
        rows=[{"v":"1"},{"v":"bad"},{"v":"2"}]
        self.assertEqual(detect(rows,"v",window=2)["rows_skipped"],1)
if __name__=="__main__": unittest.main()
