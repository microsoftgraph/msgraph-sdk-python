from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import aad_user_conversation_member, access_package, access_package_assignment, access_package_assignment_policy, access_package_assignment_request, access_package_catalog, access_package_multiple_choice_question, access_package_question, access_package_subject, access_package_text_input_question, access_review_history_definition, access_review_history_instance, access_review_instance, access_review_instance_decision_item, access_review_reviewer, access_review_schedule_definition, access_review_set, access_review_stage, activity_based_timeout_policy, activity_history_item, add_large_gallery_view_operation, administrative_unit, admin_consent_request_policy, agreement, agreement_acceptance, agreement_file, agreement_file_localization, agreement_file_properties, agreement_file_version, alert, allowed_value, android_compliance_policy, android_custom_configuration, android_general_device_configuration, android_lob_app, android_managed_app_protection, android_managed_app_registration, android_store_app, android_work_profile_compliance_policy, android_work_profile_custom_configuration, android_work_profile_general_device_configuration, anonymous_guest_conversation_member, apple_device_features_configuration_base, apple_managed_identity_provider, apple_push_notification_certificate, application, application_template, approval, approval_stage, app_catalogs, app_consent_approval_route, app_consent_request, app_management_policy, app_role_assignment, app_scope, associated_team_info, attachment, attachment_base, attachment_session, attack_simulation_root, attendance_record, attribute_mapping_function_schema, attribute_set, audio_routing_group, audit_event, audit_log_root, authentication, authentication_combination_configuration, authentication_context_class_reference, authentication_flows_policy, authentication_method, authentication_methods_policy, authentication_method_configuration, authentication_method_mode_detail, authentication_method_target, authentication_strength_policy, authentication_strength_root, authored_note, authorization_policy, azure_communication_services_user_conversation_member, b2x_identity_user_flow, base_item, base_item_version, bitlocker, bitlocker_recovery_key, booking_appointment, booking_business, booking_currency, booking_customer, booking_customer_base, booking_custom_question, booking_service, booking_staff_member, booking_staff_member_base, browser_shared_cookie, browser_site, browser_site_list, built_in_identity_provider, calendar, calendar_group, calendar_permission, calendar_sharing_message, call, cancel_media_processing_operation, certificate_based_auth_configuration, change_tracked_entity, channel, chat, chat_message, chat_message_hosted_content, chat_message_info, checklist_item, claims_mapping_policy, column_definition, column_link, comms_operation, compliance_management_partner, conditional_access_policy, conditional_access_root, conditional_access_template, connected_organization, contact, contact_folder, content_sharing_session, content_type, contract, conversation, conversation_member, conversation_thread, country_named_location, cross_tenant_access_policy, cross_tenant_access_policy_configuration_default, custom_security_attribute_definition, data_policy_operation, default_managed_app_protection, delegated_admin_access_assignment, delegated_admin_customer, delegated_admin_relationship, delegated_admin_relationship_operation, delegated_admin_relationship_request, delegated_admin_service_management_detail, delegated_permission_classification, deleted_team, detected_app, device, device_and_app_management_role_assignment, device_and_app_management_role_definition, device_app_management, device_category, device_compliance_action_item, device_compliance_device_overview, device_compliance_device_status, device_compliance_policy, device_compliance_policy_assignment, device_compliance_policy_device_state_summary, device_compliance_policy_setting_state_summary, device_compliance_policy_state, device_compliance_scheduled_action_for_rule, device_compliance_setting_state, device_compliance_user_overview, device_compliance_user_status, device_configuration, device_configuration_assignment, device_configuration_device_overview, device_configuration_device_state_summary, device_configuration_device_status, device_configuration_state, device_configuration_user_overview, device_configuration_user_status, device_enrollment_configuration, device_enrollment_limit_configuration, device_enrollment_platform_restrictions_configuration, device_enrollment_windows_hello_for_business_configuration, device_install_state, device_management, device_management_exchange_connector, device_management_export_job, device_management_partner, device_management_reports, device_management_troubleshooting_event, directory, directory_audit, directory_definition, directory_object, directory_object_partner_reference, directory_role, directory_role_template, document_set_version, domain, domain_dns_cname_record, domain_dns_mx_record, domain_dns_record, domain_dns_srv_record, domain_dns_txt_record, domain_dns_unavailable_record, drive, drive_item, drive_item_version, edge, edition_upgrade_configuration, education_assignment, education_assignment_defaults, education_assignment_resource, education_assignment_settings, education_category, education_class, education_feedback_outcome, education_feedback_resource_outcome, education_organization, education_outcome, education_points_outcome, education_rubric, education_rubric_outcome, education_school, education_submission, education_submission_resource, education_user, email_authentication_method, email_authentication_method_configuration, email_file_assessment_request, endpoint, enrollment_configuration_assignment, enrollment_troubleshooting_event, enterprise_code_signing_certificate, entitlement_management, entitlement_management_settings, event, event_message, event_message_request, event_message_response, extension, extension_property, external_domain_name, e_book_install_summary, feature_rollout_policy, federated_identity_credential, fido2_authentication_method, fido2_authentication_method_configuration, fido2_combination_configuration, field_value_set, file_assessment_request, file_attachment, filter_operator_schema, group, group_lifecycle_policy, group_setting, group_setting_template, home_realm_discovery_policy, identity_api_connector, identity_built_in_user_flow_attribute, identity_container, identity_custom_user_flow_attribute, identity_provider, identity_provider_base, identity_security_defaults_enforcement_policy, identity_user_flow, identity_user_flow_attribute, identity_user_flow_attribute_assignment, imported_windows_autopilot_device_identity, imported_windows_autopilot_device_identity_upload, inference_classification, inference_classification_override, internal_domain_federation, internet_explorer_mode, invitation, invite_participants_operation, iosi_pad_o_s_web_clip, ios_certificate_profile, ios_compliance_policy, ios_custom_configuration, ios_device_features_configuration, ios_general_device_configuration, ios_lob_app, ios_lob_app_provisioning_configuration_assignment, ios_managed_app_protection, ios_managed_app_registration, ios_mobile_app_configuration, ios_store_app, ios_update_configuration, ios_update_device_status, ios_vpp_app, ios_vpp_e_book, ios_vpp_e_book_assignment, ip_named_location, item_activity, item_activity_stat, item_analytics, item_attachment, learning_content, learning_provider, license_details, linked_resource, list, list_item, list_item_version, localized_notification_message, long_running_operation, mac_o_s_compliance_policy, mac_o_s_custom_configuration, mac_o_s_device_features_configuration, mac_o_s_general_device_configuration, mac_o_s_lob_app, mac_o_s_microsoft_edge_app, mac_o_s_office_suite_app, mail_assessment_request, mail_folder, mail_search_folder, managed_android_lob_app, managed_android_store_app, managed_app, managed_app_configuration, managed_app_operation, managed_app_policy, managed_app_policy_deployment_summary, managed_app_protection, managed_app_registration, managed_app_status, managed_app_status_raw, managed_device, managed_device_mobile_app_configuration, managed_device_mobile_app_configuration_assignment, managed_device_mobile_app_configuration_device_status, managed_device_mobile_app_configuration_device_summary, managed_device_mobile_app_configuration_user_status, managed_device_mobile_app_configuration_user_summary, managed_device_overview, managed_e_book, managed_e_book_assignment, managed_i_o_s_lob_app, managed_i_o_s_store_app, managed_mobile_app, managed_mobile_lob_app, mdm_windows_information_protection_policy, meeting_attendance_report, message, message_rule, microsoft_account_user_conversation_member, microsoft_authenticator_authentication_method, microsoft_authenticator_authentication_method_configuration, microsoft_authenticator_authentication_method_target, microsoft_store_for_business_app, mobile_app, mobile_app_assignment, mobile_app_category, mobile_app_content, mobile_app_content_file, mobile_contained_app, mobile_lob_app, mobile_threat_defense_connector, multi_value_legacy_extended_property, mute_participant_operation, named_location, notebook, notification_message_template, offer_shift_request, office_graph_insights, onenote, onenote_entity_base_model, onenote_entity_hierarchy_model, onenote_entity_schema_object_model, onenote_operation, onenote_page, onenote_resource, onenote_section, online_meeting, on_premises_conditional_access_settings, on_premises_directory_synchronization, open_shift, open_shift_change_request, open_type_extension, operation, organization, organizational_branding, organizational_branding_localization, organizational_branding_properties, org_contact, outlook_category, outlook_item, outlook_user, o_auth2_permission_grant, participant, participant_joining_notification, participant_left_notification, password_authentication_method, permission, permission_grant_condition_set, permission_grant_policy, person, phone_authentication_method, pinned_chat_message_info, place, planner, planner_assigned_to_task_board_task_format, planner_bucket, planner_bucket_task_board_task_format, planner_group, planner_plan, planner_plan_details, planner_progress_task_board_task_format, planner_task, planner_task_details, planner_user, play_prompt_operation, policy_base, policy_root, post, presence, printer, printer_base, printer_create_operation, printer_share, print_connector, print_document, print_job, print_operation, print_service, print_service_endpoint, print_task, print_task_definition, print_task_trigger, print_usage, print_usage_by_printer, print_usage_by_user, profile_photo, provisioning_object_summary, rbac_application, record_operation, reference_attachment, remote_assistance_partner, request, resource_operation, resource_specific_permission_grant, rich_long_running_operation, risky_service_principal, risky_service_principal_history_item, risky_user, risky_user_history_item, risk_detection, role_assignment, role_definition, room, room_list, saml_or_ws_fed_external_domain_federation, saml_or_ws_fed_provider, schedule, schedule_change_request, scheduling_group, schema_extension, scoped_role_membership, search_entity, section_group, secure_score, secure_score_control_profile, security_reports_root, service_announcement, service_announcement_attachment, service_announcement_base, service_health, service_health_issue, service_principal, service_principal_risk_detection, service_update_message, setting_state_device_summary, shared_drive_item, shared_insight, shared_p_c_configuration, shared_with_channel_team_info, sharepoint, sharepoint_settings, shift, shift_preferences, sign_in, simulation, simulation_automation, simulation_automation_run, single_value_legacy_extended_property, site, skype_for_business_user_conversation_member, skype_user_conversation_member, sms_authentication_method_configuration, sms_authentication_method_target, social_identity_provider, software_oath_authentication_method, software_oath_authentication_method_configuration, software_update_status_summary, start_hold_music_operation, stop_hold_music_operation, sts_policy, subject_rights_request, subscribed_sku, subscribe_to_tone_operation, subscription, swap_shifts_change_request, synchronization, synchronization_job, synchronization_schema, synchronization_template, targeted_managed_app_configuration, targeted_managed_app_policy_assignment, targeted_managed_app_protection, task_file_attachment, team, teams_app, teams_app_definition, teams_app_installation, teams_async_operation, teams_tab, teams_template, teamwork, teamwork_bot, teamwork_hosted_content, teamwork_tag, teamwork_tag_member, team_info, telecom_expense_management_partner, temporary_access_pass_authentication_method, temporary_access_pass_authentication_method_configuration, tenant_app_management_policy, terms_and_conditions, terms_and_conditions_acceptance_status, terms_and_conditions_assignment, terms_of_use_container, threat_assessment_request, threat_assessment_result, thumbnail_set, time_off, time_off_reason, time_off_request, todo, todo_task, todo_task_list, token_issuance_policy, token_lifetime_policy, trending, unified_rbac_resource_action, unified_rbac_resource_namespace, unified_role_assignment, unified_role_assignment_schedule, unified_role_assignment_schedule_instance, unified_role_assignment_schedule_request, unified_role_definition, unified_role_eligibility_schedule, unified_role_eligibility_schedule_instance, unified_role_eligibility_schedule_request, unified_role_management_policy, unified_role_management_policy_approval_rule, unified_role_management_policy_assignment, unified_role_management_policy_authentication_context_rule, unified_role_management_policy_enablement_rule, unified_role_management_policy_expiration_rule, unified_role_management_policy_notification_rule, unified_role_management_policy_rule, unified_role_schedule_base, unified_role_schedule_instance_base, unmute_participant_operation, update_recording_status_operation, url_assessment_request, used_insight, user, user_activity, user_consent_request, user_experience_analytics_device_performance, user_flow_language_configuration, user_flow_language_page, user_install_state_summary, user_scope_teams_app_installation, user_settings, user_teamwork, voice_authentication_method_configuration, vpp_token, web_app, win32_lob_app, windows10_compliance_policy, windows10_custom_configuration, windows10_endpoint_protection_configuration, windows10_enterprise_modern_app_management_configuration, windows10_general_configuration, windows10_mobile_compliance_policy, windows10_secure_assessment_configuration, windows10_team_general_configuration, windows81_compliance_policy, windows81_general_configuration, windows_app_x, windows_autopilot_device_identity, windows_defender_advanced_threat_protection_configuration, windows_hello_for_business_authentication_method, windows_information_protection, windows_information_protection_app_learning_summary, windows_information_protection_app_locker_file, windows_information_protection_network_learning_summary, windows_information_protection_policy, windows_microsoft_edge_app, windows_mobile_m_s_i, windows_phone81_compliance_policy, windows_phone81_custom_configuration, windows_phone81_general_configuration, windows_universal_app_x, windows_universal_app_x_contained_app, windows_update_for_business_configuration, windows_web_app, workbook, workbook_application, workbook_chart, workbook_chart_area_format, workbook_chart_axes, workbook_chart_axis, workbook_chart_axis_format, workbook_chart_axis_title, workbook_chart_axis_title_format, workbook_chart_data_labels, workbook_chart_data_label_format, workbook_chart_fill, workbook_chart_font, workbook_chart_gridlines, workbook_chart_gridlines_format, workbook_chart_legend, workbook_chart_legend_format, workbook_chart_line_format, workbook_chart_point, workbook_chart_point_format, workbook_chart_series, workbook_chart_series_format, workbook_chart_title, workbook_chart_title_format, workbook_comment, workbook_comment_reply, workbook_filter, workbook_format_protection, workbook_functions, workbook_function_result, workbook_named_item, workbook_operation, workbook_pivot_table, workbook_range, workbook_range_border, workbook_range_fill, workbook_range_font, workbook_range_format, workbook_range_sort, workbook_range_view, workbook_table, workbook_table_column, workbook_table_row, workbook_table_sort, workbook_worksheet, workbook_worksheet_protection, workforce_integration, x509_certificate_authentication_method_configuration
    from .call_records import call_record, segment, session
    from .external_connectors import connection_operation, external_activity, external_activity_result, external_connection, external_group, external_item, identity, schema
    from .security import alert, case, cases_root, case_operation, data_set, data_source, data_source_container, ediscovery_add_to_review_set_operation, ediscovery_case, ediscovery_case_settings, ediscovery_custodian, ediscovery_estimate_operation, ediscovery_hold_operation, ediscovery_index_operation, ediscovery_noncustodial_data_source, ediscovery_purge_data_operation, ediscovery_review_set, ediscovery_review_set_query, ediscovery_review_tag, ediscovery_search, ediscovery_tag_operation, incident, retention_event, retention_event_type, search, security, site_source, tag, triggers_root, trigger_types_root, unified_group_source, user_source
    from .term_store import group, relation, set, store, term

@dataclass
class Entity(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The unique idenfier for an entity. Read-only.
    id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Entity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Entity
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.aadUserConversationMember".casefold():
            from . import aad_user_conversation_member

            return aad_user_conversation_member.AadUserConversationMember()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessPackage".casefold():
            from . import access_package

            return access_package.AccessPackage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessPackageAssignment".casefold():
            from . import access_package_assignment

            return access_package_assignment.AccessPackageAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessPackageAssignmentPolicy".casefold():
            from . import access_package_assignment_policy

            return access_package_assignment_policy.AccessPackageAssignmentPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessPackageAssignmentRequest".casefold():
            from . import access_package_assignment_request

            return access_package_assignment_request.AccessPackageAssignmentRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessPackageCatalog".casefold():
            from . import access_package_catalog

            return access_package_catalog.AccessPackageCatalog()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessPackageMultipleChoiceQuestion".casefold():
            from . import access_package_multiple_choice_question

            return access_package_multiple_choice_question.AccessPackageMultipleChoiceQuestion()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessPackageQuestion".casefold():
            from . import access_package_question

            return access_package_question.AccessPackageQuestion()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessPackageSubject".casefold():
            from . import access_package_subject

            return access_package_subject.AccessPackageSubject()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessPackageTextInputQuestion".casefold():
            from . import access_package_text_input_question

            return access_package_text_input_question.AccessPackageTextInputQuestion()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessReviewHistoryDefinition".casefold():
            from . import access_review_history_definition

            return access_review_history_definition.AccessReviewHistoryDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessReviewHistoryInstance".casefold():
            from . import access_review_history_instance

            return access_review_history_instance.AccessReviewHistoryInstance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessReviewInstance".casefold():
            from . import access_review_instance

            return access_review_instance.AccessReviewInstance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessReviewInstanceDecisionItem".casefold():
            from . import access_review_instance_decision_item

            return access_review_instance_decision_item.AccessReviewInstanceDecisionItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessReviewReviewer".casefold():
            from . import access_review_reviewer

            return access_review_reviewer.AccessReviewReviewer()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessReviewScheduleDefinition".casefold():
            from . import access_review_schedule_definition

            return access_review_schedule_definition.AccessReviewScheduleDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessReviewSet".casefold():
            from . import access_review_set

            return access_review_set.AccessReviewSet()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessReviewStage".casefold():
            from . import access_review_stage

            return access_review_stage.AccessReviewStage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.activityBasedTimeoutPolicy".casefold():
            from . import activity_based_timeout_policy

            return activity_based_timeout_policy.ActivityBasedTimeoutPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.activityHistoryItem".casefold():
            from . import activity_history_item

            return activity_history_item.ActivityHistoryItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.addLargeGalleryViewOperation".casefold():
            from . import add_large_gallery_view_operation

            return add_large_gallery_view_operation.AddLargeGalleryViewOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.adminConsentRequestPolicy".casefold():
            from . import admin_consent_request_policy

            return admin_consent_request_policy.AdminConsentRequestPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.administrativeUnit".casefold():
            from . import administrative_unit

            return administrative_unit.AdministrativeUnit()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.agreement".casefold():
            from . import agreement

            return agreement.Agreement()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.agreementAcceptance".casefold():
            from . import agreement_acceptance

            return agreement_acceptance.AgreementAcceptance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.agreementFile".casefold():
            from . import agreement_file

            return agreement_file.AgreementFile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.agreementFileLocalization".casefold():
            from . import agreement_file_localization

            return agreement_file_localization.AgreementFileLocalization()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.agreementFileProperties".casefold():
            from . import agreement_file_properties

            return agreement_file_properties.AgreementFileProperties()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.agreementFileVersion".casefold():
            from . import agreement_file_version

            return agreement_file_version.AgreementFileVersion()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.alert".casefold():
            from . import alert
            from .security import alert

            return alert.Alert()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.allowedValue".casefold():
            from . import allowed_value

            return allowed_value.AllowedValue()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidCompliancePolicy".casefold():
            from . import android_compliance_policy

            return android_compliance_policy.AndroidCompliancePolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidCustomConfiguration".casefold():
            from . import android_custom_configuration

            return android_custom_configuration.AndroidCustomConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidGeneralDeviceConfiguration".casefold():
            from . import android_general_device_configuration

            return android_general_device_configuration.AndroidGeneralDeviceConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidLobApp".casefold():
            from . import android_lob_app

            return android_lob_app.AndroidLobApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidManagedAppProtection".casefold():
            from . import android_managed_app_protection

            return android_managed_app_protection.AndroidManagedAppProtection()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidManagedAppRegistration".casefold():
            from . import android_managed_app_registration

            return android_managed_app_registration.AndroidManagedAppRegistration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidStoreApp".casefold():
            from . import android_store_app

            return android_store_app.AndroidStoreApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidWorkProfileCompliancePolicy".casefold():
            from . import android_work_profile_compliance_policy

            return android_work_profile_compliance_policy.AndroidWorkProfileCompliancePolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidWorkProfileCustomConfiguration".casefold():
            from . import android_work_profile_custom_configuration

            return android_work_profile_custom_configuration.AndroidWorkProfileCustomConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidWorkProfileGeneralDeviceConfiguration".casefold():
            from . import android_work_profile_general_device_configuration

            return android_work_profile_general_device_configuration.AndroidWorkProfileGeneralDeviceConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.anonymousGuestConversationMember".casefold():
            from . import anonymous_guest_conversation_member

            return anonymous_guest_conversation_member.AnonymousGuestConversationMember()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.appCatalogs".casefold():
            from . import app_catalogs

            return app_catalogs.AppCatalogs()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.appConsentApprovalRoute".casefold():
            from . import app_consent_approval_route

            return app_consent_approval_route.AppConsentApprovalRoute()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.appConsentRequest".casefold():
            from . import app_consent_request

            return app_consent_request.AppConsentRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.appleDeviceFeaturesConfigurationBase".casefold():
            from . import apple_device_features_configuration_base

            return apple_device_features_configuration_base.AppleDeviceFeaturesConfigurationBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.appleManagedIdentityProvider".casefold():
            from . import apple_managed_identity_provider

            return apple_managed_identity_provider.AppleManagedIdentityProvider()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.applePushNotificationCertificate".casefold():
            from . import apple_push_notification_certificate

            return apple_push_notification_certificate.ApplePushNotificationCertificate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.application".casefold():
            from . import application

            return application.Application()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.applicationTemplate".casefold():
            from . import application_template

            return application_template.ApplicationTemplate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.appManagementPolicy".casefold():
            from . import app_management_policy

            return app_management_policy.AppManagementPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.appRoleAssignment".casefold():
            from . import app_role_assignment

            return app_role_assignment.AppRoleAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.approval".casefold():
            from . import approval

            return approval.Approval()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.approvalStage".casefold():
            from . import approval_stage

            return approval_stage.ApprovalStage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.appScope".casefold():
            from . import app_scope

            return app_scope.AppScope()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.associatedTeamInfo".casefold():
            from . import associated_team_info

            return associated_team_info.AssociatedTeamInfo()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.attachment".casefold():
            from . import attachment

            return attachment.Attachment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.attachmentBase".casefold():
            from . import attachment_base

            return attachment_base.AttachmentBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.attachmentSession".casefold():
            from . import attachment_session

            return attachment_session.AttachmentSession()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.attackSimulationRoot".casefold():
            from . import attack_simulation_root

            return attack_simulation_root.AttackSimulationRoot()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.attendanceRecord".casefold():
            from . import attendance_record

            return attendance_record.AttendanceRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.attributeMappingFunctionSchema".casefold():
            from . import attribute_mapping_function_schema

            return attribute_mapping_function_schema.AttributeMappingFunctionSchema()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.attributeSet".casefold():
            from . import attribute_set

            return attribute_set.AttributeSet()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.audioRoutingGroup".casefold():
            from . import audio_routing_group

            return audio_routing_group.AudioRoutingGroup()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.auditEvent".casefold():
            from . import audit_event

            return audit_event.AuditEvent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.auditLogRoot".casefold():
            from . import audit_log_root

            return audit_log_root.AuditLogRoot()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.authentication".casefold():
            from . import authentication

            return authentication.Authentication()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.authenticationCombinationConfiguration".casefold():
            from . import authentication_combination_configuration

            return authentication_combination_configuration.AuthenticationCombinationConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.authenticationContextClassReference".casefold():
            from . import authentication_context_class_reference

            return authentication_context_class_reference.AuthenticationContextClassReference()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.authenticationFlowsPolicy".casefold():
            from . import authentication_flows_policy

            return authentication_flows_policy.AuthenticationFlowsPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.authenticationMethod".casefold():
            from . import authentication_method

            return authentication_method.AuthenticationMethod()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.authenticationMethodConfiguration".casefold():
            from . import authentication_method_configuration

            return authentication_method_configuration.AuthenticationMethodConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.authenticationMethodModeDetail".casefold():
            from . import authentication_method_mode_detail

            return authentication_method_mode_detail.AuthenticationMethodModeDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.authenticationMethodsPolicy".casefold():
            from . import authentication_methods_policy

            return authentication_methods_policy.AuthenticationMethodsPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.authenticationMethodTarget".casefold():
            from . import authentication_method_target

            return authentication_method_target.AuthenticationMethodTarget()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.authenticationStrengthPolicy".casefold():
            from . import authentication_strength_policy

            return authentication_strength_policy.AuthenticationStrengthPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.authenticationStrengthRoot".casefold():
            from . import authentication_strength_root

            return authentication_strength_root.AuthenticationStrengthRoot()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.authoredNote".casefold():
            from . import authored_note

            return authored_note.AuthoredNote()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.authorizationPolicy".casefold():
            from . import authorization_policy

            return authorization_policy.AuthorizationPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.azureCommunicationServicesUserConversationMember".casefold():
            from . import azure_communication_services_user_conversation_member

            return azure_communication_services_user_conversation_member.AzureCommunicationServicesUserConversationMember()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.b2xIdentityUserFlow".casefold():
            from . import b2x_identity_user_flow

            return b2x_identity_user_flow.B2xIdentityUserFlow()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.baseItem".casefold():
            from . import base_item

            return base_item.BaseItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.baseItemVersion".casefold():
            from . import base_item_version

            return base_item_version.BaseItemVersion()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.bitlocker".casefold():
            from . import bitlocker

            return bitlocker.Bitlocker()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.bitlockerRecoveryKey".casefold():
            from . import bitlocker_recovery_key

            return bitlocker_recovery_key.BitlockerRecoveryKey()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.bookingAppointment".casefold():
            from . import booking_appointment

            return booking_appointment.BookingAppointment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.bookingBusiness".casefold():
            from . import booking_business

            return booking_business.BookingBusiness()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.bookingCurrency".casefold():
            from . import booking_currency

            return booking_currency.BookingCurrency()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.bookingCustomer".casefold():
            from . import booking_customer

            return booking_customer.BookingCustomer()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.bookingCustomerBase".casefold():
            from . import booking_customer_base

            return booking_customer_base.BookingCustomerBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.bookingCustomQuestion".casefold():
            from . import booking_custom_question

            return booking_custom_question.BookingCustomQuestion()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.bookingService".casefold():
            from . import booking_service

            return booking_service.BookingService()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.bookingStaffMember".casefold():
            from . import booking_staff_member

            return booking_staff_member.BookingStaffMember()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.bookingStaffMemberBase".casefold():
            from . import booking_staff_member_base

            return booking_staff_member_base.BookingStaffMemberBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.browserSharedCookie".casefold():
            from . import browser_shared_cookie

            return browser_shared_cookie.BrowserSharedCookie()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.browserSite".casefold():
            from . import browser_site

            return browser_site.BrowserSite()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.browserSiteList".casefold():
            from . import browser_site_list

            return browser_site_list.BrowserSiteList()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.builtInIdentityProvider".casefold():
            from . import built_in_identity_provider

            return built_in_identity_provider.BuiltInIdentityProvider()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.calendar".casefold():
            from . import calendar

            return calendar.Calendar()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.calendarGroup".casefold():
            from . import calendar_group

            return calendar_group.CalendarGroup()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.calendarPermission".casefold():
            from . import calendar_permission

            return calendar_permission.CalendarPermission()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.calendarSharingMessage".casefold():
            from . import calendar_sharing_message

            return calendar_sharing_message.CalendarSharingMessage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.call".casefold():
            from . import call

            return call.Call()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.callRecords.callRecord".casefold():
            from .call_records import call_record

            return call_record.CallRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.callRecords.segment".casefold():
            from .call_records import segment

            return segment.Segment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.callRecords.session".casefold():
            from .call_records import session

            return session.Session()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cancelMediaProcessingOperation".casefold():
            from . import cancel_media_processing_operation

            return cancel_media_processing_operation.CancelMediaProcessingOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.certificateBasedAuthConfiguration".casefold():
            from . import certificate_based_auth_configuration

            return certificate_based_auth_configuration.CertificateBasedAuthConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.changeTrackedEntity".casefold():
            from . import change_tracked_entity

            return change_tracked_entity.ChangeTrackedEntity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.channel".casefold():
            from . import channel

            return channel.Channel()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.chat".casefold():
            from . import chat

            return chat.Chat()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.chatMessage".casefold():
            from . import chat_message

            return chat_message.ChatMessage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.chatMessageHostedContent".casefold():
            from . import chat_message_hosted_content

            return chat_message_hosted_content.ChatMessageHostedContent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.chatMessageInfo".casefold():
            from . import chat_message_info

            return chat_message_info.ChatMessageInfo()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.checklistItem".casefold():
            from . import checklist_item

            return checklist_item.ChecklistItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.claimsMappingPolicy".casefold():
            from . import claims_mapping_policy

            return claims_mapping_policy.ClaimsMappingPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.columnDefinition".casefold():
            from . import column_definition

            return column_definition.ColumnDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.columnLink".casefold():
            from . import column_link

            return column_link.ColumnLink()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.commsOperation".casefold():
            from . import comms_operation

            return comms_operation.CommsOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.complianceManagementPartner".casefold():
            from . import compliance_management_partner

            return compliance_management_partner.ComplianceManagementPartner()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.conditionalAccessPolicy".casefold():
            from . import conditional_access_policy

            return conditional_access_policy.ConditionalAccessPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.conditionalAccessRoot".casefold():
            from . import conditional_access_root

            return conditional_access_root.ConditionalAccessRoot()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.conditionalAccessTemplate".casefold():
            from . import conditional_access_template

            return conditional_access_template.ConditionalAccessTemplate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.connectedOrganization".casefold():
            from . import connected_organization

            return connected_organization.ConnectedOrganization()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.contact".casefold():
            from . import contact

            return contact.Contact()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.contactFolder".casefold():
            from . import contact_folder

            return contact_folder.ContactFolder()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.contentSharingSession".casefold():
            from . import content_sharing_session

            return content_sharing_session.ContentSharingSession()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.contentType".casefold():
            from . import content_type

            return content_type.ContentType()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.contract".casefold():
            from . import contract

            return contract.Contract()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.conversation".casefold():
            from . import conversation

            return conversation.Conversation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.conversationMember".casefold():
            from . import conversation_member

            return conversation_member.ConversationMember()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.conversationThread".casefold():
            from . import conversation_thread

            return conversation_thread.ConversationThread()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.countryNamedLocation".casefold():
            from . import country_named_location

            return country_named_location.CountryNamedLocation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.crossTenantAccessPolicy".casefold():
            from . import cross_tenant_access_policy

            return cross_tenant_access_policy.CrossTenantAccessPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.crossTenantAccessPolicyConfigurationDefault".casefold():
            from . import cross_tenant_access_policy_configuration_default

            return cross_tenant_access_policy_configuration_default.CrossTenantAccessPolicyConfigurationDefault()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.customSecurityAttributeDefinition".casefold():
            from . import custom_security_attribute_definition

            return custom_security_attribute_definition.CustomSecurityAttributeDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.dataPolicyOperation".casefold():
            from . import data_policy_operation

            return data_policy_operation.DataPolicyOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.defaultManagedAppProtection".casefold():
            from . import default_managed_app_protection

            return default_managed_app_protection.DefaultManagedAppProtection()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.delegatedAdminAccessAssignment".casefold():
            from . import delegated_admin_access_assignment

            return delegated_admin_access_assignment.DelegatedAdminAccessAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.delegatedAdminCustomer".casefold():
            from . import delegated_admin_customer

            return delegated_admin_customer.DelegatedAdminCustomer()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.delegatedAdminRelationship".casefold():
            from . import delegated_admin_relationship

            return delegated_admin_relationship.DelegatedAdminRelationship()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.delegatedAdminRelationshipOperation".casefold():
            from . import delegated_admin_relationship_operation

            return delegated_admin_relationship_operation.DelegatedAdminRelationshipOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.delegatedAdminRelationshipRequest".casefold():
            from . import delegated_admin_relationship_request

            return delegated_admin_relationship_request.DelegatedAdminRelationshipRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.delegatedAdminServiceManagementDetail".casefold():
            from . import delegated_admin_service_management_detail

            return delegated_admin_service_management_detail.DelegatedAdminServiceManagementDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.delegatedPermissionClassification".casefold():
            from . import delegated_permission_classification

            return delegated_permission_classification.DelegatedPermissionClassification()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deletedTeam".casefold():
            from . import deleted_team

            return deleted_team.DeletedTeam()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.detectedApp".casefold():
            from . import detected_app

            return detected_app.DetectedApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.device".casefold():
            from . import device

            return device.Device()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceAndAppManagementRoleAssignment".casefold():
            from . import device_and_app_management_role_assignment

            return device_and_app_management_role_assignment.DeviceAndAppManagementRoleAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceAndAppManagementRoleDefinition".casefold():
            from . import device_and_app_management_role_definition

            return device_and_app_management_role_definition.DeviceAndAppManagementRoleDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceAppManagement".casefold():
            from . import device_app_management

            return device_app_management.DeviceAppManagement()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceCategory".casefold():
            from . import device_category

            return device_category.DeviceCategory()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceComplianceActionItem".casefold():
            from . import device_compliance_action_item

            return device_compliance_action_item.DeviceComplianceActionItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceComplianceDeviceOverview".casefold():
            from . import device_compliance_device_overview

            return device_compliance_device_overview.DeviceComplianceDeviceOverview()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceComplianceDeviceStatus".casefold():
            from . import device_compliance_device_status

            return device_compliance_device_status.DeviceComplianceDeviceStatus()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceCompliancePolicy".casefold():
            from . import device_compliance_policy

            return device_compliance_policy.DeviceCompliancePolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceCompliancePolicyAssignment".casefold():
            from . import device_compliance_policy_assignment

            return device_compliance_policy_assignment.DeviceCompliancePolicyAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceCompliancePolicyDeviceStateSummary".casefold():
            from . import device_compliance_policy_device_state_summary

            return device_compliance_policy_device_state_summary.DeviceCompliancePolicyDeviceStateSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceCompliancePolicySettingStateSummary".casefold():
            from . import device_compliance_policy_setting_state_summary

            return device_compliance_policy_setting_state_summary.DeviceCompliancePolicySettingStateSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceCompliancePolicyState".casefold():
            from . import device_compliance_policy_state

            return device_compliance_policy_state.DeviceCompliancePolicyState()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceComplianceScheduledActionForRule".casefold():
            from . import device_compliance_scheduled_action_for_rule

            return device_compliance_scheduled_action_for_rule.DeviceComplianceScheduledActionForRule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceComplianceSettingState".casefold():
            from . import device_compliance_setting_state

            return device_compliance_setting_state.DeviceComplianceSettingState()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceComplianceUserOverview".casefold():
            from . import device_compliance_user_overview

            return device_compliance_user_overview.DeviceComplianceUserOverview()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceComplianceUserStatus".casefold():
            from . import device_compliance_user_status

            return device_compliance_user_status.DeviceComplianceUserStatus()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceConfiguration".casefold():
            from . import device_configuration

            return device_configuration.DeviceConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceConfigurationAssignment".casefold():
            from . import device_configuration_assignment

            return device_configuration_assignment.DeviceConfigurationAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceConfigurationDeviceOverview".casefold():
            from . import device_configuration_device_overview

            return device_configuration_device_overview.DeviceConfigurationDeviceOverview()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceConfigurationDeviceStateSummary".casefold():
            from . import device_configuration_device_state_summary

            return device_configuration_device_state_summary.DeviceConfigurationDeviceStateSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceConfigurationDeviceStatus".casefold():
            from . import device_configuration_device_status

            return device_configuration_device_status.DeviceConfigurationDeviceStatus()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceConfigurationState".casefold():
            from . import device_configuration_state

            return device_configuration_state.DeviceConfigurationState()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceConfigurationUserOverview".casefold():
            from . import device_configuration_user_overview

            return device_configuration_user_overview.DeviceConfigurationUserOverview()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceConfigurationUserStatus".casefold():
            from . import device_configuration_user_status

            return device_configuration_user_status.DeviceConfigurationUserStatus()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceEnrollmentConfiguration".casefold():
            from . import device_enrollment_configuration

            return device_enrollment_configuration.DeviceEnrollmentConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceEnrollmentLimitConfiguration".casefold():
            from . import device_enrollment_limit_configuration

            return device_enrollment_limit_configuration.DeviceEnrollmentLimitConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceEnrollmentPlatformRestrictionsConfiguration".casefold():
            from . import device_enrollment_platform_restrictions_configuration

            return device_enrollment_platform_restrictions_configuration.DeviceEnrollmentPlatformRestrictionsConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceEnrollmentWindowsHelloForBusinessConfiguration".casefold():
            from . import device_enrollment_windows_hello_for_business_configuration

            return device_enrollment_windows_hello_for_business_configuration.DeviceEnrollmentWindowsHelloForBusinessConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceInstallState".casefold():
            from . import device_install_state

            return device_install_state.DeviceInstallState()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagement".casefold():
            from . import device_management

            return device_management.DeviceManagement()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementExchangeConnector".casefold():
            from . import device_management_exchange_connector

            return device_management_exchange_connector.DeviceManagementExchangeConnector()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementExportJob".casefold():
            from . import device_management_export_job

            return device_management_export_job.DeviceManagementExportJob()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementPartner".casefold():
            from . import device_management_partner

            return device_management_partner.DeviceManagementPartner()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementReports".casefold():
            from . import device_management_reports

            return device_management_reports.DeviceManagementReports()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementTroubleshootingEvent".casefold():
            from . import device_management_troubleshooting_event

            return device_management_troubleshooting_event.DeviceManagementTroubleshootingEvent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.directory".casefold():
            from . import directory

            return directory.Directory()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.directoryAudit".casefold():
            from . import directory_audit

            return directory_audit.DirectoryAudit()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.directoryDefinition".casefold():
            from . import directory_definition

            return directory_definition.DirectoryDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.directoryObject".casefold():
            from . import directory_object

            return directory_object.DirectoryObject()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.directoryObjectPartnerReference".casefold():
            from . import directory_object_partner_reference

            return directory_object_partner_reference.DirectoryObjectPartnerReference()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.directoryRole".casefold():
            from . import directory_role

            return directory_role.DirectoryRole()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.directoryRoleTemplate".casefold():
            from . import directory_role_template

            return directory_role_template.DirectoryRoleTemplate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.documentSetVersion".casefold():
            from . import document_set_version

            return document_set_version.DocumentSetVersion()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.domain".casefold():
            from . import domain

            return domain.Domain()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.domainDnsCnameRecord".casefold():
            from . import domain_dns_cname_record

            return domain_dns_cname_record.DomainDnsCnameRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.domainDnsMxRecord".casefold():
            from . import domain_dns_mx_record

            return domain_dns_mx_record.DomainDnsMxRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.domainDnsRecord".casefold():
            from . import domain_dns_record

            return domain_dns_record.DomainDnsRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.domainDnsSrvRecord".casefold():
            from . import domain_dns_srv_record

            return domain_dns_srv_record.DomainDnsSrvRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.domainDnsTxtRecord".casefold():
            from . import domain_dns_txt_record

            return domain_dns_txt_record.DomainDnsTxtRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.domainDnsUnavailableRecord".casefold():
            from . import domain_dns_unavailable_record

            return domain_dns_unavailable_record.DomainDnsUnavailableRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.drive".casefold():
            from . import drive

            return drive.Drive()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.driveItem".casefold():
            from . import drive_item

            return drive_item.DriveItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.driveItemVersion".casefold():
            from . import drive_item_version

            return drive_item_version.DriveItemVersion()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.eBookInstallSummary".casefold():
            from . import e_book_install_summary

            return e_book_install_summary.EBookInstallSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.edge".casefold():
            from . import edge

            return edge.Edge()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.editionUpgradeConfiguration".casefold():
            from . import edition_upgrade_configuration

            return edition_upgrade_configuration.EditionUpgradeConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationAssignment".casefold():
            from . import education_assignment

            return education_assignment.EducationAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationAssignmentDefaults".casefold():
            from . import education_assignment_defaults

            return education_assignment_defaults.EducationAssignmentDefaults()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationAssignmentResource".casefold():
            from . import education_assignment_resource

            return education_assignment_resource.EducationAssignmentResource()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationAssignmentSettings".casefold():
            from . import education_assignment_settings

            return education_assignment_settings.EducationAssignmentSettings()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationCategory".casefold():
            from . import education_category

            return education_category.EducationCategory()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationClass".casefold():
            from . import education_class

            return education_class.EducationClass()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationFeedbackOutcome".casefold():
            from . import education_feedback_outcome

            return education_feedback_outcome.EducationFeedbackOutcome()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationFeedbackResourceOutcome".casefold():
            from . import education_feedback_resource_outcome

            return education_feedback_resource_outcome.EducationFeedbackResourceOutcome()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationOrganization".casefold():
            from . import education_organization

            return education_organization.EducationOrganization()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationOutcome".casefold():
            from . import education_outcome

            return education_outcome.EducationOutcome()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationPointsOutcome".casefold():
            from . import education_points_outcome

            return education_points_outcome.EducationPointsOutcome()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationRubric".casefold():
            from . import education_rubric

            return education_rubric.EducationRubric()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationRubricOutcome".casefold():
            from . import education_rubric_outcome

            return education_rubric_outcome.EducationRubricOutcome()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationSchool".casefold():
            from . import education_school

            return education_school.EducationSchool()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationSubmission".casefold():
            from . import education_submission

            return education_submission.EducationSubmission()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationSubmissionResource".casefold():
            from . import education_submission_resource

            return education_submission_resource.EducationSubmissionResource()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationUser".casefold():
            from . import education_user

            return education_user.EducationUser()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.emailAuthenticationMethod".casefold():
            from . import email_authentication_method

            return email_authentication_method.EmailAuthenticationMethod()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.emailAuthenticationMethodConfiguration".casefold():
            from . import email_authentication_method_configuration

            return email_authentication_method_configuration.EmailAuthenticationMethodConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.emailFileAssessmentRequest".casefold():
            from . import email_file_assessment_request

            return email_file_assessment_request.EmailFileAssessmentRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.endpoint".casefold():
            from . import endpoint

            return endpoint.Endpoint()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.enrollmentConfigurationAssignment".casefold():
            from . import enrollment_configuration_assignment

            return enrollment_configuration_assignment.EnrollmentConfigurationAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.enrollmentTroubleshootingEvent".casefold():
            from . import enrollment_troubleshooting_event

            return enrollment_troubleshooting_event.EnrollmentTroubleshootingEvent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.enterpriseCodeSigningCertificate".casefold():
            from . import enterprise_code_signing_certificate

            return enterprise_code_signing_certificate.EnterpriseCodeSigningCertificate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.entitlementManagement".casefold():
            from . import entitlement_management

            return entitlement_management.EntitlementManagement()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.entitlementManagementSettings".casefold():
            from . import entitlement_management_settings

            return entitlement_management_settings.EntitlementManagementSettings()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.event".casefold():
            from . import event

            return event.Event()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.eventMessage".casefold():
            from . import event_message

            return event_message.EventMessage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.eventMessageRequest".casefold():
            from . import event_message_request

            return event_message_request.EventMessageRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.eventMessageResponse".casefold():
            from . import event_message_response

            return event_message_response.EventMessageResponse()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.extension".casefold():
            from . import extension

            return extension.Extension()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.extensionProperty".casefold():
            from . import extension_property

            return extension_property.ExtensionProperty()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.externalConnectors.connectionOperation".casefold():
            from .external_connectors import connection_operation

            return connection_operation.ConnectionOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.externalConnectors.externalActivity".casefold():
            from .external_connectors import external_activity

            return external_activity.ExternalActivity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.externalConnectors.externalActivityResult".casefold():
            from .external_connectors import external_activity_result

            return external_activity_result.ExternalActivityResult()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.externalConnectors.externalConnection".casefold():
            from .external_connectors import external_connection

            return external_connection.ExternalConnection()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.externalConnectors.externalGroup".casefold():
            from .external_connectors import external_group

            return external_group.ExternalGroup()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.externalConnectors.externalItem".casefold():
            from .external_connectors import external_item

            return external_item.ExternalItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.externalConnectors.identity".casefold():
            from .external_connectors import identity

            return identity.Identity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.externalConnectors.schema".casefold():
            from .external_connectors import schema

            return schema.Schema()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.externalDomainName".casefold():
            from . import external_domain_name

            return external_domain_name.ExternalDomainName()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.featureRolloutPolicy".casefold():
            from . import feature_rollout_policy

            return feature_rollout_policy.FeatureRolloutPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.federatedIdentityCredential".casefold():
            from . import federated_identity_credential

            return federated_identity_credential.FederatedIdentityCredential()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.fido2AuthenticationMethod".casefold():
            from . import fido2_authentication_method

            return fido2_authentication_method.Fido2AuthenticationMethod()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.fido2AuthenticationMethodConfiguration".casefold():
            from . import fido2_authentication_method_configuration

            return fido2_authentication_method_configuration.Fido2AuthenticationMethodConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.fido2CombinationConfiguration".casefold():
            from . import fido2_combination_configuration

            return fido2_combination_configuration.Fido2CombinationConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.fieldValueSet".casefold():
            from . import field_value_set

            return field_value_set.FieldValueSet()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.fileAssessmentRequest".casefold():
            from . import file_assessment_request

            return file_assessment_request.FileAssessmentRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.fileAttachment".casefold():
            from . import file_attachment

            return file_attachment.FileAttachment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.filterOperatorSchema".casefold():
            from . import filter_operator_schema

            return filter_operator_schema.FilterOperatorSchema()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.group".casefold():
            from . import group
            from .term_store import group

            return group.Group()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupLifecyclePolicy".casefold():
            from . import group_lifecycle_policy

            return group_lifecycle_policy.GroupLifecyclePolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupSetting".casefold():
            from . import group_setting

            return group_setting.GroupSetting()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupSettingTemplate".casefold():
            from . import group_setting_template

            return group_setting_template.GroupSettingTemplate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.homeRealmDiscoveryPolicy".casefold():
            from . import home_realm_discovery_policy

            return home_realm_discovery_policy.HomeRealmDiscoveryPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identityApiConnector".casefold():
            from . import identity_api_connector

            return identity_api_connector.IdentityApiConnector()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identityBuiltInUserFlowAttribute".casefold():
            from . import identity_built_in_user_flow_attribute

            return identity_built_in_user_flow_attribute.IdentityBuiltInUserFlowAttribute()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identityContainer".casefold():
            from . import identity_container

            return identity_container.IdentityContainer()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identityCustomUserFlowAttribute".casefold():
            from . import identity_custom_user_flow_attribute

            return identity_custom_user_flow_attribute.IdentityCustomUserFlowAttribute()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identityProvider".casefold():
            from . import identity_provider

            return identity_provider.IdentityProvider()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identityProviderBase".casefold():
            from . import identity_provider_base

            return identity_provider_base.IdentityProviderBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identitySecurityDefaultsEnforcementPolicy".casefold():
            from . import identity_security_defaults_enforcement_policy

            return identity_security_defaults_enforcement_policy.IdentitySecurityDefaultsEnforcementPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identityUserFlow".casefold():
            from . import identity_user_flow

            return identity_user_flow.IdentityUserFlow()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identityUserFlowAttribute".casefold():
            from . import identity_user_flow_attribute

            return identity_user_flow_attribute.IdentityUserFlowAttribute()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identityUserFlowAttributeAssignment".casefold():
            from . import identity_user_flow_attribute_assignment

            return identity_user_flow_attribute_assignment.IdentityUserFlowAttributeAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.importedWindowsAutopilotDeviceIdentity".casefold():
            from . import imported_windows_autopilot_device_identity

            return imported_windows_autopilot_device_identity.ImportedWindowsAutopilotDeviceIdentity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.importedWindowsAutopilotDeviceIdentityUpload".casefold():
            from . import imported_windows_autopilot_device_identity_upload

            return imported_windows_autopilot_device_identity_upload.ImportedWindowsAutopilotDeviceIdentityUpload()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.inferenceClassification".casefold():
            from . import inference_classification

            return inference_classification.InferenceClassification()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.inferenceClassificationOverride".casefold():
            from . import inference_classification_override

            return inference_classification_override.InferenceClassificationOverride()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.internalDomainFederation".casefold():
            from . import internal_domain_federation

            return internal_domain_federation.InternalDomainFederation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.internetExplorerMode".casefold():
            from . import internet_explorer_mode

            return internet_explorer_mode.InternetExplorerMode()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.invitation".casefold():
            from . import invitation

            return invitation.Invitation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.inviteParticipantsOperation".casefold():
            from . import invite_participants_operation

            return invite_participants_operation.InviteParticipantsOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosCertificateProfile".casefold():
            from . import ios_certificate_profile

            return ios_certificate_profile.IosCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosCompliancePolicy".casefold():
            from . import ios_compliance_policy

            return ios_compliance_policy.IosCompliancePolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosCustomConfiguration".casefold():
            from . import ios_custom_configuration

            return ios_custom_configuration.IosCustomConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosDeviceFeaturesConfiguration".casefold():
            from . import ios_device_features_configuration

            return ios_device_features_configuration.IosDeviceFeaturesConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosGeneralDeviceConfiguration".casefold():
            from . import ios_general_device_configuration

            return ios_general_device_configuration.IosGeneralDeviceConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosiPadOSWebClip".casefold():
            from . import iosi_pad_o_s_web_clip

            return iosi_pad_o_s_web_clip.IosiPadOSWebClip()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosLobApp".casefold():
            from . import ios_lob_app

            return ios_lob_app.IosLobApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosLobAppProvisioningConfigurationAssignment".casefold():
            from . import ios_lob_app_provisioning_configuration_assignment

            return ios_lob_app_provisioning_configuration_assignment.IosLobAppProvisioningConfigurationAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosManagedAppProtection".casefold():
            from . import ios_managed_app_protection

            return ios_managed_app_protection.IosManagedAppProtection()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosManagedAppRegistration".casefold():
            from . import ios_managed_app_registration

            return ios_managed_app_registration.IosManagedAppRegistration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosMobileAppConfiguration".casefold():
            from . import ios_mobile_app_configuration

            return ios_mobile_app_configuration.IosMobileAppConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosStoreApp".casefold():
            from . import ios_store_app

            return ios_store_app.IosStoreApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosUpdateConfiguration".casefold():
            from . import ios_update_configuration

            return ios_update_configuration.IosUpdateConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosUpdateDeviceStatus".casefold():
            from . import ios_update_device_status

            return ios_update_device_status.IosUpdateDeviceStatus()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosVppApp".casefold():
            from . import ios_vpp_app

            return ios_vpp_app.IosVppApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosVppEBook".casefold():
            from . import ios_vpp_e_book

            return ios_vpp_e_book.IosVppEBook()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosVppEBookAssignment".casefold():
            from . import ios_vpp_e_book_assignment

            return ios_vpp_e_book_assignment.IosVppEBookAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.ipNamedLocation".casefold():
            from . import ip_named_location

            return ip_named_location.IpNamedLocation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.itemActivity".casefold():
            from . import item_activity

            return item_activity.ItemActivity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.itemActivityStat".casefold():
            from . import item_activity_stat

            return item_activity_stat.ItemActivityStat()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.itemAnalytics".casefold():
            from . import item_analytics

            return item_analytics.ItemAnalytics()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.itemAttachment".casefold():
            from . import item_attachment

            return item_attachment.ItemAttachment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.learningContent".casefold():
            from . import learning_content

            return learning_content.LearningContent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.learningProvider".casefold():
            from . import learning_provider

            return learning_provider.LearningProvider()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.licenseDetails".casefold():
            from . import license_details

            return license_details.LicenseDetails()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.linkedResource".casefold():
            from . import linked_resource

            return linked_resource.LinkedResource()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.list".casefold():
            from . import list

            return list.List()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.listItem".casefold():
            from . import list_item

            return list_item.ListItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.listItemVersion".casefold():
            from . import list_item_version

            return list_item_version.ListItemVersion()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.localizedNotificationMessage".casefold():
            from . import localized_notification_message

            return localized_notification_message.LocalizedNotificationMessage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.longRunningOperation".casefold():
            from . import long_running_operation

            return long_running_operation.LongRunningOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSCompliancePolicy".casefold():
            from . import mac_o_s_compliance_policy

            return mac_o_s_compliance_policy.MacOSCompliancePolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSCustomConfiguration".casefold():
            from . import mac_o_s_custom_configuration

            return mac_o_s_custom_configuration.MacOSCustomConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSDeviceFeaturesConfiguration".casefold():
            from . import mac_o_s_device_features_configuration

            return mac_o_s_device_features_configuration.MacOSDeviceFeaturesConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSGeneralDeviceConfiguration".casefold():
            from . import mac_o_s_general_device_configuration

            return mac_o_s_general_device_configuration.MacOSGeneralDeviceConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSLobApp".casefold():
            from . import mac_o_s_lob_app

            return mac_o_s_lob_app.MacOSLobApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSMicrosoftEdgeApp".casefold():
            from . import mac_o_s_microsoft_edge_app

            return mac_o_s_microsoft_edge_app.MacOSMicrosoftEdgeApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSOfficeSuiteApp".casefold():
            from . import mac_o_s_office_suite_app

            return mac_o_s_office_suite_app.MacOSOfficeSuiteApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mailAssessmentRequest".casefold():
            from . import mail_assessment_request

            return mail_assessment_request.MailAssessmentRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mailFolder".casefold():
            from . import mail_folder

            return mail_folder.MailFolder()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mailSearchFolder".casefold():
            from . import mail_search_folder

            return mail_search_folder.MailSearchFolder()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedAndroidLobApp".casefold():
            from . import managed_android_lob_app

            return managed_android_lob_app.ManagedAndroidLobApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedAndroidStoreApp".casefold():
            from . import managed_android_store_app

            return managed_android_store_app.ManagedAndroidStoreApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedApp".casefold():
            from . import managed_app

            return managed_app.ManagedApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedAppConfiguration".casefold():
            from . import managed_app_configuration

            return managed_app_configuration.ManagedAppConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedAppOperation".casefold():
            from . import managed_app_operation

            return managed_app_operation.ManagedAppOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedAppPolicy".casefold():
            from . import managed_app_policy

            return managed_app_policy.ManagedAppPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedAppPolicyDeploymentSummary".casefold():
            from . import managed_app_policy_deployment_summary

            return managed_app_policy_deployment_summary.ManagedAppPolicyDeploymentSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedAppProtection".casefold():
            from . import managed_app_protection

            return managed_app_protection.ManagedAppProtection()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedAppRegistration".casefold():
            from . import managed_app_registration

            return managed_app_registration.ManagedAppRegistration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedAppStatus".casefold():
            from . import managed_app_status

            return managed_app_status.ManagedAppStatus()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedAppStatusRaw".casefold():
            from . import managed_app_status_raw

            return managed_app_status_raw.ManagedAppStatusRaw()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedDevice".casefold():
            from . import managed_device

            return managed_device.ManagedDevice()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedDeviceMobileAppConfiguration".casefold():
            from . import managed_device_mobile_app_configuration

            return managed_device_mobile_app_configuration.ManagedDeviceMobileAppConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedDeviceMobileAppConfigurationAssignment".casefold():
            from . import managed_device_mobile_app_configuration_assignment

            return managed_device_mobile_app_configuration_assignment.ManagedDeviceMobileAppConfigurationAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedDeviceMobileAppConfigurationDeviceStatus".casefold():
            from . import managed_device_mobile_app_configuration_device_status

            return managed_device_mobile_app_configuration_device_status.ManagedDeviceMobileAppConfigurationDeviceStatus()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedDeviceMobileAppConfigurationDeviceSummary".casefold():
            from . import managed_device_mobile_app_configuration_device_summary

            return managed_device_mobile_app_configuration_device_summary.ManagedDeviceMobileAppConfigurationDeviceSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedDeviceMobileAppConfigurationUserStatus".casefold():
            from . import managed_device_mobile_app_configuration_user_status

            return managed_device_mobile_app_configuration_user_status.ManagedDeviceMobileAppConfigurationUserStatus()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedDeviceMobileAppConfigurationUserSummary".casefold():
            from . import managed_device_mobile_app_configuration_user_summary

            return managed_device_mobile_app_configuration_user_summary.ManagedDeviceMobileAppConfigurationUserSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedDeviceOverview".casefold():
            from . import managed_device_overview

            return managed_device_overview.ManagedDeviceOverview()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedEBook".casefold():
            from . import managed_e_book

            return managed_e_book.ManagedEBook()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedEBookAssignment".casefold():
            from . import managed_e_book_assignment

            return managed_e_book_assignment.ManagedEBookAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedIOSLobApp".casefold():
            from . import managed_i_o_s_lob_app

            return managed_i_o_s_lob_app.ManagedIOSLobApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedIOSStoreApp".casefold():
            from . import managed_i_o_s_store_app

            return managed_i_o_s_store_app.ManagedIOSStoreApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedMobileApp".casefold():
            from . import managed_mobile_app

            return managed_mobile_app.ManagedMobileApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedMobileLobApp".casefold():
            from . import managed_mobile_lob_app

            return managed_mobile_lob_app.ManagedMobileLobApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mdmWindowsInformationProtectionPolicy".casefold():
            from . import mdm_windows_information_protection_policy

            return mdm_windows_information_protection_policy.MdmWindowsInformationProtectionPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.meetingAttendanceReport".casefold():
            from . import meeting_attendance_report

            return meeting_attendance_report.MeetingAttendanceReport()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.message".casefold():
            from . import message

            return message.Message()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.messageRule".casefold():
            from . import message_rule

            return message_rule.MessageRule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.microsoftAccountUserConversationMember".casefold():
            from . import microsoft_account_user_conversation_member

            return microsoft_account_user_conversation_member.MicrosoftAccountUserConversationMember()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.microsoftAuthenticatorAuthenticationMethod".casefold():
            from . import microsoft_authenticator_authentication_method

            return microsoft_authenticator_authentication_method.MicrosoftAuthenticatorAuthenticationMethod()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.microsoftAuthenticatorAuthenticationMethodConfiguration".casefold():
            from . import microsoft_authenticator_authentication_method_configuration

            return microsoft_authenticator_authentication_method_configuration.MicrosoftAuthenticatorAuthenticationMethodConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.microsoftAuthenticatorAuthenticationMethodTarget".casefold():
            from . import microsoft_authenticator_authentication_method_target

            return microsoft_authenticator_authentication_method_target.MicrosoftAuthenticatorAuthenticationMethodTarget()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.microsoftStoreForBusinessApp".casefold():
            from . import microsoft_store_for_business_app

            return microsoft_store_for_business_app.MicrosoftStoreForBusinessApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mobileApp".casefold():
            from . import mobile_app

            return mobile_app.MobileApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mobileAppAssignment".casefold():
            from . import mobile_app_assignment

            return mobile_app_assignment.MobileAppAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mobileAppCategory".casefold():
            from . import mobile_app_category

            return mobile_app_category.MobileAppCategory()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mobileAppContent".casefold():
            from . import mobile_app_content

            return mobile_app_content.MobileAppContent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mobileAppContentFile".casefold():
            from . import mobile_app_content_file

            return mobile_app_content_file.MobileAppContentFile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mobileContainedApp".casefold():
            from . import mobile_contained_app

            return mobile_contained_app.MobileContainedApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mobileLobApp".casefold():
            from . import mobile_lob_app

            return mobile_lob_app.MobileLobApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mobileThreatDefenseConnector".casefold():
            from . import mobile_threat_defense_connector

            return mobile_threat_defense_connector.MobileThreatDefenseConnector()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.multiValueLegacyExtendedProperty".casefold():
            from . import multi_value_legacy_extended_property

            return multi_value_legacy_extended_property.MultiValueLegacyExtendedProperty()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.muteParticipantOperation".casefold():
            from . import mute_participant_operation

            return mute_participant_operation.MuteParticipantOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.namedLocation".casefold():
            from . import named_location

            return named_location.NamedLocation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.notebook".casefold():
            from . import notebook

            return notebook.Notebook()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.notificationMessageTemplate".casefold():
            from . import notification_message_template

            return notification_message_template.NotificationMessageTemplate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.oAuth2PermissionGrant".casefold():
            from . import o_auth2_permission_grant

            return o_auth2_permission_grant.OAuth2PermissionGrant()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.offerShiftRequest".casefold():
            from . import offer_shift_request

            return offer_shift_request.OfferShiftRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.officeGraphInsights".casefold():
            from . import office_graph_insights

            return office_graph_insights.OfficeGraphInsights()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onenote".casefold():
            from . import onenote

            return onenote.Onenote()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onenoteEntityBaseModel".casefold():
            from . import onenote_entity_base_model

            return onenote_entity_base_model.OnenoteEntityBaseModel()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onenoteEntityHierarchyModel".casefold():
            from . import onenote_entity_hierarchy_model

            return onenote_entity_hierarchy_model.OnenoteEntityHierarchyModel()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onenoteEntitySchemaObjectModel".casefold():
            from . import onenote_entity_schema_object_model

            return onenote_entity_schema_object_model.OnenoteEntitySchemaObjectModel()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onenoteOperation".casefold():
            from . import onenote_operation

            return onenote_operation.OnenoteOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onenotePage".casefold():
            from . import onenote_page

            return onenote_page.OnenotePage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onenoteResource".casefold():
            from . import onenote_resource

            return onenote_resource.OnenoteResource()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onenoteSection".casefold():
            from . import onenote_section

            return onenote_section.OnenoteSection()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onlineMeeting".casefold():
            from . import online_meeting

            return online_meeting.OnlineMeeting()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onPremisesConditionalAccessSettings".casefold():
            from . import on_premises_conditional_access_settings

            return on_premises_conditional_access_settings.OnPremisesConditionalAccessSettings()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onPremisesDirectorySynchronization".casefold():
            from . import on_premises_directory_synchronization

            return on_premises_directory_synchronization.OnPremisesDirectorySynchronization()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.openShift".casefold():
            from . import open_shift

            return open_shift.OpenShift()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.openShiftChangeRequest".casefold():
            from . import open_shift_change_request

            return open_shift_change_request.OpenShiftChangeRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.openTypeExtension".casefold():
            from . import open_type_extension

            return open_type_extension.OpenTypeExtension()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.operation".casefold():
            from . import operation

            return operation.Operation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.organization".casefold():
            from . import organization

            return organization.Organization()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.organizationalBranding".casefold():
            from . import organizational_branding

            return organizational_branding.OrganizationalBranding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.organizationalBrandingLocalization".casefold():
            from . import organizational_branding_localization

            return organizational_branding_localization.OrganizationalBrandingLocalization()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.organizationalBrandingProperties".casefold():
            from . import organizational_branding_properties

            return organizational_branding_properties.OrganizationalBrandingProperties()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.orgContact".casefold():
            from . import org_contact

            return org_contact.OrgContact()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.outlookCategory".casefold():
            from . import outlook_category

            return outlook_category.OutlookCategory()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.outlookItem".casefold():
            from . import outlook_item

            return outlook_item.OutlookItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.outlookUser".casefold():
            from . import outlook_user

            return outlook_user.OutlookUser()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.participant".casefold():
            from . import participant

            return participant.Participant()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.participantJoiningNotification".casefold():
            from . import participant_joining_notification

            return participant_joining_notification.ParticipantJoiningNotification()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.participantLeftNotification".casefold():
            from . import participant_left_notification

            return participant_left_notification.ParticipantLeftNotification()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.passwordAuthenticationMethod".casefold():
            from . import password_authentication_method

            return password_authentication_method.PasswordAuthenticationMethod()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.permission".casefold():
            from . import permission

            return permission.Permission()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.permissionGrantConditionSet".casefold():
            from . import permission_grant_condition_set

            return permission_grant_condition_set.PermissionGrantConditionSet()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.permissionGrantPolicy".casefold():
            from . import permission_grant_policy

            return permission_grant_policy.PermissionGrantPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.person".casefold():
            from . import person

            return person.Person()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.phoneAuthenticationMethod".casefold():
            from . import phone_authentication_method

            return phone_authentication_method.PhoneAuthenticationMethod()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.pinnedChatMessageInfo".casefold():
            from . import pinned_chat_message_info

            return pinned_chat_message_info.PinnedChatMessageInfo()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.place".casefold():
            from . import place

            return place.Place()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.planner".casefold():
            from . import planner

            return planner.Planner()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.plannerAssignedToTaskBoardTaskFormat".casefold():
            from . import planner_assigned_to_task_board_task_format

            return planner_assigned_to_task_board_task_format.PlannerAssignedToTaskBoardTaskFormat()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.plannerBucket".casefold():
            from . import planner_bucket

            return planner_bucket.PlannerBucket()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.plannerBucketTaskBoardTaskFormat".casefold():
            from . import planner_bucket_task_board_task_format

            return planner_bucket_task_board_task_format.PlannerBucketTaskBoardTaskFormat()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.plannerGroup".casefold():
            from . import planner_group

            return planner_group.PlannerGroup()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.plannerPlan".casefold():
            from . import planner_plan

            return planner_plan.PlannerPlan()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.plannerPlanDetails".casefold():
            from . import planner_plan_details

            return planner_plan_details.PlannerPlanDetails()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.plannerProgressTaskBoardTaskFormat".casefold():
            from . import planner_progress_task_board_task_format

            return planner_progress_task_board_task_format.PlannerProgressTaskBoardTaskFormat()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.plannerTask".casefold():
            from . import planner_task

            return planner_task.PlannerTask()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.plannerTaskDetails".casefold():
            from . import planner_task_details

            return planner_task_details.PlannerTaskDetails()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.plannerUser".casefold():
            from . import planner_user

            return planner_user.PlannerUser()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.playPromptOperation".casefold():
            from . import play_prompt_operation

            return play_prompt_operation.PlayPromptOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.policyBase".casefold():
            from . import policy_base

            return policy_base.PolicyBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.policyRoot".casefold():
            from . import policy_root

            return policy_root.PolicyRoot()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.post".casefold():
            from . import post

            return post.Post()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.presence".casefold():
            from . import presence

            return presence.Presence()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.printConnector".casefold():
            from . import print_connector

            return print_connector.PrintConnector()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.printDocument".casefold():
            from . import print_document

            return print_document.PrintDocument()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.printer".casefold():
            from . import printer

            return printer.Printer()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.printerBase".casefold():
            from . import printer_base

            return printer_base.PrinterBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.printerCreateOperation".casefold():
            from . import printer_create_operation

            return printer_create_operation.PrinterCreateOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.printerShare".casefold():
            from . import printer_share

            return printer_share.PrinterShare()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.printJob".casefold():
            from . import print_job

            return print_job.PrintJob()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.printOperation".casefold():
            from . import print_operation

            return print_operation.PrintOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.printService".casefold():
            from . import print_service

            return print_service.PrintService()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.printServiceEndpoint".casefold():
            from . import print_service_endpoint

            return print_service_endpoint.PrintServiceEndpoint()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.printTask".casefold():
            from . import print_task

            return print_task.PrintTask()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.printTaskDefinition".casefold():
            from . import print_task_definition

            return print_task_definition.PrintTaskDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.printTaskTrigger".casefold():
            from . import print_task_trigger

            return print_task_trigger.PrintTaskTrigger()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.printUsage".casefold():
            from . import print_usage

            return print_usage.PrintUsage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.printUsageByPrinter".casefold():
            from . import print_usage_by_printer

            return print_usage_by_printer.PrintUsageByPrinter()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.printUsageByUser".casefold():
            from . import print_usage_by_user

            return print_usage_by_user.PrintUsageByUser()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.profilePhoto".casefold():
            from . import profile_photo

            return profile_photo.ProfilePhoto()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.provisioningObjectSummary".casefold():
            from . import provisioning_object_summary

            return provisioning_object_summary.ProvisioningObjectSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.rbacApplication".casefold():
            from . import rbac_application

            return rbac_application.RbacApplication()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.recordOperation".casefold():
            from . import record_operation

            return record_operation.RecordOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.referenceAttachment".casefold():
            from . import reference_attachment

            return reference_attachment.ReferenceAttachment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.remoteAssistancePartner".casefold():
            from . import remote_assistance_partner

            return remote_assistance_partner.RemoteAssistancePartner()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.request".casefold():
            from . import request

            return request.Request()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.resourceOperation".casefold():
            from . import resource_operation

            return resource_operation.ResourceOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.resourceSpecificPermissionGrant".casefold():
            from . import resource_specific_permission_grant

            return resource_specific_permission_grant.ResourceSpecificPermissionGrant()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.richLongRunningOperation".casefold():
            from . import rich_long_running_operation

            return rich_long_running_operation.RichLongRunningOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.riskDetection".casefold():
            from . import risk_detection

            return risk_detection.RiskDetection()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.riskyServicePrincipal".casefold():
            from . import risky_service_principal

            return risky_service_principal.RiskyServicePrincipal()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.riskyServicePrincipalHistoryItem".casefold():
            from . import risky_service_principal_history_item

            return risky_service_principal_history_item.RiskyServicePrincipalHistoryItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.riskyUser".casefold():
            from . import risky_user

            return risky_user.RiskyUser()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.riskyUserHistoryItem".casefold():
            from . import risky_user_history_item

            return risky_user_history_item.RiskyUserHistoryItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.roleAssignment".casefold():
            from . import role_assignment

            return role_assignment.RoleAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.roleDefinition".casefold():
            from . import role_definition

            return role_definition.RoleDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.room".casefold():
            from . import room

            return room.Room()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.roomList".casefold():
            from . import room_list

            return room_list.RoomList()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.samlOrWsFedExternalDomainFederation".casefold():
            from . import saml_or_ws_fed_external_domain_federation

            return saml_or_ws_fed_external_domain_federation.SamlOrWsFedExternalDomainFederation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.samlOrWsFedProvider".casefold():
            from . import saml_or_ws_fed_provider

            return saml_or_ws_fed_provider.SamlOrWsFedProvider()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.schedule".casefold():
            from . import schedule

            return schedule.Schedule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.scheduleChangeRequest".casefold():
            from . import schedule_change_request

            return schedule_change_request.ScheduleChangeRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.schedulingGroup".casefold():
            from . import scheduling_group

            return scheduling_group.SchedulingGroup()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.schemaExtension".casefold():
            from . import schema_extension

            return schema_extension.SchemaExtension()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.scopedRoleMembership".casefold():
            from . import scoped_role_membership

            return scoped_role_membership.ScopedRoleMembership()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.searchEntity".casefold():
            from . import search_entity

            return search_entity.SearchEntity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sectionGroup".casefold():
            from . import section_group

            return section_group.SectionGroup()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.secureScore".casefold():
            from . import secure_score

            return secure_score.SecureScore()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.secureScoreControlProfile".casefold():
            from . import secure_score_control_profile

            return secure_score_control_profile.SecureScoreControlProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security".casefold():
            from .security import security

            return security.Security()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.alert".casefold():
            from . import alert
            from .security import alert

            return alert.Alert()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.case".casefold():
            from .security import case

            return case.Case()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.caseOperation".casefold():
            from .security import case_operation

            return case_operation.CaseOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.casesRoot".casefold():
            from .security import cases_root

            return cases_root.CasesRoot()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.dataSet".casefold():
            from .security import data_set

            return data_set.DataSet()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.dataSource".casefold():
            from .security import data_source

            return data_source.DataSource()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.dataSourceContainer".casefold():
            from .security import data_source_container

            return data_source_container.DataSourceContainer()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ediscoveryAddToReviewSetOperation".casefold():
            from .security import ediscovery_add_to_review_set_operation

            return ediscovery_add_to_review_set_operation.EdiscoveryAddToReviewSetOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ediscoveryCase".casefold():
            from .security import ediscovery_case

            return ediscovery_case.EdiscoveryCase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ediscoveryCaseSettings".casefold():
            from .security import ediscovery_case_settings

            return ediscovery_case_settings.EdiscoveryCaseSettings()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ediscoveryCustodian".casefold():
            from .security import ediscovery_custodian

            return ediscovery_custodian.EdiscoveryCustodian()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ediscoveryEstimateOperation".casefold():
            from .security import ediscovery_estimate_operation

            return ediscovery_estimate_operation.EdiscoveryEstimateOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ediscoveryHoldOperation".casefold():
            from .security import ediscovery_hold_operation

            return ediscovery_hold_operation.EdiscoveryHoldOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ediscoveryIndexOperation".casefold():
            from .security import ediscovery_index_operation

            return ediscovery_index_operation.EdiscoveryIndexOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ediscoveryNoncustodialDataSource".casefold():
            from .security import ediscovery_noncustodial_data_source

            return ediscovery_noncustodial_data_source.EdiscoveryNoncustodialDataSource()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ediscoveryPurgeDataOperation".casefold():
            from .security import ediscovery_purge_data_operation

            return ediscovery_purge_data_operation.EdiscoveryPurgeDataOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ediscoveryReviewSet".casefold():
            from .security import ediscovery_review_set

            return ediscovery_review_set.EdiscoveryReviewSet()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ediscoveryReviewSetQuery".casefold():
            from .security import ediscovery_review_set_query

            return ediscovery_review_set_query.EdiscoveryReviewSetQuery()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ediscoveryReviewTag".casefold():
            from .security import ediscovery_review_tag

            return ediscovery_review_tag.EdiscoveryReviewTag()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ediscoverySearch".casefold():
            from .security import ediscovery_search

            return ediscovery_search.EdiscoverySearch()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ediscoveryTagOperation".casefold():
            from .security import ediscovery_tag_operation

            return ediscovery_tag_operation.EdiscoveryTagOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.incident".casefold():
            from .security import incident

            return incident.Incident()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.retentionEvent".casefold():
            from .security import retention_event

            return retention_event.RetentionEvent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.retentionEventType".casefold():
            from .security import retention_event_type

            return retention_event_type.RetentionEventType()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.search".casefold():
            from .security import search

            return search.Search()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.siteSource".casefold():
            from .security import site_source

            return site_source.SiteSource()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.tag".casefold():
            from .security import tag

            return tag.Tag()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.triggersRoot".casefold():
            from .security import triggers_root

            return triggers_root.TriggersRoot()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.triggerTypesRoot".casefold():
            from .security import trigger_types_root

            return trigger_types_root.TriggerTypesRoot()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.unifiedGroupSource".casefold():
            from .security import unified_group_source

            return unified_group_source.UnifiedGroupSource()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.userSource".casefold():
            from .security import user_source

            return user_source.UserSource()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.securityReportsRoot".casefold():
            from . import security_reports_root

            return security_reports_root.SecurityReportsRoot()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.serviceAnnouncement".casefold():
            from . import service_announcement

            return service_announcement.ServiceAnnouncement()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.serviceAnnouncementAttachment".casefold():
            from . import service_announcement_attachment

            return service_announcement_attachment.ServiceAnnouncementAttachment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.serviceAnnouncementBase".casefold():
            from . import service_announcement_base

            return service_announcement_base.ServiceAnnouncementBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.serviceHealth".casefold():
            from . import service_health

            return service_health.ServiceHealth()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.serviceHealthIssue".casefold():
            from . import service_health_issue

            return service_health_issue.ServiceHealthIssue()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.servicePrincipal".casefold():
            from . import service_principal

            return service_principal.ServicePrincipal()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.servicePrincipalRiskDetection".casefold():
            from . import service_principal_risk_detection

            return service_principal_risk_detection.ServicePrincipalRiskDetection()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.serviceUpdateMessage".casefold():
            from . import service_update_message

            return service_update_message.ServiceUpdateMessage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.settingStateDeviceSummary".casefold():
            from . import setting_state_device_summary

            return setting_state_device_summary.SettingStateDeviceSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sharedDriveItem".casefold():
            from . import shared_drive_item

            return shared_drive_item.SharedDriveItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sharedInsight".casefold():
            from . import shared_insight

            return shared_insight.SharedInsight()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sharedPCConfiguration".casefold():
            from . import shared_p_c_configuration

            return shared_p_c_configuration.SharedPCConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sharedWithChannelTeamInfo".casefold():
            from . import shared_with_channel_team_info

            return shared_with_channel_team_info.SharedWithChannelTeamInfo()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sharepoint".casefold():
            from . import sharepoint

            return sharepoint.Sharepoint()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sharepointSettings".casefold():
            from . import sharepoint_settings

            return sharepoint_settings.SharepointSettings()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.shift".casefold():
            from . import shift

            return shift.Shift()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.shiftPreferences".casefold():
            from . import shift_preferences

            return shift_preferences.ShiftPreferences()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.signIn".casefold():
            from . import sign_in

            return sign_in.SignIn()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.simulation".casefold():
            from . import simulation

            return simulation.Simulation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.simulationAutomation".casefold():
            from . import simulation_automation

            return simulation_automation.SimulationAutomation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.simulationAutomationRun".casefold():
            from . import simulation_automation_run

            return simulation_automation_run.SimulationAutomationRun()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.singleValueLegacyExtendedProperty".casefold():
            from . import single_value_legacy_extended_property

            return single_value_legacy_extended_property.SingleValueLegacyExtendedProperty()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.site".casefold():
            from . import site

            return site.Site()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.skypeForBusinessUserConversationMember".casefold():
            from . import skype_for_business_user_conversation_member

            return skype_for_business_user_conversation_member.SkypeForBusinessUserConversationMember()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.skypeUserConversationMember".casefold():
            from . import skype_user_conversation_member

            return skype_user_conversation_member.SkypeUserConversationMember()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.smsAuthenticationMethodConfiguration".casefold():
            from . import sms_authentication_method_configuration

            return sms_authentication_method_configuration.SmsAuthenticationMethodConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.smsAuthenticationMethodTarget".casefold():
            from . import sms_authentication_method_target

            return sms_authentication_method_target.SmsAuthenticationMethodTarget()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.socialIdentityProvider".casefold():
            from . import social_identity_provider

            return social_identity_provider.SocialIdentityProvider()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.softwareOathAuthenticationMethod".casefold():
            from . import software_oath_authentication_method

            return software_oath_authentication_method.SoftwareOathAuthenticationMethod()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.softwareOathAuthenticationMethodConfiguration".casefold():
            from . import software_oath_authentication_method_configuration

            return software_oath_authentication_method_configuration.SoftwareOathAuthenticationMethodConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.softwareUpdateStatusSummary".casefold():
            from . import software_update_status_summary

            return software_update_status_summary.SoftwareUpdateStatusSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.startHoldMusicOperation".casefold():
            from . import start_hold_music_operation

            return start_hold_music_operation.StartHoldMusicOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.stopHoldMusicOperation".casefold():
            from . import stop_hold_music_operation

            return stop_hold_music_operation.StopHoldMusicOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.stsPolicy".casefold():
            from . import sts_policy

            return sts_policy.StsPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.subjectRightsRequest".casefold():
            from . import subject_rights_request

            return subject_rights_request.SubjectRightsRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.subscribedSku".casefold():
            from . import subscribed_sku

            return subscribed_sku.SubscribedSku()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.subscribeToToneOperation".casefold():
            from . import subscribe_to_tone_operation

            return subscribe_to_tone_operation.SubscribeToToneOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.subscription".casefold():
            from . import subscription

            return subscription.Subscription()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.swapShiftsChangeRequest".casefold():
            from . import swap_shifts_change_request

            return swap_shifts_change_request.SwapShiftsChangeRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.synchronization".casefold():
            from . import synchronization

            return synchronization.Synchronization()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.synchronizationJob".casefold():
            from . import synchronization_job

            return synchronization_job.SynchronizationJob()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.synchronizationSchema".casefold():
            from . import synchronization_schema

            return synchronization_schema.SynchronizationSchema()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.synchronizationTemplate".casefold():
            from . import synchronization_template

            return synchronization_template.SynchronizationTemplate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.targetedManagedAppConfiguration".casefold():
            from . import targeted_managed_app_configuration

            return targeted_managed_app_configuration.TargetedManagedAppConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.targetedManagedAppPolicyAssignment".casefold():
            from . import targeted_managed_app_policy_assignment

            return targeted_managed_app_policy_assignment.TargetedManagedAppPolicyAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.targetedManagedAppProtection".casefold():
            from . import targeted_managed_app_protection

            return targeted_managed_app_protection.TargetedManagedAppProtection()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.taskFileAttachment".casefold():
            from . import task_file_attachment

            return task_file_attachment.TaskFileAttachment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.team".casefold():
            from . import team

            return team.Team()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamInfo".casefold():
            from . import team_info

            return team_info.TeamInfo()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamsApp".casefold():
            from . import teams_app

            return teams_app.TeamsApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamsAppDefinition".casefold():
            from . import teams_app_definition

            return teams_app_definition.TeamsAppDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamsAppInstallation".casefold():
            from . import teams_app_installation

            return teams_app_installation.TeamsAppInstallation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamsAsyncOperation".casefold():
            from . import teams_async_operation

            return teams_async_operation.TeamsAsyncOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamsTab".casefold():
            from . import teams_tab

            return teams_tab.TeamsTab()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamsTemplate".casefold():
            from . import teams_template

            return teams_template.TeamsTemplate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamwork".casefold():
            from . import teamwork

            return teamwork.Teamwork()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamworkBot".casefold():
            from . import teamwork_bot

            return teamwork_bot.TeamworkBot()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamworkHostedContent".casefold():
            from . import teamwork_hosted_content

            return teamwork_hosted_content.TeamworkHostedContent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamworkTag".casefold():
            from . import teamwork_tag

            return teamwork_tag.TeamworkTag()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamworkTagMember".casefold():
            from . import teamwork_tag_member

            return teamwork_tag_member.TeamworkTagMember()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.telecomExpenseManagementPartner".casefold():
            from . import telecom_expense_management_partner

            return telecom_expense_management_partner.TelecomExpenseManagementPartner()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.temporaryAccessPassAuthenticationMethod".casefold():
            from . import temporary_access_pass_authentication_method

            return temporary_access_pass_authentication_method.TemporaryAccessPassAuthenticationMethod()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.temporaryAccessPassAuthenticationMethodConfiguration".casefold():
            from . import temporary_access_pass_authentication_method_configuration

            return temporary_access_pass_authentication_method_configuration.TemporaryAccessPassAuthenticationMethodConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.tenantAppManagementPolicy".casefold():
            from . import tenant_app_management_policy

            return tenant_app_management_policy.TenantAppManagementPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.termsAndConditions".casefold():
            from . import terms_and_conditions

            return terms_and_conditions.TermsAndConditions()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.termsAndConditionsAcceptanceStatus".casefold():
            from . import terms_and_conditions_acceptance_status

            return terms_and_conditions_acceptance_status.TermsAndConditionsAcceptanceStatus()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.termsAndConditionsAssignment".casefold():
            from . import terms_and_conditions_assignment

            return terms_and_conditions_assignment.TermsAndConditionsAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.termsOfUseContainer".casefold():
            from . import terms_of_use_container

            return terms_of_use_container.TermsOfUseContainer()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.termStore.group".casefold():
            from . import group
            from .term_store import group

            return group.Group()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.termStore.relation".casefold():
            from .term_store import relation

            return relation.Relation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.termStore.set".casefold():
            from .term_store import set

            return set.Set()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.termStore.store".casefold():
            from .term_store import store

            return store.Store()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.termStore.term".casefold():
            from .term_store import term

            return term.Term()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.threatAssessmentRequest".casefold():
            from . import threat_assessment_request

            return threat_assessment_request.ThreatAssessmentRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.threatAssessmentResult".casefold():
            from . import threat_assessment_result

            return threat_assessment_result.ThreatAssessmentResult()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.thumbnailSet".casefold():
            from . import thumbnail_set

            return thumbnail_set.ThumbnailSet()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.timeOff".casefold():
            from . import time_off

            return time_off.TimeOff()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.timeOffReason".casefold():
            from . import time_off_reason

            return time_off_reason.TimeOffReason()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.timeOffRequest".casefold():
            from . import time_off_request

            return time_off_request.TimeOffRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.todo".casefold():
            from . import todo

            return todo.Todo()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.todoTask".casefold():
            from . import todo_task

            return todo_task.TodoTask()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.todoTaskList".casefold():
            from . import todo_task_list

            return todo_task_list.TodoTaskList()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.tokenIssuancePolicy".casefold():
            from . import token_issuance_policy

            return token_issuance_policy.TokenIssuancePolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.tokenLifetimePolicy".casefold():
            from . import token_lifetime_policy

            return token_lifetime_policy.TokenLifetimePolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.trending".casefold():
            from . import trending

            return trending.Trending()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRbacResourceAction".casefold():
            from . import unified_rbac_resource_action

            return unified_rbac_resource_action.UnifiedRbacResourceAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRbacResourceNamespace".casefold():
            from . import unified_rbac_resource_namespace

            return unified_rbac_resource_namespace.UnifiedRbacResourceNamespace()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRoleAssignment".casefold():
            from . import unified_role_assignment

            return unified_role_assignment.UnifiedRoleAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRoleAssignmentSchedule".casefold():
            from . import unified_role_assignment_schedule

            return unified_role_assignment_schedule.UnifiedRoleAssignmentSchedule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRoleAssignmentScheduleInstance".casefold():
            from . import unified_role_assignment_schedule_instance

            return unified_role_assignment_schedule_instance.UnifiedRoleAssignmentScheduleInstance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRoleAssignmentScheduleRequest".casefold():
            from . import unified_role_assignment_schedule_request

            return unified_role_assignment_schedule_request.UnifiedRoleAssignmentScheduleRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRoleDefinition".casefold():
            from . import unified_role_definition

            return unified_role_definition.UnifiedRoleDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRoleEligibilitySchedule".casefold():
            from . import unified_role_eligibility_schedule

            return unified_role_eligibility_schedule.UnifiedRoleEligibilitySchedule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRoleEligibilityScheduleInstance".casefold():
            from . import unified_role_eligibility_schedule_instance

            return unified_role_eligibility_schedule_instance.UnifiedRoleEligibilityScheduleInstance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRoleEligibilityScheduleRequest".casefold():
            from . import unified_role_eligibility_schedule_request

            return unified_role_eligibility_schedule_request.UnifiedRoleEligibilityScheduleRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRoleManagementPolicy".casefold():
            from . import unified_role_management_policy

            return unified_role_management_policy.UnifiedRoleManagementPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRoleManagementPolicyApprovalRule".casefold():
            from . import unified_role_management_policy_approval_rule

            return unified_role_management_policy_approval_rule.UnifiedRoleManagementPolicyApprovalRule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRoleManagementPolicyAssignment".casefold():
            from . import unified_role_management_policy_assignment

            return unified_role_management_policy_assignment.UnifiedRoleManagementPolicyAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRoleManagementPolicyAuthenticationContextRule".casefold():
            from . import unified_role_management_policy_authentication_context_rule

            return unified_role_management_policy_authentication_context_rule.UnifiedRoleManagementPolicyAuthenticationContextRule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRoleManagementPolicyEnablementRule".casefold():
            from . import unified_role_management_policy_enablement_rule

            return unified_role_management_policy_enablement_rule.UnifiedRoleManagementPolicyEnablementRule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRoleManagementPolicyExpirationRule".casefold():
            from . import unified_role_management_policy_expiration_rule

            return unified_role_management_policy_expiration_rule.UnifiedRoleManagementPolicyExpirationRule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRoleManagementPolicyNotificationRule".casefold():
            from . import unified_role_management_policy_notification_rule

            return unified_role_management_policy_notification_rule.UnifiedRoleManagementPolicyNotificationRule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRoleManagementPolicyRule".casefold():
            from . import unified_role_management_policy_rule

            return unified_role_management_policy_rule.UnifiedRoleManagementPolicyRule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRoleScheduleBase".casefold():
            from . import unified_role_schedule_base

            return unified_role_schedule_base.UnifiedRoleScheduleBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRoleScheduleInstanceBase".casefold():
            from . import unified_role_schedule_instance_base

            return unified_role_schedule_instance_base.UnifiedRoleScheduleInstanceBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unmuteParticipantOperation".casefold():
            from . import unmute_participant_operation

            return unmute_participant_operation.UnmuteParticipantOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.updateRecordingStatusOperation".casefold():
            from . import update_recording_status_operation

            return update_recording_status_operation.UpdateRecordingStatusOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.urlAssessmentRequest".casefold():
            from . import url_assessment_request

            return url_assessment_request.UrlAssessmentRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.usedInsight".casefold():
            from . import used_insight

            return used_insight.UsedInsight()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.user".casefold():
            from . import user

            return user.User()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userActivity".casefold():
            from . import user_activity

            return user_activity.UserActivity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userConsentRequest".casefold():
            from . import user_consent_request

            return user_consent_request.UserConsentRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userExperienceAnalyticsDevicePerformance".casefold():
            from . import user_experience_analytics_device_performance

            return user_experience_analytics_device_performance.UserExperienceAnalyticsDevicePerformance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userFlowLanguageConfiguration".casefold():
            from . import user_flow_language_configuration

            return user_flow_language_configuration.UserFlowLanguageConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userFlowLanguagePage".casefold():
            from . import user_flow_language_page

            return user_flow_language_page.UserFlowLanguagePage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userInstallStateSummary".casefold():
            from . import user_install_state_summary

            return user_install_state_summary.UserInstallStateSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userScopeTeamsAppInstallation".casefold():
            from . import user_scope_teams_app_installation

            return user_scope_teams_app_installation.UserScopeTeamsAppInstallation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userSettings".casefold():
            from . import user_settings

            return user_settings.UserSettings()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userTeamwork".casefold():
            from . import user_teamwork

            return user_teamwork.UserTeamwork()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.voiceAuthenticationMethodConfiguration".casefold():
            from . import voice_authentication_method_configuration

            return voice_authentication_method_configuration.VoiceAuthenticationMethodConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.vppToken".casefold():
            from . import vpp_token

            return vpp_token.VppToken()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.webApp".casefold():
            from . import web_app

            return web_app.WebApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.win32LobApp".casefold():
            from . import win32_lob_app

            return win32_lob_app.Win32LobApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10CompliancePolicy".casefold():
            from . import windows10_compliance_policy

            return windows10_compliance_policy.Windows10CompliancePolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10CustomConfiguration".casefold():
            from . import windows10_custom_configuration

            return windows10_custom_configuration.Windows10CustomConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10EndpointProtectionConfiguration".casefold():
            from . import windows10_endpoint_protection_configuration

            return windows10_endpoint_protection_configuration.Windows10EndpointProtectionConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10EnterpriseModernAppManagementConfiguration".casefold():
            from . import windows10_enterprise_modern_app_management_configuration

            return windows10_enterprise_modern_app_management_configuration.Windows10EnterpriseModernAppManagementConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10GeneralConfiguration".casefold():
            from . import windows10_general_configuration

            return windows10_general_configuration.Windows10GeneralConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10MobileCompliancePolicy".casefold():
            from . import windows10_mobile_compliance_policy

            return windows10_mobile_compliance_policy.Windows10MobileCompliancePolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10SecureAssessmentConfiguration".casefold():
            from . import windows10_secure_assessment_configuration

            return windows10_secure_assessment_configuration.Windows10SecureAssessmentConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10TeamGeneralConfiguration".casefold():
            from . import windows10_team_general_configuration

            return windows10_team_general_configuration.Windows10TeamGeneralConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows81CompliancePolicy".casefold():
            from . import windows81_compliance_policy

            return windows81_compliance_policy.Windows81CompliancePolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows81GeneralConfiguration".casefold():
            from . import windows81_general_configuration

            return windows81_general_configuration.Windows81GeneralConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsAppX".casefold():
            from . import windows_app_x

            return windows_app_x.WindowsAppX()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsAutopilotDeviceIdentity".casefold():
            from . import windows_autopilot_device_identity

            return windows_autopilot_device_identity.WindowsAutopilotDeviceIdentity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsDefenderAdvancedThreatProtectionConfiguration".casefold():
            from . import windows_defender_advanced_threat_protection_configuration

            return windows_defender_advanced_threat_protection_configuration.WindowsDefenderAdvancedThreatProtectionConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsHelloForBusinessAuthenticationMethod".casefold():
            from . import windows_hello_for_business_authentication_method

            return windows_hello_for_business_authentication_method.WindowsHelloForBusinessAuthenticationMethod()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsInformationProtection".casefold():
            from . import windows_information_protection

            return windows_information_protection.WindowsInformationProtection()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsInformationProtectionAppLearningSummary".casefold():
            from . import windows_information_protection_app_learning_summary

            return windows_information_protection_app_learning_summary.WindowsInformationProtectionAppLearningSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsInformationProtectionAppLockerFile".casefold():
            from . import windows_information_protection_app_locker_file

            return windows_information_protection_app_locker_file.WindowsInformationProtectionAppLockerFile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsInformationProtectionNetworkLearningSummary".casefold():
            from . import windows_information_protection_network_learning_summary

            return windows_information_protection_network_learning_summary.WindowsInformationProtectionNetworkLearningSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsInformationProtectionPolicy".casefold():
            from . import windows_information_protection_policy

            return windows_information_protection_policy.WindowsInformationProtectionPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsMicrosoftEdgeApp".casefold():
            from . import windows_microsoft_edge_app

            return windows_microsoft_edge_app.WindowsMicrosoftEdgeApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsMobileMSI".casefold():
            from . import windows_mobile_m_s_i

            return windows_mobile_m_s_i.WindowsMobileMSI()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsPhone81CompliancePolicy".casefold():
            from . import windows_phone81_compliance_policy

            return windows_phone81_compliance_policy.WindowsPhone81CompliancePolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsPhone81CustomConfiguration".casefold():
            from . import windows_phone81_custom_configuration

            return windows_phone81_custom_configuration.WindowsPhone81CustomConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsPhone81GeneralConfiguration".casefold():
            from . import windows_phone81_general_configuration

            return windows_phone81_general_configuration.WindowsPhone81GeneralConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsUniversalAppX".casefold():
            from . import windows_universal_app_x

            return windows_universal_app_x.WindowsUniversalAppX()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsUniversalAppXContainedApp".casefold():
            from . import windows_universal_app_x_contained_app

            return windows_universal_app_x_contained_app.WindowsUniversalAppXContainedApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsUpdateForBusinessConfiguration".casefold():
            from . import windows_update_for_business_configuration

            return windows_update_for_business_configuration.WindowsUpdateForBusinessConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsWebApp".casefold():
            from . import windows_web_app

            return windows_web_app.WindowsWebApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbook".casefold():
            from . import workbook

            return workbook.Workbook()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookApplication".casefold():
            from . import workbook_application

            return workbook_application.WorkbookApplication()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookChart".casefold():
            from . import workbook_chart

            return workbook_chart.WorkbookChart()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookChartAreaFormat".casefold():
            from . import workbook_chart_area_format

            return workbook_chart_area_format.WorkbookChartAreaFormat()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookChartAxes".casefold():
            from . import workbook_chart_axes

            return workbook_chart_axes.WorkbookChartAxes()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookChartAxis".casefold():
            from . import workbook_chart_axis

            return workbook_chart_axis.WorkbookChartAxis()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookChartAxisFormat".casefold():
            from . import workbook_chart_axis_format

            return workbook_chart_axis_format.WorkbookChartAxisFormat()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookChartAxisTitle".casefold():
            from . import workbook_chart_axis_title

            return workbook_chart_axis_title.WorkbookChartAxisTitle()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookChartAxisTitleFormat".casefold():
            from . import workbook_chart_axis_title_format

            return workbook_chart_axis_title_format.WorkbookChartAxisTitleFormat()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookChartDataLabelFormat".casefold():
            from . import workbook_chart_data_label_format

            return workbook_chart_data_label_format.WorkbookChartDataLabelFormat()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookChartDataLabels".casefold():
            from . import workbook_chart_data_labels

            return workbook_chart_data_labels.WorkbookChartDataLabels()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookChartFill".casefold():
            from . import workbook_chart_fill

            return workbook_chart_fill.WorkbookChartFill()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookChartFont".casefold():
            from . import workbook_chart_font

            return workbook_chart_font.WorkbookChartFont()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookChartGridlines".casefold():
            from . import workbook_chart_gridlines

            return workbook_chart_gridlines.WorkbookChartGridlines()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookChartGridlinesFormat".casefold():
            from . import workbook_chart_gridlines_format

            return workbook_chart_gridlines_format.WorkbookChartGridlinesFormat()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookChartLegend".casefold():
            from . import workbook_chart_legend

            return workbook_chart_legend.WorkbookChartLegend()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookChartLegendFormat".casefold():
            from . import workbook_chart_legend_format

            return workbook_chart_legend_format.WorkbookChartLegendFormat()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookChartLineFormat".casefold():
            from . import workbook_chart_line_format

            return workbook_chart_line_format.WorkbookChartLineFormat()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookChartPoint".casefold():
            from . import workbook_chart_point

            return workbook_chart_point.WorkbookChartPoint()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookChartPointFormat".casefold():
            from . import workbook_chart_point_format

            return workbook_chart_point_format.WorkbookChartPointFormat()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookChartSeries".casefold():
            from . import workbook_chart_series

            return workbook_chart_series.WorkbookChartSeries()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookChartSeriesFormat".casefold():
            from . import workbook_chart_series_format

            return workbook_chart_series_format.WorkbookChartSeriesFormat()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookChartTitle".casefold():
            from . import workbook_chart_title

            return workbook_chart_title.WorkbookChartTitle()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookChartTitleFormat".casefold():
            from . import workbook_chart_title_format

            return workbook_chart_title_format.WorkbookChartTitleFormat()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookComment".casefold():
            from . import workbook_comment

            return workbook_comment.WorkbookComment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookCommentReply".casefold():
            from . import workbook_comment_reply

            return workbook_comment_reply.WorkbookCommentReply()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookFilter".casefold():
            from . import workbook_filter

            return workbook_filter.WorkbookFilter()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookFormatProtection".casefold():
            from . import workbook_format_protection

            return workbook_format_protection.WorkbookFormatProtection()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookFunctionResult".casefold():
            from . import workbook_function_result

            return workbook_function_result.WorkbookFunctionResult()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookFunctions".casefold():
            from . import workbook_functions

            return workbook_functions.WorkbookFunctions()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookNamedItem".casefold():
            from . import workbook_named_item

            return workbook_named_item.WorkbookNamedItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookOperation".casefold():
            from . import workbook_operation

            return workbook_operation.WorkbookOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookPivotTable".casefold():
            from . import workbook_pivot_table

            return workbook_pivot_table.WorkbookPivotTable()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookRange".casefold():
            from . import workbook_range

            return workbook_range.WorkbookRange()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookRangeBorder".casefold():
            from . import workbook_range_border

            return workbook_range_border.WorkbookRangeBorder()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookRangeFill".casefold():
            from . import workbook_range_fill

            return workbook_range_fill.WorkbookRangeFill()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookRangeFont".casefold():
            from . import workbook_range_font

            return workbook_range_font.WorkbookRangeFont()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookRangeFormat".casefold():
            from . import workbook_range_format

            return workbook_range_format.WorkbookRangeFormat()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookRangeSort".casefold():
            from . import workbook_range_sort

            return workbook_range_sort.WorkbookRangeSort()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookRangeView".casefold():
            from . import workbook_range_view

            return workbook_range_view.WorkbookRangeView()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookTable".casefold():
            from . import workbook_table

            return workbook_table.WorkbookTable()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookTableColumn".casefold():
            from . import workbook_table_column

            return workbook_table_column.WorkbookTableColumn()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookTableRow".casefold():
            from . import workbook_table_row

            return workbook_table_row.WorkbookTableRow()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookTableSort".casefold():
            from . import workbook_table_sort

            return workbook_table_sort.WorkbookTableSort()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookWorksheet".casefold():
            from . import workbook_worksheet

            return workbook_worksheet.WorkbookWorksheet()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookWorksheetProtection".casefold():
            from . import workbook_worksheet_protection

            return workbook_worksheet_protection.WorkbookWorksheetProtection()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workforceIntegration".casefold():
            from . import workforce_integration

            return workforce_integration.WorkforceIntegration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.x509CertificateAuthenticationMethodConfiguration".casefold():
            from . import x509_certificate_authentication_method_configuration

            return x509_certificate_authentication_method_configuration.X509CertificateAuthenticationMethodConfiguration()
        return Entity()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import aad_user_conversation_member, access_package, access_package_assignment, access_package_assignment_policy, access_package_assignment_request, access_package_catalog, access_package_multiple_choice_question, access_package_question, access_package_subject, access_package_text_input_question, access_review_history_definition, access_review_history_instance, access_review_instance, access_review_instance_decision_item, access_review_reviewer, access_review_schedule_definition, access_review_set, access_review_stage, activity_based_timeout_policy, activity_history_item, add_large_gallery_view_operation, administrative_unit, admin_consent_request_policy, agreement, agreement_acceptance, agreement_file, agreement_file_localization, agreement_file_properties, agreement_file_version, alert, allowed_value, android_compliance_policy, android_custom_configuration, android_general_device_configuration, android_lob_app, android_managed_app_protection, android_managed_app_registration, android_store_app, android_work_profile_compliance_policy, android_work_profile_custom_configuration, android_work_profile_general_device_configuration, anonymous_guest_conversation_member, apple_device_features_configuration_base, apple_managed_identity_provider, apple_push_notification_certificate, application, application_template, approval, approval_stage, app_catalogs, app_consent_approval_route, app_consent_request, app_management_policy, app_role_assignment, app_scope, associated_team_info, attachment, attachment_base, attachment_session, attack_simulation_root, attendance_record, attribute_mapping_function_schema, attribute_set, audio_routing_group, audit_event, audit_log_root, authentication, authentication_combination_configuration, authentication_context_class_reference, authentication_flows_policy, authentication_method, authentication_methods_policy, authentication_method_configuration, authentication_method_mode_detail, authentication_method_target, authentication_strength_policy, authentication_strength_root, authored_note, authorization_policy, azure_communication_services_user_conversation_member, b2x_identity_user_flow, base_item, base_item_version, bitlocker, bitlocker_recovery_key, booking_appointment, booking_business, booking_currency, booking_customer, booking_customer_base, booking_custom_question, booking_service, booking_staff_member, booking_staff_member_base, browser_shared_cookie, browser_site, browser_site_list, built_in_identity_provider, calendar, calendar_group, calendar_permission, calendar_sharing_message, call, cancel_media_processing_operation, certificate_based_auth_configuration, change_tracked_entity, channel, chat, chat_message, chat_message_hosted_content, chat_message_info, checklist_item, claims_mapping_policy, column_definition, column_link, comms_operation, compliance_management_partner, conditional_access_policy, conditional_access_root, conditional_access_template, connected_organization, contact, contact_folder, content_sharing_session, content_type, contract, conversation, conversation_member, conversation_thread, country_named_location, cross_tenant_access_policy, cross_tenant_access_policy_configuration_default, custom_security_attribute_definition, data_policy_operation, default_managed_app_protection, delegated_admin_access_assignment, delegated_admin_customer, delegated_admin_relationship, delegated_admin_relationship_operation, delegated_admin_relationship_request, delegated_admin_service_management_detail, delegated_permission_classification, deleted_team, detected_app, device, device_and_app_management_role_assignment, device_and_app_management_role_definition, device_app_management, device_category, device_compliance_action_item, device_compliance_device_overview, device_compliance_device_status, device_compliance_policy, device_compliance_policy_assignment, device_compliance_policy_device_state_summary, device_compliance_policy_setting_state_summary, device_compliance_policy_state, device_compliance_scheduled_action_for_rule, device_compliance_setting_state, device_compliance_user_overview, device_compliance_user_status, device_configuration, device_configuration_assignment, device_configuration_device_overview, device_configuration_device_state_summary, device_configuration_device_status, device_configuration_state, device_configuration_user_overview, device_configuration_user_status, device_enrollment_configuration, device_enrollment_limit_configuration, device_enrollment_platform_restrictions_configuration, device_enrollment_windows_hello_for_business_configuration, device_install_state, device_management, device_management_exchange_connector, device_management_export_job, device_management_partner, device_management_reports, device_management_troubleshooting_event, directory, directory_audit, directory_definition, directory_object, directory_object_partner_reference, directory_role, directory_role_template, document_set_version, domain, domain_dns_cname_record, domain_dns_mx_record, domain_dns_record, domain_dns_srv_record, domain_dns_txt_record, domain_dns_unavailable_record, drive, drive_item, drive_item_version, edge, edition_upgrade_configuration, education_assignment, education_assignment_defaults, education_assignment_resource, education_assignment_settings, education_category, education_class, education_feedback_outcome, education_feedback_resource_outcome, education_organization, education_outcome, education_points_outcome, education_rubric, education_rubric_outcome, education_school, education_submission, education_submission_resource, education_user, email_authentication_method, email_authentication_method_configuration, email_file_assessment_request, endpoint, enrollment_configuration_assignment, enrollment_troubleshooting_event, enterprise_code_signing_certificate, entitlement_management, entitlement_management_settings, event, event_message, event_message_request, event_message_response, extension, extension_property, external_domain_name, e_book_install_summary, feature_rollout_policy, federated_identity_credential, fido2_authentication_method, fido2_authentication_method_configuration, fido2_combination_configuration, field_value_set, file_assessment_request, file_attachment, filter_operator_schema, group, group_lifecycle_policy, group_setting, group_setting_template, home_realm_discovery_policy, identity_api_connector, identity_built_in_user_flow_attribute, identity_container, identity_custom_user_flow_attribute, identity_provider, identity_provider_base, identity_security_defaults_enforcement_policy, identity_user_flow, identity_user_flow_attribute, identity_user_flow_attribute_assignment, imported_windows_autopilot_device_identity, imported_windows_autopilot_device_identity_upload, inference_classification, inference_classification_override, internal_domain_federation, internet_explorer_mode, invitation, invite_participants_operation, iosi_pad_o_s_web_clip, ios_certificate_profile, ios_compliance_policy, ios_custom_configuration, ios_device_features_configuration, ios_general_device_configuration, ios_lob_app, ios_lob_app_provisioning_configuration_assignment, ios_managed_app_protection, ios_managed_app_registration, ios_mobile_app_configuration, ios_store_app, ios_update_configuration, ios_update_device_status, ios_vpp_app, ios_vpp_e_book, ios_vpp_e_book_assignment, ip_named_location, item_activity, item_activity_stat, item_analytics, item_attachment, learning_content, learning_provider, license_details, linked_resource, list, list_item, list_item_version, localized_notification_message, long_running_operation, mac_o_s_compliance_policy, mac_o_s_custom_configuration, mac_o_s_device_features_configuration, mac_o_s_general_device_configuration, mac_o_s_lob_app, mac_o_s_microsoft_edge_app, mac_o_s_office_suite_app, mail_assessment_request, mail_folder, mail_search_folder, managed_android_lob_app, managed_android_store_app, managed_app, managed_app_configuration, managed_app_operation, managed_app_policy, managed_app_policy_deployment_summary, managed_app_protection, managed_app_registration, managed_app_status, managed_app_status_raw, managed_device, managed_device_mobile_app_configuration, managed_device_mobile_app_configuration_assignment, managed_device_mobile_app_configuration_device_status, managed_device_mobile_app_configuration_device_summary, managed_device_mobile_app_configuration_user_status, managed_device_mobile_app_configuration_user_summary, managed_device_overview, managed_e_book, managed_e_book_assignment, managed_i_o_s_lob_app, managed_i_o_s_store_app, managed_mobile_app, managed_mobile_lob_app, mdm_windows_information_protection_policy, meeting_attendance_report, message, message_rule, microsoft_account_user_conversation_member, microsoft_authenticator_authentication_method, microsoft_authenticator_authentication_method_configuration, microsoft_authenticator_authentication_method_target, microsoft_store_for_business_app, mobile_app, mobile_app_assignment, mobile_app_category, mobile_app_content, mobile_app_content_file, mobile_contained_app, mobile_lob_app, mobile_threat_defense_connector, multi_value_legacy_extended_property, mute_participant_operation, named_location, notebook, notification_message_template, offer_shift_request, office_graph_insights, onenote, onenote_entity_base_model, onenote_entity_hierarchy_model, onenote_entity_schema_object_model, onenote_operation, onenote_page, onenote_resource, onenote_section, online_meeting, on_premises_conditional_access_settings, on_premises_directory_synchronization, open_shift, open_shift_change_request, open_type_extension, operation, organization, organizational_branding, organizational_branding_localization, organizational_branding_properties, org_contact, outlook_category, outlook_item, outlook_user, o_auth2_permission_grant, participant, participant_joining_notification, participant_left_notification, password_authentication_method, permission, permission_grant_condition_set, permission_grant_policy, person, phone_authentication_method, pinned_chat_message_info, place, planner, planner_assigned_to_task_board_task_format, planner_bucket, planner_bucket_task_board_task_format, planner_group, planner_plan, planner_plan_details, planner_progress_task_board_task_format, planner_task, planner_task_details, planner_user, play_prompt_operation, policy_base, policy_root, post, presence, printer, printer_base, printer_create_operation, printer_share, print_connector, print_document, print_job, print_operation, print_service, print_service_endpoint, print_task, print_task_definition, print_task_trigger, print_usage, print_usage_by_printer, print_usage_by_user, profile_photo, provisioning_object_summary, rbac_application, record_operation, reference_attachment, remote_assistance_partner, request, resource_operation, resource_specific_permission_grant, rich_long_running_operation, risky_service_principal, risky_service_principal_history_item, risky_user, risky_user_history_item, risk_detection, role_assignment, role_definition, room, room_list, saml_or_ws_fed_external_domain_federation, saml_or_ws_fed_provider, schedule, schedule_change_request, scheduling_group, schema_extension, scoped_role_membership, search_entity, section_group, secure_score, secure_score_control_profile, security_reports_root, service_announcement, service_announcement_attachment, service_announcement_base, service_health, service_health_issue, service_principal, service_principal_risk_detection, service_update_message, setting_state_device_summary, shared_drive_item, shared_insight, shared_p_c_configuration, shared_with_channel_team_info, sharepoint, sharepoint_settings, shift, shift_preferences, sign_in, simulation, simulation_automation, simulation_automation_run, single_value_legacy_extended_property, site, skype_for_business_user_conversation_member, skype_user_conversation_member, sms_authentication_method_configuration, sms_authentication_method_target, social_identity_provider, software_oath_authentication_method, software_oath_authentication_method_configuration, software_update_status_summary, start_hold_music_operation, stop_hold_music_operation, sts_policy, subject_rights_request, subscribed_sku, subscribe_to_tone_operation, subscription, swap_shifts_change_request, synchronization, synchronization_job, synchronization_schema, synchronization_template, targeted_managed_app_configuration, targeted_managed_app_policy_assignment, targeted_managed_app_protection, task_file_attachment, team, teams_app, teams_app_definition, teams_app_installation, teams_async_operation, teams_tab, teams_template, teamwork, teamwork_bot, teamwork_hosted_content, teamwork_tag, teamwork_tag_member, team_info, telecom_expense_management_partner, temporary_access_pass_authentication_method, temporary_access_pass_authentication_method_configuration, tenant_app_management_policy, terms_and_conditions, terms_and_conditions_acceptance_status, terms_and_conditions_assignment, terms_of_use_container, threat_assessment_request, threat_assessment_result, thumbnail_set, time_off, time_off_reason, time_off_request, todo, todo_task, todo_task_list, token_issuance_policy, token_lifetime_policy, trending, unified_rbac_resource_action, unified_rbac_resource_namespace, unified_role_assignment, unified_role_assignment_schedule, unified_role_assignment_schedule_instance, unified_role_assignment_schedule_request, unified_role_definition, unified_role_eligibility_schedule, unified_role_eligibility_schedule_instance, unified_role_eligibility_schedule_request, unified_role_management_policy, unified_role_management_policy_approval_rule, unified_role_management_policy_assignment, unified_role_management_policy_authentication_context_rule, unified_role_management_policy_enablement_rule, unified_role_management_policy_expiration_rule, unified_role_management_policy_notification_rule, unified_role_management_policy_rule, unified_role_schedule_base, unified_role_schedule_instance_base, unmute_participant_operation, update_recording_status_operation, url_assessment_request, used_insight, user, user_activity, user_consent_request, user_experience_analytics_device_performance, user_flow_language_configuration, user_flow_language_page, user_install_state_summary, user_scope_teams_app_installation, user_settings, user_teamwork, voice_authentication_method_configuration, vpp_token, web_app, win32_lob_app, windows10_compliance_policy, windows10_custom_configuration, windows10_endpoint_protection_configuration, windows10_enterprise_modern_app_management_configuration, windows10_general_configuration, windows10_mobile_compliance_policy, windows10_secure_assessment_configuration, windows10_team_general_configuration, windows81_compliance_policy, windows81_general_configuration, windows_app_x, windows_autopilot_device_identity, windows_defender_advanced_threat_protection_configuration, windows_hello_for_business_authentication_method, windows_information_protection, windows_information_protection_app_learning_summary, windows_information_protection_app_locker_file, windows_information_protection_network_learning_summary, windows_information_protection_policy, windows_microsoft_edge_app, windows_mobile_m_s_i, windows_phone81_compliance_policy, windows_phone81_custom_configuration, windows_phone81_general_configuration, windows_universal_app_x, windows_universal_app_x_contained_app, windows_update_for_business_configuration, windows_web_app, workbook, workbook_application, workbook_chart, workbook_chart_area_format, workbook_chart_axes, workbook_chart_axis, workbook_chart_axis_format, workbook_chart_axis_title, workbook_chart_axis_title_format, workbook_chart_data_labels, workbook_chart_data_label_format, workbook_chart_fill, workbook_chart_font, workbook_chart_gridlines, workbook_chart_gridlines_format, workbook_chart_legend, workbook_chart_legend_format, workbook_chart_line_format, workbook_chart_point, workbook_chart_point_format, workbook_chart_series, workbook_chart_series_format, workbook_chart_title, workbook_chart_title_format, workbook_comment, workbook_comment_reply, workbook_filter, workbook_format_protection, workbook_functions, workbook_function_result, workbook_named_item, workbook_operation, workbook_pivot_table, workbook_range, workbook_range_border, workbook_range_fill, workbook_range_font, workbook_range_format, workbook_range_sort, workbook_range_view, workbook_table, workbook_table_column, workbook_table_row, workbook_table_sort, workbook_worksheet, workbook_worksheet_protection, workforce_integration, x509_certificate_authentication_method_configuration
        from .call_records import call_record, segment, session
        from .external_connectors import connection_operation, external_activity, external_activity_result, external_connection, external_group, external_item, identity, schema
        from .security import alert, case, cases_root, case_operation, data_set, data_source, data_source_container, ediscovery_add_to_review_set_operation, ediscovery_case, ediscovery_case_settings, ediscovery_custodian, ediscovery_estimate_operation, ediscovery_hold_operation, ediscovery_index_operation, ediscovery_noncustodial_data_source, ediscovery_purge_data_operation, ediscovery_review_set, ediscovery_review_set_query, ediscovery_review_tag, ediscovery_search, ediscovery_tag_operation, incident, retention_event, retention_event_type, search, security, site_source, tag, triggers_root, trigger_types_root, unified_group_source, user_source
        from .term_store import group, relation, set, store, term

        from . import aad_user_conversation_member, access_package, access_package_assignment, access_package_assignment_policy, access_package_assignment_request, access_package_catalog, access_package_multiple_choice_question, access_package_question, access_package_subject, access_package_text_input_question, access_review_history_definition, access_review_history_instance, access_review_instance, access_review_instance_decision_item, access_review_reviewer, access_review_schedule_definition, access_review_set, access_review_stage, activity_based_timeout_policy, activity_history_item, add_large_gallery_view_operation, administrative_unit, admin_consent_request_policy, agreement, agreement_acceptance, agreement_file, agreement_file_localization, agreement_file_properties, agreement_file_version, alert, allowed_value, android_compliance_policy, android_custom_configuration, android_general_device_configuration, android_lob_app, android_managed_app_protection, android_managed_app_registration, android_store_app, android_work_profile_compliance_policy, android_work_profile_custom_configuration, android_work_profile_general_device_configuration, anonymous_guest_conversation_member, apple_device_features_configuration_base, apple_managed_identity_provider, apple_push_notification_certificate, application, application_template, approval, approval_stage, app_catalogs, app_consent_approval_route, app_consent_request, app_management_policy, app_role_assignment, app_scope, associated_team_info, attachment, attachment_base, attachment_session, attack_simulation_root, attendance_record, attribute_mapping_function_schema, attribute_set, audio_routing_group, audit_event, audit_log_root, authentication, authentication_combination_configuration, authentication_context_class_reference, authentication_flows_policy, authentication_method, authentication_methods_policy, authentication_method_configuration, authentication_method_mode_detail, authentication_method_target, authentication_strength_policy, authentication_strength_root, authored_note, authorization_policy, azure_communication_services_user_conversation_member, b2x_identity_user_flow, base_item, base_item_version, bitlocker, bitlocker_recovery_key, booking_appointment, booking_business, booking_currency, booking_customer, booking_customer_base, booking_custom_question, booking_service, booking_staff_member, booking_staff_member_base, browser_shared_cookie, browser_site, browser_site_list, built_in_identity_provider, calendar, calendar_group, calendar_permission, calendar_sharing_message, call, cancel_media_processing_operation, certificate_based_auth_configuration, change_tracked_entity, channel, chat, chat_message, chat_message_hosted_content, chat_message_info, checklist_item, claims_mapping_policy, column_definition, column_link, comms_operation, compliance_management_partner, conditional_access_policy, conditional_access_root, conditional_access_template, connected_organization, contact, contact_folder, content_sharing_session, content_type, contract, conversation, conversation_member, conversation_thread, country_named_location, cross_tenant_access_policy, cross_tenant_access_policy_configuration_default, custom_security_attribute_definition, data_policy_operation, default_managed_app_protection, delegated_admin_access_assignment, delegated_admin_customer, delegated_admin_relationship, delegated_admin_relationship_operation, delegated_admin_relationship_request, delegated_admin_service_management_detail, delegated_permission_classification, deleted_team, detected_app, device, device_and_app_management_role_assignment, device_and_app_management_role_definition, device_app_management, device_category, device_compliance_action_item, device_compliance_device_overview, device_compliance_device_status, device_compliance_policy, device_compliance_policy_assignment, device_compliance_policy_device_state_summary, device_compliance_policy_setting_state_summary, device_compliance_policy_state, device_compliance_scheduled_action_for_rule, device_compliance_setting_state, device_compliance_user_overview, device_compliance_user_status, device_configuration, device_configuration_assignment, device_configuration_device_overview, device_configuration_device_state_summary, device_configuration_device_status, device_configuration_state, device_configuration_user_overview, device_configuration_user_status, device_enrollment_configuration, device_enrollment_limit_configuration, device_enrollment_platform_restrictions_configuration, device_enrollment_windows_hello_for_business_configuration, device_install_state, device_management, device_management_exchange_connector, device_management_export_job, device_management_partner, device_management_reports, device_management_troubleshooting_event, directory, directory_audit, directory_definition, directory_object, directory_object_partner_reference, directory_role, directory_role_template, document_set_version, domain, domain_dns_cname_record, domain_dns_mx_record, domain_dns_record, domain_dns_srv_record, domain_dns_txt_record, domain_dns_unavailable_record, drive, drive_item, drive_item_version, edge, edition_upgrade_configuration, education_assignment, education_assignment_defaults, education_assignment_resource, education_assignment_settings, education_category, education_class, education_feedback_outcome, education_feedback_resource_outcome, education_organization, education_outcome, education_points_outcome, education_rubric, education_rubric_outcome, education_school, education_submission, education_submission_resource, education_user, email_authentication_method, email_authentication_method_configuration, email_file_assessment_request, endpoint, enrollment_configuration_assignment, enrollment_troubleshooting_event, enterprise_code_signing_certificate, entitlement_management, entitlement_management_settings, event, event_message, event_message_request, event_message_response, extension, extension_property, external_domain_name, e_book_install_summary, feature_rollout_policy, federated_identity_credential, fido2_authentication_method, fido2_authentication_method_configuration, fido2_combination_configuration, field_value_set, file_assessment_request, file_attachment, filter_operator_schema, group, group_lifecycle_policy, group_setting, group_setting_template, home_realm_discovery_policy, identity_api_connector, identity_built_in_user_flow_attribute, identity_container, identity_custom_user_flow_attribute, identity_provider, identity_provider_base, identity_security_defaults_enforcement_policy, identity_user_flow, identity_user_flow_attribute, identity_user_flow_attribute_assignment, imported_windows_autopilot_device_identity, imported_windows_autopilot_device_identity_upload, inference_classification, inference_classification_override, internal_domain_federation, internet_explorer_mode, invitation, invite_participants_operation, iosi_pad_o_s_web_clip, ios_certificate_profile, ios_compliance_policy, ios_custom_configuration, ios_device_features_configuration, ios_general_device_configuration, ios_lob_app, ios_lob_app_provisioning_configuration_assignment, ios_managed_app_protection, ios_managed_app_registration, ios_mobile_app_configuration, ios_store_app, ios_update_configuration, ios_update_device_status, ios_vpp_app, ios_vpp_e_book, ios_vpp_e_book_assignment, ip_named_location, item_activity, item_activity_stat, item_analytics, item_attachment, learning_content, learning_provider, license_details, linked_resource, list, list_item, list_item_version, localized_notification_message, long_running_operation, mac_o_s_compliance_policy, mac_o_s_custom_configuration, mac_o_s_device_features_configuration, mac_o_s_general_device_configuration, mac_o_s_lob_app, mac_o_s_microsoft_edge_app, mac_o_s_office_suite_app, mail_assessment_request, mail_folder, mail_search_folder, managed_android_lob_app, managed_android_store_app, managed_app, managed_app_configuration, managed_app_operation, managed_app_policy, managed_app_policy_deployment_summary, managed_app_protection, managed_app_registration, managed_app_status, managed_app_status_raw, managed_device, managed_device_mobile_app_configuration, managed_device_mobile_app_configuration_assignment, managed_device_mobile_app_configuration_device_status, managed_device_mobile_app_configuration_device_summary, managed_device_mobile_app_configuration_user_status, managed_device_mobile_app_configuration_user_summary, managed_device_overview, managed_e_book, managed_e_book_assignment, managed_i_o_s_lob_app, managed_i_o_s_store_app, managed_mobile_app, managed_mobile_lob_app, mdm_windows_information_protection_policy, meeting_attendance_report, message, message_rule, microsoft_account_user_conversation_member, microsoft_authenticator_authentication_method, microsoft_authenticator_authentication_method_configuration, microsoft_authenticator_authentication_method_target, microsoft_store_for_business_app, mobile_app, mobile_app_assignment, mobile_app_category, mobile_app_content, mobile_app_content_file, mobile_contained_app, mobile_lob_app, mobile_threat_defense_connector, multi_value_legacy_extended_property, mute_participant_operation, named_location, notebook, notification_message_template, offer_shift_request, office_graph_insights, onenote, onenote_entity_base_model, onenote_entity_hierarchy_model, onenote_entity_schema_object_model, onenote_operation, onenote_page, onenote_resource, onenote_section, online_meeting, on_premises_conditional_access_settings, on_premises_directory_synchronization, open_shift, open_shift_change_request, open_type_extension, operation, organization, organizational_branding, organizational_branding_localization, organizational_branding_properties, org_contact, outlook_category, outlook_item, outlook_user, o_auth2_permission_grant, participant, participant_joining_notification, participant_left_notification, password_authentication_method, permission, permission_grant_condition_set, permission_grant_policy, person, phone_authentication_method, pinned_chat_message_info, place, planner, planner_assigned_to_task_board_task_format, planner_bucket, planner_bucket_task_board_task_format, planner_group, planner_plan, planner_plan_details, planner_progress_task_board_task_format, planner_task, planner_task_details, planner_user, play_prompt_operation, policy_base, policy_root, post, presence, printer, printer_base, printer_create_operation, printer_share, print_connector, print_document, print_job, print_operation, print_service, print_service_endpoint, print_task, print_task_definition, print_task_trigger, print_usage, print_usage_by_printer, print_usage_by_user, profile_photo, provisioning_object_summary, rbac_application, record_operation, reference_attachment, remote_assistance_partner, request, resource_operation, resource_specific_permission_grant, rich_long_running_operation, risky_service_principal, risky_service_principal_history_item, risky_user, risky_user_history_item, risk_detection, role_assignment, role_definition, room, room_list, saml_or_ws_fed_external_domain_federation, saml_or_ws_fed_provider, schedule, schedule_change_request, scheduling_group, schema_extension, scoped_role_membership, search_entity, section_group, secure_score, secure_score_control_profile, security_reports_root, service_announcement, service_announcement_attachment, service_announcement_base, service_health, service_health_issue, service_principal, service_principal_risk_detection, service_update_message, setting_state_device_summary, shared_drive_item, shared_insight, shared_p_c_configuration, shared_with_channel_team_info, sharepoint, sharepoint_settings, shift, shift_preferences, sign_in, simulation, simulation_automation, simulation_automation_run, single_value_legacy_extended_property, site, skype_for_business_user_conversation_member, skype_user_conversation_member, sms_authentication_method_configuration, sms_authentication_method_target, social_identity_provider, software_oath_authentication_method, software_oath_authentication_method_configuration, software_update_status_summary, start_hold_music_operation, stop_hold_music_operation, sts_policy, subject_rights_request, subscribed_sku, subscribe_to_tone_operation, subscription, swap_shifts_change_request, synchronization, synchronization_job, synchronization_schema, synchronization_template, targeted_managed_app_configuration, targeted_managed_app_policy_assignment, targeted_managed_app_protection, task_file_attachment, team, teams_app, teams_app_definition, teams_app_installation, teams_async_operation, teams_tab, teams_template, teamwork, teamwork_bot, teamwork_hosted_content, teamwork_tag, teamwork_tag_member, team_info, telecom_expense_management_partner, temporary_access_pass_authentication_method, temporary_access_pass_authentication_method_configuration, tenant_app_management_policy, terms_and_conditions, terms_and_conditions_acceptance_status, terms_and_conditions_assignment, terms_of_use_container, threat_assessment_request, threat_assessment_result, thumbnail_set, time_off, time_off_reason, time_off_request, todo, todo_task, todo_task_list, token_issuance_policy, token_lifetime_policy, trending, unified_rbac_resource_action, unified_rbac_resource_namespace, unified_role_assignment, unified_role_assignment_schedule, unified_role_assignment_schedule_instance, unified_role_assignment_schedule_request, unified_role_definition, unified_role_eligibility_schedule, unified_role_eligibility_schedule_instance, unified_role_eligibility_schedule_request, unified_role_management_policy, unified_role_management_policy_approval_rule, unified_role_management_policy_assignment, unified_role_management_policy_authentication_context_rule, unified_role_management_policy_enablement_rule, unified_role_management_policy_expiration_rule, unified_role_management_policy_notification_rule, unified_role_management_policy_rule, unified_role_schedule_base, unified_role_schedule_instance_base, unmute_participant_operation, update_recording_status_operation, url_assessment_request, used_insight, user, user_activity, user_consent_request, user_experience_analytics_device_performance, user_flow_language_configuration, user_flow_language_page, user_install_state_summary, user_scope_teams_app_installation, user_settings, user_teamwork, voice_authentication_method_configuration, vpp_token, web_app, win32_lob_app, windows10_compliance_policy, windows10_custom_configuration, windows10_endpoint_protection_configuration, windows10_enterprise_modern_app_management_configuration, windows10_general_configuration, windows10_mobile_compliance_policy, windows10_secure_assessment_configuration, windows10_team_general_configuration, windows81_compliance_policy, windows81_general_configuration, windows_app_x, windows_autopilot_device_identity, windows_defender_advanced_threat_protection_configuration, windows_hello_for_business_authentication_method, windows_information_protection, windows_information_protection_app_learning_summary, windows_information_protection_app_locker_file, windows_information_protection_network_learning_summary, windows_information_protection_policy, windows_microsoft_edge_app, windows_mobile_m_s_i, windows_phone81_compliance_policy, windows_phone81_custom_configuration, windows_phone81_general_configuration, windows_universal_app_x, windows_universal_app_x_contained_app, windows_update_for_business_configuration, windows_web_app, workbook, workbook_application, workbook_chart, workbook_chart_area_format, workbook_chart_axes, workbook_chart_axis, workbook_chart_axis_format, workbook_chart_axis_title, workbook_chart_axis_title_format, workbook_chart_data_labels, workbook_chart_data_label_format, workbook_chart_fill, workbook_chart_font, workbook_chart_gridlines, workbook_chart_gridlines_format, workbook_chart_legend, workbook_chart_legend_format, workbook_chart_line_format, workbook_chart_point, workbook_chart_point_format, workbook_chart_series, workbook_chart_series_format, workbook_chart_title, workbook_chart_title_format, workbook_comment, workbook_comment_reply, workbook_filter, workbook_format_protection, workbook_functions, workbook_function_result, workbook_named_item, workbook_operation, workbook_pivot_table, workbook_range, workbook_range_border, workbook_range_fill, workbook_range_font, workbook_range_format, workbook_range_sort, workbook_range_view, workbook_table, workbook_table_column, workbook_table_row, workbook_table_sort, workbook_worksheet, workbook_worksheet_protection, workforce_integration, x509_certificate_authentication_method_configuration
        from .call_records import call_record, segment, session
        from .external_connectors import connection_operation, external_activity, external_activity_result, external_connection, external_group, external_item, identity, schema
        from .security import alert, case, cases_root, case_operation, data_set, data_source, data_source_container, ediscovery_add_to_review_set_operation, ediscovery_case, ediscovery_case_settings, ediscovery_custodian, ediscovery_estimate_operation, ediscovery_hold_operation, ediscovery_index_operation, ediscovery_noncustodial_data_source, ediscovery_purge_data_operation, ediscovery_review_set, ediscovery_review_set_query, ediscovery_review_tag, ediscovery_search, ediscovery_tag_operation, incident, retention_event, retention_event_type, search, security, site_source, tag, triggers_root, trigger_types_root, unified_group_source, user_source
        from .term_store import group, relation, set, store, term

        fields: Dict[str, Callable[[Any], None]] = {
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("id", self.id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

