from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .exchange_protection_policy import ExchangeProtectionPolicy
    from .identity_set import IdentitySet
    from .one_drive_for_business_protection_policy import OneDriveForBusinessProtectionPolicy
    from .protection_policy_artifact_count import ProtectionPolicyArtifactCount
    from .protection_policy_status import ProtectionPolicyStatus
    from .retention_setting import RetentionSetting
    from .share_point_protection_policy import SharePointProtectionPolicy

from .entity import Entity

@dataclass
class ProtectionPolicyBase(Entity, Parsable):
    # The identity of person who created the policy.
    created_by: Optional[IdentitySet] = None
    # The time of creation of the policy.
    created_date_time: Optional[datetime.datetime] = None
    # The name of the policy to be created.
    display_name: Optional[str] = None
    # The isEnabled property
    is_enabled: Optional[bool] = None
    # The identity of the person who last modified the policy.
    last_modified_by: Optional[IdentitySet] = None
    # The timestamp of the last modification of the policy.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The protectionPolicyArtifactCount property
    protection_policy_artifact_count: Optional[ProtectionPolicyArtifactCount] = None
    # Contains the retention setting details for the policy.
    retention_settings: Optional[list[RetentionSetting]] = None
    # The aggregated status of the protection units associated with the policy. The possible values are: inactive, activeWithErrors, updating, active, unknownFutureValue.
    status: Optional[ProtectionPolicyStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ProtectionPolicyBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ProtectionPolicyBase
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.exchangeProtectionPolicy".casefold():
            from .exchange_protection_policy import ExchangeProtectionPolicy

            return ExchangeProtectionPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.oneDriveForBusinessProtectionPolicy".casefold():
            from .one_drive_for_business_protection_policy import OneDriveForBusinessProtectionPolicy

            return OneDriveForBusinessProtectionPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sharePointProtectionPolicy".casefold():
            from .share_point_protection_policy import SharePointProtectionPolicy

            return SharePointProtectionPolicy()
        return ProtectionPolicyBase()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .exchange_protection_policy import ExchangeProtectionPolicy
        from .identity_set import IdentitySet
        from .one_drive_for_business_protection_policy import OneDriveForBusinessProtectionPolicy
        from .protection_policy_artifact_count import ProtectionPolicyArtifactCount
        from .protection_policy_status import ProtectionPolicyStatus
        from .retention_setting import RetentionSetting
        from .share_point_protection_policy import SharePointProtectionPolicy

        from .entity import Entity
        from .exchange_protection_policy import ExchangeProtectionPolicy
        from .identity_set import IdentitySet
        from .one_drive_for_business_protection_policy import OneDriveForBusinessProtectionPolicy
        from .protection_policy_artifact_count import ProtectionPolicyArtifactCount
        from .protection_policy_status import ProtectionPolicyStatus
        from .retention_setting import RetentionSetting
        from .share_point_protection_policy import SharePointProtectionPolicy

        fields: dict[str, Callable[[Any], None]] = {
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(IdentitySet)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "isEnabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(IdentitySet)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "protectionPolicyArtifactCount": lambda n : setattr(self, 'protection_policy_artifact_count', n.get_object_value(ProtectionPolicyArtifactCount)),
            "retentionSettings": lambda n : setattr(self, 'retention_settings', n.get_collection_of_object_values(RetentionSetting)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(ProtectionPolicyStatus)),
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
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("isEnabled", self.is_enabled)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_object_value("protectionPolicyArtifactCount", self.protection_policy_artifact_count)
        writer.write_collection_of_object_values("retentionSettings", self.retention_settings)
        writer.write_enum_value("status", self.status)
    

