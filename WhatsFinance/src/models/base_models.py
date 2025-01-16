from pydantic import BaseModel, field_validator, Field


class UserModel(BaseModel):
    name: str
    phone: str
    email: str
    password: str


class SendMessageModel(BaseModel):
    template_name: str = Field(default=None)

    @field_validator('template_name', mode='before')
    @classmethod    
    def validate_template_name(cls, v):
        template_map = {
            1: "orcamento_atualizado",
            2: "gasto_adicionado",
        }
        return template_map.get(v, None)

