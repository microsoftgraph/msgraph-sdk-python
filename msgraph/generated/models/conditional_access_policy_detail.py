from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

conditional_access_condition_set = lazy_import('msgraph.generated.models.conditional_access_condition_set')
conditional_access_grant_controls = lazy_import('msgraph.generated.models.conditional_access_grant_controls')
conditional_access_session_controls = lazy_import('msgraph.generated.models.conditional_access_session_controls')

class ConditionalAccessPolicyDetail(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
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
        Instantiates a new conditionalAccessPolicyDetail and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The conditions property
        self._conditions: Optional[conditional_access_condition_set.ConditionalAccessConditionSet] = None
        # Represents grant controls that must be fulfilled for the policy.
        self._grant_controls: Optional[conditional_access_grant_controls.ConditionalAccessGrantControls] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Represents a complex type of session controls that is enforced after sign-in.
        self._session_controls: Optional[conditional_access_session_controls.ConditionalAccessSessionControls] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ConditionalAccessPolicyDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ConditionalAccessPolicyDetail
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ConditionalAccessPolicyDetail()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "conditions": lambda n : setattr(self, 'conditions', n.get_object_value(conditional_access_condition_set.ConditionalAccessConditionSet)),
            "grant_controls": lambda n : setattr(self, 'grant_controls', n.get_object_value(conditional_access_grant_controls.ConditionalAccessGrantControls)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "session_controls": lambda n : setattr(self, 'session_controls', n.get_object_value(conditional_access_session_controls.ConditionalAccessSessionControls)),
        }
        return fields
    
    @property
    def grant_controls(self,) -> Optional[conditional_access_grant_controls.ConditionalAccessGrantControls]:
        """
        Gets the grantControls property value. Represents grant controls that must be fulfilled for the policy.
        Returns: Optional[conditional_access_grant_controls.ConditionalAccessGrantControls]
        """
        return self._grant_controls
    
    @grant_controls.setter
    def grant_controls(self,value: Optional[conditional_access_grant_controls.ConditionalAccessGrantControls] = None) -> None:
        """
        Sets the grantControls property value. Represents grant controls that must be fulfilled for the policy.
        Args:
            value: Value to set for the grantControls property.
        """
        self._grant_controls = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("conditions", self.conditions)
        writer.write_object_value("grantControls", self.grant_controls)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("sessionControls", self.session_controls)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def session_controls(self,) -> Optional[conditional_access_session_controls.ConditionalAccessSessionControls]:
        """
        Gets the sessionControls property value. Represents a complex type of session controls that is enforced after sign-in.
        Returns: Optional[conditional_access_session_controls.ConditionalAccessSessionControls]
        """
        return self._session_controls
    
    @session_controls.setter
    def session_controls(self,value: Optional[conditional_access_session_controls.ConditionalAccessSessionControls] = None) -> None:
        """
        Sets the sessionControls property value. Represents a complex type of session controls that is enforced after sign-in.
        Args:
            value: Value to set for the sessionControls property.
        """
        self._session_controls = value
    

