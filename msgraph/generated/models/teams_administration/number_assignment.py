from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .activation_state import ActivationState
    from .assignment_category import AssignmentCategory
    from .assignment_status import AssignmentStatus
    from .customer_action import CustomerAction
    from .number_capability import NumberCapability
    from .number_source import NumberSource
    from .number_type import NumberType
    from .port_in_status import PortInStatus
    from .reverse_number_lookup_option import ReverseNumberLookupOption

from ..entity import Entity

@dataclass
class NumberAssignment(Entity, Parsable):
    # The activationState property
    activation_state: Optional[ActivationState] = None
    # Contains the assignment category such as Primary or Private. The possible values are: primary, private, alternate, unknownFutureValue.
    assignment_category: Optional[AssignmentCategory] = None
    # The assignment status of the phone number. The possible values are: unassigned, internalError, userAssigned, conferenceAssigned, voiceApplicationAssigned, thirdPartyAppAssigned, policyAssigned, unknownFutureValue.
    assignment_status: Optional[AssignmentStatus] = None
    # The ID of the object the phone number is assigned to, either the ObjectId of a user or resource account, or the policy instance ID of a Teams shared calling routing policy instance.
    assignment_target_id: Optional[str] = None
    # The list of capabilities assigned to the phone number.
    capabilities: Optional[list[NumberCapability]] = None
    # The city where the phone number is located or associated with.
    city: Optional[str] = None
    # The ID of the civic address assigned to the phone number.
    civic_address_id: Optional[str] = None
    # The ISO country code assigned to the phone number.
    iso_country_code: Optional[str] = None
    # The ID of the location assigned to the phone number.
    location_id: Optional[str] = None
    # This property is reserved for internal Microsoft use.
    network_site_id: Optional[str] = None
    # The source of the phone number. online is used for phone numbers assigned in Microsoft 365, and onPremises is used for phone numbers assigned in AD on-premises, which are synchronized into Microsoft 365. The possible values are: online, onPremises, unknownFutureValue.
    number_source: Optional[NumberSource] = None
    # The numberType property
    number_type: Optional[NumberType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The ID of the operator.
    operator_id: Optional[str] = None
    # The status of any port in order covering the phone number. The possible values are: completed, firmOrderCommitmentAccepted, unknownFutureValue.
    port_in_status: Optional[PortInStatus] = None
    # Status of Reverse Number Lookup (RNL). If set to skipInternalVoip, calls are routed through the external Public Switched Telephone Network (PSTN) instead of using internal VoIP resolution.
    reverse_number_lookup_options: Optional[list[ReverseNumberLookupOption]] = None
    # Indicates what customer actions are available to modify the number.
    supported_customer_actions: Optional[list[CustomerAction]] = None
    # The telephone number in the record. The recorded telephone number is always displayed with a '+' prefix, regardless of whether it was originally assigned with one.
    telephone_number: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> NumberAssignment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: NumberAssignment
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return NumberAssignment()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .activation_state import ActivationState
        from .assignment_category import AssignmentCategory
        from .assignment_status import AssignmentStatus
        from .customer_action import CustomerAction
        from .number_capability import NumberCapability
        from .number_source import NumberSource
        from .number_type import NumberType
        from .port_in_status import PortInStatus
        from .reverse_number_lookup_option import ReverseNumberLookupOption

        from ..entity import Entity
        from .activation_state import ActivationState
        from .assignment_category import AssignmentCategory
        from .assignment_status import AssignmentStatus
        from .customer_action import CustomerAction
        from .number_capability import NumberCapability
        from .number_source import NumberSource
        from .number_type import NumberType
        from .port_in_status import PortInStatus
        from .reverse_number_lookup_option import ReverseNumberLookupOption

        fields: dict[str, Callable[[Any], None]] = {
            "activationState": lambda n : setattr(self, 'activation_state', n.get_enum_value(ActivationState)),
            "assignmentCategory": lambda n : setattr(self, 'assignment_category', n.get_enum_value(AssignmentCategory)),
            "assignmentStatus": lambda n : setattr(self, 'assignment_status', n.get_enum_value(AssignmentStatus)),
            "assignmentTargetId": lambda n : setattr(self, 'assignment_target_id', n.get_str_value()),
            "capabilities": lambda n : setattr(self, 'capabilities', n.get_collection_of_enum_values(NumberCapability)),
            "city": lambda n : setattr(self, 'city', n.get_str_value()),
            "civicAddressId": lambda n : setattr(self, 'civic_address_id', n.get_str_value()),
            "isoCountryCode": lambda n : setattr(self, 'iso_country_code', n.get_str_value()),
            "locationId": lambda n : setattr(self, 'location_id', n.get_str_value()),
            "networkSiteId": lambda n : setattr(self, 'network_site_id', n.get_str_value()),
            "numberSource": lambda n : setattr(self, 'number_source', n.get_enum_value(NumberSource)),
            "numberType": lambda n : setattr(self, 'number_type', n.get_enum_value(NumberType)),
            "operatorId": lambda n : setattr(self, 'operator_id', n.get_str_value()),
            "portInStatus": lambda n : setattr(self, 'port_in_status', n.get_enum_value(PortInStatus)),
            "reverseNumberLookupOptions": lambda n : setattr(self, 'reverse_number_lookup_options', n.get_collection_of_enum_values(ReverseNumberLookupOption)),
            "supportedCustomerActions": lambda n : setattr(self, 'supported_customer_actions', n.get_collection_of_enum_values(CustomerAction)),
            "telephoneNumber": lambda n : setattr(self, 'telephone_number', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_enum_value("activationState", self.activation_state)
        writer.write_enum_value("assignmentCategory", self.assignment_category)
        writer.write_enum_value("assignmentStatus", self.assignment_status)
        writer.write_str_value("assignmentTargetId", self.assignment_target_id)
        writer.write_collection_of_enum_values("capabilities", self.capabilities)
        writer.write_str_value("city", self.city)
        writer.write_str_value("civicAddressId", self.civic_address_id)
        writer.write_str_value("isoCountryCode", self.iso_country_code)
        writer.write_str_value("locationId", self.location_id)
        writer.write_str_value("networkSiteId", self.network_site_id)
        writer.write_enum_value("numberSource", self.number_source)
        writer.write_enum_value("numberType", self.number_type)
        writer.write_str_value("operatorId", self.operator_id)
        writer.write_enum_value("portInStatus", self.port_in_status)
        writer.write_collection_of_enum_values("reverseNumberLookupOptions", self.reverse_number_lookup_options)
        writer.write_collection_of_enum_values("supportedCustomerActions", self.supported_customer_actions)
        writer.write_str_value("telephoneNumber", self.telephone_number)
    

