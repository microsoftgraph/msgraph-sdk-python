from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .......models import workbook_functions
    from .......models.o_data_errors import o_data_error
    from .abs import abs_request_builder
    from .accr_int import accr_int_request_builder
    from .accr_int_m import accr_int_m_request_builder
    from .acos import acos_request_builder
    from .acosh import acosh_request_builder
    from .acot import acot_request_builder
    from .acoth import acoth_request_builder
    from .amor_degrc import amor_degrc_request_builder
    from .amor_linc import amor_linc_request_builder
    from .and_ import and_request_builder
    from .arabic import arabic_request_builder
    from .areas import areas_request_builder
    from .asc import asc_request_builder
    from .asin import asin_request_builder
    from .asinh import asinh_request_builder
    from .atan import atan_request_builder
    from .atan2 import atan2_request_builder
    from .atanh import atanh_request_builder
    from .ave_dev import ave_dev_request_builder
    from .average import average_request_builder
    from .average_a import average_a_request_builder
    from .average_if import average_if_request_builder
    from .average_ifs import average_ifs_request_builder
    from .baht_text import baht_text_request_builder
    from .base import base_request_builder
    from .bessel_i import bessel_i_request_builder
    from .bessel_j import bessel_j_request_builder
    from .bessel_k import bessel_k_request_builder
    from .bessel_y import bessel_y_request_builder
    from .beta_dist import beta_dist_request_builder
    from .beta_inv import beta_inv_request_builder
    from .bin2_dec import bin2_dec_request_builder
    from .bin2_hex import bin2_hex_request_builder
    from .bin2_oct import bin2_oct_request_builder
    from .binom_dist import binom_dist_request_builder
    from .binom_dist_range import binom_dist_range_request_builder
    from .binom_inv import binom_inv_request_builder
    from .bitand import bitand_request_builder
    from .bitlshift import bitlshift_request_builder
    from .bitor import bitor_request_builder
    from .bitrshift import bitrshift_request_builder
    from .bitxor import bitxor_request_builder
    from .ceiling_math import ceiling_math_request_builder
    from .ceiling_precise import ceiling_precise_request_builder
    from .char import char_request_builder
    from .chi_sq_dist import chi_sq_dist_request_builder
    from .chi_sq_dist_r_t import chi_sq_dist_r_t_request_builder
    from .chi_sq_inv import chi_sq_inv_request_builder
    from .chi_sq_inv_r_t import chi_sq_inv_r_t_request_builder
    from .choose import choose_request_builder
    from .clean import clean_request_builder
    from .code import code_request_builder
    from .columns import columns_request_builder
    from .combin import combin_request_builder
    from .combina import combina_request_builder
    from .complex import complex_request_builder
    from .concatenate import concatenate_request_builder
    from .confidence_norm import confidence_norm_request_builder
    from .confidence_t import confidence_t_request_builder
    from .convert import convert_request_builder
    from .cos import cos_request_builder
    from .cosh import cosh_request_builder
    from .cot import cot_request_builder
    from .coth import coth_request_builder
    from .count import count_request_builder
    from .count_a import count_a_request_builder
    from .count_blank import count_blank_request_builder
    from .count_if import count_if_request_builder
    from .count_ifs import count_ifs_request_builder
    from .coup_day_bs import coup_day_bs_request_builder
    from .coup_days import coup_days_request_builder
    from .coup_days_nc import coup_days_nc_request_builder
    from .coup_ncd import coup_ncd_request_builder
    from .coup_num import coup_num_request_builder
    from .coup_pcd import coup_pcd_request_builder
    from .csc import csc_request_builder
    from .csch import csch_request_builder
    from .cum_i_pmt import cum_i_pmt_request_builder
    from .cum_princ import cum_princ_request_builder
    from .date import date_request_builder
    from .datevalue import datevalue_request_builder
    from .daverage import daverage_request_builder
    from .day import day_request_builder
    from .days import days_request_builder
    from .days360 import days360_request_builder
    from .db import db_request_builder
    from .dbcs import dbcs_request_builder
    from .dcount import dcount_request_builder
    from .dcount_a import dcount_a_request_builder
    from .ddb import ddb_request_builder
    from .dec2_bin import dec2_bin_request_builder
    from .dec2_hex import dec2_hex_request_builder
    from .dec2_oct import dec2_oct_request_builder
    from .decimal import decimal_request_builder
    from .degrees import degrees_request_builder
    from .delta import delta_request_builder
    from .dev_sq import dev_sq_request_builder
    from .dget import dget_request_builder
    from .disc import disc_request_builder
    from .dmax import dmax_request_builder
    from .dmin import dmin_request_builder
    from .dollar import dollar_request_builder
    from .dollar_de import dollar_de_request_builder
    from .dollar_fr import dollar_fr_request_builder
    from .dproduct import dproduct_request_builder
    from .dst_dev import dst_dev_request_builder
    from .dst_dev_p import dst_dev_p_request_builder
    from .dsum import dsum_request_builder
    from .duration import duration_request_builder
    from .dvar import dvar_request_builder
    from .dvar_p import dvar_p_request_builder
    from .ecma_ceiling import ecma_ceiling_request_builder
    from .edate import edate_request_builder
    from .effect import effect_request_builder
    from .eo_month import eo_month_request_builder
    from .erf import erf_request_builder
    from .erf_c import erf_c_request_builder
    from .erf_c_precise import erf_c_precise_request_builder
    from .erf_precise import erf_precise_request_builder
    from .error_type import error_type_request_builder
    from .even import even_request_builder
    from .exact import exact_request_builder
    from .exp import exp_request_builder
    from .expon_dist import expon_dist_request_builder
    from .fact import fact_request_builder
    from .fact_double import fact_double_request_builder
    from .false_ import false_request_builder
    from .find import find_request_builder
    from .find_b import find_b_request_builder
    from .fisher import fisher_request_builder
    from .fisher_inv import fisher_inv_request_builder
    from .fixed import fixed_request_builder
    from .floor_math import floor_math_request_builder
    from .floor_precise import floor_precise_request_builder
    from .fv import fv_request_builder
    from .fvschedule import fvschedule_request_builder
    from .f_dist import f_dist_request_builder
    from .f_dist_r_t import f_dist_r_t_request_builder
    from .f_inv import f_inv_request_builder
    from .f_inv_r_t import f_inv_r_t_request_builder
    from .gamma import gamma_request_builder
    from .gamma_ln import gamma_ln_request_builder
    from .gamma_ln_precise import gamma_ln_precise_request_builder
    from .gamma_dist import gamma_dist_request_builder
    from .gamma_inv import gamma_inv_request_builder
    from .gauss import gauss_request_builder
    from .gcd import gcd_request_builder
    from .geo_mean import geo_mean_request_builder
    from .ge_step import ge_step_request_builder
    from .har_mean import har_mean_request_builder
    from .hex2_bin import hex2_bin_request_builder
    from .hex2_dec import hex2_dec_request_builder
    from .hex2_oct import hex2_oct_request_builder
    from .hlookup import hlookup_request_builder
    from .hour import hour_request_builder
    from .hyperlink import hyperlink_request_builder
    from .hyp_geom_dist import hyp_geom_dist_request_builder
    from .if_ import if_request_builder
    from .im_abs import im_abs_request_builder
    from .imaginary import imaginary_request_builder
    from .im_argument import im_argument_request_builder
    from .im_conjugate import im_conjugate_request_builder
    from .im_cos import im_cos_request_builder
    from .im_cosh import im_cosh_request_builder
    from .im_cot import im_cot_request_builder
    from .im_csc import im_csc_request_builder
    from .im_csch import im_csch_request_builder
    from .im_div import im_div_request_builder
    from .im_exp import im_exp_request_builder
    from .im_ln import im_ln_request_builder
    from .im_log10 import im_log10_request_builder
    from .im_log2 import im_log2_request_builder
    from .im_power import im_power_request_builder
    from .im_product import im_product_request_builder
    from .im_real import im_real_request_builder
    from .im_sec import im_sec_request_builder
    from .im_sech import im_sech_request_builder
    from .im_sin import im_sin_request_builder
    from .im_sinh import im_sinh_request_builder
    from .im_sqrt import im_sqrt_request_builder
    from .im_sub import im_sub_request_builder
    from .im_sum import im_sum_request_builder
    from .im_tan import im_tan_request_builder
    from .int import int_request_builder
    from .int_rate import int_rate_request_builder
    from .ipmt import ipmt_request_builder
    from .irr import irr_request_builder
    from .is_err import is_err_request_builder
    from .is_error import is_error_request_builder
    from .is_even import is_even_request_builder
    from .is_formula import is_formula_request_builder
    from .is_logical import is_logical_request_builder
    from .is_n_a import is_n_a_request_builder
    from .is_non_text import is_non_text_request_builder
    from .is_number import is_number_request_builder
    from .is_odd import is_odd_request_builder
    from .iso_week_num import iso_week_num_request_builder
    from .iso_ceiling import iso_ceiling_request_builder
    from .ispmt import ispmt_request_builder
    from .isref import isref_request_builder
    from .is_text import is_text_request_builder
    from .kurt import kurt_request_builder
    from .large import large_request_builder
    from .lcm import lcm_request_builder
    from .left import left_request_builder
    from .leftb import leftb_request_builder
    from .len import len_request_builder
    from .lenb import lenb_request_builder
    from .ln import ln_request_builder
    from .log import log_request_builder
    from .log10 import log10_request_builder
    from .log_norm_dist import log_norm_dist_request_builder
    from .log_norm_inv import log_norm_inv_request_builder
    from .lookup import lookup_request_builder
    from .lower import lower_request_builder
    from .match import match_request_builder
    from .max import max_request_builder
    from .max_a import max_a_request_builder
    from .mduration import mduration_request_builder
    from .median import median_request_builder
    from .mid import mid_request_builder
    from .midb import midb_request_builder
    from .min import min_request_builder
    from .min_a import min_a_request_builder
    from .minute import minute_request_builder
    from .mirr import mirr_request_builder
    from .mod import mod_request_builder
    from .month import month_request_builder
    from .mround import mround_request_builder
    from .multi_nomial import multi_nomial_request_builder
    from .n import n_request_builder
    from .na import na_request_builder
    from .neg_binom_dist import neg_binom_dist_request_builder
    from .network_days import network_days_request_builder
    from .network_days_intl import network_days_intl_request_builder
    from .nominal import nominal_request_builder
    from .norm_dist import norm_dist_request_builder
    from .norm_inv import norm_inv_request_builder
    from .norm_s_dist import norm_s_dist_request_builder
    from .norm_s_inv import norm_s_inv_request_builder
    from .not_ import not_request_builder
    from .now import now_request_builder
    from .nper import nper_request_builder
    from .npv import npv_request_builder
    from .number_value import number_value_request_builder
    from .oct2_bin import oct2_bin_request_builder
    from .oct2_dec import oct2_dec_request_builder
    from .oct2_hex import oct2_hex_request_builder
    from .odd import odd_request_builder
    from .odd_f_price import odd_f_price_request_builder
    from .odd_f_yield import odd_f_yield_request_builder
    from .odd_l_price import odd_l_price_request_builder
    from .odd_l_yield import odd_l_yield_request_builder
    from .or_ import or_request_builder
    from .pduration import pduration_request_builder
    from .percentile_exc import percentile_exc_request_builder
    from .percentile_inc import percentile_inc_request_builder
    from .percent_rank_exc import percent_rank_exc_request_builder
    from .percent_rank_inc import percent_rank_inc_request_builder
    from .permut import permut_request_builder
    from .permutationa import permutationa_request_builder
    from .phi import phi_request_builder
    from .pi import pi_request_builder
    from .pmt import pmt_request_builder
    from .poisson_dist import poisson_dist_request_builder
    from .power import power_request_builder
    from .ppmt import ppmt_request_builder
    from .price import price_request_builder
    from .price_disc import price_disc_request_builder
    from .price_mat import price_mat_request_builder
    from .product import product_request_builder
    from .proper import proper_request_builder
    from .pv import pv_request_builder
    from .quartile_exc import quartile_exc_request_builder
    from .quartile_inc import quartile_inc_request_builder
    from .quotient import quotient_request_builder
    from .radians import radians_request_builder
    from .rand import rand_request_builder
    from .rand_between import rand_between_request_builder
    from .rank_avg import rank_avg_request_builder
    from .rank_eq import rank_eq_request_builder
    from .rate import rate_request_builder
    from .received import received_request_builder
    from .replace import replace_request_builder
    from .replace_b import replace_b_request_builder
    from .rept import rept_request_builder
    from .right import right_request_builder
    from .rightb import rightb_request_builder
    from .roman import roman_request_builder
    from .round import round_request_builder
    from .round_down import round_down_request_builder
    from .round_up import round_up_request_builder
    from .rows import rows_request_builder
    from .rri import rri_request_builder
    from .sec import sec_request_builder
    from .sech import sech_request_builder
    from .second import second_request_builder
    from .series_sum import series_sum_request_builder
    from .sheet import sheet_request_builder
    from .sheets import sheets_request_builder
    from .sign import sign_request_builder
    from .sin import sin_request_builder
    from .sinh import sinh_request_builder
    from .skew import skew_request_builder
    from .skew_p import skew_p_request_builder
    from .sln import sln_request_builder
    from .small import small_request_builder
    from .sqrt import sqrt_request_builder
    from .sqrt_pi import sqrt_pi_request_builder
    from .standardize import standardize_request_builder
    from .st_dev_a import st_dev_a_request_builder
    from .st_dev_p_a import st_dev_p_a_request_builder
    from .st_dev_p import st_dev_p_request_builder
    from .st_dev_s import st_dev_s_request_builder
    from .substitute import substitute_request_builder
    from .subtotal import subtotal_request_builder
    from .sum import sum_request_builder
    from .sum_if import sum_if_request_builder
    from .sum_ifs import sum_ifs_request_builder
    from .sum_sq import sum_sq_request_builder
    from .syd import syd_request_builder
    from .t import t_request_builder
    from .tan import tan_request_builder
    from .tanh import tanh_request_builder
    from .tbill_eq import tbill_eq_request_builder
    from .tbill_price import tbill_price_request_builder
    from .tbill_yield import tbill_yield_request_builder
    from .text import text_request_builder
    from .time import time_request_builder
    from .timevalue import timevalue_request_builder
    from .today import today_request_builder
    from .trim import trim_request_builder
    from .trim_mean import trim_mean_request_builder
    from .true_ import true_request_builder
    from .trunc import trunc_request_builder
    from .type import type_request_builder
    from .t_dist import t_dist_request_builder
    from .t_dist_2_t import t_dist_2_t_request_builder
    from .t_dist_r_t import t_dist_r_t_request_builder
    from .t_inv import t_inv_request_builder
    from .t_inv_2_t import t_inv_2_t_request_builder
    from .unichar import unichar_request_builder
    from .unicode import unicode_request_builder
    from .upper import upper_request_builder
    from .usdollar import usdollar_request_builder
    from .value import value_request_builder
    from .var_a import var_a_request_builder
    from .var_p_a import var_p_a_request_builder
    from .var_p import var_p_request_builder
    from .var_s import var_s_request_builder
    from .vdb import vdb_request_builder
    from .vlookup import vlookup_request_builder
    from .weekday import weekday_request_builder
    from .week_num import week_num_request_builder
    from .weibull_dist import weibull_dist_request_builder
    from .work_day import work_day_request_builder
    from .work_day_intl import work_day_intl_request_builder
    from .xirr import xirr_request_builder
    from .xnpv import xnpv_request_builder
    from .xor import xor_request_builder
    from .year import year_request_builder
    from .year_frac import year_frac_request_builder
    from .yield_disc import yield_disc_request_builder
    from .yield_mat import yield_mat_request_builder
    from .yield_ import yield_request_builder
    from .z_test import z_test_request_builder

class FunctionsRequestBuilder():
    """
    Provides operations to manage the functions property of the microsoft.graph.workbook entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new FunctionsRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/drives/{drive%2Did}/items/{driveItem%2Did}/workbook/functions{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[FunctionsRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property functions for drives
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .......models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[FunctionsRequestBuilderGetRequestConfiguration] = None) -> Optional[workbook_functions.WorkbookFunctions]:
        """
        Get functions from drives
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[workbook_functions.WorkbookFunctions]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .......models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .......models import workbook_functions

        return await self.request_adapter.send_async(request_info, workbook_functions.WorkbookFunctions, error_mapping)
    
    async def patch(self,body: Optional[workbook_functions.WorkbookFunctions] = None, request_configuration: Optional[FunctionsRequestBuilderPatchRequestConfiguration] = None) -> Optional[workbook_functions.WorkbookFunctions]:
        """
        Update the navigation property functions in drives
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[workbook_functions.WorkbookFunctions]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .......models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .......models import workbook_functions

        return await self.request_adapter.send_async(request_info, workbook_functions.WorkbookFunctions, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[FunctionsRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property functions for drives
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.DELETE
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[FunctionsRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get functions from drives
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def to_patch_request_information(self,body: Optional[workbook_functions.WorkbookFunctions] = None, request_configuration: Optional[FunctionsRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property functions in drives
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PATCH
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    @property
    def abs(self) -> abs_request_builder.AbsRequestBuilder:
        """
        Provides operations to call the abs method.
        """
        from .abs import abs_request_builder

        return abs_request_builder.AbsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def accr_int(self) -> accr_int_request_builder.AccrIntRequestBuilder:
        """
        Provides operations to call the accrInt method.
        """
        from .accr_int import accr_int_request_builder

        return accr_int_request_builder.AccrIntRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def accr_int_m(self) -> accr_int_m_request_builder.AccrIntMRequestBuilder:
        """
        Provides operations to call the accrIntM method.
        """
        from .accr_int_m import accr_int_m_request_builder

        return accr_int_m_request_builder.AccrIntMRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def acos(self) -> acos_request_builder.AcosRequestBuilder:
        """
        Provides operations to call the acos method.
        """
        from .acos import acos_request_builder

        return acos_request_builder.AcosRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def acosh(self) -> acosh_request_builder.AcoshRequestBuilder:
        """
        Provides operations to call the acosh method.
        """
        from .acosh import acosh_request_builder

        return acosh_request_builder.AcoshRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def acot(self) -> acot_request_builder.AcotRequestBuilder:
        """
        Provides operations to call the acot method.
        """
        from .acot import acot_request_builder

        return acot_request_builder.AcotRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def acoth(self) -> acoth_request_builder.AcothRequestBuilder:
        """
        Provides operations to call the acoth method.
        """
        from .acoth import acoth_request_builder

        return acoth_request_builder.AcothRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def amor_degrc(self) -> amor_degrc_request_builder.AmorDegrcRequestBuilder:
        """
        Provides operations to call the amorDegrc method.
        """
        from .amor_degrc import amor_degrc_request_builder

        return amor_degrc_request_builder.AmorDegrcRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def amor_linc(self) -> amor_linc_request_builder.AmorLincRequestBuilder:
        """
        Provides operations to call the amorLinc method.
        """
        from .amor_linc import amor_linc_request_builder

        return amor_linc_request_builder.AmorLincRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def and_(self) -> and_request_builder.AndRequestBuilder:
        """
        Provides operations to call the and method.
        """
        from .and_ import and_request_builder

        return and_request_builder.AndRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def arabic(self) -> arabic_request_builder.ArabicRequestBuilder:
        """
        Provides operations to call the arabic method.
        """
        from .arabic import arabic_request_builder

        return arabic_request_builder.ArabicRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def areas(self) -> areas_request_builder.AreasRequestBuilder:
        """
        Provides operations to call the areas method.
        """
        from .areas import areas_request_builder

        return areas_request_builder.AreasRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def asc(self) -> asc_request_builder.AscRequestBuilder:
        """
        Provides operations to call the asc method.
        """
        from .asc import asc_request_builder

        return asc_request_builder.AscRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def asin(self) -> asin_request_builder.AsinRequestBuilder:
        """
        Provides operations to call the asin method.
        """
        from .asin import asin_request_builder

        return asin_request_builder.AsinRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def asinh(self) -> asinh_request_builder.AsinhRequestBuilder:
        """
        Provides operations to call the asinh method.
        """
        from .asinh import asinh_request_builder

        return asinh_request_builder.AsinhRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def atan(self) -> atan_request_builder.AtanRequestBuilder:
        """
        Provides operations to call the atan method.
        """
        from .atan import atan_request_builder

        return atan_request_builder.AtanRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def atan2(self) -> atan2_request_builder.Atan2RequestBuilder:
        """
        Provides operations to call the atan2 method.
        """
        from .atan2 import atan2_request_builder

        return atan2_request_builder.Atan2RequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def atanh(self) -> atanh_request_builder.AtanhRequestBuilder:
        """
        Provides operations to call the atanh method.
        """
        from .atanh import atanh_request_builder

        return atanh_request_builder.AtanhRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def ave_dev(self) -> ave_dev_request_builder.AveDevRequestBuilder:
        """
        Provides operations to call the aveDev method.
        """
        from .ave_dev import ave_dev_request_builder

        return ave_dev_request_builder.AveDevRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def average(self) -> average_request_builder.AverageRequestBuilder:
        """
        Provides operations to call the average method.
        """
        from .average import average_request_builder

        return average_request_builder.AverageRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def average_a(self) -> average_a_request_builder.AverageARequestBuilder:
        """
        Provides operations to call the averageA method.
        """
        from .average_a import average_a_request_builder

        return average_a_request_builder.AverageARequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def average_if(self) -> average_if_request_builder.AverageIfRequestBuilder:
        """
        Provides operations to call the averageIf method.
        """
        from .average_if import average_if_request_builder

        return average_if_request_builder.AverageIfRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def average_ifs(self) -> average_ifs_request_builder.AverageIfsRequestBuilder:
        """
        Provides operations to call the averageIfs method.
        """
        from .average_ifs import average_ifs_request_builder

        return average_ifs_request_builder.AverageIfsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def baht_text(self) -> baht_text_request_builder.BahtTextRequestBuilder:
        """
        Provides operations to call the bahtText method.
        """
        from .baht_text import baht_text_request_builder

        return baht_text_request_builder.BahtTextRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def base(self) -> base_request_builder.BaseRequestBuilder:
        """
        Provides operations to call the base method.
        """
        from .base import base_request_builder

        return base_request_builder.BaseRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def bessel_i(self) -> bessel_i_request_builder.BesselIRequestBuilder:
        """
        Provides operations to call the besselI method.
        """
        from .bessel_i import bessel_i_request_builder

        return bessel_i_request_builder.BesselIRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def bessel_j(self) -> bessel_j_request_builder.BesselJRequestBuilder:
        """
        Provides operations to call the besselJ method.
        """
        from .bessel_j import bessel_j_request_builder

        return bessel_j_request_builder.BesselJRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def bessel_k(self) -> bessel_k_request_builder.BesselKRequestBuilder:
        """
        Provides operations to call the besselK method.
        """
        from .bessel_k import bessel_k_request_builder

        return bessel_k_request_builder.BesselKRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def bessel_y(self) -> bessel_y_request_builder.BesselYRequestBuilder:
        """
        Provides operations to call the besselY method.
        """
        from .bessel_y import bessel_y_request_builder

        return bessel_y_request_builder.BesselYRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def beta_dist(self) -> beta_dist_request_builder.Beta_DistRequestBuilder:
        """
        Provides operations to call the beta_Dist method.
        """
        from .beta_dist import beta_dist_request_builder

        return beta_dist_request_builder.Beta_DistRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def beta_inv(self) -> beta_inv_request_builder.Beta_InvRequestBuilder:
        """
        Provides operations to call the beta_Inv method.
        """
        from .beta_inv import beta_inv_request_builder

        return beta_inv_request_builder.Beta_InvRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def bin2_dec(self) -> bin2_dec_request_builder.Bin2DecRequestBuilder:
        """
        Provides operations to call the bin2Dec method.
        """
        from .bin2_dec import bin2_dec_request_builder

        return bin2_dec_request_builder.Bin2DecRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def bin2_hex(self) -> bin2_hex_request_builder.Bin2HexRequestBuilder:
        """
        Provides operations to call the bin2Hex method.
        """
        from .bin2_hex import bin2_hex_request_builder

        return bin2_hex_request_builder.Bin2HexRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def bin2_oct(self) -> bin2_oct_request_builder.Bin2OctRequestBuilder:
        """
        Provides operations to call the bin2Oct method.
        """
        from .bin2_oct import bin2_oct_request_builder

        return bin2_oct_request_builder.Bin2OctRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def binom_dist(self) -> binom_dist_request_builder.Binom_DistRequestBuilder:
        """
        Provides operations to call the binom_Dist method.
        """
        from .binom_dist import binom_dist_request_builder

        return binom_dist_request_builder.Binom_DistRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def binom_dist_range(self) -> binom_dist_range_request_builder.Binom_Dist_RangeRequestBuilder:
        """
        Provides operations to call the binom_Dist_Range method.
        """
        from .binom_dist_range import binom_dist_range_request_builder

        return binom_dist_range_request_builder.Binom_Dist_RangeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def binom_inv(self) -> binom_inv_request_builder.Binom_InvRequestBuilder:
        """
        Provides operations to call the binom_Inv method.
        """
        from .binom_inv import binom_inv_request_builder

        return binom_inv_request_builder.Binom_InvRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def bitand(self) -> bitand_request_builder.BitandRequestBuilder:
        """
        Provides operations to call the bitand method.
        """
        from .bitand import bitand_request_builder

        return bitand_request_builder.BitandRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def bitlshift(self) -> bitlshift_request_builder.BitlshiftRequestBuilder:
        """
        Provides operations to call the bitlshift method.
        """
        from .bitlshift import bitlshift_request_builder

        return bitlshift_request_builder.BitlshiftRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def bitor(self) -> bitor_request_builder.BitorRequestBuilder:
        """
        Provides operations to call the bitor method.
        """
        from .bitor import bitor_request_builder

        return bitor_request_builder.BitorRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def bitrshift(self) -> bitrshift_request_builder.BitrshiftRequestBuilder:
        """
        Provides operations to call the bitrshift method.
        """
        from .bitrshift import bitrshift_request_builder

        return bitrshift_request_builder.BitrshiftRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def bitxor(self) -> bitxor_request_builder.BitxorRequestBuilder:
        """
        Provides operations to call the bitxor method.
        """
        from .bitxor import bitxor_request_builder

        return bitxor_request_builder.BitxorRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def ceiling_math(self) -> ceiling_math_request_builder.Ceiling_MathRequestBuilder:
        """
        Provides operations to call the ceiling_Math method.
        """
        from .ceiling_math import ceiling_math_request_builder

        return ceiling_math_request_builder.Ceiling_MathRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def ceiling_precise(self) -> ceiling_precise_request_builder.Ceiling_PreciseRequestBuilder:
        """
        Provides operations to call the ceiling_Precise method.
        """
        from .ceiling_precise import ceiling_precise_request_builder

        return ceiling_precise_request_builder.Ceiling_PreciseRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def char(self) -> char_request_builder.CharRequestBuilder:
        """
        Provides operations to call the char method.
        """
        from .char import char_request_builder

        return char_request_builder.CharRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def chi_sq_dist(self) -> chi_sq_dist_request_builder.ChiSq_DistRequestBuilder:
        """
        Provides operations to call the chiSq_Dist method.
        """
        from .chi_sq_dist import chi_sq_dist_request_builder

        return chi_sq_dist_request_builder.ChiSq_DistRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def chi_sq_dist_r_t(self) -> chi_sq_dist_r_t_request_builder.ChiSq_Dist_RTRequestBuilder:
        """
        Provides operations to call the chiSq_Dist_RT method.
        """
        from .chi_sq_dist_r_t import chi_sq_dist_r_t_request_builder

        return chi_sq_dist_r_t_request_builder.ChiSq_Dist_RTRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def chi_sq_inv(self) -> chi_sq_inv_request_builder.ChiSq_InvRequestBuilder:
        """
        Provides operations to call the chiSq_Inv method.
        """
        from .chi_sq_inv import chi_sq_inv_request_builder

        return chi_sq_inv_request_builder.ChiSq_InvRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def chi_sq_inv_r_t(self) -> chi_sq_inv_r_t_request_builder.ChiSq_Inv_RTRequestBuilder:
        """
        Provides operations to call the chiSq_Inv_RT method.
        """
        from .chi_sq_inv_r_t import chi_sq_inv_r_t_request_builder

        return chi_sq_inv_r_t_request_builder.ChiSq_Inv_RTRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def choose(self) -> choose_request_builder.ChooseRequestBuilder:
        """
        Provides operations to call the choose method.
        """
        from .choose import choose_request_builder

        return choose_request_builder.ChooseRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def clean(self) -> clean_request_builder.CleanRequestBuilder:
        """
        Provides operations to call the clean method.
        """
        from .clean import clean_request_builder

        return clean_request_builder.CleanRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def code(self) -> code_request_builder.CodeRequestBuilder:
        """
        Provides operations to call the code method.
        """
        from .code import code_request_builder

        return code_request_builder.CodeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def columns(self) -> columns_request_builder.ColumnsRequestBuilder:
        """
        Provides operations to call the columns method.
        """
        from .columns import columns_request_builder

        return columns_request_builder.ColumnsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def combin(self) -> combin_request_builder.CombinRequestBuilder:
        """
        Provides operations to call the combin method.
        """
        from .combin import combin_request_builder

        return combin_request_builder.CombinRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def combina(self) -> combina_request_builder.CombinaRequestBuilder:
        """
        Provides operations to call the combina method.
        """
        from .combina import combina_request_builder

        return combina_request_builder.CombinaRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def complex(self) -> complex_request_builder.ComplexRequestBuilder:
        """
        Provides operations to call the complex method.
        """
        from .complex import complex_request_builder

        return complex_request_builder.ComplexRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def concatenate(self) -> concatenate_request_builder.ConcatenateRequestBuilder:
        """
        Provides operations to call the concatenate method.
        """
        from .concatenate import concatenate_request_builder

        return concatenate_request_builder.ConcatenateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def confidence_norm(self) -> confidence_norm_request_builder.Confidence_NormRequestBuilder:
        """
        Provides operations to call the confidence_Norm method.
        """
        from .confidence_norm import confidence_norm_request_builder

        return confidence_norm_request_builder.Confidence_NormRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def confidence_t(self) -> confidence_t_request_builder.Confidence_TRequestBuilder:
        """
        Provides operations to call the confidence_T method.
        """
        from .confidence_t import confidence_t_request_builder

        return confidence_t_request_builder.Confidence_TRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def convert(self) -> convert_request_builder.ConvertRequestBuilder:
        """
        Provides operations to call the convert method.
        """
        from .convert import convert_request_builder

        return convert_request_builder.ConvertRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def cos(self) -> cos_request_builder.CosRequestBuilder:
        """
        Provides operations to call the cos method.
        """
        from .cos import cos_request_builder

        return cos_request_builder.CosRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def cosh(self) -> cosh_request_builder.CoshRequestBuilder:
        """
        Provides operations to call the cosh method.
        """
        from .cosh import cosh_request_builder

        return cosh_request_builder.CoshRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def cot(self) -> cot_request_builder.CotRequestBuilder:
        """
        Provides operations to call the cot method.
        """
        from .cot import cot_request_builder

        return cot_request_builder.CotRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def coth(self) -> coth_request_builder.CothRequestBuilder:
        """
        Provides operations to call the coth method.
        """
        from .coth import coth_request_builder

        return coth_request_builder.CothRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def count(self) -> count_request_builder.CountRequestBuilder:
        """
        Provides operations to call the count method.
        """
        from .count import count_request_builder

        return count_request_builder.CountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def count_a(self) -> count_a_request_builder.CountARequestBuilder:
        """
        Provides operations to call the countA method.
        """
        from .count_a import count_a_request_builder

        return count_a_request_builder.CountARequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def count_blank(self) -> count_blank_request_builder.CountBlankRequestBuilder:
        """
        Provides operations to call the countBlank method.
        """
        from .count_blank import count_blank_request_builder

        return count_blank_request_builder.CountBlankRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def count_if(self) -> count_if_request_builder.CountIfRequestBuilder:
        """
        Provides operations to call the countIf method.
        """
        from .count_if import count_if_request_builder

        return count_if_request_builder.CountIfRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def count_ifs(self) -> count_ifs_request_builder.CountIfsRequestBuilder:
        """
        Provides operations to call the countIfs method.
        """
        from .count_ifs import count_ifs_request_builder

        return count_ifs_request_builder.CountIfsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def coup_day_bs(self) -> coup_day_bs_request_builder.CoupDayBsRequestBuilder:
        """
        Provides operations to call the coupDayBs method.
        """
        from .coup_day_bs import coup_day_bs_request_builder

        return coup_day_bs_request_builder.CoupDayBsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def coup_days(self) -> coup_days_request_builder.CoupDaysRequestBuilder:
        """
        Provides operations to call the coupDays method.
        """
        from .coup_days import coup_days_request_builder

        return coup_days_request_builder.CoupDaysRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def coup_days_nc(self) -> coup_days_nc_request_builder.CoupDaysNcRequestBuilder:
        """
        Provides operations to call the coupDaysNc method.
        """
        from .coup_days_nc import coup_days_nc_request_builder

        return coup_days_nc_request_builder.CoupDaysNcRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def coup_ncd(self) -> coup_ncd_request_builder.CoupNcdRequestBuilder:
        """
        Provides operations to call the coupNcd method.
        """
        from .coup_ncd import coup_ncd_request_builder

        return coup_ncd_request_builder.CoupNcdRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def coup_num(self) -> coup_num_request_builder.CoupNumRequestBuilder:
        """
        Provides operations to call the coupNum method.
        """
        from .coup_num import coup_num_request_builder

        return coup_num_request_builder.CoupNumRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def coup_pcd(self) -> coup_pcd_request_builder.CoupPcdRequestBuilder:
        """
        Provides operations to call the coupPcd method.
        """
        from .coup_pcd import coup_pcd_request_builder

        return coup_pcd_request_builder.CoupPcdRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def csc(self) -> csc_request_builder.CscRequestBuilder:
        """
        Provides operations to call the csc method.
        """
        from .csc import csc_request_builder

        return csc_request_builder.CscRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def csch(self) -> csch_request_builder.CschRequestBuilder:
        """
        Provides operations to call the csch method.
        """
        from .csch import csch_request_builder

        return csch_request_builder.CschRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def cum_i_pmt(self) -> cum_i_pmt_request_builder.CumIPmtRequestBuilder:
        """
        Provides operations to call the cumIPmt method.
        """
        from .cum_i_pmt import cum_i_pmt_request_builder

        return cum_i_pmt_request_builder.CumIPmtRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def cum_princ(self) -> cum_princ_request_builder.CumPrincRequestBuilder:
        """
        Provides operations to call the cumPrinc method.
        """
        from .cum_princ import cum_princ_request_builder

        return cum_princ_request_builder.CumPrincRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def date(self) -> date_request_builder.DateRequestBuilder:
        """
        Provides operations to call the date method.
        """
        from .date import date_request_builder

        return date_request_builder.DateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def datevalue(self) -> datevalue_request_builder.DatevalueRequestBuilder:
        """
        Provides operations to call the datevalue method.
        """
        from .datevalue import datevalue_request_builder

        return datevalue_request_builder.DatevalueRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def daverage(self) -> daverage_request_builder.DaverageRequestBuilder:
        """
        Provides operations to call the daverage method.
        """
        from .daverage import daverage_request_builder

        return daverage_request_builder.DaverageRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def day(self) -> day_request_builder.DayRequestBuilder:
        """
        Provides operations to call the day method.
        """
        from .day import day_request_builder

        return day_request_builder.DayRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def days(self) -> days_request_builder.DaysRequestBuilder:
        """
        Provides operations to call the days method.
        """
        from .days import days_request_builder

        return days_request_builder.DaysRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def days360(self) -> days360_request_builder.Days360RequestBuilder:
        """
        Provides operations to call the days360 method.
        """
        from .days360 import days360_request_builder

        return days360_request_builder.Days360RequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def db(self) -> db_request_builder.DbRequestBuilder:
        """
        Provides operations to call the db method.
        """
        from .db import db_request_builder

        return db_request_builder.DbRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dbcs(self) -> dbcs_request_builder.DbcsRequestBuilder:
        """
        Provides operations to call the dbcs method.
        """
        from .dbcs import dbcs_request_builder

        return dbcs_request_builder.DbcsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dcount(self) -> dcount_request_builder.DcountRequestBuilder:
        """
        Provides operations to call the dcount method.
        """
        from .dcount import dcount_request_builder

        return dcount_request_builder.DcountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dcount_a(self) -> dcount_a_request_builder.DcountARequestBuilder:
        """
        Provides operations to call the dcountA method.
        """
        from .dcount_a import dcount_a_request_builder

        return dcount_a_request_builder.DcountARequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def ddb(self) -> ddb_request_builder.DdbRequestBuilder:
        """
        Provides operations to call the ddb method.
        """
        from .ddb import ddb_request_builder

        return ddb_request_builder.DdbRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dec2_bin(self) -> dec2_bin_request_builder.Dec2BinRequestBuilder:
        """
        Provides operations to call the dec2Bin method.
        """
        from .dec2_bin import dec2_bin_request_builder

        return dec2_bin_request_builder.Dec2BinRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dec2_hex(self) -> dec2_hex_request_builder.Dec2HexRequestBuilder:
        """
        Provides operations to call the dec2Hex method.
        """
        from .dec2_hex import dec2_hex_request_builder

        return dec2_hex_request_builder.Dec2HexRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dec2_oct(self) -> dec2_oct_request_builder.Dec2OctRequestBuilder:
        """
        Provides operations to call the dec2Oct method.
        """
        from .dec2_oct import dec2_oct_request_builder

        return dec2_oct_request_builder.Dec2OctRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def decimal(self) -> decimal_request_builder.DecimalRequestBuilder:
        """
        Provides operations to call the decimal method.
        """
        from .decimal import decimal_request_builder

        return decimal_request_builder.DecimalRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def degrees(self) -> degrees_request_builder.DegreesRequestBuilder:
        """
        Provides operations to call the degrees method.
        """
        from .degrees import degrees_request_builder

        return degrees_request_builder.DegreesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def delta(self) -> delta_request_builder.DeltaRequestBuilder:
        """
        Provides operations to call the delta method.
        """
        from .delta import delta_request_builder

        return delta_request_builder.DeltaRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dev_sq(self) -> dev_sq_request_builder.DevSqRequestBuilder:
        """
        Provides operations to call the devSq method.
        """
        from .dev_sq import dev_sq_request_builder

        return dev_sq_request_builder.DevSqRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dget(self) -> dget_request_builder.DgetRequestBuilder:
        """
        Provides operations to call the dget method.
        """
        from .dget import dget_request_builder

        return dget_request_builder.DgetRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def disc(self) -> disc_request_builder.DiscRequestBuilder:
        """
        Provides operations to call the disc method.
        """
        from .disc import disc_request_builder

        return disc_request_builder.DiscRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dmax(self) -> dmax_request_builder.DmaxRequestBuilder:
        """
        Provides operations to call the dmax method.
        """
        from .dmax import dmax_request_builder

        return dmax_request_builder.DmaxRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dmin(self) -> dmin_request_builder.DminRequestBuilder:
        """
        Provides operations to call the dmin method.
        """
        from .dmin import dmin_request_builder

        return dmin_request_builder.DminRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dollar(self) -> dollar_request_builder.DollarRequestBuilder:
        """
        Provides operations to call the dollar method.
        """
        from .dollar import dollar_request_builder

        return dollar_request_builder.DollarRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dollar_de(self) -> dollar_de_request_builder.DollarDeRequestBuilder:
        """
        Provides operations to call the dollarDe method.
        """
        from .dollar_de import dollar_de_request_builder

        return dollar_de_request_builder.DollarDeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dollar_fr(self) -> dollar_fr_request_builder.DollarFrRequestBuilder:
        """
        Provides operations to call the dollarFr method.
        """
        from .dollar_fr import dollar_fr_request_builder

        return dollar_fr_request_builder.DollarFrRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dproduct(self) -> dproduct_request_builder.DproductRequestBuilder:
        """
        Provides operations to call the dproduct method.
        """
        from .dproduct import dproduct_request_builder

        return dproduct_request_builder.DproductRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dst_dev(self) -> dst_dev_request_builder.DstDevRequestBuilder:
        """
        Provides operations to call the dstDev method.
        """
        from .dst_dev import dst_dev_request_builder

        return dst_dev_request_builder.DstDevRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dst_dev_p(self) -> dst_dev_p_request_builder.DstDevPRequestBuilder:
        """
        Provides operations to call the dstDevP method.
        """
        from .dst_dev_p import dst_dev_p_request_builder

        return dst_dev_p_request_builder.DstDevPRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dsum(self) -> dsum_request_builder.DsumRequestBuilder:
        """
        Provides operations to call the dsum method.
        """
        from .dsum import dsum_request_builder

        return dsum_request_builder.DsumRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def duration(self) -> duration_request_builder.DurationRequestBuilder:
        """
        Provides operations to call the duration method.
        """
        from .duration import duration_request_builder

        return duration_request_builder.DurationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dvar(self) -> dvar_request_builder.DvarRequestBuilder:
        """
        Provides operations to call the dvar method.
        """
        from .dvar import dvar_request_builder

        return dvar_request_builder.DvarRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dvar_p(self) -> dvar_p_request_builder.DvarPRequestBuilder:
        """
        Provides operations to call the dvarP method.
        """
        from .dvar_p import dvar_p_request_builder

        return dvar_p_request_builder.DvarPRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def ecma_ceiling(self) -> ecma_ceiling_request_builder.Ecma_CeilingRequestBuilder:
        """
        Provides operations to call the ecma_Ceiling method.
        """
        from .ecma_ceiling import ecma_ceiling_request_builder

        return ecma_ceiling_request_builder.Ecma_CeilingRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def edate(self) -> edate_request_builder.EdateRequestBuilder:
        """
        Provides operations to call the edate method.
        """
        from .edate import edate_request_builder

        return edate_request_builder.EdateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def effect(self) -> effect_request_builder.EffectRequestBuilder:
        """
        Provides operations to call the effect method.
        """
        from .effect import effect_request_builder

        return effect_request_builder.EffectRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def eo_month(self) -> eo_month_request_builder.EoMonthRequestBuilder:
        """
        Provides operations to call the eoMonth method.
        """
        from .eo_month import eo_month_request_builder

        return eo_month_request_builder.EoMonthRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def erf(self) -> erf_request_builder.ErfRequestBuilder:
        """
        Provides operations to call the erf method.
        """
        from .erf import erf_request_builder

        return erf_request_builder.ErfRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def erf_precise(self) -> erf_precise_request_builder.Erf_PreciseRequestBuilder:
        """
        Provides operations to call the erf_Precise method.
        """
        from .erf_precise import erf_precise_request_builder

        return erf_precise_request_builder.Erf_PreciseRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def erf_c(self) -> erf_c_request_builder.ErfCRequestBuilder:
        """
        Provides operations to call the erfC method.
        """
        from .erf_c import erf_c_request_builder

        return erf_c_request_builder.ErfCRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def erf_c_precise(self) -> erf_c_precise_request_builder.ErfC_PreciseRequestBuilder:
        """
        Provides operations to call the erfC_Precise method.
        """
        from .erf_c_precise import erf_c_precise_request_builder

        return erf_c_precise_request_builder.ErfC_PreciseRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def error_type(self) -> error_type_request_builder.Error_TypeRequestBuilder:
        """
        Provides operations to call the error_Type method.
        """
        from .error_type import error_type_request_builder

        return error_type_request_builder.Error_TypeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def even(self) -> even_request_builder.EvenRequestBuilder:
        """
        Provides operations to call the even method.
        """
        from .even import even_request_builder

        return even_request_builder.EvenRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def exact(self) -> exact_request_builder.ExactRequestBuilder:
        """
        Provides operations to call the exact method.
        """
        from .exact import exact_request_builder

        return exact_request_builder.ExactRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def exp(self) -> exp_request_builder.ExpRequestBuilder:
        """
        Provides operations to call the exp method.
        """
        from .exp import exp_request_builder

        return exp_request_builder.ExpRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def expon_dist(self) -> expon_dist_request_builder.Expon_DistRequestBuilder:
        """
        Provides operations to call the expon_Dist method.
        """
        from .expon_dist import expon_dist_request_builder

        return expon_dist_request_builder.Expon_DistRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def f_dist(self) -> f_dist_request_builder.F_DistRequestBuilder:
        """
        Provides operations to call the f_Dist method.
        """
        from .f_dist import f_dist_request_builder

        return f_dist_request_builder.F_DistRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def f_dist_r_t(self) -> f_dist_r_t_request_builder.F_Dist_RTRequestBuilder:
        """
        Provides operations to call the f_Dist_RT method.
        """
        from .f_dist_r_t import f_dist_r_t_request_builder

        return f_dist_r_t_request_builder.F_Dist_RTRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def f_inv(self) -> f_inv_request_builder.F_InvRequestBuilder:
        """
        Provides operations to call the f_Inv method.
        """
        from .f_inv import f_inv_request_builder

        return f_inv_request_builder.F_InvRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def f_inv_r_t(self) -> f_inv_r_t_request_builder.F_Inv_RTRequestBuilder:
        """
        Provides operations to call the f_Inv_RT method.
        """
        from .f_inv_r_t import f_inv_r_t_request_builder

        return f_inv_r_t_request_builder.F_Inv_RTRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def fact(self) -> fact_request_builder.FactRequestBuilder:
        """
        Provides operations to call the fact method.
        """
        from .fact import fact_request_builder

        return fact_request_builder.FactRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def fact_double(self) -> fact_double_request_builder.FactDoubleRequestBuilder:
        """
        Provides operations to call the factDouble method.
        """
        from .fact_double import fact_double_request_builder

        return fact_double_request_builder.FactDoubleRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def false_(self) -> false_request_builder.FalseRequestBuilder:
        """
        Provides operations to call the false method.
        """
        from .false_ import false_request_builder

        return false_request_builder.FalseRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def find(self) -> find_request_builder.FindRequestBuilder:
        """
        Provides operations to call the find method.
        """
        from .find import find_request_builder

        return find_request_builder.FindRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def find_b(self) -> find_b_request_builder.FindBRequestBuilder:
        """
        Provides operations to call the findB method.
        """
        from .find_b import find_b_request_builder

        return find_b_request_builder.FindBRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def fisher(self) -> fisher_request_builder.FisherRequestBuilder:
        """
        Provides operations to call the fisher method.
        """
        from .fisher import fisher_request_builder

        return fisher_request_builder.FisherRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def fisher_inv(self) -> fisher_inv_request_builder.FisherInvRequestBuilder:
        """
        Provides operations to call the fisherInv method.
        """
        from .fisher_inv import fisher_inv_request_builder

        return fisher_inv_request_builder.FisherInvRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def fixed(self) -> fixed_request_builder.FixedRequestBuilder:
        """
        Provides operations to call the fixed method.
        """
        from .fixed import fixed_request_builder

        return fixed_request_builder.FixedRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def floor_math(self) -> floor_math_request_builder.Floor_MathRequestBuilder:
        """
        Provides operations to call the floor_Math method.
        """
        from .floor_math import floor_math_request_builder

        return floor_math_request_builder.Floor_MathRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def floor_precise(self) -> floor_precise_request_builder.Floor_PreciseRequestBuilder:
        """
        Provides operations to call the floor_Precise method.
        """
        from .floor_precise import floor_precise_request_builder

        return floor_precise_request_builder.Floor_PreciseRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def fv(self) -> fv_request_builder.FvRequestBuilder:
        """
        Provides operations to call the fv method.
        """
        from .fv import fv_request_builder

        return fv_request_builder.FvRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def fvschedule(self) -> fvschedule_request_builder.FvscheduleRequestBuilder:
        """
        Provides operations to call the fvschedule method.
        """
        from .fvschedule import fvschedule_request_builder

        return fvschedule_request_builder.FvscheduleRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def gamma(self) -> gamma_request_builder.GammaRequestBuilder:
        """
        Provides operations to call the gamma method.
        """
        from .gamma import gamma_request_builder

        return gamma_request_builder.GammaRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def gamma_dist(self) -> gamma_dist_request_builder.Gamma_DistRequestBuilder:
        """
        Provides operations to call the gamma_Dist method.
        """
        from .gamma_dist import gamma_dist_request_builder

        return gamma_dist_request_builder.Gamma_DistRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def gamma_inv(self) -> gamma_inv_request_builder.Gamma_InvRequestBuilder:
        """
        Provides operations to call the gamma_Inv method.
        """
        from .gamma_inv import gamma_inv_request_builder

        return gamma_inv_request_builder.Gamma_InvRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def gamma_ln(self) -> gamma_ln_request_builder.GammaLnRequestBuilder:
        """
        Provides operations to call the gammaLn method.
        """
        from .gamma_ln import gamma_ln_request_builder

        return gamma_ln_request_builder.GammaLnRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def gamma_ln_precise(self) -> gamma_ln_precise_request_builder.GammaLn_PreciseRequestBuilder:
        """
        Provides operations to call the gammaLn_Precise method.
        """
        from .gamma_ln_precise import gamma_ln_precise_request_builder

        return gamma_ln_precise_request_builder.GammaLn_PreciseRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def gauss(self) -> gauss_request_builder.GaussRequestBuilder:
        """
        Provides operations to call the gauss method.
        """
        from .gauss import gauss_request_builder

        return gauss_request_builder.GaussRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def gcd(self) -> gcd_request_builder.GcdRequestBuilder:
        """
        Provides operations to call the gcd method.
        """
        from .gcd import gcd_request_builder

        return gcd_request_builder.GcdRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def geo_mean(self) -> geo_mean_request_builder.GeoMeanRequestBuilder:
        """
        Provides operations to call the geoMean method.
        """
        from .geo_mean import geo_mean_request_builder

        return geo_mean_request_builder.GeoMeanRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def ge_step(self) -> ge_step_request_builder.GeStepRequestBuilder:
        """
        Provides operations to call the geStep method.
        """
        from .ge_step import ge_step_request_builder

        return ge_step_request_builder.GeStepRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def har_mean(self) -> har_mean_request_builder.HarMeanRequestBuilder:
        """
        Provides operations to call the harMean method.
        """
        from .har_mean import har_mean_request_builder

        return har_mean_request_builder.HarMeanRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def hex2_bin(self) -> hex2_bin_request_builder.Hex2BinRequestBuilder:
        """
        Provides operations to call the hex2Bin method.
        """
        from .hex2_bin import hex2_bin_request_builder

        return hex2_bin_request_builder.Hex2BinRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def hex2_dec(self) -> hex2_dec_request_builder.Hex2DecRequestBuilder:
        """
        Provides operations to call the hex2Dec method.
        """
        from .hex2_dec import hex2_dec_request_builder

        return hex2_dec_request_builder.Hex2DecRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def hex2_oct(self) -> hex2_oct_request_builder.Hex2OctRequestBuilder:
        """
        Provides operations to call the hex2Oct method.
        """
        from .hex2_oct import hex2_oct_request_builder

        return hex2_oct_request_builder.Hex2OctRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def hlookup(self) -> hlookup_request_builder.HlookupRequestBuilder:
        """
        Provides operations to call the hlookup method.
        """
        from .hlookup import hlookup_request_builder

        return hlookup_request_builder.HlookupRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def hour(self) -> hour_request_builder.HourRequestBuilder:
        """
        Provides operations to call the hour method.
        """
        from .hour import hour_request_builder

        return hour_request_builder.HourRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def hyperlink(self) -> hyperlink_request_builder.HyperlinkRequestBuilder:
        """
        Provides operations to call the hyperlink method.
        """
        from .hyperlink import hyperlink_request_builder

        return hyperlink_request_builder.HyperlinkRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def hyp_geom_dist(self) -> hyp_geom_dist_request_builder.HypGeom_DistRequestBuilder:
        """
        Provides operations to call the hypGeom_Dist method.
        """
        from .hyp_geom_dist import hyp_geom_dist_request_builder

        return hyp_geom_dist_request_builder.HypGeom_DistRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def if_(self) -> if_request_builder.IfRequestBuilder:
        """
        Provides operations to call the if method.
        """
        from .if_ import if_request_builder

        return if_request_builder.IfRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def im_abs(self) -> im_abs_request_builder.ImAbsRequestBuilder:
        """
        Provides operations to call the imAbs method.
        """
        from .im_abs import im_abs_request_builder

        return im_abs_request_builder.ImAbsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def imaginary(self) -> imaginary_request_builder.ImaginaryRequestBuilder:
        """
        Provides operations to call the imaginary method.
        """
        from .imaginary import imaginary_request_builder

        return imaginary_request_builder.ImaginaryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def im_argument(self) -> im_argument_request_builder.ImArgumentRequestBuilder:
        """
        Provides operations to call the imArgument method.
        """
        from .im_argument import im_argument_request_builder

        return im_argument_request_builder.ImArgumentRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def im_conjugate(self) -> im_conjugate_request_builder.ImConjugateRequestBuilder:
        """
        Provides operations to call the imConjugate method.
        """
        from .im_conjugate import im_conjugate_request_builder

        return im_conjugate_request_builder.ImConjugateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def im_cos(self) -> im_cos_request_builder.ImCosRequestBuilder:
        """
        Provides operations to call the imCos method.
        """
        from .im_cos import im_cos_request_builder

        return im_cos_request_builder.ImCosRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def im_cosh(self) -> im_cosh_request_builder.ImCoshRequestBuilder:
        """
        Provides operations to call the imCosh method.
        """
        from .im_cosh import im_cosh_request_builder

        return im_cosh_request_builder.ImCoshRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def im_cot(self) -> im_cot_request_builder.ImCotRequestBuilder:
        """
        Provides operations to call the imCot method.
        """
        from .im_cot import im_cot_request_builder

        return im_cot_request_builder.ImCotRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def im_csc(self) -> im_csc_request_builder.ImCscRequestBuilder:
        """
        Provides operations to call the imCsc method.
        """
        from .im_csc import im_csc_request_builder

        return im_csc_request_builder.ImCscRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def im_csch(self) -> im_csch_request_builder.ImCschRequestBuilder:
        """
        Provides operations to call the imCsch method.
        """
        from .im_csch import im_csch_request_builder

        return im_csch_request_builder.ImCschRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def im_div(self) -> im_div_request_builder.ImDivRequestBuilder:
        """
        Provides operations to call the imDiv method.
        """
        from .im_div import im_div_request_builder

        return im_div_request_builder.ImDivRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def im_exp(self) -> im_exp_request_builder.ImExpRequestBuilder:
        """
        Provides operations to call the imExp method.
        """
        from .im_exp import im_exp_request_builder

        return im_exp_request_builder.ImExpRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def im_ln(self) -> im_ln_request_builder.ImLnRequestBuilder:
        """
        Provides operations to call the imLn method.
        """
        from .im_ln import im_ln_request_builder

        return im_ln_request_builder.ImLnRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def im_log10(self) -> im_log10_request_builder.ImLog10RequestBuilder:
        """
        Provides operations to call the imLog10 method.
        """
        from .im_log10 import im_log10_request_builder

        return im_log10_request_builder.ImLog10RequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def im_log2(self) -> im_log2_request_builder.ImLog2RequestBuilder:
        """
        Provides operations to call the imLog2 method.
        """
        from .im_log2 import im_log2_request_builder

        return im_log2_request_builder.ImLog2RequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def im_power(self) -> im_power_request_builder.ImPowerRequestBuilder:
        """
        Provides operations to call the imPower method.
        """
        from .im_power import im_power_request_builder

        return im_power_request_builder.ImPowerRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def im_product(self) -> im_product_request_builder.ImProductRequestBuilder:
        """
        Provides operations to call the imProduct method.
        """
        from .im_product import im_product_request_builder

        return im_product_request_builder.ImProductRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def im_real(self) -> im_real_request_builder.ImRealRequestBuilder:
        """
        Provides operations to call the imReal method.
        """
        from .im_real import im_real_request_builder

        return im_real_request_builder.ImRealRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def im_sec(self) -> im_sec_request_builder.ImSecRequestBuilder:
        """
        Provides operations to call the imSec method.
        """
        from .im_sec import im_sec_request_builder

        return im_sec_request_builder.ImSecRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def im_sech(self) -> im_sech_request_builder.ImSechRequestBuilder:
        """
        Provides operations to call the imSech method.
        """
        from .im_sech import im_sech_request_builder

        return im_sech_request_builder.ImSechRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def im_sin(self) -> im_sin_request_builder.ImSinRequestBuilder:
        """
        Provides operations to call the imSin method.
        """
        from .im_sin import im_sin_request_builder

        return im_sin_request_builder.ImSinRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def im_sinh(self) -> im_sinh_request_builder.ImSinhRequestBuilder:
        """
        Provides operations to call the imSinh method.
        """
        from .im_sinh import im_sinh_request_builder

        return im_sinh_request_builder.ImSinhRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def im_sqrt(self) -> im_sqrt_request_builder.ImSqrtRequestBuilder:
        """
        Provides operations to call the imSqrt method.
        """
        from .im_sqrt import im_sqrt_request_builder

        return im_sqrt_request_builder.ImSqrtRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def im_sub(self) -> im_sub_request_builder.ImSubRequestBuilder:
        """
        Provides operations to call the imSub method.
        """
        from .im_sub import im_sub_request_builder

        return im_sub_request_builder.ImSubRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def im_sum(self) -> im_sum_request_builder.ImSumRequestBuilder:
        """
        Provides operations to call the imSum method.
        """
        from .im_sum import im_sum_request_builder

        return im_sum_request_builder.ImSumRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def im_tan(self) -> im_tan_request_builder.ImTanRequestBuilder:
        """
        Provides operations to call the imTan method.
        """
        from .im_tan import im_tan_request_builder

        return im_tan_request_builder.ImTanRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def int(self) -> int_request_builder.IntRequestBuilder:
        """
        Provides operations to call the int method.
        """
        from .int import int_request_builder

        return int_request_builder.IntRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def int_rate(self) -> int_rate_request_builder.IntRateRequestBuilder:
        """
        Provides operations to call the intRate method.
        """
        from .int_rate import int_rate_request_builder

        return int_rate_request_builder.IntRateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def ipmt(self) -> ipmt_request_builder.IpmtRequestBuilder:
        """
        Provides operations to call the ipmt method.
        """
        from .ipmt import ipmt_request_builder

        return ipmt_request_builder.IpmtRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def irr(self) -> irr_request_builder.IrrRequestBuilder:
        """
        Provides operations to call the irr method.
        """
        from .irr import irr_request_builder

        return irr_request_builder.IrrRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def is_err(self) -> is_err_request_builder.IsErrRequestBuilder:
        """
        Provides operations to call the isErr method.
        """
        from .is_err import is_err_request_builder

        return is_err_request_builder.IsErrRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def is_error(self) -> is_error_request_builder.IsErrorRequestBuilder:
        """
        Provides operations to call the isError method.
        """
        from .is_error import is_error_request_builder

        return is_error_request_builder.IsErrorRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def is_even(self) -> is_even_request_builder.IsEvenRequestBuilder:
        """
        Provides operations to call the isEven method.
        """
        from .is_even import is_even_request_builder

        return is_even_request_builder.IsEvenRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def is_formula(self) -> is_formula_request_builder.IsFormulaRequestBuilder:
        """
        Provides operations to call the isFormula method.
        """
        from .is_formula import is_formula_request_builder

        return is_formula_request_builder.IsFormulaRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def is_logical(self) -> is_logical_request_builder.IsLogicalRequestBuilder:
        """
        Provides operations to call the isLogical method.
        """
        from .is_logical import is_logical_request_builder

        return is_logical_request_builder.IsLogicalRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def is_n_a(self) -> is_n_a_request_builder.IsNARequestBuilder:
        """
        Provides operations to call the isNA method.
        """
        from .is_n_a import is_n_a_request_builder

        return is_n_a_request_builder.IsNARequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def is_non_text(self) -> is_non_text_request_builder.IsNonTextRequestBuilder:
        """
        Provides operations to call the isNonText method.
        """
        from .is_non_text import is_non_text_request_builder

        return is_non_text_request_builder.IsNonTextRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def is_number(self) -> is_number_request_builder.IsNumberRequestBuilder:
        """
        Provides operations to call the isNumber method.
        """
        from .is_number import is_number_request_builder

        return is_number_request_builder.IsNumberRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def iso_ceiling(self) -> iso_ceiling_request_builder.Iso_CeilingRequestBuilder:
        """
        Provides operations to call the iso_Ceiling method.
        """
        from .iso_ceiling import iso_ceiling_request_builder

        return iso_ceiling_request_builder.Iso_CeilingRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def is_odd(self) -> is_odd_request_builder.IsOddRequestBuilder:
        """
        Provides operations to call the isOdd method.
        """
        from .is_odd import is_odd_request_builder

        return is_odd_request_builder.IsOddRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def iso_week_num(self) -> iso_week_num_request_builder.IsoWeekNumRequestBuilder:
        """
        Provides operations to call the isoWeekNum method.
        """
        from .iso_week_num import iso_week_num_request_builder

        return iso_week_num_request_builder.IsoWeekNumRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def ispmt(self) -> ispmt_request_builder.IspmtRequestBuilder:
        """
        Provides operations to call the ispmt method.
        """
        from .ispmt import ispmt_request_builder

        return ispmt_request_builder.IspmtRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def isref(self) -> isref_request_builder.IsrefRequestBuilder:
        """
        Provides operations to call the isref method.
        """
        from .isref import isref_request_builder

        return isref_request_builder.IsrefRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def is_text(self) -> is_text_request_builder.IsTextRequestBuilder:
        """
        Provides operations to call the isText method.
        """
        from .is_text import is_text_request_builder

        return is_text_request_builder.IsTextRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def kurt(self) -> kurt_request_builder.KurtRequestBuilder:
        """
        Provides operations to call the kurt method.
        """
        from .kurt import kurt_request_builder

        return kurt_request_builder.KurtRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def large(self) -> large_request_builder.LargeRequestBuilder:
        """
        Provides operations to call the large method.
        """
        from .large import large_request_builder

        return large_request_builder.LargeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def lcm(self) -> lcm_request_builder.LcmRequestBuilder:
        """
        Provides operations to call the lcm method.
        """
        from .lcm import lcm_request_builder

        return lcm_request_builder.LcmRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def left(self) -> left_request_builder.LeftRequestBuilder:
        """
        Provides operations to call the left method.
        """
        from .left import left_request_builder

        return left_request_builder.LeftRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def leftb(self) -> leftb_request_builder.LeftbRequestBuilder:
        """
        Provides operations to call the leftb method.
        """
        from .leftb import leftb_request_builder

        return leftb_request_builder.LeftbRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def len(self) -> len_request_builder.LenRequestBuilder:
        """
        Provides operations to call the len method.
        """
        from .len import len_request_builder

        return len_request_builder.LenRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def lenb(self) -> lenb_request_builder.LenbRequestBuilder:
        """
        Provides operations to call the lenb method.
        """
        from .lenb import lenb_request_builder

        return lenb_request_builder.LenbRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def ln(self) -> ln_request_builder.LnRequestBuilder:
        """
        Provides operations to call the ln method.
        """
        from .ln import ln_request_builder

        return ln_request_builder.LnRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def log(self) -> log_request_builder.LogRequestBuilder:
        """
        Provides operations to call the log method.
        """
        from .log import log_request_builder

        return log_request_builder.LogRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def log10(self) -> log10_request_builder.Log10RequestBuilder:
        """
        Provides operations to call the log10 method.
        """
        from .log10 import log10_request_builder

        return log10_request_builder.Log10RequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def log_norm_dist(self) -> log_norm_dist_request_builder.LogNorm_DistRequestBuilder:
        """
        Provides operations to call the logNorm_Dist method.
        """
        from .log_norm_dist import log_norm_dist_request_builder

        return log_norm_dist_request_builder.LogNorm_DistRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def log_norm_inv(self) -> log_norm_inv_request_builder.LogNorm_InvRequestBuilder:
        """
        Provides operations to call the logNorm_Inv method.
        """
        from .log_norm_inv import log_norm_inv_request_builder

        return log_norm_inv_request_builder.LogNorm_InvRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def lookup(self) -> lookup_request_builder.LookupRequestBuilder:
        """
        Provides operations to call the lookup method.
        """
        from .lookup import lookup_request_builder

        return lookup_request_builder.LookupRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def lower(self) -> lower_request_builder.LowerRequestBuilder:
        """
        Provides operations to call the lower method.
        """
        from .lower import lower_request_builder

        return lower_request_builder.LowerRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def match(self) -> match_request_builder.MatchRequestBuilder:
        """
        Provides operations to call the match method.
        """
        from .match import match_request_builder

        return match_request_builder.MatchRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def max(self) -> max_request_builder.MaxRequestBuilder:
        """
        Provides operations to call the max method.
        """
        from .max import max_request_builder

        return max_request_builder.MaxRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def max_a(self) -> max_a_request_builder.MaxARequestBuilder:
        """
        Provides operations to call the maxA method.
        """
        from .max_a import max_a_request_builder

        return max_a_request_builder.MaxARequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mduration(self) -> mduration_request_builder.MdurationRequestBuilder:
        """
        Provides operations to call the mduration method.
        """
        from .mduration import mduration_request_builder

        return mduration_request_builder.MdurationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def median(self) -> median_request_builder.MedianRequestBuilder:
        """
        Provides operations to call the median method.
        """
        from .median import median_request_builder

        return median_request_builder.MedianRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mid(self) -> mid_request_builder.MidRequestBuilder:
        """
        Provides operations to call the mid method.
        """
        from .mid import mid_request_builder

        return mid_request_builder.MidRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def midb(self) -> midb_request_builder.MidbRequestBuilder:
        """
        Provides operations to call the midb method.
        """
        from .midb import midb_request_builder

        return midb_request_builder.MidbRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def min(self) -> min_request_builder.MinRequestBuilder:
        """
        Provides operations to call the min method.
        """
        from .min import min_request_builder

        return min_request_builder.MinRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def min_a(self) -> min_a_request_builder.MinARequestBuilder:
        """
        Provides operations to call the minA method.
        """
        from .min_a import min_a_request_builder

        return min_a_request_builder.MinARequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def minute(self) -> minute_request_builder.MinuteRequestBuilder:
        """
        Provides operations to call the minute method.
        """
        from .minute import minute_request_builder

        return minute_request_builder.MinuteRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mirr(self) -> mirr_request_builder.MirrRequestBuilder:
        """
        Provides operations to call the mirr method.
        """
        from .mirr import mirr_request_builder

        return mirr_request_builder.MirrRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mod(self) -> mod_request_builder.ModRequestBuilder:
        """
        Provides operations to call the mod method.
        """
        from .mod import mod_request_builder

        return mod_request_builder.ModRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def month(self) -> month_request_builder.MonthRequestBuilder:
        """
        Provides operations to call the month method.
        """
        from .month import month_request_builder

        return month_request_builder.MonthRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mround(self) -> mround_request_builder.MroundRequestBuilder:
        """
        Provides operations to call the mround method.
        """
        from .mround import mround_request_builder

        return mround_request_builder.MroundRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def multi_nomial(self) -> multi_nomial_request_builder.MultiNomialRequestBuilder:
        """
        Provides operations to call the multiNomial method.
        """
        from .multi_nomial import multi_nomial_request_builder

        return multi_nomial_request_builder.MultiNomialRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def n(self) -> n_request_builder.NRequestBuilder:
        """
        Provides operations to call the n method.
        """
        from .n import n_request_builder

        return n_request_builder.NRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def na(self) -> na_request_builder.NaRequestBuilder:
        """
        Provides operations to call the na method.
        """
        from .na import na_request_builder

        return na_request_builder.NaRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def neg_binom_dist(self) -> neg_binom_dist_request_builder.NegBinom_DistRequestBuilder:
        """
        Provides operations to call the negBinom_Dist method.
        """
        from .neg_binom_dist import neg_binom_dist_request_builder

        return neg_binom_dist_request_builder.NegBinom_DistRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def network_days(self) -> network_days_request_builder.NetworkDaysRequestBuilder:
        """
        Provides operations to call the networkDays method.
        """
        from .network_days import network_days_request_builder

        return network_days_request_builder.NetworkDaysRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def network_days_intl(self) -> network_days_intl_request_builder.NetworkDays_IntlRequestBuilder:
        """
        Provides operations to call the networkDays_Intl method.
        """
        from .network_days_intl import network_days_intl_request_builder

        return network_days_intl_request_builder.NetworkDays_IntlRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def nominal(self) -> nominal_request_builder.NominalRequestBuilder:
        """
        Provides operations to call the nominal method.
        """
        from .nominal import nominal_request_builder

        return nominal_request_builder.NominalRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def norm_dist(self) -> norm_dist_request_builder.Norm_DistRequestBuilder:
        """
        Provides operations to call the norm_Dist method.
        """
        from .norm_dist import norm_dist_request_builder

        return norm_dist_request_builder.Norm_DistRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def norm_inv(self) -> norm_inv_request_builder.Norm_InvRequestBuilder:
        """
        Provides operations to call the norm_Inv method.
        """
        from .norm_inv import norm_inv_request_builder

        return norm_inv_request_builder.Norm_InvRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def norm_s_dist(self) -> norm_s_dist_request_builder.Norm_S_DistRequestBuilder:
        """
        Provides operations to call the norm_S_Dist method.
        """
        from .norm_s_dist import norm_s_dist_request_builder

        return norm_s_dist_request_builder.Norm_S_DistRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def norm_s_inv(self) -> norm_s_inv_request_builder.Norm_S_InvRequestBuilder:
        """
        Provides operations to call the norm_S_Inv method.
        """
        from .norm_s_inv import norm_s_inv_request_builder

        return norm_s_inv_request_builder.Norm_S_InvRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def not_(self) -> not_request_builder.NotRequestBuilder:
        """
        Provides operations to call the not method.
        """
        from .not_ import not_request_builder

        return not_request_builder.NotRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def now(self) -> now_request_builder.NowRequestBuilder:
        """
        Provides operations to call the now method.
        """
        from .now import now_request_builder

        return now_request_builder.NowRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def nper(self) -> nper_request_builder.NperRequestBuilder:
        """
        Provides operations to call the nper method.
        """
        from .nper import nper_request_builder

        return nper_request_builder.NperRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def npv(self) -> npv_request_builder.NpvRequestBuilder:
        """
        Provides operations to call the npv method.
        """
        from .npv import npv_request_builder

        return npv_request_builder.NpvRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def number_value(self) -> number_value_request_builder.NumberValueRequestBuilder:
        """
        Provides operations to call the numberValue method.
        """
        from .number_value import number_value_request_builder

        return number_value_request_builder.NumberValueRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def oct2_bin(self) -> oct2_bin_request_builder.Oct2BinRequestBuilder:
        """
        Provides operations to call the oct2Bin method.
        """
        from .oct2_bin import oct2_bin_request_builder

        return oct2_bin_request_builder.Oct2BinRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def oct2_dec(self) -> oct2_dec_request_builder.Oct2DecRequestBuilder:
        """
        Provides operations to call the oct2Dec method.
        """
        from .oct2_dec import oct2_dec_request_builder

        return oct2_dec_request_builder.Oct2DecRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def oct2_hex(self) -> oct2_hex_request_builder.Oct2HexRequestBuilder:
        """
        Provides operations to call the oct2Hex method.
        """
        from .oct2_hex import oct2_hex_request_builder

        return oct2_hex_request_builder.Oct2HexRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def odd(self) -> odd_request_builder.OddRequestBuilder:
        """
        Provides operations to call the odd method.
        """
        from .odd import odd_request_builder

        return odd_request_builder.OddRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def odd_f_price(self) -> odd_f_price_request_builder.OddFPriceRequestBuilder:
        """
        Provides operations to call the oddFPrice method.
        """
        from .odd_f_price import odd_f_price_request_builder

        return odd_f_price_request_builder.OddFPriceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def odd_f_yield(self) -> odd_f_yield_request_builder.OddFYieldRequestBuilder:
        """
        Provides operations to call the oddFYield method.
        """
        from .odd_f_yield import odd_f_yield_request_builder

        return odd_f_yield_request_builder.OddFYieldRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def odd_l_price(self) -> odd_l_price_request_builder.OddLPriceRequestBuilder:
        """
        Provides operations to call the oddLPrice method.
        """
        from .odd_l_price import odd_l_price_request_builder

        return odd_l_price_request_builder.OddLPriceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def odd_l_yield(self) -> odd_l_yield_request_builder.OddLYieldRequestBuilder:
        """
        Provides operations to call the oddLYield method.
        """
        from .odd_l_yield import odd_l_yield_request_builder

        return odd_l_yield_request_builder.OddLYieldRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def or_(self) -> or_request_builder.OrRequestBuilder:
        """
        Provides operations to call the or method.
        """
        from .or_ import or_request_builder

        return or_request_builder.OrRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def pduration(self) -> pduration_request_builder.PdurationRequestBuilder:
        """
        Provides operations to call the pduration method.
        """
        from .pduration import pduration_request_builder

        return pduration_request_builder.PdurationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def percentile_exc(self) -> percentile_exc_request_builder.Percentile_ExcRequestBuilder:
        """
        Provides operations to call the percentile_Exc method.
        """
        from .percentile_exc import percentile_exc_request_builder

        return percentile_exc_request_builder.Percentile_ExcRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def percentile_inc(self) -> percentile_inc_request_builder.Percentile_IncRequestBuilder:
        """
        Provides operations to call the percentile_Inc method.
        """
        from .percentile_inc import percentile_inc_request_builder

        return percentile_inc_request_builder.Percentile_IncRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def percent_rank_exc(self) -> percent_rank_exc_request_builder.PercentRank_ExcRequestBuilder:
        """
        Provides operations to call the percentRank_Exc method.
        """
        from .percent_rank_exc import percent_rank_exc_request_builder

        return percent_rank_exc_request_builder.PercentRank_ExcRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def percent_rank_inc(self) -> percent_rank_inc_request_builder.PercentRank_IncRequestBuilder:
        """
        Provides operations to call the percentRank_Inc method.
        """
        from .percent_rank_inc import percent_rank_inc_request_builder

        return percent_rank_inc_request_builder.PercentRank_IncRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def permut(self) -> permut_request_builder.PermutRequestBuilder:
        """
        Provides operations to call the permut method.
        """
        from .permut import permut_request_builder

        return permut_request_builder.PermutRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def permutationa(self) -> permutationa_request_builder.PermutationaRequestBuilder:
        """
        Provides operations to call the permutationa method.
        """
        from .permutationa import permutationa_request_builder

        return permutationa_request_builder.PermutationaRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def phi(self) -> phi_request_builder.PhiRequestBuilder:
        """
        Provides operations to call the phi method.
        """
        from .phi import phi_request_builder

        return phi_request_builder.PhiRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def pi(self) -> pi_request_builder.PiRequestBuilder:
        """
        Provides operations to call the pi method.
        """
        from .pi import pi_request_builder

        return pi_request_builder.PiRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def pmt(self) -> pmt_request_builder.PmtRequestBuilder:
        """
        Provides operations to call the pmt method.
        """
        from .pmt import pmt_request_builder

        return pmt_request_builder.PmtRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def poisson_dist(self) -> poisson_dist_request_builder.Poisson_DistRequestBuilder:
        """
        Provides operations to call the poisson_Dist method.
        """
        from .poisson_dist import poisson_dist_request_builder

        return poisson_dist_request_builder.Poisson_DistRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def power(self) -> power_request_builder.PowerRequestBuilder:
        """
        Provides operations to call the power method.
        """
        from .power import power_request_builder

        return power_request_builder.PowerRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def ppmt(self) -> ppmt_request_builder.PpmtRequestBuilder:
        """
        Provides operations to call the ppmt method.
        """
        from .ppmt import ppmt_request_builder

        return ppmt_request_builder.PpmtRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def price(self) -> price_request_builder.PriceRequestBuilder:
        """
        Provides operations to call the price method.
        """
        from .price import price_request_builder

        return price_request_builder.PriceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def price_disc(self) -> price_disc_request_builder.PriceDiscRequestBuilder:
        """
        Provides operations to call the priceDisc method.
        """
        from .price_disc import price_disc_request_builder

        return price_disc_request_builder.PriceDiscRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def price_mat(self) -> price_mat_request_builder.PriceMatRequestBuilder:
        """
        Provides operations to call the priceMat method.
        """
        from .price_mat import price_mat_request_builder

        return price_mat_request_builder.PriceMatRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def product(self) -> product_request_builder.ProductRequestBuilder:
        """
        Provides operations to call the product method.
        """
        from .product import product_request_builder

        return product_request_builder.ProductRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def proper(self) -> proper_request_builder.ProperRequestBuilder:
        """
        Provides operations to call the proper method.
        """
        from .proper import proper_request_builder

        return proper_request_builder.ProperRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def pv(self) -> pv_request_builder.PvRequestBuilder:
        """
        Provides operations to call the pv method.
        """
        from .pv import pv_request_builder

        return pv_request_builder.PvRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def quartile_exc(self) -> quartile_exc_request_builder.Quartile_ExcRequestBuilder:
        """
        Provides operations to call the quartile_Exc method.
        """
        from .quartile_exc import quartile_exc_request_builder

        return quartile_exc_request_builder.Quartile_ExcRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def quartile_inc(self) -> quartile_inc_request_builder.Quartile_IncRequestBuilder:
        """
        Provides operations to call the quartile_Inc method.
        """
        from .quartile_inc import quartile_inc_request_builder

        return quartile_inc_request_builder.Quartile_IncRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def quotient(self) -> quotient_request_builder.QuotientRequestBuilder:
        """
        Provides operations to call the quotient method.
        """
        from .quotient import quotient_request_builder

        return quotient_request_builder.QuotientRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def radians(self) -> radians_request_builder.RadiansRequestBuilder:
        """
        Provides operations to call the radians method.
        """
        from .radians import radians_request_builder

        return radians_request_builder.RadiansRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def rand(self) -> rand_request_builder.RandRequestBuilder:
        """
        Provides operations to call the rand method.
        """
        from .rand import rand_request_builder

        return rand_request_builder.RandRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def rand_between(self) -> rand_between_request_builder.RandBetweenRequestBuilder:
        """
        Provides operations to call the randBetween method.
        """
        from .rand_between import rand_between_request_builder

        return rand_between_request_builder.RandBetweenRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def rank_avg(self) -> rank_avg_request_builder.Rank_AvgRequestBuilder:
        """
        Provides operations to call the rank_Avg method.
        """
        from .rank_avg import rank_avg_request_builder

        return rank_avg_request_builder.Rank_AvgRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def rank_eq(self) -> rank_eq_request_builder.Rank_EqRequestBuilder:
        """
        Provides operations to call the rank_Eq method.
        """
        from .rank_eq import rank_eq_request_builder

        return rank_eq_request_builder.Rank_EqRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def rate(self) -> rate_request_builder.RateRequestBuilder:
        """
        Provides operations to call the rate method.
        """
        from .rate import rate_request_builder

        return rate_request_builder.RateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def received(self) -> received_request_builder.ReceivedRequestBuilder:
        """
        Provides operations to call the received method.
        """
        from .received import received_request_builder

        return received_request_builder.ReceivedRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def replace(self) -> replace_request_builder.ReplaceRequestBuilder:
        """
        Provides operations to call the replace method.
        """
        from .replace import replace_request_builder

        return replace_request_builder.ReplaceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def replace_b(self) -> replace_b_request_builder.ReplaceBRequestBuilder:
        """
        Provides operations to call the replaceB method.
        """
        from .replace_b import replace_b_request_builder

        return replace_b_request_builder.ReplaceBRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def rept(self) -> rept_request_builder.ReptRequestBuilder:
        """
        Provides operations to call the rept method.
        """
        from .rept import rept_request_builder

        return rept_request_builder.ReptRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def right(self) -> right_request_builder.RightRequestBuilder:
        """
        Provides operations to call the right method.
        """
        from .right import right_request_builder

        return right_request_builder.RightRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def rightb(self) -> rightb_request_builder.RightbRequestBuilder:
        """
        Provides operations to call the rightb method.
        """
        from .rightb import rightb_request_builder

        return rightb_request_builder.RightbRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def roman(self) -> roman_request_builder.RomanRequestBuilder:
        """
        Provides operations to call the roman method.
        """
        from .roman import roman_request_builder

        return roman_request_builder.RomanRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def round(self) -> round_request_builder.RoundRequestBuilder:
        """
        Provides operations to call the round method.
        """
        from .round import round_request_builder

        return round_request_builder.RoundRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def round_down(self) -> round_down_request_builder.RoundDownRequestBuilder:
        """
        Provides operations to call the roundDown method.
        """
        from .round_down import round_down_request_builder

        return round_down_request_builder.RoundDownRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def round_up(self) -> round_up_request_builder.RoundUpRequestBuilder:
        """
        Provides operations to call the roundUp method.
        """
        from .round_up import round_up_request_builder

        return round_up_request_builder.RoundUpRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def rows(self) -> rows_request_builder.RowsRequestBuilder:
        """
        Provides operations to call the rows method.
        """
        from .rows import rows_request_builder

        return rows_request_builder.RowsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def rri(self) -> rri_request_builder.RriRequestBuilder:
        """
        Provides operations to call the rri method.
        """
        from .rri import rri_request_builder

        return rri_request_builder.RriRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sec(self) -> sec_request_builder.SecRequestBuilder:
        """
        Provides operations to call the sec method.
        """
        from .sec import sec_request_builder

        return sec_request_builder.SecRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sech(self) -> sech_request_builder.SechRequestBuilder:
        """
        Provides operations to call the sech method.
        """
        from .sech import sech_request_builder

        return sech_request_builder.SechRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def second(self) -> second_request_builder.SecondRequestBuilder:
        """
        Provides operations to call the second method.
        """
        from .second import second_request_builder

        return second_request_builder.SecondRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def series_sum(self) -> series_sum_request_builder.SeriesSumRequestBuilder:
        """
        Provides operations to call the seriesSum method.
        """
        from .series_sum import series_sum_request_builder

        return series_sum_request_builder.SeriesSumRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sheet(self) -> sheet_request_builder.SheetRequestBuilder:
        """
        Provides operations to call the sheet method.
        """
        from .sheet import sheet_request_builder

        return sheet_request_builder.SheetRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sheets(self) -> sheets_request_builder.SheetsRequestBuilder:
        """
        Provides operations to call the sheets method.
        """
        from .sheets import sheets_request_builder

        return sheets_request_builder.SheetsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sign(self) -> sign_request_builder.SignRequestBuilder:
        """
        Provides operations to call the sign method.
        """
        from .sign import sign_request_builder

        return sign_request_builder.SignRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sin(self) -> sin_request_builder.SinRequestBuilder:
        """
        Provides operations to call the sin method.
        """
        from .sin import sin_request_builder

        return sin_request_builder.SinRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sinh(self) -> sinh_request_builder.SinhRequestBuilder:
        """
        Provides operations to call the sinh method.
        """
        from .sinh import sinh_request_builder

        return sinh_request_builder.SinhRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def skew(self) -> skew_request_builder.SkewRequestBuilder:
        """
        Provides operations to call the skew method.
        """
        from .skew import skew_request_builder

        return skew_request_builder.SkewRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def skew_p(self) -> skew_p_request_builder.Skew_pRequestBuilder:
        """
        Provides operations to call the skew_p method.
        """
        from .skew_p import skew_p_request_builder

        return skew_p_request_builder.Skew_pRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sln(self) -> sln_request_builder.SlnRequestBuilder:
        """
        Provides operations to call the sln method.
        """
        from .sln import sln_request_builder

        return sln_request_builder.SlnRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def small(self) -> small_request_builder.SmallRequestBuilder:
        """
        Provides operations to call the small method.
        """
        from .small import small_request_builder

        return small_request_builder.SmallRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sqrt(self) -> sqrt_request_builder.SqrtRequestBuilder:
        """
        Provides operations to call the sqrt method.
        """
        from .sqrt import sqrt_request_builder

        return sqrt_request_builder.SqrtRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sqrt_pi(self) -> sqrt_pi_request_builder.SqrtPiRequestBuilder:
        """
        Provides operations to call the sqrtPi method.
        """
        from .sqrt_pi import sqrt_pi_request_builder

        return sqrt_pi_request_builder.SqrtPiRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def standardize(self) -> standardize_request_builder.StandardizeRequestBuilder:
        """
        Provides operations to call the standardize method.
        """
        from .standardize import standardize_request_builder

        return standardize_request_builder.StandardizeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def st_dev_p(self) -> st_dev_p_request_builder.StDev_PRequestBuilder:
        """
        Provides operations to call the stDev_P method.
        """
        from .st_dev_p import st_dev_p_request_builder

        return st_dev_p_request_builder.StDev_PRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def st_dev_s(self) -> st_dev_s_request_builder.StDev_SRequestBuilder:
        """
        Provides operations to call the stDev_S method.
        """
        from .st_dev_s import st_dev_s_request_builder

        return st_dev_s_request_builder.StDev_SRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def st_dev_a(self) -> st_dev_a_request_builder.StDevARequestBuilder:
        """
        Provides operations to call the stDevA method.
        """
        from .st_dev_a import st_dev_a_request_builder

        return st_dev_a_request_builder.StDevARequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def st_dev_p_a(self) -> st_dev_p_a_request_builder.StDevPARequestBuilder:
        """
        Provides operations to call the stDevPA method.
        """
        from .st_dev_p_a import st_dev_p_a_request_builder

        return st_dev_p_a_request_builder.StDevPARequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def substitute(self) -> substitute_request_builder.SubstituteRequestBuilder:
        """
        Provides operations to call the substitute method.
        """
        from .substitute import substitute_request_builder

        return substitute_request_builder.SubstituteRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def subtotal(self) -> subtotal_request_builder.SubtotalRequestBuilder:
        """
        Provides operations to call the subtotal method.
        """
        from .subtotal import subtotal_request_builder

        return subtotal_request_builder.SubtotalRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sum(self) -> sum_request_builder.SumRequestBuilder:
        """
        Provides operations to call the sum method.
        """
        from .sum import sum_request_builder

        return sum_request_builder.SumRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sum_if(self) -> sum_if_request_builder.SumIfRequestBuilder:
        """
        Provides operations to call the sumIf method.
        """
        from .sum_if import sum_if_request_builder

        return sum_if_request_builder.SumIfRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sum_ifs(self) -> sum_ifs_request_builder.SumIfsRequestBuilder:
        """
        Provides operations to call the sumIfs method.
        """
        from .sum_ifs import sum_ifs_request_builder

        return sum_ifs_request_builder.SumIfsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sum_sq(self) -> sum_sq_request_builder.SumSqRequestBuilder:
        """
        Provides operations to call the sumSq method.
        """
        from .sum_sq import sum_sq_request_builder

        return sum_sq_request_builder.SumSqRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def syd(self) -> syd_request_builder.SydRequestBuilder:
        """
        Provides operations to call the syd method.
        """
        from .syd import syd_request_builder

        return syd_request_builder.SydRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def t(self) -> t_request_builder.TRequestBuilder:
        """
        Provides operations to call the t method.
        """
        from .t import t_request_builder

        return t_request_builder.TRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def t_dist(self) -> t_dist_request_builder.T_DistRequestBuilder:
        """
        Provides operations to call the t_Dist method.
        """
        from .t_dist import t_dist_request_builder

        return t_dist_request_builder.T_DistRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def t_dist_2_t(self) -> t_dist_2_t_request_builder.T_Dist_2TRequestBuilder:
        """
        Provides operations to call the t_Dist_2T method.
        """
        from .t_dist_2_t import t_dist_2_t_request_builder

        return t_dist_2_t_request_builder.T_Dist_2TRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def t_dist_r_t(self) -> t_dist_r_t_request_builder.T_Dist_RTRequestBuilder:
        """
        Provides operations to call the t_Dist_RT method.
        """
        from .t_dist_r_t import t_dist_r_t_request_builder

        return t_dist_r_t_request_builder.T_Dist_RTRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def t_inv(self) -> t_inv_request_builder.T_InvRequestBuilder:
        """
        Provides operations to call the t_Inv method.
        """
        from .t_inv import t_inv_request_builder

        return t_inv_request_builder.T_InvRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def t_inv_2_t(self) -> t_inv_2_t_request_builder.T_Inv_2TRequestBuilder:
        """
        Provides operations to call the t_Inv_2T method.
        """
        from .t_inv_2_t import t_inv_2_t_request_builder

        return t_inv_2_t_request_builder.T_Inv_2TRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tan(self) -> tan_request_builder.TanRequestBuilder:
        """
        Provides operations to call the tan method.
        """
        from .tan import tan_request_builder

        return tan_request_builder.TanRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tanh(self) -> tanh_request_builder.TanhRequestBuilder:
        """
        Provides operations to call the tanh method.
        """
        from .tanh import tanh_request_builder

        return tanh_request_builder.TanhRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tbill_eq(self) -> tbill_eq_request_builder.TbillEqRequestBuilder:
        """
        Provides operations to call the tbillEq method.
        """
        from .tbill_eq import tbill_eq_request_builder

        return tbill_eq_request_builder.TbillEqRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tbill_price(self) -> tbill_price_request_builder.TbillPriceRequestBuilder:
        """
        Provides operations to call the tbillPrice method.
        """
        from .tbill_price import tbill_price_request_builder

        return tbill_price_request_builder.TbillPriceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tbill_yield(self) -> tbill_yield_request_builder.TbillYieldRequestBuilder:
        """
        Provides operations to call the tbillYield method.
        """
        from .tbill_yield import tbill_yield_request_builder

        return tbill_yield_request_builder.TbillYieldRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def text(self) -> text_request_builder.TextRequestBuilder:
        """
        Provides operations to call the text method.
        """
        from .text import text_request_builder

        return text_request_builder.TextRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def time(self) -> time_request_builder.TimeRequestBuilder:
        """
        Provides operations to call the time method.
        """
        from .time import time_request_builder

        return time_request_builder.TimeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def timevalue(self) -> timevalue_request_builder.TimevalueRequestBuilder:
        """
        Provides operations to call the timevalue method.
        """
        from .timevalue import timevalue_request_builder

        return timevalue_request_builder.TimevalueRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def today(self) -> today_request_builder.TodayRequestBuilder:
        """
        Provides operations to call the today method.
        """
        from .today import today_request_builder

        return today_request_builder.TodayRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def trim(self) -> trim_request_builder.TrimRequestBuilder:
        """
        Provides operations to call the trim method.
        """
        from .trim import trim_request_builder

        return trim_request_builder.TrimRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def trim_mean(self) -> trim_mean_request_builder.TrimMeanRequestBuilder:
        """
        Provides operations to call the trimMean method.
        """
        from .trim_mean import trim_mean_request_builder

        return trim_mean_request_builder.TrimMeanRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def true_(self) -> true_request_builder.TrueRequestBuilder:
        """
        Provides operations to call the true method.
        """
        from .true_ import true_request_builder

        return true_request_builder.TrueRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def trunc(self) -> trunc_request_builder.TruncRequestBuilder:
        """
        Provides operations to call the trunc method.
        """
        from .trunc import trunc_request_builder

        return trunc_request_builder.TruncRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def type(self) -> type_request_builder.TypeRequestBuilder:
        """
        Provides operations to call the type method.
        """
        from .type import type_request_builder

        return type_request_builder.TypeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def unichar(self) -> unichar_request_builder.UnicharRequestBuilder:
        """
        Provides operations to call the unichar method.
        """
        from .unichar import unichar_request_builder

        return unichar_request_builder.UnicharRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def unicode(self) -> unicode_request_builder.UnicodeRequestBuilder:
        """
        Provides operations to call the unicode method.
        """
        from .unicode import unicode_request_builder

        return unicode_request_builder.UnicodeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def upper(self) -> upper_request_builder.UpperRequestBuilder:
        """
        Provides operations to call the upper method.
        """
        from .upper import upper_request_builder

        return upper_request_builder.UpperRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def usdollar(self) -> usdollar_request_builder.UsdollarRequestBuilder:
        """
        Provides operations to call the usdollar method.
        """
        from .usdollar import usdollar_request_builder

        return usdollar_request_builder.UsdollarRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def value(self) -> value_request_builder.ValueRequestBuilder:
        """
        Provides operations to call the value method.
        """
        from .value import value_request_builder

        return value_request_builder.ValueRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def var_p(self) -> var_p_request_builder.Var_PRequestBuilder:
        """
        Provides operations to call the var_P method.
        """
        from .var_p import var_p_request_builder

        return var_p_request_builder.Var_PRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def var_s(self) -> var_s_request_builder.Var_SRequestBuilder:
        """
        Provides operations to call the var_S method.
        """
        from .var_s import var_s_request_builder

        return var_s_request_builder.Var_SRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def var_a(self) -> var_a_request_builder.VarARequestBuilder:
        """
        Provides operations to call the varA method.
        """
        from .var_a import var_a_request_builder

        return var_a_request_builder.VarARequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def var_p_a(self) -> var_p_a_request_builder.VarPARequestBuilder:
        """
        Provides operations to call the varPA method.
        """
        from .var_p_a import var_p_a_request_builder

        return var_p_a_request_builder.VarPARequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def vdb(self) -> vdb_request_builder.VdbRequestBuilder:
        """
        Provides operations to call the vdb method.
        """
        from .vdb import vdb_request_builder

        return vdb_request_builder.VdbRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def vlookup(self) -> vlookup_request_builder.VlookupRequestBuilder:
        """
        Provides operations to call the vlookup method.
        """
        from .vlookup import vlookup_request_builder

        return vlookup_request_builder.VlookupRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def weekday(self) -> weekday_request_builder.WeekdayRequestBuilder:
        """
        Provides operations to call the weekday method.
        """
        from .weekday import weekday_request_builder

        return weekday_request_builder.WeekdayRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def week_num(self) -> week_num_request_builder.WeekNumRequestBuilder:
        """
        Provides operations to call the weekNum method.
        """
        from .week_num import week_num_request_builder

        return week_num_request_builder.WeekNumRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def weibull_dist(self) -> weibull_dist_request_builder.Weibull_DistRequestBuilder:
        """
        Provides operations to call the weibull_Dist method.
        """
        from .weibull_dist import weibull_dist_request_builder

        return weibull_dist_request_builder.Weibull_DistRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def work_day(self) -> work_day_request_builder.WorkDayRequestBuilder:
        """
        Provides operations to call the workDay method.
        """
        from .work_day import work_day_request_builder

        return work_day_request_builder.WorkDayRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def work_day_intl(self) -> work_day_intl_request_builder.WorkDay_IntlRequestBuilder:
        """
        Provides operations to call the workDay_Intl method.
        """
        from .work_day_intl import work_day_intl_request_builder

        return work_day_intl_request_builder.WorkDay_IntlRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def xirr(self) -> xirr_request_builder.XirrRequestBuilder:
        """
        Provides operations to call the xirr method.
        """
        from .xirr import xirr_request_builder

        return xirr_request_builder.XirrRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def xnpv(self) -> xnpv_request_builder.XnpvRequestBuilder:
        """
        Provides operations to call the xnpv method.
        """
        from .xnpv import xnpv_request_builder

        return xnpv_request_builder.XnpvRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def xor(self) -> xor_request_builder.XorRequestBuilder:
        """
        Provides operations to call the xor method.
        """
        from .xor import xor_request_builder

        return xor_request_builder.XorRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def year(self) -> year_request_builder.YearRequestBuilder:
        """
        Provides operations to call the year method.
        """
        from .year import year_request_builder

        return year_request_builder.YearRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def year_frac(self) -> year_frac_request_builder.YearFracRequestBuilder:
        """
        Provides operations to call the yearFrac method.
        """
        from .year_frac import year_frac_request_builder

        return year_frac_request_builder.YearFracRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def yield_(self) -> yield_request_builder.YieldRequestBuilder:
        """
        Provides operations to call the yield method.
        """
        from .yield_ import yield_request_builder

        return yield_request_builder.YieldRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def yield_disc(self) -> yield_disc_request_builder.YieldDiscRequestBuilder:
        """
        Provides operations to call the yieldDisc method.
        """
        from .yield_disc import yield_disc_request_builder

        return yield_disc_request_builder.YieldDiscRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def yield_mat(self) -> yield_mat_request_builder.YieldMatRequestBuilder:
        """
        Provides operations to call the yieldMat method.
        """
        from .yield_mat import yield_mat_request_builder

        return yield_mat_request_builder.YieldMatRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def z_test(self) -> z_test_request_builder.Z_TestRequestBuilder:
        """
        Provides operations to call the z_Test method.
        """
        from .z_test import z_test_request_builder

        return z_test_request_builder.Z_TestRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class FunctionsRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class FunctionsRequestBuilderGetQueryParameters():
        """
        Get functions from drives
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            Args:
                originalName: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise Exception("original_name cannot be undefined")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    @dataclass
    class FunctionsRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[FunctionsRequestBuilder.FunctionsRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class FunctionsRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

