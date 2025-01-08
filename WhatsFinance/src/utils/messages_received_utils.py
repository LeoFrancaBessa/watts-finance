from datetime import datetime

class MessagesReceivedUtils:
    def __init__(self, data):
        self.data = data

    def get_data(self):
        return self.data
    
    def get_contact_name(self):
        return self.data['entry'][0]['changes'][0]['value']['contacts'][0]['profile']['name']
    
    def get_contact_number(self):
        return self.data['entry'][0]['changes'][0]['value']['contacts'][0]['wa_id']
    
    def get_message_date(self):
        date = self.data['entry'][0]['changes'][0]['value']['messages'][0]['timestamp']
        return datetime.fromtimestamp(int(date))
    
    def get_message_body(self):
        return self.data['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']
    
    def get_object(self):
        return {
            'contact_name' : self.get_contact_name(),
            'contact_phone' : self.get_contact_number(),
            'message_body' : self.get_message_body(),
            'message_date' : self.get_message_date()
        }
