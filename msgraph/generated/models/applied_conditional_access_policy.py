from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

applied_conditional_access_policy_result = lazy_import('msgraph.generated.models.applied_conditional_access_policy_result')

class AppliedConditionalAccessPolicy(AdditionalDataHolder, Parsable):
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new appliedConditionalAccessPolicy and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Refers to the Name of the conditional access policy (example: 'Require MFA for Salesforce').
        self._display_name: Optional[str] = None
        # Refers to the grant controls enforced by the conditional access policy (example: 'Require multi-factor authentication').
        self._enforced_grant_controls: Optional[List[str]] = None
        # Refers to the session controls enforced by the conditional access policy (example: 'Require app enforced controls').
        self._enforced_session_controls: Optional[List[str]] = None
        # An identifier of the conditional access policy.
        self._id: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Indicates the result of the CA policy that was triggered. Possible values are: success, failure, notApplied (Policy isn't applied because policy conditions were not met),notEnabled (This is due to the policy in disabled state), unknown, unknownFutureValue.
        self._result: Optional[applied_conditional_access_policy_result.AppliedConditionalAccessPolicyResult] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AppliedConditionalAccessPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AppliedConditionalAccessPolicy
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AppliedConditionalAccessPolicy()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Refers to the Name of the conditional access policy (example: 'Require MFA for Salesforce').
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Refers to the Name of the conditional access policy (example: 'Require MFA for Salesforce').
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def enforced_grant_controls(self,) -> Optional[List[str]]:
        """
        Gets the enforcedGrantControls property value. Refers to the grant controls enforced by the conditional access policy (example: 'Require multi-factor authentication').
        Returns: Optional[List[str]]
        """
        return self._enforced_grant_controls
    
    @enforced_grant_controls.setter
    def enforced_grant_controls(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the enforcedGrantControls property value. Refers to the grant controls enforced by the conditional access policy (example: 'Require multi-factor authentication').
        Args:
            value: Value to set for the enforcedGrantControls property.
        """
        self._enforced_grant_controls = value
    
    @property
    def enforced_session_controls(self,) -> Optional[List[str]]:
        """
        Gets the enforcedSessionControls property value. Refers to the session controls enforced by the conditional access policy (example: 'Require app enforced controls').
        Returns: Optional[List[str]]
        """
        return self._enforced_session_controls
    
    @enforced_session_controls.setter
    def enforced_session_controls(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the enforcedSessionControls property value. Refers to the session controls enforced by the conditional access policy (example: 'Require app enforced controls').
        Args:
            value: Value to set for the enforcedSessionControls property.
        """
        self._enforced_session_controls = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "enforced_grant_controls": lambda n : setattr(self, 'enforced_grant_controls', n.get_collection_of_primitive_values(str)),
            "enforced_session_controls": lambda n : setattr(self, 'enforced_session_controls', n.get_collection_of_primitive_values(str)),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "result": lambda n : setattr(self, 'result', n.get_enum_value(applied_conditional_access_policy_result.AppliedConditionalAccessPolicyResult)),
        }
        return fields
    
    @property
    def id(self,) -> Optional[str]:
        """
        Gets the id property value. An identifier of the conditional access policy.
        Returns: Optional[str]
        """
        return self._id
    
    @id.setter
    def id(self,value: Optional[str] = None) -> None:
        """
        Sets the id property value. An identifier of the conditional access policy.
        Args:
            value: Value to set for the id property.
        """
        self._id = value
    
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
    
    @property
    def result(self,) -> Optional[applied_conditional_access_policy_result.AppliedConditionalAccessPolicyResult]:
        """
        Gets the result property value. Indicates the result of the CA policy that was triggered. Possible values are: success, failure, notApplied (Policy isn't applied because policy conditions were not met),notEnabled (This is due to the policy in disabled state), unknown, unknownFutureValue.
        Returns: Optional[applied_conditional_access_policy_result.AppliedConditionalAccessPolicyResult]
        """
        return self._result
    
    @result.setter
    def result(self,value: Optional[applied_conditional_access_policy_result.AppliedConditionalAccessPolicyResult] = None) -> None:
        """
        Sets the result property value. Indicates the result of the CA policy that was triggered. Possible values are: success, failure, notApplied (Policy isn't applied because policy conditions were not met),notEnabled (This is due to the policy in disabled state), unknown, unknownFutureValue.
        Args:
            value: Value to set for the result property.
        """
        self._result = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_primitive_values("enforcedGrantControls", self.enforced_grant_controls)
        writer.write_collection_of_primitive_values("enforcedSessionControls", self.enforced_session_controls)
        writer.write_str_value("id", self.id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("result", self.result)
        writer.write_additional_data_value(self.additional_data)
    

