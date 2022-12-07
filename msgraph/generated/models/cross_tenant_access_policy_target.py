from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

cross_tenant_access_policy_target_type = lazy_import('msgraph.generated.models.cross_tenant_access_policy_target_type')

class CrossTenantAccessPolicyTarget(AdditionalDataHolder, Parsable):
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
        Instantiates a new crossTenantAccessPolicyTarget and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # The unique identifier of the user, group, or application; one of the following keywords: AllUsers and AllApplications; or for targets that are applications, you may use reserved values.
        self._target: Optional[str] = None
        # The type of resource that you want to target. The possible values are: user, group, application, unknownFutureValue.
        self._target_type: Optional[cross_tenant_access_policy_target_type.CrossTenantAccessPolicyTargetType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CrossTenantAccessPolicyTarget:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CrossTenantAccessPolicyTarget
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CrossTenantAccessPolicyTarget()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "target": lambda n : setattr(self, 'target', n.get_str_value()),
            "target_type": lambda n : setattr(self, 'target_type', n.get_enum_value(cross_tenant_access_policy_target_type.CrossTenantAccessPolicyTargetType)),
        }
        return fields
    
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("target", self.target)
        writer.write_enum_value("targetType", self.target_type)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def target(self,) -> Optional[str]:
        """
        Gets the target property value. The unique identifier of the user, group, or application; one of the following keywords: AllUsers and AllApplications; or for targets that are applications, you may use reserved values.
        Returns: Optional[str]
        """
        return self._target
    
    @target.setter
    def target(self,value: Optional[str] = None) -> None:
        """
        Sets the target property value. The unique identifier of the user, group, or application; one of the following keywords: AllUsers and AllApplications; or for targets that are applications, you may use reserved values.
        Args:
            value: Value to set for the target property.
        """
        self._target = value
    
    @property
    def target_type(self,) -> Optional[cross_tenant_access_policy_target_type.CrossTenantAccessPolicyTargetType]:
        """
        Gets the targetType property value. The type of resource that you want to target. The possible values are: user, group, application, unknownFutureValue.
        Returns: Optional[cross_tenant_access_policy_target_type.CrossTenantAccessPolicyTargetType]
        """
        return self._target_type
    
    @target_type.setter
    def target_type(self,value: Optional[cross_tenant_access_policy_target_type.CrossTenantAccessPolicyTargetType] = None) -> None:
        """
        Sets the targetType property value. The type of resource that you want to target. The possible values are: user, group, application, unknownFutureValue.
        Args:
            value: Value to set for the targetType property.
        """
        self._target_type = value
    

