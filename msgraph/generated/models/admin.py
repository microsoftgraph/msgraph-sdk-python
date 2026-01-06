from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .admin_microsoft365_apps import AdminMicrosoft365Apps
    from .admin_report_settings import AdminReportSettings
    from .edge import Edge
    from .people_admin_settings import PeopleAdminSettings
    from .service_announcement import ServiceAnnouncement
    from .sharepoint import Sharepoint
    from .teams_administration.teams_admin_root import TeamsAdminRoot

@dataclass
class Admin(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # A container for Microsoft Edge resources. Read-only.
    edge: Optional[Edge] = None
    # A container for the Microsoft 365 apps admin functionality.
    microsoft365_apps: Optional[AdminMicrosoft365Apps] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Represents a setting to control people-related admin settings in the tenant.
    people: Optional[PeopleAdminSettings] = None
    # A container for administrative resources to manage reports.
    report_settings: Optional[AdminReportSettings] = None
    # A container for service communications resources. Read-only.
    service_announcement: Optional[ServiceAnnouncement] = None
    # The sharepoint property
    sharepoint: Optional[Sharepoint] = None
    # Represents a collection of user configurations.
    teams: Optional[TeamsAdminRoot] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Admin:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Admin
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Admin()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .admin_microsoft365_apps import AdminMicrosoft365Apps
        from .admin_report_settings import AdminReportSettings
        from .edge import Edge
        from .people_admin_settings import PeopleAdminSettings
        from .service_announcement import ServiceAnnouncement
        from .sharepoint import Sharepoint
        from .teams_administration.teams_admin_root import TeamsAdminRoot

        from .admin_microsoft365_apps import AdminMicrosoft365Apps
        from .admin_report_settings import AdminReportSettings
        from .edge import Edge
        from .people_admin_settings import PeopleAdminSettings
        from .service_announcement import ServiceAnnouncement
        from .sharepoint import Sharepoint
        from .teams_administration.teams_admin_root import TeamsAdminRoot

        fields: dict[str, Callable[[Any], None]] = {
            "edge": lambda n : setattr(self, 'edge', n.get_object_value(Edge)),
            "microsoft365Apps": lambda n : setattr(self, 'microsoft365_apps', n.get_object_value(AdminMicrosoft365Apps)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "people": lambda n : setattr(self, 'people', n.get_object_value(PeopleAdminSettings)),
            "reportSettings": lambda n : setattr(self, 'report_settings', n.get_object_value(AdminReportSettings)),
            "serviceAnnouncement": lambda n : setattr(self, 'service_announcement', n.get_object_value(ServiceAnnouncement)),
            "sharepoint": lambda n : setattr(self, 'sharepoint', n.get_object_value(Sharepoint)),
            "teams": lambda n : setattr(self, 'teams', n.get_object_value(TeamsAdminRoot)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("edge", self.edge)
        writer.write_object_value("microsoft365Apps", self.microsoft365_apps)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("people", self.people)
        writer.write_object_value("reportSettings", self.report_settings)
        writer.write_object_value("serviceAnnouncement", self.service_announcement)
        writer.write_object_value("sharepoint", self.sharepoint)
        writer.write_object_value("teams", self.teams)
        writer.write_additional_data_value(self.additional_data)
    

