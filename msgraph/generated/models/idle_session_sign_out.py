from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class IdleSessionSignOut(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Indicates whether the idle session sign-out policy is enabled.
    is_enabled: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Number of seconds of inactivity after which a user is signed out.
    sign_out_after_in_seconds: Optional[int] = None
    # Number of seconds of inactivity after which a user is notified that they'll be signed out.
    warn_after_in_seconds: Optional[int] = None
    
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
    

