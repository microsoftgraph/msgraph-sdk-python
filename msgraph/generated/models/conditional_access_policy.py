from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

conditional_access_condition_set = lazy_import('msgraph.generated.models.conditional_access_condition_set')
conditional_access_grant_controls = lazy_import('msgraph.generated.models.conditional_access_grant_controls')
conditional_access_policy_state = lazy_import('msgraph.generated.models.conditional_access_policy_state')
conditional_access_session_controls = lazy_import('msgraph.generated.models.conditional_access_session_controls')
entity = lazy_import('msgraph.generated.models.entity')

class ConditionalAccessPolicy(entity.Entity):
    """
    Provides operations to manage the admin singleton.
    """
    @property
    def conditions(self,) -> Optional[conditional_access_condition_set.ConditionalAccessConditionSet]:
        """
        Gets the conditions property value. The conditions property
        Returns: Optional[conditional_access_condition_set.ConditionalAccessConditionSet]
        """
        return self._conditions
    
    @conditions.setter
    def conditions(self,value: Optional[conditional_access_condition_set.ConditionalAccessConditionSet] = None) -> None:
        """
        Sets the conditions property value. The conditions property
        Args:
            value: Value to set for the conditions property.
        """
        self._conditions = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new conditionalAccessPolicy and sets the default values.
        """
        super().__init__()
        # The conditions property
        self._conditions: Optional[conditional_access_condition_set.ConditionalAccessConditionSet] = None
        # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Readonly.
        self._created_date_time: Optional[datetime] = None
        # The description property
        self._description: Optional[str] = None
        # Specifies a display name for the conditionalAccessPolicy object.
        self._display_name: Optional[str] = None
        # Specifies the grant controls that must be fulfilled to pass the policy.
        self._grant_controls: Optional[conditional_access_grant_controls.ConditionalAccessGrantControls] = None
        # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Readonly.
        self._modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Specifies the session controls that are enforced after sign-in.
        self._session_controls: Optional[conditional_access_session_controls.ConditionalAccessSessionControls] = None
        # The state property
        self._state: Optional[conditional_access_policy_state.ConditionalAccessPolicyState] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Readonly.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Readonly.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
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
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The description property
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The description property
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Specifies a display name for the conditionalAccessPolicy object.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Specifies a display name for the conditionalAccessPolicy object.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "conditions": lambda n : setattr(self, 'conditions', n.get_object_value(conditional_access_condition_set.ConditionalAccessConditionSet)),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "grant_controls": lambda n : setattr(self, 'grant_controls', n.get_object_value(conditional_access_grant_controls.ConditionalAccessGrantControls)),
            "modified_date_time": lambda n : setattr(self, 'modified_date_time', n.get_datetime_value()),
            "session_controls": lambda n : setattr(self, 'session_controls', n.get_object_value(conditional_access_session_controls.ConditionalAccessSessionControls)),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(conditional_access_policy_state.ConditionalAccessPolicyState)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def grant_controls(self,) -> Optional[conditional_access_grant_controls.ConditionalAccessGrantControls]:
        """
        Gets the grantControls property value. Specifies the grant controls that must be fulfilled to pass the policy.
        Returns: Optional[conditional_access_grant_controls.ConditionalAccessGrantControls]
        """
        return self._grant_controls
    
    @grant_controls.setter
    def grant_controls(self,value: Optional[conditional_access_grant_controls.ConditionalAccessGrantControls] = None) -> None:
        """
        Sets the grantControls property value. Specifies the grant controls that must be fulfilled to pass the policy.
        Args:
            value: Value to set for the grantControls property.
        """
        self._grant_controls = value
    
    @property
    def modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the modifiedDateTime property value. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Readonly.
        Returns: Optional[datetime]
        """
        return self._modified_date_time
    
    @modified_date_time.setter
    def modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the modifiedDateTime property value. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Readonly.
        Args:
            value: Value to set for the modifiedDateTime property.
        """
        self._modified_date_time = value
    
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
    
    @property
    def session_controls(self,) -> Optional[conditional_access_session_controls.ConditionalAccessSessionControls]:
        """
        Gets the sessionControls property value. Specifies the session controls that are enforced after sign-in.
        Returns: Optional[conditional_access_session_controls.ConditionalAccessSessionControls]
        """
        return self._session_controls
    
    @session_controls.setter
    def session_controls(self,value: Optional[conditional_access_session_controls.ConditionalAccessSessionControls] = None) -> None:
        """
        Sets the sessionControls property value. Specifies the session controls that are enforced after sign-in.
        Args:
            value: Value to set for the sessionControls property.
        """
        self._session_controls = value
    
    @property
    def state(self,) -> Optional[conditional_access_policy_state.ConditionalAccessPolicyState]:
        """
        Gets the state property value. The state property
        Returns: Optional[conditional_access_policy_state.ConditionalAccessPolicyState]
        """
        return self._state
    
    @state.setter
    def state(self,value: Optional[conditional_access_policy_state.ConditionalAccessPolicyState] = None) -> None:
        """
        Sets the state property value. The state property
        Args:
            value: Value to set for the state property.
        """
        self._state = value
    

