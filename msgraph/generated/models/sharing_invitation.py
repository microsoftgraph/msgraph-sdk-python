from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

identity_set = lazy_import('msgraph.generated.models.identity_set')

class SharingInvitation(AdditionalDataHolder, Parsable):
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
        Instantiates a new sharingInvitation and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The email address provided for the recipient of the sharing invitation. Read-only.
        self._email: Optional[str] = None
        # Provides information about who sent the invitation that created this permission, if that information is available. Read-only.
        self._invited_by: Optional[identity_set.IdentitySet] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The redeemedBy property
        self._redeemed_by: Optional[str] = None
        # If true the recipient of the invitation needs to sign in in order to access the shared item. Read-only.
        self._sign_in_required: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SharingInvitation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SharingInvitation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SharingInvitation()
    
    @property
    def email(self,) -> Optional[str]:
        """
        Gets the email property value. The email address provided for the recipient of the sharing invitation. Read-only.
        Returns: Optional[str]
        """
        return self._email
    
    @email.setter
    def email(self,value: Optional[str] = None) -> None:
        """
        Sets the email property value. The email address provided for the recipient of the sharing invitation. Read-only.
        Args:
            value: Value to set for the email property.
        """
        self._email = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "invited_by": lambda n : setattr(self, 'invited_by', n.get_object_value(identity_set.IdentitySet)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "redeemed_by": lambda n : setattr(self, 'redeemed_by', n.get_str_value()),
            "sign_in_required": lambda n : setattr(self, 'sign_in_required', n.get_bool_value()),
        }
        return fields
    
    @property
    def invited_by(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the invitedBy property value. Provides information about who sent the invitation that created this permission, if that information is available. Read-only.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._invited_by
    
    @invited_by.setter
    def invited_by(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the invitedBy property value. Provides information about who sent the invitation that created this permission, if that information is available. Read-only.
        Args:
            value: Value to set for the invitedBy property.
        """
        self._invited_by = value
    
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
    def redeemed_by(self,) -> Optional[str]:
        """
        Gets the redeemedBy property value. The redeemedBy property
        Returns: Optional[str]
        """
        return self._redeemed_by
    
    @redeemed_by.setter
    def redeemed_by(self,value: Optional[str] = None) -> None:
        """
        Sets the redeemedBy property value. The redeemedBy property
        Args:
            value: Value to set for the redeemedBy property.
        """
        self._redeemed_by = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("email", self.email)
        writer.write_object_value("invitedBy", self.invited_by)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("redeemedBy", self.redeemed_by)
        writer.write_bool_value("signInRequired", self.sign_in_required)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def sign_in_required(self,) -> Optional[bool]:
        """
        Gets the signInRequired property value. If true the recipient of the invitation needs to sign in in order to access the shared item. Read-only.
        Returns: Optional[bool]
        """
        return self._sign_in_required
    
    @sign_in_required.setter
    def sign_in_required(self,value: Optional[bool] = None) -> None:
        """
        Sets the signInRequired property value. If true the recipient of the invitation needs to sign in in order to access the shared item. Read-only.
        Args:
            value: Value to set for the signInRequired property.
        """
        self._sign_in_required = value
    

