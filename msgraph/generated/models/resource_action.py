from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class ResourceAction(AdditionalDataHolder, Parsable):
    """
    Set of allowed and not allowed actions for a resource.
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
    def allowed_resource_actions(self,) -> Optional[List[str]]:
        """
        Gets the allowedResourceActions property value. Allowed Actions
        Returns: Optional[List[str]]
        """
        return self._allowed_resource_actions
    
    @allowed_resource_actions.setter
    def allowed_resource_actions(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the allowedResourceActions property value. Allowed Actions
        Args:
            value: Value to set for the allowedResourceActions property.
        """
        self._allowed_resource_actions = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new resourceAction and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Allowed Actions
        self._allowed_resource_actions: Optional[List[str]] = None
        # Not Allowed Actions.
        self._not_allowed_resource_actions: Optional[List[str]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ResourceAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ResourceAction
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ResourceAction()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "allowed_resource_actions": lambda n : setattr(self, 'allowed_resource_actions', n.get_collection_of_primitive_values(str)),
            "not_allowed_resource_actions": lambda n : setattr(self, 'not_allowed_resource_actions', n.get_collection_of_primitive_values(str)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def not_allowed_resource_actions(self,) -> Optional[List[str]]:
        """
        Gets the notAllowedResourceActions property value. Not Allowed Actions.
        Returns: Optional[List[str]]
        """
        return self._not_allowed_resource_actions
    
    @not_allowed_resource_actions.setter
    def not_allowed_resource_actions(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the notAllowedResourceActions property value. Not Allowed Actions.
        Args:
            value: Value to set for the notAllowedResourceActions property.
        """
        self._not_allowed_resource_actions = value
    
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
        writer.write_collection_of_primitive_values("allowedResourceActions", self.allowed_resource_actions)
        writer.write_collection_of_primitive_values("notAllowedResourceActions", self.not_allowed_resource_actions)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

