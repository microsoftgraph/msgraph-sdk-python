from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import conditional_access_all_external_tenants, conditional_access_enumerated_external_tenants, conditional_access_external_tenants_membership_kind

class ConditionalAccessExternalTenants(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new conditionalAccessExternalTenants and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The membership kind. Possible values are: all, enumerated, unknownFutureValue. The enumerated member references an conditionalAccessEnumeratedExternalTenants object.
        self._membership_kind: Optional[conditional_access_external_tenants_membership_kind.ConditionalAccessExternalTenantsMembershipKind] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ConditionalAccessExternalTenants:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ConditionalAccessExternalTenants
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.conditionalAccessAllExternalTenants":
                from . import conditional_access_all_external_tenants

                return conditional_access_all_external_tenants.ConditionalAccessAllExternalTenants()
            if mapping_value == "#microsoft.graph.conditionalAccessEnumeratedExternalTenants":
                from . import conditional_access_enumerated_external_tenants

                return conditional_access_enumerated_external_tenants.ConditionalAccessEnumeratedExternalTenants()
        return ConditionalAccessExternalTenants()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import conditional_access_all_external_tenants, conditional_access_enumerated_external_tenants, conditional_access_external_tenants_membership_kind

        fields: Dict[str, Callable[[Any], None]] = {
            "membershipKind": lambda n : setattr(self, 'membership_kind', n.get_enum_value(conditional_access_external_tenants_membership_kind.ConditionalAccessExternalTenantsMembershipKind)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def membership_kind(self,) -> Optional[conditional_access_external_tenants_membership_kind.ConditionalAccessExternalTenantsMembershipKind]:
        """
        Gets the membershipKind property value. The membership kind. Possible values are: all, enumerated, unknownFutureValue. The enumerated member references an conditionalAccessEnumeratedExternalTenants object.
        Returns: Optional[conditional_access_external_tenants_membership_kind.ConditionalAccessExternalTenantsMembershipKind]
        """
        return self._membership_kind
    
    @membership_kind.setter
    def membership_kind(self,value: Optional[conditional_access_external_tenants_membership_kind.ConditionalAccessExternalTenantsMembershipKind] = None) -> None:
        """
        Sets the membershipKind property value. The membership kind. Possible values are: all, enumerated, unknownFutureValue. The enumerated member references an conditionalAccessEnumeratedExternalTenants object.
        Args:
            value: Value to set for the membership_kind property.
        """
        self._membership_kind = value
    
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
        writer.write_enum_value("membershipKind", self.membership_kind)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

