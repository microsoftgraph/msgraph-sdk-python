from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

vm_cloud_provider = lazy_import('msgraph.generated.models.security.vm_cloud_provider')

class VmMetadata(AdditionalDataHolder, Parsable):
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
    def cloud_provider(self,) -> Optional[vm_cloud_provider.VmCloudProvider]:
        """
        Gets the cloudProvider property value. The cloudProvider property
        Returns: Optional[vm_cloud_provider.VmCloudProvider]
        """
        return self._cloud_provider
    
    @cloud_provider.setter
    def cloud_provider(self,value: Optional[vm_cloud_provider.VmCloudProvider] = None) -> None:
        """
        Sets the cloudProvider property value. The cloudProvider property
        Args:
            value: Value to set for the cloudProvider property.
        """
        self._cloud_provider = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new vmMetadata and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The cloudProvider property
        self._cloud_provider: Optional[vm_cloud_provider.VmCloudProvider] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Unique identifier of the Azure resource.
        self._resource_id: Optional[str] = None
        # Unique identifier of the Azure subscription the customer tenant belongs to.
        self._subscription_id: Optional[str] = None
        # Unique identifier of the virtual machine instance.
        self._vm_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> VmMetadata:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: VmMetadata
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return VmMetadata()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "cloud_provider": lambda n : setattr(self, 'cloud_provider', n.get_enum_value(vm_cloud_provider.VmCloudProvider)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "resource_id": lambda n : setattr(self, 'resource_id', n.get_str_value()),
            "subscription_id": lambda n : setattr(self, 'subscription_id', n.get_str_value()),
            "vm_id": lambda n : setattr(self, 'vm_id', n.get_str_value()),
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
    
    @property
    def resource_id(self,) -> Optional[str]:
        """
        Gets the resourceId property value. Unique identifier of the Azure resource.
        Returns: Optional[str]
        """
        return self._resource_id
    
    @resource_id.setter
    def resource_id(self,value: Optional[str] = None) -> None:
        """
        Sets the resourceId property value. Unique identifier of the Azure resource.
        Args:
            value: Value to set for the resourceId property.
        """
        self._resource_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_enum_value("cloudProvider", self.cloud_provider)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("resourceId", self.resource_id)
        writer.write_str_value("subscriptionId", self.subscription_id)
        writer.write_str_value("vmId", self.vm_id)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def subscription_id(self,) -> Optional[str]:
        """
        Gets the subscriptionId property value. Unique identifier of the Azure subscription the customer tenant belongs to.
        Returns: Optional[str]
        """
        return self._subscription_id
    
    @subscription_id.setter
    def subscription_id(self,value: Optional[str] = None) -> None:
        """
        Sets the subscriptionId property value. Unique identifier of the Azure subscription the customer tenant belongs to.
        Args:
            value: Value to set for the subscriptionId property.
        """
        self._subscription_id = value
    
    @property
    def vm_id(self,) -> Optional[str]:
        """
        Gets the vmId property value. Unique identifier of the virtual machine instance.
        Returns: Optional[str]
        """
        return self._vm_id
    
    @vm_id.setter
    def vm_id(self,value: Optional[str] = None) -> None:
        """
        Sets the vmId property value. Unique identifier of the virtual machine instance.
        Args:
            value: Value to set for the vmId property.
        """
        self._vm_id = value
    

