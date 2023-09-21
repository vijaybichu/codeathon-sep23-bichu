def is_valid_ip_address(ip_address):
    """
    Validates an IP address.

    Args:
        ip_address (str): The IP address to validate.

    Returns:
        bool: True if the IP address is valid, False otherwise.
    """
    try:
        # Split the IP address into its components
        components = ip_address.split('.')
        
        # Check that there are exactly 4 components
        if len(components) != 4:
            raise ValueError('Invalid IP address')
        
        # Check that each component is an integer between 0 and 255
        for component in components:
            if not component.isdigit():
                raise ValueError('Invalid IP address')
            if int(component) < 0 or int(component) > 255:
                raise ValueError('Invalid IP address')
        
        # If all checks pass, the IP address is valid
        return True
    
    except ValueError:
        # If an exception is raised, the IP address is invalid
        return False

import unittest

class TestIsValidIPAddress(unittest.TestCase):
    def test_valid_ip_address(self):
        # Test a valid IP address
        ip_address = '192.168.0.1'
        is_valid = is_valid_ip_address(ip_address)
        self.assertTrue(is_valid)
    
    def test_invalid_ip_address(self):
        # Test an invalid IP address
        ip_address = '256.0.0.1'
        is_valid = is_valid_ip_address(ip_address)
        self.assertFalse(is_valid)
    
    def test_missing_components(self):
        # Test an IP address with missing components
        ip_address = '192.168.1'
        is_valid = is_valid_ip_address(ip_address)
        self.assertFalse(is_valid)
    
    def test_extra_components(self):
        # Test an IP address with extra components
        ip_address = '192.168.0.1.2'
        is_valid = is_valid_ip_address(ip_address)
        self.assertFalse(is_valid)
    
    def test_non_numeric_components(self):
        # Test an IP address with non-numeric components
        ip_address = '192.168.0.a'
        is_valid = is_valid_ip_address(ip_address)
        self.assertFalse(is_valid)

if __name__ == '__main__':
    unittest.main()
