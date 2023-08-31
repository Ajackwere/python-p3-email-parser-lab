# your code goes here!
class EmailAddressParser:
    def __init__(self, email_string):
        self.email_string = email_string

    def parse(self):
        addresses = self.email_string.replace(",", " ").split()
        parsed_addresses = []
        for address in addresses:
            address = address.strip()
            if "@" in address and "." in address:
                parsed_addresses.append(address)
        unique_addresses = set(parsed_addresses)
        sorted_addresses = sorted(unique_addresses)
        return sorted_addresses
    