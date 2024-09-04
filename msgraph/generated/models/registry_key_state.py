from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .registry_hive import RegistryHive
    from .registry_operation import RegistryOperation
    from .registry_value_type import RegistryValueType

@dataclass
class RegistryKeyState(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # A Windows registry hive : HKEYCURRENTCONFIG HKEYCURRENTUSER HKEYLOCALMACHINE/SAM HKEYLOCALMACHINE/Security HKEYLOCALMACHINE/Software HKEYLOCALMACHINE/System HKEY_USERS/.Default. Possible values are: unknown, currentConfig, currentUser, localMachineSam, localMachineSecurity, localMachineSoftware, localMachineSystem, usersDefault.
    hive: Optional[RegistryHive] = None
    # Current (i.e. changed) registry key (excludes HIVE).
    key: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Previous (i.e. before changed) registry key (excludes HIVE).
    old_key: Optional[str] = None
    # Previous (i.e. before changed) registry key value data (contents).
    old_value_data: Optional[str] = None
    # Previous (i.e. before changed) registry key value name.
    old_value_name: Optional[str] = None
    # Operation that changed the registry key name and/or value. Possible values are: unknown, create, modify, delete.
    operation: Optional[RegistryOperation] = None
    # Process ID (PID) of the process that modified the registry key (process details will appear in the alert 'processes' collection).
    process_id: Optional[int] = None
    # Current (i.e. changed) registry key value data (contents).
    value_data: Optional[str] = None
    # Current (i.e. changed) registry key value name
    value_name: Optional[str] = None
    # Registry key value type REGBINARY REGDWORD REGDWORDLITTLEENDIAN REGDWORDBIGENDIANREGEXPANDSZ REGLINK REGMULTISZ REGNONE REGQWORD REGQWORDLITTLEENDIAN REG_SZ Possible values are: unknown, binary, dword, dwordLittleEndian, dwordBigEndian, expandSz, link, multiSz, none, qword, qwordlittleEndian, sz.
    value_type: Optional[RegistryValueType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RegistryKeyState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RegistryKeyState
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RegistryKeyState()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .registry_hive import RegistryHive
        from .registry_operation import RegistryOperation
        from .registry_value_type import RegistryValueType

        from .registry_hive import RegistryHive
        from .registry_operation import RegistryOperation
        from .registry_value_type import RegistryValueType

        fields: Dict[str, Callable[[Any], None]] = {
            "hive": lambda n : setattr(self, 'hive', n.get_enum_value(RegistryHive)),
            "key": lambda n : setattr(self, 'key', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "oldKey": lambda n : setattr(self, 'old_key', n.get_str_value()),
            "oldValueData": lambda n : setattr(self, 'old_value_data', n.get_str_value()),
            "oldValueName": lambda n : setattr(self, 'old_value_name', n.get_str_value()),
            "operation": lambda n : setattr(self, 'operation', n.get_enum_value(RegistryOperation)),
            "processId": lambda n : setattr(self, 'process_id', n.get_int_value()),
            "valueData": lambda n : setattr(self, 'value_data', n.get_str_value()),
            "valueName": lambda n : setattr(self, 'value_name', n.get_str_value()),
            "valueType": lambda n : setattr(self, 'value_type', n.get_enum_value(RegistryValueType)),
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
        writer.write_enum_value("hive", self.hive)
        writer.write_str_value("key", self.key)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("oldKey", self.old_key)
        writer.write_str_value("oldValueData", self.old_value_data)
        writer.write_str_value("oldValueName", self.old_value_name)
        writer.write_enum_value("operation", self.operation)
        writer.write_int_value("processId", self.process_id)
        writer.write_str_value("valueData", self.value_data)
        writer.write_str_value("valueName", self.value_name)
        writer.write_enum_value("valueType", self.value_type)
        writer.write_additional_data_value(self.additional_data)
    

