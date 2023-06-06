from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import conditional_access_condition_set, conditional_access_grant_controls, conditional_access_policy_state, conditional_access_session_controls, entity

from . import entity

@dataclass
class ConditionalAccessPolicy(entity.Entity):
    # The conditions property
    conditions: Optional[conditional_access_condition_set.ConditionalAccessConditionSet] = None
    # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Readonly.
    created_date_time: Optional[datetime] = None
    # The description property
    description: Optional[str] = None
    # Specifies a display name for the conditionalAccessPolicy object.
    display_name: Optional[str] = None
    # Specifies the grant controls that must be fulfilled to pass the policy.
    grant_controls: Optional[conditional_access_grant_controls.ConditionalAccessGrantControls] = None
    # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Readonly.
    modified_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Specifies the session controls that are enforced after sign-in.
    session_controls: Optional[conditional_access_session_controls.ConditionalAccessSessionControls] = None
    # The state property
    state: Optional[conditional_access_policy_state.ConditionalAccessPolicyState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ConditionalAccessPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ConditionalAccessPolicy
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ConditionalAccessPolicy()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import conditional_access_condition_set, conditional_access_grant_controls, conditional_access_policy_state, conditional_access_session_controls, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "conditions": lambda n : setattr(self, 'conditions', n.get_object_value(conditional_access_condition_set.ConditionalAccessConditionSet)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "grantControls": lambda n : setattr(self, 'grant_controls', n.get_object_value(conditional_access_grant_controls.ConditionalAccessGrantControls)),
            "modifiedDateTime": lambda n : setattr(self, 'modified_date_time', n.get_datetime_value()),
            "sessionControls": lambda n : setattr(self, 'session_controls', n.get_object_value(conditional_access_session_controls.ConditionalAccessSessionControls)),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(conditional_access_policy_state.ConditionalAccessPolicyState)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("conditions", self.conditions)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("grantControls", self.grant_controls)
        writer.write_datetime_value("modifiedDateTime", self.modified_date_time)
        writer.write_object_value("sessionControls", self.session_controls)
        writer.write_enum_value("state", self.state)
    

