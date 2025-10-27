# Domain Model

class User:

    def __init__(self, firstname, lastname, email, telephone, fax, company, address1, address2,
                                     city, zone_id, postcode, country_id, loginname, password):
        self.firstname = firstname   # required
        self.lastname = lastname     # required
        self.email = email           # required
        self.telephone = telephone
        self.fax = fax
        self.company = company
        self.address1 = address1     # required
        self.address2 = address2
        self.city = city             # required
        self.zone_id = zone_id       # required
        self.postcode = postcode     # required
        self.country_id = country_id # required
        self.loginname = loginname   # required
        self.password = password     # required

