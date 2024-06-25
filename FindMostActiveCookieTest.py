import unittest
from FindMostActiveCookie import findMostActiveCookies

class TestMostActiveCookie(unittest.TestCase):
    def test_find_most_active_cookies_single(self):
        log_lines = [
            "cookie,timestamp",
            "AtY0laUfhglK3lC7,2018-12-09T14:19:00+00:00",
            "SAZuXPGUrfbcn5UA,2018-12-09T10:13:00+00:00",
            "5UAVanZf6UtGyKVS,2018-12-09T07:25:00+00:00",
            "AtY0laUfhglK3lC7,2018-12-09T06:19:00+00:00",
            "SAZuXPGUrfbcn5UA,2018-12-08T22:03:00+00:00",
            "4sMM2LxV07bPJzwf,2018-12-08T21:30:00+00:00",
            "fbcn5UAVanZf6UtG,2018-12-08T09:30:00+00:00",
            "4sMM2LxV07bPJzwf,2018-12-07T23:30:00+00:00",
        ]
        result = findMostActiveCookies(log_lines, '2018-12-09')
        self.assertEqual(result, ['AtY0laUfhglK3lC7'])

    def test_find_most_active_cookies_multiple(self):
        log_lines = [
            "cookie,timestamp",
            "AtY0laUfhglK3lC7,2018-12-09T14:19:00+00:00",
            "SAZuXPGUrfbcn5UA,2018-12-09T14:19:00+00:00",
            "AtY0laUfhglK3lC7,2018-12-09T06:19:00+00:00",
            "SAZuXPGUrfbcn5UA,2018-12-09T06:19:00+00:00",
        ]
        result = findMostActiveCookies(log_lines, '2018-12-09')
        self.assertCountEqual(result, ['AtY0laUfhglK3lC7', 'SAZuXPGUrfbcn5UA'])

    def test_find_most_active_cookies_no_result(self):
        log_lines = [
            "cookie,timestamp",
            "AtY0laUfhglK3lC7,2018-12-08T14:19:00+00:00",
            "SAZuXPGUrfbcn5UA,2018-12-08T10:13:00+00:00",
        ]
        result = findMostActiveCookies(log_lines, '2018-12-09')
        self.assertEqual(result, [])

    def test_find_most_active_cookies_expected(self):
        log_lines = [
            "cookie,timestamp",
            "AtY0laUfhglK3lC7,2018-12-08T14:19:00+00:00",
            "SAZuXPGUrfbcn5UA,2018-12-08T10:13:00+00:00",
            "5UAVanZf6UtGyKVS,2018-12-08T07:25:00+00:00",
            "AtY0laUfhglK3lC7,2018-12-08T06:19:00+00:00",
            "SAZuXPGUrfbcn5UA,2018-12-08T22:03:00+00:00",
            "4sMM2LxV07bPJzwf,2018-12-08T21:30:00+00:00",
            "fbcn5UAVanZf6UtG,2018-12-08T09:30:00+00:00",
            "4sMM2LxV07bPJzwf,2018-12-07T23:30:00+00:00",
        ]
        result = findMostActiveCookies(log_lines, '2018-12-08')
        self.assertEqual(result, ['AtY0laUfhglK3lC7', 'SAZuXPGUrfbcn5UA'])

    def test_cookies_with_different_time_zones(self):
        log_lines = [
            "cookie,timestamp",
            "AtY0laUfhglK3lC7,2018-12-09T08:00:00+00:00",
            "SAZuXPGUrfbcn5UA,2018-12-09T08:00:00-05:00",
            "5UAVanZf6UtGyKVS,2018-12-09T08:00:00+02:00"
        ]
        result = findMostActiveCookies(log_lines, '2018-12-09')
        self.assertEqual(result, ['AtY0laUfhglK3lC7', 'SAZuXPGUrfbcn5UA', '5UAVanZf6UtGyKVS'])


if __name__ == '__main__':
    unittest.main()
