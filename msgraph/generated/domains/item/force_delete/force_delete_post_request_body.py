from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class ForceDeletePostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the forceDelete method.
    """
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
        Instantiates a new forceDeletePostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The disableUserAccounts property
        self._disable_user_accounts: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ForceDeletePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ForceDeletePostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ForceDeletePostRequestBody()
    
    @property
    def disable_user_accounts(self,) -> Optional[bool]:
        """
        Gets the disableUserAccounts property value. The disableUserAccounts property
        Returns: Optional[bool]
        """
        return self._disable_user_accounts
    
    @disable_user_accounts.setter
    def disable_user_accounts(self,value: Optional[bool] = None) -> None:
        """
        Sets the disableUserAccounts property value. The disableUserAccounts property
        Args:
            value: Value to set for the disableUserAccounts property.
        """
        self._disable_user_accounts = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "disable_user_accounts": lambda n : setattr(self, 'disable_user_accounts', n.get_bool_value()),
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
        writer.write_bool_value("disableUserAccounts", self.disable_user_accounts)
        writer.write_additional_data_value(self.additional_data)
    

