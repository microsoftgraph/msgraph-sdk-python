from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
identity_user_flow_attribute = lazy_import('msgraph.generated.models.identity_user_flow_attribute')
identity_user_flow_attribute_input_type = lazy_import('msgraph.generated.models.identity_user_flow_attribute_input_type')
user_attribute_values_item = lazy_import('msgraph.generated.models.user_attribute_values_item')

class IdentityUserFlowAttributeAssignment(entity.Entity):
    """
    Provides operations to manage the collection of agreement entities.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new identityUserFlowAttributeAssignment and sets the default values.
        """
        super().__init__()
        # The display name of the identityUserFlowAttribute within a user flow.
        self._display_name: Optional[str] = None
        # Determines whether the identityUserFlowAttribute is optional. true means the user doesn't have to provide a value. false means the user cannot complete sign-up without providing a value.
        self._is_optional: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Determines whether the identityUserFlowAttribute requires verification. This is only used for verifying the user's phone number or email address.
        self._requires_verification: Optional[bool] = None
        # The user attribute that you want to add to your user flow.
        self._user_attribute: Optional[identity_user_flow_attribute.IdentityUserFlowAttribute] = None
        # The input options for the user flow attribute. Only applicable when the userInputType is radioSingleSelect, dropdownSingleSelect, or checkboxMultiSelect.
        self._user_attribute_values: Optional[List[user_attribute_values_item.UserAttributeValuesItem]] = None
        # The userInputType property
        self._user_input_type: Optional[identity_user_flow_attribute_input_type.IdentityUserFlowAttributeInputType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IdentityUserFlowAttributeAssignment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IdentityUserFlowAttributeAssignment
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IdentityUserFlowAttributeAssignment()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name of the identityUserFlowAttribute within a user flow.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name of the identityUserFlowAttribute within a user flow.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "is_optional": lambda n : setattr(self, 'is_optional', n.get_bool_value()),
            "requires_verification": lambda n : setattr(self, 'requires_verification', n.get_bool_value()),
            "user_attribute": lambda n : setattr(self, 'user_attribute', n.get_object_value(identity_user_flow_attribute.IdentityUserFlowAttribute)),
            "user_attribute_values": lambda n : setattr(self, 'user_attribute_values', n.get_collection_of_object_values(user_attribute_values_item.UserAttributeValuesItem)),
            "user_input_type": lambda n : setattr(self, 'user_input_type', n.get_enum_value(identity_user_flow_attribute_input_type.IdentityUserFlowAttributeInputType)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_optional(self,) -> Optional[bool]:
        """
        Gets the isOptional property value. Determines whether the identityUserFlowAttribute is optional. true means the user doesn't have to provide a value. false means the user cannot complete sign-up without providing a value.
        Returns: Optional[bool]
        """
        return self._is_optional
    
    @is_optional.setter
    def is_optional(self,value: Optional[bool] = None) -> None:
        """
        Sets the isOptional property value. Determines whether the identityUserFlowAttribute is optional. true means the user doesn't have to provide a value. false means the user cannot complete sign-up without providing a value.
        Args:
            value: Value to set for the isOptional property.
        """
        self._is_optional = value
    
    @property
    def requires_verification(self,) -> Optional[bool]:
        """
        Gets the requiresVerification property value. Determines whether the identityUserFlowAttribute requires verification. This is only used for verifying the user's phone number or email address.
        Returns: Optional[bool]
        """
        return self._requires_verification
    
    @requires_verification.setter
    def requires_verification(self,value: Optional[bool] = None) -> None:
        """
        Sets the requiresVerification property value. Determines whether the identityUserFlowAttribute requires verification. This is only used for verifying the user's phone number or email address.
        Args:
            value: Value to set for the requiresVerification property.
        """
        self._requires_verification = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("isOptional", self.is_optional)
        writer.write_bool_value("requiresVerification", self.requires_verification)
        writer.write_object_value("userAttribute", self.user_attribute)
        writer.write_collection_of_object_values("userAttributeValues", self.user_attribute_values)
        writer.write_enum_value("userInputType", self.user_input_type)
    
    @property
    def user_attribute(self,) -> Optional[identity_user_flow_attribute.IdentityUserFlowAttribute]:
        """
        Gets the userAttribute property value. The user attribute that you want to add to your user flow.
        Returns: Optional[identity_user_flow_attribute.IdentityUserFlowAttribute]
        """
        return self._user_attribute
    
    @user_attribute.setter
    def user_attribute(self,value: Optional[identity_user_flow_attribute.IdentityUserFlowAttribute] = None) -> None:
        """
        Sets the userAttribute property value. The user attribute that you want to add to your user flow.
        Args:
            value: Value to set for the userAttribute property.
        """
        self._user_attribute = value
    
    @property
    def user_attribute_values(self,) -> Optional[List[user_attribute_values_item.UserAttributeValuesItem]]:
        """
        Gets the userAttributeValues property value. The input options for the user flow attribute. Only applicable when the userInputType is radioSingleSelect, dropdownSingleSelect, or checkboxMultiSelect.
        Returns: Optional[List[user_attribute_values_item.UserAttributeValuesItem]]
        """
        return self._user_attribute_values
    
    @user_attribute_values.setter
    def user_attribute_values(self,value: Optional[List[user_attribute_values_item.UserAttributeValuesItem]] = None) -> None:
        """
        Sets the userAttributeValues property value. The input options for the user flow attribute. Only applicable when the userInputType is radioSingleSelect, dropdownSingleSelect, or checkboxMultiSelect.
        Args:
            value: Value to set for the userAttributeValues property.
        """
        self._user_attribute_values = value
    
    @property
    def user_input_type(self,) -> Optional[identity_user_flow_attribute_input_type.IdentityUserFlowAttributeInputType]:
        """
        Gets the userInputType property value. The userInputType property
        Returns: Optional[identity_user_flow_attribute_input_type.IdentityUserFlowAttributeInputType]
        """
        return self._user_input_type
    
    @user_input_type.setter
    def user_input_type(self,value: Optional[identity_user_flow_attribute_input_type.IdentityUserFlowAttributeInputType] = None) -> None:
        """
        Sets the userInputType property value. The userInputType property
        Args:
            value: Value to set for the userInputType property.
        """
        self._user_input_type = value
    

