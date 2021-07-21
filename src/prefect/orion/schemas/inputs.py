"""
Reduced schemas for accepting API inputs
"""

from typing import List
from uuid import UUID

from pydantic import Field

from prefect.orion.utilities.functions import ParameterSchema
from prefect.orion.utilities.schemas import PrefectBaseModel


class FlowCreate(PrefectBaseModel):
    name: str = Field(..., example="my-flow")
    tags: List[str] = Field(default_factory=list, example=["tag-1", "tag-2"])
    parameters: ParameterSchema = Field(default_factory=ParameterSchema)


class FlowRunCreate(PrefectBaseModel):
    flow_id: UUID
    flow_version: str = Field(..., example="v1.0")
    parameters: dict = Field(default_factory=dict)
    parent_task_run_id: UUID = None
    context: dict = Field(default_factory=dict, example={"my_var": "my_val"})
    tags: List[str] = Field(default_factory=list, example=["tag-1", "tag-2"])
