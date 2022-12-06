from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

registry_hive = lazy_import('msgraph.generated.models.registry_hive')
registry_operation = lazy_import('msgraph.generated.models.registry_operation')
registry_value_type = lazy_import('msgraph.generated.models.registry_value_type')

class RegistryKeyState(AdditionalDataHolder, Parsable):
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
        Instantiates a new registryKeyState and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # A Windows registry hive : HKEY_CURRENT_CONFIG HKEY_CURRENT_USER HKEY_LOCAL_MACHINE/SAM HKEY_LOCAL_MACHINE/Security HKEY_LOCAL_MACHINE/Software HKEY_LOCAL_MACHINE/System HKEY_USERS/.Default. Possible values are: unknown, currentConfig, currentUser, localMachineSam, localMachineSecurity, localMachineSoftware, localMachineSystem, usersDefault.
        self._hive: Optional[registry_hive.RegistryHive] = None
        # Current (i.e. changed) registry key (excludes HIVE).
        self._key: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Previous (i.e. before changed) registry key (excludes HIVE).
        self._old_key: Optional[str] = None
        # Previous (i.e. before changed) registry key value data (contents).
        self._old_value_data: Optional[str] = None
        # Previous (i.e. before changed) registry key value name.
        self._old_value_name: Optional[str] = None
        # Operation that changed the registry key name and/or value. Possible values are: unknown, create, modify, delete.
        self._operation: Optional[registry_operation.RegistryOperation] = None
        # Process ID (PID) of the process that modified the registry key (process details will appear in the alert 'processes' collection).
        self._process_id: Optional[int] = None
        # Current (i.e. changed) registry key value data (contents).
        self._value_data: Optional[str] = None
        # Current (i.e. changed) registry key value name
        self._value_name: Optional[str] = None
        # Registry key value type REG_BINARY REG_DWORD REG_DWORD_LITTLE_ENDIAN REG_DWORD_BIG_ENDIANREG_EXPAND_SZ REG_LINK REG_MULTI_SZ REG_NONE REG_QWORD REG_QWORD_LITTLE_ENDIAN REG_SZ Possible values are: unknown, binary, dword, dwordLittleEndian, dwordBigEndian, expandSz, link, multiSz, none, qword, qwordlittleEndian, sz.
        self._value_type: Optional[registry_value_type.RegistryValueType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RegistryKeyState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RegistryKeyState
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RegistryKeyState()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "hive": lambda n : setattr(self, 'hive', n.get_enum_value(registry_hive.RegistryHive)),
            "key": lambda n : setattr(self, 'key', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "old_key": lambda n : setattr(self, 'old_key', n.get_str_value()),
            "old_value_data": lambda n : setattr(self, 'old_value_data', n.get_str_value()),
            "old_value_name": lambda n : setattr(self, 'old_value_name', n.get_str_value()),
            "operation": lambda n : setattr(self, 'operation', n.get_enum_value(registry_operation.RegistryOperation)),
            "process_id": lambda n : setattr(self, 'process_id', n.get_int_value()),
            "value_data": lambda n : setattr(self, 'value_data', n.get_str_value()),
            "value_name": lambda n : setattr(self, 'value_name', n.get_str_value()),
            "value_type": lambda n : setattr(self, 'value_type', n.get_enum_value(registry_value_type.RegistryValueType)),
        }
        return fields
    
    @property
    def hive(self,) -> Optional[registry_hive.RegistryHive]:
        """
        Gets the hive property value. A Windows registry hive : HKEY_CURRENT_CONFIG HKEY_CURRENT_USER HKEY_LOCAL_MACHINE/SAM HKEY_LOCAL_MACHINE/Security HKEY_LOCAL_MACHINE/Software HKEY_LOCAL_MACHINE/System HKEY_USERS/.Default. Possible values are: unknown, currentConfig, currentUser, localMachineSam, localMachineSecurity, localMachineSoftware, localMachineSystem, usersDefault.
        Returns: Optional[registry_hive.RegistryHive]
        """
        return self._hive
    
    @hive.setter
    def hive(self,value: Optional[registry_hive.RegistryHive] = None) -> None:
        """
        Sets the hive property value. A Windows registry hive : HKEY_CURRENT_CONFIG HKEY_CURRENT_USER HKEY_LOCAL_MACHINE/SAM HKEY_LOCAL_MACHINE/Security HKEY_LOCAL_MACHINE/Software HKEY_LOCAL_MACHINE/System HKEY_USERS/.Default. Possible values are: unknown, currentConfig, currentUser, localMachineSam, localMachineSecurity, localMachineSoftware, localMachineSystem, usersDefault.
        Args:
            value: Value to set for the hive property.
        """
        self._hive = value
    
    @property
    def key(self,) -> Optional[str]:
        """
        Gets the key property value. Current (i.e. changed) registry key (excludes HIVE).
        Returns: Optional[str]
        """
        return self._key
    
    @key.setter
    def key(self,value: Optional[str] = None) -> None:
        """
        Sets the key property value. Current (i.e. changed) registry key (excludes HIVE).
        Args:
            value: Value to set for the key property.
        """
        self._key = value
    
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
    
    @property
    def old_key(self,) -> Optional[str]:
        """
        Gets the oldKey property value. Previous (i.e. before changed) registry key (excludes HIVE).
        Returns: Optional[str]
        """
        return self._old_key
    
    @old_key.setter
    def old_key(self,value: Optional[str] = None) -> None:
        """
        Sets the oldKey property value. Previous (i.e. before changed) registry key (excludes HIVE).
        Args:
            value: Value to set for the oldKey property.
        """
        self._old_key = value
    
    @property
    def old_value_data(self,) -> Optional[str]:
        """
        Gets the oldValueData property value. Previous (i.e. before changed) registry key value data (contents).
        Returns: Optional[str]
        """
        return self._old_value_data
    
    @old_value_data.setter
    def old_value_data(self,value: Optional[str] = None) -> None:
        """
        Sets the oldValueData property value. Previous (i.e. before changed) registry key value data (contents).
        Args:
            value: Value to set for the oldValueData property.
        """
        self._old_value_data = value
    
    @property
    def old_value_name(self,) -> Optional[str]:
        """
        Gets the oldValueName property value. Previous (i.e. before changed) registry key value name.
        Returns: Optional[str]
        """
        return self._old_value_name
    
    @old_value_name.setter
    def old_value_name(self,value: Optional[str] = None) -> None:
        """
        Sets the oldValueName property value. Previous (i.e. before changed) registry key value name.
        Args:
            value: Value to set for the oldValueName property.
        """
        self._old_value_name = value
    
    @property
    def operation(self,) -> Optional[registry_operation.RegistryOperation]:
        """
        Gets the operation property value. Operation that changed the registry key name and/or value. Possible values are: unknown, create, modify, delete.
        Returns: Optional[registry_operation.RegistryOperation]
        """
        return self._operation
    
    @operation.setter
    def operation(self,value: Optional[registry_operation.RegistryOperation] = None) -> None:
        """
        Sets the operation property value. Operation that changed the registry key name and/or value. Possible values are: unknown, create, modify, delete.
        Args:
            value: Value to set for the operation property.
        """
        self._operation = value
    
    @property
    def process_id(self,) -> Optional[int]:
        """
        Gets the processId property value. Process ID (PID) of the process that modified the registry key (process details will appear in the alert 'processes' collection).
        Returns: Optional[int]
        """
        return self._process_id
    
    @process_id.setter
    def process_id(self,value: Optional[int] = None) -> None:
        """
        Sets the processId property value. Process ID (PID) of the process that modified the registry key (process details will appear in the alert 'processes' collection).
        Args:
            value: Value to set for the processId property.
        """
        self._process_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
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
    
    @property
    def value_data(self,) -> Optional[str]:
        """
        Gets the valueData property value. Current (i.e. changed) registry key value data (contents).
        Returns: Optional[str]
        """
        return self._value_data
    
    @value_data.setter
    def value_data(self,value: Optional[str] = None) -> None:
        """
        Sets the valueData property value. Current (i.e. changed) registry key value data (contents).
        Args:
            value: Value to set for the valueData property.
        """
        self._value_data = value
    
    @property
    def value_name(self,) -> Optional[str]:
        """
        Gets the valueName property value. Current (i.e. changed) registry key value name
        Returns: Optional[str]
        """
        return self._value_name
    
    @value_name.setter
    def value_name(self,value: Optional[str] = None) -> None:
        """
        Sets the valueName property value. Current (i.e. changed) registry key value name
        Args:
            value: Value to set for the valueName property.
        """
        self._value_name = value
    
    @property
    def value_type(self,) -> Optional[registry_value_type.RegistryValueType]:
        """
        Gets the valueType property value. Registry key value type REG_BINARY REG_DWORD REG_DWORD_LITTLE_ENDIAN REG_DWORD_BIG_ENDIANREG_EXPAND_SZ REG_LINK REG_MULTI_SZ REG_NONE REG_QWORD REG_QWORD_LITTLE_ENDIAN REG_SZ Possible values are: unknown, binary, dword, dwordLittleEndian, dwordBigEndian, expandSz, link, multiSz, none, qword, qwordlittleEndian, sz.
        Returns: Optional[registry_value_type.RegistryValueType]
        """
        return self._value_type
    
    @value_type.setter
    def value_type(self,value: Optional[registry_value_type.RegistryValueType] = None) -> None:
        """
        Sets the valueType property value. Registry key value type REG_BINARY REG_DWORD REG_DWORD_LITTLE_ENDIAN REG_DWORD_BIG_ENDIANREG_EXPAND_SZ REG_LINK REG_MULTI_SZ REG_NONE REG_QWORD REG_QWORD_LITTLE_ENDIAN REG_SZ Possible values are: unknown, binary, dword, dwordLittleEndian, dwordBigEndian, expandSz, link, multiSz, none, qword, qwordlittleEndian, sz.
        Args:
            value: Value to set for the valueType property.
        """
        self._value_type = value
    

