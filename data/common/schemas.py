from typing import List, Union
from pydantic import BaseModel


class Label(BaseModel):
    label: str
    value: Union[int, float]
    color: str


class Chart(BaseModel):
    chart_type: str
    chart_title: str
    data: List[Label]
