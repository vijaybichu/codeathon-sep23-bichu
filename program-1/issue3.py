def is_valid_ip_address(ip_address):
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
