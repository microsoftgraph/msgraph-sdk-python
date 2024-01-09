from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .edge import Edge
    from .people_admin_settings import PeopleAdminSettings
    from .service_announcement import ServiceAnnouncement
    from .sharepoint import Sharepoint

@dataclass
class Admin(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # A container for Microsoft Edge resources. Read-only.
    edge: Optional[Edge] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Represents a setting to control people-related admin settings in the tenant.
    people: Optional[PeopleAdminSettings] = None
    # A container for service communications resources. Read-only.
    service_announcement: Optional[ServiceAnnouncement] = None
    # The sharepoint property
    sharepoint: Optional[Sharepoint] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Admin:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Admin
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Admin()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .edge import Edge
        from .people_admin_settings import PeopleAdminSettings
        from .service_announcement import ServiceAnnouncement
        from .sharepoint import Sharepoint

        from .edge import Edge
        from .people_admin_settings import PeopleAdminSettings
        from .service_announcement import ServiceAnnouncement
        from .sharepoint import Sharepoint

        fields: Dict[str, Callable[[Any], None]] = {
            "edge": lambda n : setattr(self, 'edge', n.get_object_value(Edge)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "people": lambda n : setattr(self, 'people', n.get_object_value(PeopleAdminSettings)),
            "serviceAnnouncement": lambda n : setattr(self, 'service_announcement', n.get_object_value(ServiceAnnouncement)),
            "sharepoint": lambda n : setattr(self, 'sharepoint', n.get_object_value(Sharepoint)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("edge", self.edge)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("people", self.people)
        writer.write_object_value("serviceAnnouncement", self.service_announcement)
        writer.write_object_value("sharepoint", self.sharepoint)
        writer.write_additional_data_value(self.additional_data)
    

