from tortoise import Tortoise, fields
from tortoise.models import Model


class MessageReceived(Model):
    id = fields.IntField(pk=True)
    contact_name = fields.CharField(max_length=255)
    contact_phone = fields.CharField(max_length=255)
    message_body = fields.TextField()
    message_date = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "message_received"
        table_description = "Table to store messages received from WhatsApp"

    def __str__(self):
        return f"MessageReceived(id={self.id}, contact_name={self.contact_name}, contact_phone={self.contact_phone}, message_body={self.message_body}, message_date={self.message_date})"


class MessageSent(Model):
    id = fields.IntField(pk=True)
    contact_phone = fields.CharField(max_length=255)
    message_body = fields.TextField()
    message_date = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "message_sent"
        table_description = "Table to store messages sent to WhatsApp"

    def __str__(self):
        return f"MessageSent(id={self.id}, contact_name={self.contact_name}, contact_phone={self.contact_phone}, message_body={self.message_body}, message_date={self.message_date})"


class User(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    phone = fields.CharField(max_length=255)
    email = fields.CharField(max_length=255)
    password = fields.CharField(max_length=255)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "user"
        table_description = "Table to store users"

    def __str__(self):
        return f"User(id={self.id}, name={self.name}, phone={self.phone}, email={self.email}, created_at={self.created_at}, updated_at={self.updated_at})"


class UserMonthlyBudget(Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField("models.User", related_name="user_monthly_budget")
    month = fields.IntField()
    year = fields.IntField()
    budget = fields.FloatField()
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "user_monthly_budget"
        table_description = "Table to store user monthly budget"

    def __str__(self):
        return f"UserMonthlyBudget(id={self.id}, user_id={self.user_id}, month={self.month}, year={self.year}, budget={self.budget}, created_at={self.created_at}, updated_at={self.updated_at})"


class UserSpent(Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField("models.User", related_name="user_spent")
    spent_date = fields.DatetimeField(null=True, blank=True, default=None)
    spent_value = fields.FloatField()
    spent_category = fields.CharField(max_length=255, null=True, blank=True, default=None)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "user_spent"
        table_description = "Table to store user spent"

    def __str__(self):
        return f"UserSpent(id={self.id}, user_id={self.user_id}, spent_date={self.spent_date}, spent_value={self.spent_value}, spent_description={self.spent_description}, created_at={self.created_at}, updated_at={self.updated_at})"

