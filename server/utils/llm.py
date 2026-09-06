import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

MODEL_ROUTER = "groq/compound-mini"
MODEL_SOLVER = "groq/compound"
START_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)
