from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .booking_page_access_control import BookingPageAccessControl

@dataclass
class BookingPageSettings(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The accessControl property
    access_control: Optional[BookingPageAccessControl] = None
    # Custom color for bookings page. Value should be in Hex format. Example: `#123456`.
    booking_page_color_code: Optional[str] = None
    # The time zone of the customer. For a list of possible values, see [dateTimeTimeZone](https://learn.microsoft.com/en-us/graph/api/resources/datetimetimezone?view=graph-rest-beta).
    business_time_zone: Optional[str] = None
    # Customer consent message that is displayed in the Booking page.
    customer_consent_message: Optional[str] = None
    # Enforcing One Time Password (OTP) during appointment creation.
    enforce_one_time_password: Optional[bool] = None
    # Enable display of business logo display on the Bookings page.
    is_business_logo_display_enabled: Optional[bool] = None
    # Enforces customer consent on the customer consent message before appointment is booked.
    is_customer_consent_enabled: Optional[bool] = None
    # Disable booking page to be indexed by search engines. False by default.
    is_search_engine_indexability_disabled: Optional[bool] = None
    # If business time zone the default value for the time slots that we show in the bookings page. False by default.
    is_time_slot_time_zone_set_to_business_time_zone: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The URL of the business' Privacy Policy.
    privacy_policy_web_url: Optional[str] = None
    # The URL of the business' Terms and Conditions.
    terms_and_conditions_web_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BookingPageSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BookingPageSettings
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return BookingPageSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .booking_page_access_control import BookingPageAccessControl

        from .booking_page_access_control import BookingPageAccessControl

        fields: Dict[str, Callable[[Any], None]] = {
            "accessControl": lambda n : setattr(self, 'access_control', n.get_enum_value(BookingPageAccessControl)),
            "bookingPageColorCode": lambda n : setattr(self, 'booking_page_color_code', n.get_str_value()),
            "businessTimeZone": lambda n : setattr(self, 'business_time_zone', n.get_str_value()),
            "customerConsentMessage": lambda n : setattr(self, 'customer_consent_message', n.get_str_value()),
            "enforceOneTimePassword": lambda n : setattr(self, 'enforce_one_time_password', n.get_bool_value()),
            "isBusinessLogoDisplayEnabled": lambda n : setattr(self, 'is_business_logo_display_enabled', n.get_bool_value()),
            "isCustomerConsentEnabled": lambda n : setattr(self, 'is_customer_consent_enabled', n.get_bool_value()),
            "isSearchEngineIndexabilityDisabled": lambda n : setattr(self, 'is_search_engine_indexability_disabled', n.get_bool_value()),
            "isTimeSlotTimeZoneSetToBusinessTimeZone": lambda n : setattr(self, 'is_time_slot_time_zone_set_to_business_time_zone', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "privacyPolicyWebUrl": lambda n : setattr(self, 'privacy_policy_web_url', n.get_str_value()),
            "termsAndConditionsWebUrl": lambda n : setattr(self, 'terms_and_conditions_web_url', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_enum_value("accessControl", self.access_control)
        writer.write_str_value("bookingPageColorCode", self.booking_page_color_code)
        writer.write_str_value("businessTimeZone", self.business_time_zone)
        writer.write_str_value("customerConsentMessage", self.customer_consent_message)
        writer.write_bool_value("enforceOneTimePassword", self.enforce_one_time_password)
        writer.write_bool_value("isBusinessLogoDisplayEnabled", self.is_business_logo_display_enabled)
        writer.write_bool_value("isCustomerConsentEnabled", self.is_customer_consent_enabled)
        writer.write_bool_value("isSearchEngineIndexabilityDisabled", self.is_search_engine_indexability_disabled)
        writer.write_bool_value("isTimeSlotTimeZoneSetToBusinessTimeZone", self.is_time_slot_time_zone_set_to_business_time_zone)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("privacyPolicyWebUrl", self.privacy_policy_web_url)
        writer.write_str_value("termsAndConditionsWebUrl", self.terms_and_conditions_web_url)
        writer.write_additional_data_value(self.additional_data)
    

