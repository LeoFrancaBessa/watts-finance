from src.services.openai import get_intent_message
from src.models.models import User, UserMonthlyBudget, UserSpent
from datetime import datetime
from dateparser import parse

async def flow(user_phone: str, message: str):
    try:
        intent_message = get_intent_message(message)
        if "intent" not in intent_message:
            return None
        else:
            user = await User.filter(phone=user_phone).first()
            if not user:
                return None
            intent = intent_message["intent"]
            parameters = intent_message["parameters"]
            
            if intent == "Adicionar orçamento":
                user_monthly_budget = await UserMonthlyBudget.filter(user=user, month=datetime.now().month, year=datetime.now().year).first()
                if user_monthly_budget:
                    user_monthly_budget.budget += parameters["amount"]
                    await user_monthly_budget.save()
                else:
                    await UserMonthlyBudget.create(user=user, month=datetime.now().month, budget=parameters["amount"], year=datetime.now().year)
                return 1
            
            elif intent == "Registrar gasto":
                parameters_date = parameters["date"] if "date" in parameters else None
                spent_date = parse(parameters_date) if parameters_date else datetime.now()
                spent_category = parameters["category"] if "category" in parameters else None
                await UserSpent.create(user=user, spent_value=parameters["amount"], spent_category=spent_category, spent_date=spent_date)
                return 2

            elif intent == "Atualizar orçamento":
                user_monthly_budget = await UserMonthlyBudget.filter(user=user, month=datetime.now().month, year=datetime.now().year).first()
                if user_monthly_budget:
                    user_monthly_budget.budget = parameters["amount"]
                    await user_monthly_budget.save()
                else:
                    await UserMonthlyBudget.create(user=user, month=datetime.now().month, budget=parameters["amount"], year=datetime.now().year)
                return 1
            
            else:
                return None
    except Exception as e:
        print(e)
        return None



