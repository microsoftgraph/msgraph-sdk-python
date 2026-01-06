from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_pc_audit_event import CloudPcAuditEvent
    from .cloud_pc_device_image import CloudPcDeviceImage
    from .cloud_pc_gallery_image import CloudPcGalleryImage
    from .cloud_pc_on_premises_connection import CloudPcOnPremisesConnection
    from .cloud_pc_provisioning_policy import CloudPcProvisioningPolicy
    from .cloud_pc_report import CloudPcReport
    from .cloud_pc_user_setting import CloudPcUserSetting
    from .cloud_p_c import CloudPC
    from .entity import Entity

from .entity import Entity

@dataclass
class VirtualEndpoint(Entity, Parsable):
    # A collection of Cloud PC audit events.
    audit_events: Optional[list[CloudPcAuditEvent]] = None
    # A collection of cloud-managed virtual desktops.
    cloud_p_cs: Optional[list[CloudPC]] = None
    # A collection of device image resources on Cloud PC.
    device_images: Optional[list[CloudPcDeviceImage]] = None
    # A collection of gallery image resources on Cloud PC.
    gallery_images: Optional[list[CloudPcGalleryImage]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # A defined collection of Azure resource information that can be used to establish Azure network connections for Cloud PCs.
    on_premises_connections: Optional[list[CloudPcOnPremisesConnection]] = None
    # A collection of Cloud PC provisioning policies.
    provisioning_policies: Optional[list[CloudPcProvisioningPolicy]] = None
    # Cloud PC-related reports. Read-only.
    report: Optional[CloudPcReport] = None
    # A collection of Cloud PC user settings.
    user_settings: Optional[list[CloudPcUserSetting]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> VirtualEndpoint:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: VirtualEndpoint
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return VirtualEndpoint()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_pc_audit_event import CloudPcAuditEvent
        from .cloud_pc_device_image import CloudPcDeviceImage
        from .cloud_pc_gallery_image import CloudPcGalleryImage
        from .cloud_pc_on_premises_connection import CloudPcOnPremisesConnection
        from .cloud_pc_provisioning_policy import CloudPcProvisioningPolicy
        from .cloud_pc_report import CloudPcReport
        from .cloud_pc_user_setting import CloudPcUserSetting
        from .cloud_p_c import CloudPC
        from .entity import Entity

        from .cloud_pc_audit_event import CloudPcAuditEvent
        from .cloud_pc_device_image import CloudPcDeviceImage
        from .cloud_pc_gallery_image import CloudPcGalleryImage
        from .cloud_pc_on_premises_connection import CloudPcOnPremisesConnection
        from .cloud_pc_provisioning_policy import CloudPcProvisioningPolicy
        from .cloud_pc_report import CloudPcReport
        from .cloud_pc_user_setting import CloudPcUserSetting
        from .cloud_p_c import CloudPC
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "auditEvents": lambda n : setattr(self, 'audit_events', n.get_collection_of_object_values(CloudPcAuditEvent)),
            "cloudPCs": lambda n : setattr(self, 'cloud_p_cs', n.get_collection_of_object_values(CloudPC)),
            "deviceImages": lambda n : setattr(self, 'device_images', n.get_collection_of_object_values(CloudPcDeviceImage)),
            "galleryImages": lambda n : setattr(self, 'gallery_images', n.get_collection_of_object_values(CloudPcGalleryImage)),
            "onPremisesConnections": lambda n : setattr(self, 'on_premises_connections', n.get_collection_of_object_values(CloudPcOnPremisesConnection)),
            "provisioningPolicies": lambda n : setattr(self, 'provisioning_policies', n.get_collection_of_object_values(CloudPcProvisioningPolicy)),
            "report": lambda n : setattr(self, 'report', n.get_object_value(CloudPcReport)),
            "userSettings": lambda n : setattr(self, 'user_settings', n.get_collection_of_object_values(CloudPcUserSetting)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("auditEvents", self.audit_events)
        writer.write_collection_of_object_values("cloudPCs", self.cloud_p_cs)
        writer.write_collection_of_object_values("deviceImages", self.device_images)
        writer.write_collection_of_object_values("galleryImages", self.gallery_images)
        writer.write_collection_of_object_values("onPremisesConnections", self.on_premises_connections)
        writer.write_collection_of_object_values("provisioningPolicies", self.provisioning_policies)
        writer.write_object_value("report", self.report)
        writer.write_collection_of_object_values("userSettings", self.user_settings)
    

