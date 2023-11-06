
#########################################
# Methods:
#   1. Name: __init__
#      Arguments: none
#   2. Name: add
#      Purpose: add a password for a service IF it is valid, otherwise do nothing
#      Arguments: one string representing a service name,
#                 one string representing a password
#      Returns: None
#   3. Name: remove
#      Purpose: remove a password for a service
#      Arguments: one string representing a service name
#      Returns: None
#   4. Name: update
#      Purpose: update a password for a service IF it is valid, otherwise do nothing
#      Arguments: one string representing a service name,
#                 one string representing a password
#      Returns: None
#   5. Name: list_services
#      Arguments: none
#      Returns: a list of all the services for which the user has a password
#   6. Name: sort_services_by
#      Arguments: A string, either 'service' or 'added_on',
#                 (Optional) A string 'reverse' to reverse the order
#      Returns: a list of all the services for which the user has a password
#               in the order specified
#   7. Name: get_for_service
#      Arguments: one string representing a service name
#      Returns: the password for the given service, or None if none exists
#
# A reminder of the validity rules:
#   1. A password must be at least 8 characters long
#   2. A password must contain at least one of the following special characters:
#      `!`, `@`, `$`, `%` or `&`
#
# And a new rule: passwords must be unique (not reused in other services).
#
# Example usage:
#   > password_manager = PasswordManager2()
#   > password_manager.add('gmail', '12ab5!678')   # Valid password
#   > password_manager.add('facebook', '$abc1234') # Valid password
#   > password_manager.add('youtube', '3@245256')  # Valid password
#   > password_manager.add('twitter', '12345678')  # Invalid password, so ignored
#   > password_manager.get_for_service('facebook')
#   '$abc1234'
#   > password_manager.list_services()
#   ['gmail', 'facebook', 'youtube']
#   > password_manager.remove('facebook')
#   > password_manager.list_services()
#   ['gmail', 'youtube']
#   > password_manager.update('gmail', '12345678')  # Invalid password, so ignored
#   > password_manager.get_for_service('gmail')
#   '12ab5!678'
#   > password_manager.update('gmail', '%21321415')  # Valid password
#   > password_manager.get_for_service('gmail')
#   '%21321415'
#   > password_manager.sort_services_by('service')
#   ['gmail', 'youtube']
#   > password_manager.sort_services_by('added_on', 'reverse')
#   ['youtube', 'gmail']

# There are many more examples possible but the above should give you a good
# idea.


# class PasswordManager():

#     def __init__(self):
#         self.service_passwords = {}
    
#     def is_valid(self, password):
#         return len(password) > 7 and any(char in "!@$%&" for char in password)
    
#     def add(self, service_name, password):
#         if self.is_valid(password):
#             self.service_passwords[service_name] = password

#     def get_for_service(self, service_name):
#         return self.service_passwords.get(service_name, None)
    
#     def list_services(self):
#         return list(self.service_passwords.keys())

# date_t1 = now1.strftime("%d/%m/%Y %H:%M:%S")

# from datetime import datetime
# now1 = datetime.now()
# # date_t1 = now1.strftime("%H:%M:%S")
# import time
# time.sleep(1)
# now2 = datetime.now()
# # date_t2 = now2.strftime("%H:%M:%S")

# list = [now1, now2]
# print(list)
# print(list.sort(key=lambda date: datetime.strptime(date, "%H:%M:%S")))


from datetime import datetime
class PasswordManager2():
    def __init__(self):
        self.service_passwords = {}
        self.service_passwords_time = {}

    def is_valid(self, password):
        values = list(self.service_passwords.values())
        return len(password) > 7 and any(char in "!@$%&" for char in password) and password not in values
    
    def add(self, service_name, password):
        # add a password for a service IF it is valid, otherwise do nothing
        if self.is_valid(password):
            self.service_passwords[service_name] = password
            self.service_passwords_time[service_name] = {'password': password, 'added_on': datetime.now()}

    def remove(self, service_name):
        # remove a password for a service
        self.service_passwords.pop(service_name)
        self.service_passwords_time.pop(service_name)

    def update(self, service_name, password):
        # update a password for a service IF it is valid, otherwise do nothing
        if self.is_valid(password):
            self.service_passwords[service_name] = password
            self.service_passwords_time[service_name]['password'] = password

    def list_services(self):
        # Returns: a list of all the services for which the user has a password
        return list(self.service_passwords.keys())
    
    def sort_services_by(self, service_or_added_on, reverse = None):
        # Returns: a list of all the services for which the user has a password
        # in the order specified
        if service_or_added_on == 'service' and reverse == None:
            return sorted(list(self.service_passwords.keys()))
        
        elif service_or_added_on == 'service' and reverse:
            return sorted(list(self.service_passwords.keys()), reverse=True)
        
        if service_or_added_on == 'added_on':
            if reverse == None:
                date_sorted = sorted(self.service_passwords_time, key=lambda key: self.service_passwords_time[key]['added_on'])
                # sort service names by 'added_on'
                result = []
                for key in date_sorted:
                    result.append(key)
                return result
                # return key, self.service_passwords_time[key]

            else:
                date_reversed = sorted(self.service_passwords_time, key=lambda key: self.service_passwords_time[key]['added_on'], reverse=True)
                # sort service names by 'added_on' & 'reverse'
                result = []
                for key in date_reversed:
                    result.append(key)
                return result
                # return key, self.service_passwords_time[key]
            
    def get_for_service(self, service_name):
        # Returns: the password for the given service, or None if none exists
        return self.service_passwords.get(service_name, None)
    
    def testing_1(self):
        return 'self.service_passwords: ', self.service_passwords
    def testing_2(self):
        return 'self.service_passwords_time: ', self.service_passwords_time

password_manager = PasswordManager2()
password_manager.add('baidu', '%12345678')
password_manager.add('acebook', '$12345678')
password_manager.add('makersbnb', '$12345678')
# print(password_manager.list_services())
# print(password_manager.sort_services_by('service'))
# print(password_manager.sort_services_by('service', 'reverse'))
print(password_manager.sort_services_by('added_on'))

# print(password_manager.testing_1())
# print(password_manager.testing_2())