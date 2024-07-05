import os

from langfuse import Langfuse
from langfuse.callback import CallbackHandler


try:
    langfuse_handler = CallbackHandler(
        user_id=os.getenv("LANGFUSE_USER_ID", None),
    )
    langfuse_handler.auth_check()
    langfuse_client = Langfuse()

except Exception as e:
    print(f"Failed to initialize Langfuse CallbackHandler and Client: {e}")
    langfuse_handler = None
    langfuse_client = None


TAGS = [
    "Hallucination",
    "Incorrect",
    "Misleading",
    "Wrong Sources",
    "Good Sources",
    "Good Explanation",
]
