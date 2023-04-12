from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class IdleSessionSignOut(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new idleSessionSignOut and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The isEnabled property
        self._is_enabled: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The signOutAfterInSeconds property
        self._sign_out_after_in_seconds: Optional[int] = None
        # The warnAfterInSeconds property
        self._warn_after_in_seconds: Optional[int] = None
    
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
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IdleSessionSignOut:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IdleSessionSignOut
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IdleSessionSignOut()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "isEnabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "signOutAfterInSeconds": lambda n : setattr(self, 'sign_out_after_in_seconds', n.get_int_value()),
            "warnAfterInSeconds": lambda n : setattr(self, 'warn_after_in_seconds', n.get_int_value()),
        }
        return fields
    
    @property
    def is_enabled(self,) -> Optional[bool]:
        """
        Gets the isEnabled property value. The isEnabled property
        Returns: Optional[bool]
        """
        return self._is_enabled
    
    @is_enabled.setter
    def is_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isEnabled property value. The isEnabled property
        Args:
            value: Value to set for the is_enabled property.
        """
        self._is_enabled = value
    
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
            value: Value to set for the odata_type property.
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
        writer.write_bool_value("isEnabled", self.is_enabled)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("signOutAfterInSeconds", self.sign_out_after_in_seconds)
        writer.write_int_value("warnAfterInSeconds", self.warn_after_in_seconds)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def sign_out_after_in_seconds(self,) -> Optional[int]:
        """
        Gets the signOutAfterInSeconds property value. The signOutAfterInSeconds property
        Returns: Optional[int]
        """
        return self._sign_out_after_in_seconds
    
    @sign_out_after_in_seconds.setter
    def sign_out_after_in_seconds(self,value: Optional[int] = None) -> None:
        """
        Sets the signOutAfterInSeconds property value. The signOutAfterInSeconds property
        Args:
            value: Value to set for the sign_out_after_in_seconds property.
        """
        self._sign_out_after_in_seconds = value
    
    @property
    def warn_after_in_seconds(self,) -> Optional[int]:
        """
        Gets the warnAfterInSeconds property value. The warnAfterInSeconds property
        Returns: Optional[int]
        """
        return self._warn_after_in_seconds
    
    @warn_after_in_seconds.setter
    def warn_after_in_seconds(self,value: Optional[int] = None) -> None:
        """
        Sets the warnAfterInSeconds property value. The warnAfterInSeconds property
        Args:
            value: Value to set for the warn_after_in_seconds property.
        """
        self._warn_after_in_seconds = value
    

