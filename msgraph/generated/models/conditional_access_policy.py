from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .conditional_access_condition_set import ConditionalAccessConditionSet
    from .conditional_access_grant_controls import ConditionalAccessGrantControls
    from .conditional_access_policy_state import ConditionalAccessPolicyState
    from .conditional_access_session_controls import ConditionalAccessSessionControls
    from .entity import Entity
    from .what_if_analysis_result import WhatIfAnalysisResult

from .entity import Entity

@dataclass
class ConditionalAccessPolicy(Entity, Parsable):
    # The conditions property
    conditions: Optional[ConditionalAccessConditionSet] = None
    # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Readonly.
    created_date_time: Optional[datetime.datetime] = None
    # The description property
    description: Optional[str] = None
    # Specifies a display name for the conditionalAccessPolicy object.
    display_name: Optional[str] = None
    # Specifies the grant controls that must be fulfilled to pass the policy.
    grant_controls: Optional[ConditionalAccessGrantControls] = None
    # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Readonly.
    modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Specifies the session controls that are enforced after sign-in.
    session_controls: Optional[ConditionalAccessSessionControls] = None
    # The state property
    state: Optional[ConditionalAccessPolicyState] = None
    # Specifies the unique identifier of a Conditional Access template. Inherited from entity.
    template_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ConditionalAccessPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ConditionalAccessPolicy
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.whatIfAnalysisResult".casefold():
            from .what_if_analysis_result import WhatIfAnalysisResult

            return WhatIfAnalysisResult()
        return ConditionalAccessPolicy()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .conditional_access_condition_set import ConditionalAccessConditionSet
        from .conditional_access_grant_controls import ConditionalAccessGrantControls
        from .conditional_access_policy_state import ConditionalAccessPolicyState
        from .conditional_access_session_controls import ConditionalAccessSessionControls
        from .entity import Entity
        from .what_if_analysis_result import WhatIfAnalysisResult

        from .conditional_access_condition_set import ConditionalAccessConditionSet
        from .conditional_access_grant_controls import ConditionalAccessGrantControls
        from .conditional_access_policy_state import ConditionalAccessPolicyState
        from .conditional_access_session_controls import ConditionalAccessSessionControls
        from .entity import Entity
        from .what_if_analysis_result import WhatIfAnalysisResult

        fields: dict[str, Callable[[Any], None]] = {
            "conditions": lambda n : setattr(self, 'conditions', n.get_object_value(ConditionalAccessConditionSet)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "grantControls": lambda n : setattr(self, 'grant_controls', n.get_object_value(ConditionalAccessGrantControls)),
            "modifiedDateTime": lambda n : setattr(self, 'modified_date_time', n.get_datetime_value()),
            "sessionControls": lambda n : setattr(self, 'session_controls', n.get_object_value(ConditionalAccessSessionControls)),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(ConditionalAccessPolicyState)),
            "templateId": lambda n : setattr(self, 'template_id', n.get_str_value()),
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
        writer.write_object_value("conditions", self.conditions)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("grantControls", self.grant_controls)
        writer.write_datetime_value("modifiedDateTime", self.modified_date_time)
        writer.write_object_value("sessionControls", self.session_controls)
        writer.write_enum_value("state", self.state)
        writer.write_str_value("templateId", self.template_id)
    

