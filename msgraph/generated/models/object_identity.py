from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class ObjectIdentity(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Specifies the issuer of the identity, for example facebook.com. 512 character limit. For local accounts (where signInType isn't federated), this property is the local default domain name for the tenant, for example contoso.com.  For guests from other Microsoft Entra organizations, this is the domain of the federated organization, for example contoso.com. For more information about filtering behavior for this property, see Filtering on the identities property of a user.
    issuer: Optional[str] = None
    # Specifies the unique identifier assigned to the user by the issuer. 64 character limit. The combination of issuer and issuerAssignedId must be unique within the organization. Represents the sign-in name for the user, when signInType is set to emailAddress or userName (also known as local accounts).When signInType is set to: emailAddress (or a custom string that starts with emailAddress like emailAddress1), issuerAssignedId must be a valid email addressuserName, issuerAssignedId must begin with an alphabetical character or number, and can only contain alphanumeric characters and the following symbols: - or _  For more information about filtering behavior for this property, see Filtering on the identities property of a user.
    issuer_assigned_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Specifies the user sign-in types in your directory, such as emailAddress, userName, federated, or userPrincipalName. federated represents a unique identifier for a user from an issuer that can be in any format chosen by the issuer. Setting or updating a userPrincipalName identity updates the value of the userPrincipalName property on the user object. The validations performed on the userPrincipalName property on the user object, for example, verified domains and acceptable characters, are performed when setting or updating a userPrincipalName identity. Extra validation is enforced on issuerAssignedId when the sign-in type is set to emailAddress or userName. This property can also be set to any custom string.  For more information about filtering behavior for this property, see Filtering on the identities property of a user.
    sign_in_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ObjectIdentity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ObjectIdentity
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ObjectIdentity()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "issuer": lambda n : setattr(self, 'issuer', n.get_str_value()),
            "issuerAssignedId": lambda n : setattr(self, 'issuer_assigned_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "signInType": lambda n : setattr(self, 'sign_in_type', n.get_str_value()),
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
        writer.write_str_value("issuer", self.issuer)
        writer.write_str_value("issuerAssignedId", self.issuer_assigned_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("signInType", self.sign_in_type)
        writer.write_additional_data_value(self.additional_data)
    

