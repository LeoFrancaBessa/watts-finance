from tortoise import Tortoise, fields
from tortoise.models import Model

class MessageReceived(Model):
    id = fields.IntField(pk=True)
    contact_name = fields.CharField(max_length=255)
    contact_phone = fields.CharField(max_length=255)
    message_body = fields.TextField()
    message_date = fields.DatetimeField()

    class Meta:
        table = "message_received"
        table_description = "Table to store messages received from WhatsApp"

    def __str__(self):
        return f"MessageReceived(id={self.id}, contact_name={self.contact_name}, contact_phone={self.contact_phone}, message_body={self.message_body}, message_date={self.message_date})"
