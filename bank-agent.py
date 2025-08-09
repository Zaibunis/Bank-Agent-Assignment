from connection import config
from agents import Agent, Runner, RunContextWrapper, function_tool, input_guardrail, GuardrailFunctionOutput
from pydantic import BaseModel
import asyncio


class Account(BaseModel):
    name: str
    pin: int  # PIN initialized as 0 or actual PIN


class My_output(BaseModel):
    name: str
    balance: str


class Guardrail_output(BaseModel):
    is_not_bank_related: bool


# Guardrail agent to check if the user query is related to banking
guardrail_agent = Agent(
    name="Guardrail Agent",
    instructions="You are a guardrail agent and should check if the user is asking a bank-related query",
    output_type=Guardrail_output
)


@input_guardrail
async def check_bank_related(ctx: RunContextWrapper[None], agent: Agent, input: str) -> GuardrailFunctionOutput:
    result = await Runner.run_sync(guardrail_agent, input, context=ctx.context)
    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=result.final_output.is_not_bank_related,
    )


def check_user(ctx: RunContextWrapper[Account], agent: Agent) -> bool:
    # Simple user authentication check
    if ctx.context.name == "Faria" and ctx.context.pin == 234:
        return True
    else:
        return False


@function_tool(is_enabled=check_user)
def check_balance(account_number: str) -> str:
    return "The balance of the account is $100000"


bank_agent = Agent(
    name="Bank Agent",
    instructions="You are a bank agent and should answer queries related to customers and bank accounts and balance information, but make sure the user is authenticated",
    tools=[check_balance]
)


async def chat_loop():
    # Start with unknown PIN
    user_context = Account(name="Faria", pin=0)
    pin_verified = False

    while not pin_verified:
        pin = input("What is your PIN? ")
        if pin.isdigit() and int(pin) == 234:
            user_context.pin = int(pin)
            pin_verified = True
        else:
            print("Incorrect PIN, try again.")

    # Once PIN is verified, run the bank agent
    result = await Runner.run(
        bank_agent,
        "I want to know my balance, my account number is 234",
        run_config=config,
        context=user_context
    )
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(chat_loop())
