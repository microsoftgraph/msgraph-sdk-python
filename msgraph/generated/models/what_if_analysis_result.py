from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .conditional_access_policy import ConditionalAccessPolicy
    from .what_if_analysis_reasons import WhatIfAnalysisReasons

from .conditional_access_policy import ConditionalAccessPolicy

@dataclass
class WhatIfAnalysisResult(ConditionalAccessPolicy, Parsable):
    # The analysisReasons property
    analysis_reasons: Optional[WhatIfAnalysisReasons] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Specifies whether the policy applies to the sign-in properties provided in the request body. If policyApplies is true, the policy applies to the sign-in based on the sign-in properties provided. If policyApplies is false, the policy doesn't apply to the sign-in based on the sign-in properties provided and the analysisReasons property is populated to show the reason for the policy not applying.
    policy_applies: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WhatIfAnalysisResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WhatIfAnalysisResult
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WhatIfAnalysisResult()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .conditional_access_policy import ConditionalAccessPolicy
        from .what_if_analysis_reasons import WhatIfAnalysisReasons

        from .conditional_access_policy import ConditionalAccessPolicy
        from .what_if_analysis_reasons import WhatIfAnalysisReasons

        fields: dict[str, Callable[[Any], None]] = {
            "analysisReasons": lambda n : setattr(self, 'analysis_reasons', n.get_collection_of_enum_values(WhatIfAnalysisReasons)),
            "policyApplies": lambda n : setattr(self, 'policy_applies', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_enum_value("analysisReasons", self.analysis_reasons)
        writer.write_bool_value("policyApplies", self.policy_applies)
    

