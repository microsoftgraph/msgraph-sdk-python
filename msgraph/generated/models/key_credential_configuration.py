from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .app_key_credential_restriction_type import AppKeyCredentialRestrictionType
    from .app_management_restriction_state import AppManagementRestrictionState

@dataclass
class KeyCredentialConfiguration(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # String value that indicates the maximum lifetime for key expiration, defined as an ISO 8601 duration. For example, P4DT12H30M5S represents four days, 12 hours, 30 minutes, and five seconds. This property is required when restrictionType is set to keyLifetime.
    max_lifetime: Optional[datetime.timedelta] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Specifies the date from which the policy restriction applies to newly created applications. For existing applications, the enforcement date can be retroactively applied.
    restrict_for_apps_created_after_date_time: Optional[datetime.datetime] = None
    # The type of restriction being applied. Possible values are asymmetricKeyLifetime, and unknownFutureValue. Each value of restrictionType can be used only once per policy.
    restriction_type: Optional[AppKeyCredentialRestrictionType] = None
    # The state property
    state: Optional[AppManagementRestrictionState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> KeyCredentialConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: KeyCredentialConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return KeyCredentialConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .app_key_credential_restriction_type import AppKeyCredentialRestrictionType
        from .app_management_restriction_state import AppManagementRestrictionState

        from .app_key_credential_restriction_type import AppKeyCredentialRestrictionType
        from .app_management_restriction_state import AppManagementRestrictionState

        fields: dict[str, Callable[[Any], None]] = {
            "maxLifetime": lambda n : setattr(self, 'max_lifetime', n.get_timedelta_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "restrictForAppsCreatedAfterDateTime": lambda n : setattr(self, 'restrict_for_apps_created_after_date_time', n.get_datetime_value()),
            "restrictionType": lambda n : setattr(self, 'restriction_type', n.get_enum_value(AppKeyCredentialRestrictionType)),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(AppManagementRestrictionState)),
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
        writer.write_timedelta_value("maxLifetime", self.max_lifetime)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_datetime_value("restrictForAppsCreatedAfterDateTime", self.restrict_for_apps_created_after_date_time)
        writer.write_enum_value("restrictionType", self.restriction_type)
        writer.write_enum_value("state", self.state)
        writer.write_additional_data_value(self.additional_data)
    

