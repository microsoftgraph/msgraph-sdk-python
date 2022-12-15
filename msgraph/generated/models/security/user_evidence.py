from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

alert_evidence = lazy_import('msgraph.generated.models.security.alert_evidence')
user_account = lazy_import('msgraph.generated.models.security.user_account')

class UserEvidence(alert_evidence.AlertEvidence):
    def __init__(self,) -> None:
        """
        Instantiates a new UserEvidence and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The user account details.
        self._user_account: Optional[user_account.UserAccount] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserEvidence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserEvidence
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserEvidence()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "user_account": lambda n : setattr(self, 'user_account', n.get_object_value(user_account.UserAccount)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("userAccount", self.user_account)
    
    @property
    def user_account(self,) -> Optional[user_account.UserAccount]:
        """
        Gets the userAccount property value. The user account details.
        Returns: Optional[user_account.UserAccount]
        """
        return self._user_account
    
    @user_account.setter
    def user_account(self,value: Optional[user_account.UserAccount] = None) -> None:
        """
        Sets the userAccount property value. The user account details.
        Args:
            value: Value to set for the userAccount property.
        """
        self._user_account = value
    

