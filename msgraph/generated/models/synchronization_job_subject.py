from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import synchronization_linked_objects

class SynchronizationJobSubject(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new synchronizationJobSubject and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The links property
        self._links: Optional[synchronization_linked_objects.SynchronizationLinkedObjects] = None
        # The objectId property
        self._object_id: Optional[str] = None
        # The objectTypeName property
        self._object_type_name: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
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
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SynchronizationJobSubject:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SynchronizationJobSubject
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SynchronizationJobSubject()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import synchronization_linked_objects

        fields: Dict[str, Callable[[Any], None]] = {
            "links": lambda n : setattr(self, 'links', n.get_object_value(synchronization_linked_objects.SynchronizationLinkedObjects)),
            "objectId": lambda n : setattr(self, 'object_id', n.get_str_value()),
            "objectTypeName": lambda n : setattr(self, 'object_type_name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def links(self,) -> Optional[synchronization_linked_objects.SynchronizationLinkedObjects]:
        """
        Gets the links property value. The links property
        Returns: Optional[synchronization_linked_objects.SynchronizationLinkedObjects]
        """
        return self._links
    
    @links.setter
    def links(self,value: Optional[synchronization_linked_objects.SynchronizationLinkedObjects] = None) -> None:
        """
        Sets the links property value. The links property
        Args:
            value: Value to set for the links property.
        """
        self._links = value
    
    @property
    def object_id(self,) -> Optional[str]:
        """
        Gets the objectId property value. The objectId property
        Returns: Optional[str]
        """
        return self._object_id
    
    @object_id.setter
    def object_id(self,value: Optional[str] = None) -> None:
        """
        Sets the objectId property value. The objectId property
        Args:
            value: Value to set for the object_id property.
        """
        self._object_id = value
    
    @property
    def object_type_name(self,) -> Optional[str]:
        """
        Gets the objectTypeName property value. The objectTypeName property
        Returns: Optional[str]
        """
        return self._object_type_name
    
    @object_type_name.setter
    def object_type_name(self,value: Optional[str] = None) -> None:
        """
        Sets the objectTypeName property value. The objectTypeName property
        Args:
            value: Value to set for the object_type_name property.
        """
        self._object_type_name = value
    
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
            value: Value to set for the odata_type property.
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
        writer.write_object_value("links", self.links)
        writer.write_str_value("objectId", self.object_id)
        writer.write_str_value("objectTypeName", self.object_type_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

