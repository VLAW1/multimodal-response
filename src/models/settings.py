from pydantic import BaseModel
from src.models.provider import ModelProvider


class ModelSettings(BaseModel):
    model_name: str
    provider: ModelProvider


class TextModelSettings(ModelSettings):
    max_tokens: int = 2000
    temperature: float = 0.7


class ImageModelSettings(ModelSettings):
    size: str = '1024x1024'
    quality: str = 'standard'
