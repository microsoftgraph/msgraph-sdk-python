from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

audit_property = lazy_import('msgraph.generated.models.audit_property')

class AuditResource(AdditionalDataHolder, Parsable):
    """
    A class containing the properties for Audit Resource.
    """
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
    def audit_resource_type(self,) -> Optional[str]:
        """
        Gets the auditResourceType property value. Audit resource's type.
        Returns: Optional[str]
        """
        return self._audit_resource_type
    
    @audit_resource_type.setter
    def audit_resource_type(self,value: Optional[str] = None) -> None:
        """
        Sets the auditResourceType property value. Audit resource's type.
        Args:
            value: Value to set for the auditResourceType property.
        """
        self._audit_resource_type = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new auditResource and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Audit resource's type.
        self._audit_resource_type: Optional[str] = None
        # Display name.
        self._display_name: Optional[str] = None
        # List of modified properties.
        self._modified_properties: Optional[List[audit_property.AuditProperty]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Audit resource's Id.
        self._resource_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AuditResource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AuditResource
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AuditResource()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Display name.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Display name.
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
            "audit_resource_type": lambda n : setattr(self, 'audit_resource_type', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "modified_properties": lambda n : setattr(self, 'modified_properties', n.get_collection_of_object_values(audit_property.AuditProperty)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "resource_id": lambda n : setattr(self, 'resource_id', n.get_str_value()),
        }
        return fields
    
    @property
    def modified_properties(self,) -> Optional[List[audit_property.AuditProperty]]:
        """
        Gets the modifiedProperties property value. List of modified properties.
        Returns: Optional[List[audit_property.AuditProperty]]
        """
        return self._modified_properties
    
    @modified_properties.setter
    def modified_properties(self,value: Optional[List[audit_property.AuditProperty]] = None) -> None:
        """
        Sets the modifiedProperties property value. List of modified properties.
        Args:
            value: Value to set for the modifiedProperties property.
        """
        self._modified_properties = value
    
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
        Gets the resourceId property value. Audit resource's Id.
        Returns: Optional[str]
        """
        return self._resource_id
    
    @resource_id.setter
    def resource_id(self,value: Optional[str] = None) -> None:
        """
        Sets the resourceId property value. Audit resource's Id.
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
        writer.write_str_value("auditResourceType", self.audit_resource_type)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("modifiedProperties", self.modified_properties)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("resourceId", self.resource_id)
        writer.write_additional_data_value(self.additional_data)
    

