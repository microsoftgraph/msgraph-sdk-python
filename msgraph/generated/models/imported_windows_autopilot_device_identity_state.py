from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

imported_windows_autopilot_device_identity_import_status = lazy_import('msgraph.generated.models.imported_windows_autopilot_device_identity_import_status')

class ImportedWindowsAutopilotDeviceIdentityState(AdditionalDataHolder, Parsable):
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new importedWindowsAutopilotDeviceIdentityState and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Device error code reported by Device Directory Service(DDS).
        self._device_error_code: Optional[int] = None
        # Device error name reported by Device Directory Service(DDS).
        self._device_error_name: Optional[str] = None
        # The deviceImportStatus property
        self._device_import_status: Optional[imported_windows_autopilot_device_identity_import_status.ImportedWindowsAutopilotDeviceIdentityImportStatus] = None
        # Device Registration ID for successfully added device reported by Device Directory Service(DDS).
        self._device_registration_id: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ImportedWindowsAutopilotDeviceIdentityState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ImportedWindowsAutopilotDeviceIdentityState
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ImportedWindowsAutopilotDeviceIdentityState()
    
    @property
    def device_error_code(self,) -> Optional[int]:
        """
        Gets the deviceErrorCode property value. Device error code reported by Device Directory Service(DDS).
        Returns: Optional[int]
        """
        return self._device_error_code
    
    @device_error_code.setter
    def device_error_code(self,value: Optional[int] = None) -> None:
        """
        Sets the deviceErrorCode property value. Device error code reported by Device Directory Service(DDS).
        Args:
            value: Value to set for the deviceErrorCode property.
        """
        self._device_error_code = value
    
    @property
    def device_error_name(self,) -> Optional[str]:
        """
        Gets the deviceErrorName property value. Device error name reported by Device Directory Service(DDS).
        Returns: Optional[str]
        """
        return self._device_error_name
    
    @device_error_name.setter
    def device_error_name(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceErrorName property value. Device error name reported by Device Directory Service(DDS).
        Args:
            value: Value to set for the deviceErrorName property.
        """
        self._device_error_name = value
    
    @property
    def device_import_status(self,) -> Optional[imported_windows_autopilot_device_identity_import_status.ImportedWindowsAutopilotDeviceIdentityImportStatus]:
        """
        Gets the deviceImportStatus property value. The deviceImportStatus property
        Returns: Optional[imported_windows_autopilot_device_identity_import_status.ImportedWindowsAutopilotDeviceIdentityImportStatus]
        """
        return self._device_import_status
    
    @device_import_status.setter
    def device_import_status(self,value: Optional[imported_windows_autopilot_device_identity_import_status.ImportedWindowsAutopilotDeviceIdentityImportStatus] = None) -> None:
        """
        Sets the deviceImportStatus property value. The deviceImportStatus property
        Args:
            value: Value to set for the deviceImportStatus property.
        """
        self._device_import_status = value
    
    @property
    def device_registration_id(self,) -> Optional[str]:
        """
        Gets the deviceRegistrationId property value. Device Registration ID for successfully added device reported by Device Directory Service(DDS).
        Returns: Optional[str]
        """
        return self._device_registration_id
    
    @device_registration_id.setter
    def device_registration_id(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceRegistrationId property value. Device Registration ID for successfully added device reported by Device Directory Service(DDS).
        Args:
            value: Value to set for the deviceRegistrationId property.
        """
        self._device_registration_id = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "device_error_code": lambda n : setattr(self, 'device_error_code', n.get_int_value()),
            "device_error_name": lambda n : setattr(self, 'device_error_name', n.get_str_value()),
            "device_import_status": lambda n : setattr(self, 'device_import_status', n.get_enum_value(imported_windows_autopilot_device_identity_import_status.ImportedWindowsAutopilotDeviceIdentityImportStatus)),
            "device_registration_id": lambda n : setattr(self, 'device_registration_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_int_value("deviceErrorCode", self.device_error_code)
        writer.write_str_value("deviceErrorName", self.device_error_name)
        writer.write_enum_value("deviceImportStatus", self.device_import_status)
        writer.write_str_value("deviceRegistrationId", self.device_registration_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

