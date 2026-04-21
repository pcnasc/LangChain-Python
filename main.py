from pyexpat.errors import messages

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPEN_AI_API_KEY")

prompt = f"crie um roteiro de viagens de {days} dias, para uma familia de {kids} crianças que gostem de {activity}"

client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
    model="gpt-3.5-turbo"
    messages=[
        {
            "role"
        }]
)