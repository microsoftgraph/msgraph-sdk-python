from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .imported_windows_autopilot_device_identity_import_status import ImportedWindowsAutopilotDeviceIdentityImportStatus

@dataclass
class ImportedWindowsAutopilotDeviceIdentityState(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Device error code reported by Device Directory Service(DDS).
    device_error_code: Optional[int] = None
    # Device error name reported by Device Directory Service(DDS).
    device_error_name: Optional[str] = None
    # The deviceImportStatus property
    device_import_status: Optional[ImportedWindowsAutopilotDeviceIdentityImportStatus] = None
    # Device Registration ID for successfully added device reported by Device Directory Service(DDS).
    device_registration_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ImportedWindowsAutopilotDeviceIdentityState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ImportedWindowsAutopilotDeviceIdentityState
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ImportedWindowsAutopilotDeviceIdentityState()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .imported_windows_autopilot_device_identity_import_status import ImportedWindowsAutopilotDeviceIdentityImportStatus

        from .imported_windows_autopilot_device_identity_import_status import ImportedWindowsAutopilotDeviceIdentityImportStatus

        fields: Dict[str, Callable[[Any], None]] = {
            "deviceErrorCode": lambda n : setattr(self, 'device_error_code', n.get_int_value()),
            "deviceErrorName": lambda n : setattr(self, 'device_error_name', n.get_str_value()),
            "deviceImportStatus": lambda n : setattr(self, 'device_import_status', n.get_enum_value(ImportedWindowsAutopilotDeviceIdentityImportStatus)),
            "deviceRegistrationId": lambda n : setattr(self, 'device_registration_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_int_value("deviceErrorCode", self.device_error_code)
        writer.write_str_value("deviceErrorName", self.device_error_name)
        writer.write_enum_value("deviceImportStatus", self.device_import_status)
        writer.write_str_value("deviceRegistrationId", self.device_registration_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

