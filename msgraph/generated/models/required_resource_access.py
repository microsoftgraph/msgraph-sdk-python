from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

resource_access = lazy_import('msgraph.generated.models.resource_access')

class RequiredResourceAccess(AdditionalDataHolder, Parsable):
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
        Instantiates a new requiredResourceAccess and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # The list of OAuth2.0 permission scopes and app roles that the application requires from the specified resource.
        self._resource_access: Optional[List[resource_access.ResourceAccess]] = None
        # The unique identifier for the resource that the application requires access to. This should be equal to the appId declared on the target resource application.
        self._resource_app_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RequiredResourceAccess:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RequiredResourceAccess
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RequiredResourceAccess()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "resource_access": lambda n : setattr(self, 'resource_access', n.get_collection_of_object_values(resource_access.ResourceAccess)),
            "resource_app_id": lambda n : setattr(self, 'resource_app_id', n.get_str_value()),
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
    def resource_access(self,) -> Optional[List[resource_access.ResourceAccess]]:
        """
        Gets the resourceAccess property value. The list of OAuth2.0 permission scopes and app roles that the application requires from the specified resource.
        Returns: Optional[List[resource_access.ResourceAccess]]
        """
        return self._resource_access
    
    @resource_access.setter
    def resource_access(self,value: Optional[List[resource_access.ResourceAccess]] = None) -> None:
        """
        Sets the resourceAccess property value. The list of OAuth2.0 permission scopes and app roles that the application requires from the specified resource.
        Args:
            value: Value to set for the resourceAccess property.
        """
        self._resource_access = value
    
    @property
    def resource_app_id(self,) -> Optional[str]:
        """
        Gets the resourceAppId property value. The unique identifier for the resource that the application requires access to. This should be equal to the appId declared on the target resource application.
        Returns: Optional[str]
        """
        return self._resource_app_id
    
    @resource_app_id.setter
    def resource_app_id(self,value: Optional[str] = None) -> None:
        """
        Sets the resourceAppId property value. The unique identifier for the resource that the application requires access to. This should be equal to the appId declared on the target resource application.
        Args:
            value: Value to set for the resourceAppId property.
        """
        self._resource_app_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("resourceAccess", self.resource_access)
        writer.write_str_value("resourceAppId", self.resource_app_id)
        writer.write_additional_data_value(self.additional_data)
    

