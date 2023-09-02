import unittest
from network_scanner import scan_port

class TestNetworkScanner(unittest.TestCase):

    def test_scan_port_open(self):
        # Test if the scan_port function correctly identifies an open port
        ip = "127.0.0.1"
        port = 80

        # Call the scan_port function and assert that it returns True for an open port
        result = scan_port(ip, port)
        self.assertTrue(result)

    def test_scan_port_closed(self):
        # Test if the scan_port function correctly identifies a closed port
        ip = "127.0.0.1"
        port = 8080  # Assuming 8080 is closed

        # Call the scan_port function and assert that it returns False for a closed port
        result = scan_port(ip, port)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
