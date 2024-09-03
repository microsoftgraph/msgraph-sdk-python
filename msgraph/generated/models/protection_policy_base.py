from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .exchange_protection_policy import ExchangeProtectionPolicy
    from .identity_set import IdentitySet
    from .one_drive_for_business_protection_policy import OneDriveForBusinessProtectionPolicy
    from .protection_policy_status import ProtectionPolicyStatus
    from .retention_setting import RetentionSetting
    from .share_point_protection_policy import SharePointProtectionPolicy

from .entity import Entity

@dataclass
class ProtectionPolicyBase(Entity):
    # The identity of person who created the policy.
    created_by: Optional[IdentitySet] = None
    # The time of creation of the policy.
    created_date_time: Optional[datetime.datetime] = None
    # The name of the policy to be created.
    display_name: Optional[str] = None
    # The identity of the person who last modified the policy.
    last_modified_by: Optional[IdentitySet] = None
    # The timestamp of the last modification of the policy.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Contains the retention setting details for the policy.
    retention_settings: Optional[List[RetentionSetting]] = None
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
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
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
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .exchange_protection_policy import ExchangeProtectionPolicy
        from .identity_set import IdentitySet
        from .one_drive_for_business_protection_policy import OneDriveForBusinessProtectionPolicy
        from .protection_policy_status import ProtectionPolicyStatus
        from .retention_setting import RetentionSetting
        from .share_point_protection_policy import SharePointProtectionPolicy

        from .entity import Entity
        from .exchange_protection_policy import ExchangeProtectionPolicy
        from .identity_set import IdentitySet
        from .one_drive_for_business_protection_policy import OneDriveForBusinessProtectionPolicy
        from .protection_policy_status import ProtectionPolicyStatus
        from .retention_setting import RetentionSetting
        from .share_point_protection_policy import SharePointProtectionPolicy

        fields: Dict[str, Callable[[Any], None]] = {
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(IdentitySet)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(IdentitySet)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
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
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_collection_of_object_values("retentionSettings", self.retention_settings)
        writer.write_enum_value("status", self.status)
    

