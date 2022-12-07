from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

resource_action = lazy_import('msgraph.generated.models.resource_action')

class RolePermission(AdditionalDataHolder, Parsable):
    """
    Contains the set of ResourceActions determining the allowed and not allowed permissions for each role.
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new rolePermission and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # Resource Actions each containing a set of allowed and not allowed permissions.
        self._resource_actions: Optional[List[resource_action.ResourceAction]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RolePermission:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RolePermission
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RolePermission()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "resource_actions": lambda n : setattr(self, 'resource_actions', n.get_collection_of_object_values(resource_action.ResourceAction)),
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
    def resource_actions(self,) -> Optional[List[resource_action.ResourceAction]]:
        """
        Gets the resourceActions property value. Resource Actions each containing a set of allowed and not allowed permissions.
        Returns: Optional[List[resource_action.ResourceAction]]
        """
        return self._resource_actions
    
    @resource_actions.setter
    def resource_actions(self,value: Optional[List[resource_action.ResourceAction]] = None) -> None:
        """
        Sets the resourceActions property value. Resource Actions each containing a set of allowed and not allowed permissions.
        Args:
            value: Value to set for the resourceActions property.
        """
        self._resource_actions = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("resourceActions", self.resource_actions)
        writer.write_additional_data_value(self.additional_data)
    

