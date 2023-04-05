from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import edge, service_announcement

class Admin(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new Admin and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The edge property
        self._edge: Optional[edge.Edge] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # A container for service communications resources. Read-only.
        self._service_announcement: Optional[service_announcement.ServiceAnnouncement] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Admin:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Admin
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Admin()
    
    @property
    def edge(self,) -> Optional[edge.Edge]:
        """
        Gets the edge property value. The edge property
        Returns: Optional[edge.Edge]
        """
        return self._edge
    
    @edge.setter
    def edge(self,value: Optional[edge.Edge] = None) -> None:
        """
        Sets the edge property value. The edge property
        Args:
            value: Value to set for the edge property.
        """
        self._edge = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import edge, service_announcement

        fields: Dict[str, Callable[[Any], None]] = {
            "edge": lambda n : setattr(self, 'edge', n.get_object_value(edge.Edge)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "serviceAnnouncement": lambda n : setattr(self, 'service_announcement', n.get_object_value(service_announcement.ServiceAnnouncement)),
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
        writer.write_object_value("edge", self.edge)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("serviceAnnouncement", self.service_announcement)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def service_announcement(self,) -> Optional[service_announcement.ServiceAnnouncement]:
        """
        Gets the serviceAnnouncement property value. A container for service communications resources. Read-only.
        Returns: Optional[service_announcement.ServiceAnnouncement]
        """
        return self._service_announcement
    
    @service_announcement.setter
    def service_announcement(self,value: Optional[service_announcement.ServiceAnnouncement] = None) -> None:
        """
        Sets the serviceAnnouncement property value. A container for service communications resources. Read-only.
        Args:
            value: Value to set for the service_announcement property.
        """
        self._service_announcement = value
    

