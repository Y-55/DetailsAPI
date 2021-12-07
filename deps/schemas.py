from pydantic import BaseModel
from typing import List, Optional

class RFMresponse(BaseModel):
    recency_log: List[float]
    frequency_log: List[float]
    amount_log: List[float]
    lables: List[int]