import json

from litellm import completion
from pydantic import BaseModel

from app.config import settings


class LLMGateway:
    """
    Generic LLM Gateway using LiteLLM.
    Responsible for:
    - Calling the model
    - Parsing JSON
    - Validating using Pydantic
    """

    def generate_structured(
        self,
        prompt: str,
        schema: type[BaseModel],
    ):

        response = completion(
            model=settings.model_name,
            api_key=settings.groq_api_key,
            temperature=settings.temperature,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        content = response.choices[0].message.content

        try:
            data = json.loads(content)
        except Exception as e:
            raise ValueError(
                f"LLM did not return valid JSON.\n\nResponse:\n{content}"
            ) from e

        return schema(**data)


llm_gateway = LLMGateway()