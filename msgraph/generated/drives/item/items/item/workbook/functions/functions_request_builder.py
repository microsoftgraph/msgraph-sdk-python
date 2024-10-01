from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.default_query_parameters import QueryParameters
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from .......models.o_data_errors.o_data_error import ODataError
    from .......models.workbook_functions import WorkbookFunctions
    from .abs.abs_request_builder import AbsRequestBuilder
    from .accr_int.accr_int_request_builder import AccrIntRequestBuilder
    from .accr_int_m.accr_int_m_request_builder import AccrIntMRequestBuilder
    from .acos.acos_request_builder import AcosRequestBuilder
    from .acosh.acosh_request_builder import AcoshRequestBuilder
    from .acot.acot_request_builder import AcotRequestBuilder
    from .acoth.acoth_request_builder import AcothRequestBuilder
    from .amor_degrc.amor_degrc_request_builder import AmorDegrcRequestBuilder
    from .amor_linc.amor_linc_request_builder import AmorLincRequestBuilder
    from .and_.and_request_builder import AndRequestBuilder
    from .arabic.arabic_request_builder import ArabicRequestBuilder
    from .areas.areas_request_builder import AreasRequestBuilder
    from .asc.asc_request_builder import AscRequestBuilder
    from .asin.asin_request_builder import AsinRequestBuilder
    from .asinh.asinh_request_builder import AsinhRequestBuilder
    from .atan.atan_request_builder import AtanRequestBuilder
    from .atan2.atan2_request_builder import Atan2RequestBuilder
    from .atanh.atanh_request_builder import AtanhRequestBuilder
    from .average.average_request_builder import AverageRequestBuilder
    from .average_a.average_a_request_builder import AverageARequestBuilder
    from .average_if.average_if_request_builder import AverageIfRequestBuilder
    from .average_ifs.average_ifs_request_builder import AverageIfsRequestBuilder
    from .ave_dev.ave_dev_request_builder import AveDevRequestBuilder
    from .baht_text.baht_text_request_builder import BahtTextRequestBuilder
    from .base.base_request_builder_ import BaseRequestBuilder_
    from .bessel_i.bessel_i_request_builder import BesselIRequestBuilder
    from .bessel_j.bessel_j_request_builder import BesselJRequestBuilder
    from .bessel_k.bessel_k_request_builder import BesselKRequestBuilder
    from .bessel_y.bessel_y_request_builder import BesselYRequestBuilder
    from .beta_dist.beta_dist_request_builder import Beta_DistRequestBuilder
    from .beta_inv.beta_inv_request_builder import Beta_InvRequestBuilder
    from .bin2_dec.bin2_dec_request_builder import Bin2DecRequestBuilder
    from .bin2_hex.bin2_hex_request_builder import Bin2HexRequestBuilder
    from .bin2_oct.bin2_oct_request_builder import Bin2OctRequestBuilder
    from .binom_dist.binom_dist_request_builder import Binom_DistRequestBuilder
    from .binom_dist_range.binom_dist_range_request_builder import Binom_Dist_RangeRequestBuilder
    from .binom_inv.binom_inv_request_builder import Binom_InvRequestBuilder
    from .bitand.bitand_request_builder import BitandRequestBuilder
    from .bitlshift.bitlshift_request_builder import BitlshiftRequestBuilder
    from .bitor.bitor_request_builder import BitorRequestBuilder
    from .bitrshift.bitrshift_request_builder import BitrshiftRequestBuilder
    from .bitxor.bitxor_request_builder import BitxorRequestBuilder
    from .ceiling_math.ceiling_math_request_builder import Ceiling_MathRequestBuilder
    from .ceiling_precise.ceiling_precise_request_builder import Ceiling_PreciseRequestBuilder
    from .char.char_request_builder import CharRequestBuilder
    from .chi_sq_dist.chi_sq_dist_request_builder import ChiSq_DistRequestBuilder
    from .chi_sq_dist_r_t.chi_sq_dist_r_t_request_builder import ChiSq_Dist_RTRequestBuilder
    from .chi_sq_inv.chi_sq_inv_request_builder import ChiSq_InvRequestBuilder
    from .chi_sq_inv_r_t.chi_sq_inv_r_t_request_builder import ChiSq_Inv_RTRequestBuilder
    from .choose.choose_request_builder import ChooseRequestBuilder
    from .clean.clean_request_builder import CleanRequestBuilder
    from .code.code_request_builder import CodeRequestBuilder
    from .columns.columns_request_builder import ColumnsRequestBuilder
    from .combin.combin_request_builder import CombinRequestBuilder
    from .combina.combina_request_builder import CombinaRequestBuilder
    from .complex.complex_request_builder import ComplexRequestBuilder
    from .concatenate.concatenate_request_builder import ConcatenateRequestBuilder
    from .confidence_norm.confidence_norm_request_builder import Confidence_NormRequestBuilder
    from .confidence_t.confidence_t_request_builder import Confidence_TRequestBuilder
    from .convert.convert_request_builder import ConvertRequestBuilder
    from .cos.cos_request_builder import CosRequestBuilder
    from .cosh.cosh_request_builder import CoshRequestBuilder
    from .cot.cot_request_builder import CotRequestBuilder
    from .coth.coth_request_builder import CothRequestBuilder
    from .count.count_request_builder import CountRequestBuilder
    from .count_a.count_a_request_builder import CountARequestBuilder
    from .count_blank.count_blank_request_builder import CountBlankRequestBuilder
    from .count_if.count_if_request_builder import CountIfRequestBuilder
    from .count_ifs.count_ifs_request_builder import CountIfsRequestBuilder
    from .coup_days.coup_days_request_builder import CoupDaysRequestBuilder
    from .coup_days_nc.coup_days_nc_request_builder import CoupDaysNcRequestBuilder
    from .coup_day_bs.coup_day_bs_request_builder import CoupDayBsRequestBuilder
    from .coup_ncd.coup_ncd_request_builder import CoupNcdRequestBuilder
    from .coup_num.coup_num_request_builder import CoupNumRequestBuilder
    from .coup_pcd.coup_pcd_request_builder import CoupPcdRequestBuilder
    from .csc.csc_request_builder import CscRequestBuilder
    from .csch.csch_request_builder import CschRequestBuilder
    from .cum_i_pmt.cum_i_pmt_request_builder import CumIPmtRequestBuilder
    from .cum_princ.cum_princ_request_builder import CumPrincRequestBuilder
    from .date.date_request_builder import DateRequestBuilder
    from .datevalue.datevalue_request_builder import DatevalueRequestBuilder
    from .daverage.daverage_request_builder import DaverageRequestBuilder
    from .day.day_request_builder import DayRequestBuilder
    from .days.days_request_builder import DaysRequestBuilder
    from .days360.days360_request_builder import Days360RequestBuilder
    from .db.db_request_builder import DbRequestBuilder
    from .dbcs.dbcs_request_builder import DbcsRequestBuilder
    from .dcount.dcount_request_builder import DcountRequestBuilder
    from .dcount_a.dcount_a_request_builder import DcountARequestBuilder
    from .ddb.ddb_request_builder import DdbRequestBuilder
    from .dec2_bin.dec2_bin_request_builder import Dec2BinRequestBuilder
    from .dec2_hex.dec2_hex_request_builder import Dec2HexRequestBuilder
    from .dec2_oct.dec2_oct_request_builder import Dec2OctRequestBuilder
    from .decimal.decimal_request_builder import DecimalRequestBuilder
    from .degrees.degrees_request_builder import DegreesRequestBuilder
    from .delta.delta_request_builder import DeltaRequestBuilder
    from .dev_sq.dev_sq_request_builder import DevSqRequestBuilder
    from .dget.dget_request_builder import DgetRequestBuilder
    from .disc.disc_request_builder import DiscRequestBuilder
    from .dmax.dmax_request_builder import DmaxRequestBuilder
    from .dmin.dmin_request_builder import DminRequestBuilder
    from .dollar.dollar_request_builder import DollarRequestBuilder
    from .dollar_de.dollar_de_request_builder import DollarDeRequestBuilder
    from .dollar_fr.dollar_fr_request_builder import DollarFrRequestBuilder
    from .dproduct.dproduct_request_builder import DproductRequestBuilder
    from .dst_dev.dst_dev_request_builder import DstDevRequestBuilder
    from .dst_dev_p.dst_dev_p_request_builder import DstDevPRequestBuilder
    from .dsum.dsum_request_builder import DsumRequestBuilder
    from .duration.duration_request_builder import DurationRequestBuilder
    from .dvar.dvar_request_builder import DvarRequestBuilder
    from .dvar_p.dvar_p_request_builder import DvarPRequestBuilder
    from .ecma_ceiling.ecma_ceiling_request_builder import Ecma_CeilingRequestBuilder
    from .edate.edate_request_builder import EdateRequestBuilder
    from .effect.effect_request_builder import EffectRequestBuilder
    from .eo_month.eo_month_request_builder import EoMonthRequestBuilder
    from .erf.erf_request_builder import ErfRequestBuilder
    from .erf_c.erf_c_request_builder import ErfCRequestBuilder
    from .erf_c_precise.erf_c_precise_request_builder import ErfC_PreciseRequestBuilder
    from .erf_precise.erf_precise_request_builder import Erf_PreciseRequestBuilder
    from .error_type.error_type_request_builder import Error_TypeRequestBuilder
    from .even.even_request_builder import EvenRequestBuilder
    from .exact.exact_request_builder import ExactRequestBuilder
    from .exp.exp_request_builder import ExpRequestBuilder
    from .expon_dist.expon_dist_request_builder import Expon_DistRequestBuilder
    from .fact.fact_request_builder import FactRequestBuilder
    from .fact_double.fact_double_request_builder import FactDoubleRequestBuilder
    from .false_.false_request_builder import FalseRequestBuilder
    from .find.find_request_builder import FindRequestBuilder
    from .find_b.find_b_request_builder import FindBRequestBuilder
    from .fisher.fisher_request_builder import FisherRequestBuilder
    from .fisher_inv.fisher_inv_request_builder import FisherInvRequestBuilder
    from .fixed.fixed_request_builder import FixedRequestBuilder
    from .floor_math.floor_math_request_builder import Floor_MathRequestBuilder
    from .floor_precise.floor_precise_request_builder import Floor_PreciseRequestBuilder
    from .fv.fv_request_builder import FvRequestBuilder
    from .fvschedule.fvschedule_request_builder import FvscheduleRequestBuilder
    from .f_dist.f_dist_request_builder import F_DistRequestBuilder
    from .f_dist_r_t.f_dist_r_t_request_builder import F_Dist_RTRequestBuilder
    from .f_inv.f_inv_request_builder import F_InvRequestBuilder
    from .f_inv_r_t.f_inv_r_t_request_builder import F_Inv_RTRequestBuilder
    from .gamma.gamma_request_builder import GammaRequestBuilder
    from .gamma_dist.gamma_dist_request_builder import Gamma_DistRequestBuilder
    from .gamma_inv.gamma_inv_request_builder import Gamma_InvRequestBuilder
    from .gamma_ln.gamma_ln_request_builder import GammaLnRequestBuilder
    from .gamma_ln_precise.gamma_ln_precise_request_builder import GammaLn_PreciseRequestBuilder
    from .gauss.gauss_request_builder import GaussRequestBuilder
    from .gcd.gcd_request_builder import GcdRequestBuilder
    from .geo_mean.geo_mean_request_builder import GeoMeanRequestBuilder
    from .ge_step.ge_step_request_builder import GeStepRequestBuilder
    from .har_mean.har_mean_request_builder import HarMeanRequestBuilder
    from .hex2_bin.hex2_bin_request_builder import Hex2BinRequestBuilder
    from .hex2_dec.hex2_dec_request_builder import Hex2DecRequestBuilder
    from .hex2_oct.hex2_oct_request_builder import Hex2OctRequestBuilder
    from .hlookup.hlookup_request_builder import HlookupRequestBuilder
    from .hour.hour_request_builder import HourRequestBuilder
    from .hyperlink.hyperlink_request_builder import HyperlinkRequestBuilder
    from .hyp_geom_dist.hyp_geom_dist_request_builder import HypGeom_DistRequestBuilder
    from .if_.if_request_builder import IfRequestBuilder
    from .imaginary.imaginary_request_builder import ImaginaryRequestBuilder
    from .im_abs.im_abs_request_builder import ImAbsRequestBuilder
    from .im_argument.im_argument_request_builder import ImArgumentRequestBuilder
    from .im_conjugate.im_conjugate_request_builder import ImConjugateRequestBuilder
    from .im_cos.im_cos_request_builder import ImCosRequestBuilder
    from .im_cosh.im_cosh_request_builder import ImCoshRequestBuilder
    from .im_cot.im_cot_request_builder import ImCotRequestBuilder
    from .im_csc.im_csc_request_builder import ImCscRequestBuilder
    from .im_csch.im_csch_request_builder import ImCschRequestBuilder
    from .im_div.im_div_request_builder import ImDivRequestBuilder
    from .im_exp.im_exp_request_builder import ImExpRequestBuilder
    from .im_ln.im_ln_request_builder import ImLnRequestBuilder
    from .im_log10.im_log10_request_builder import ImLog10RequestBuilder
    from .im_log2.im_log2_request_builder import ImLog2RequestBuilder
    from .im_power.im_power_request_builder import ImPowerRequestBuilder
    from .im_product.im_product_request_builder import ImProductRequestBuilder
    from .im_real.im_real_request_builder import ImRealRequestBuilder
    from .im_sec.im_sec_request_builder import ImSecRequestBuilder
    from .im_sech.im_sech_request_builder import ImSechRequestBuilder
    from .im_sin.im_sin_request_builder import ImSinRequestBuilder
    from .im_sinh.im_sinh_request_builder import ImSinhRequestBuilder
    from .im_sqrt.im_sqrt_request_builder import ImSqrtRequestBuilder
    from .im_sub.im_sub_request_builder import ImSubRequestBuilder
    from .im_sum.im_sum_request_builder import ImSumRequestBuilder
    from .im_tan.im_tan_request_builder import ImTanRequestBuilder
    from .int.int_request_builder import IntRequestBuilder
    from .int_rate.int_rate_request_builder import IntRateRequestBuilder
    from .ipmt.ipmt_request_builder import IpmtRequestBuilder
    from .irr.irr_request_builder import IrrRequestBuilder
    from .iso_ceiling.iso_ceiling_request_builder import Iso_CeilingRequestBuilder
    from .iso_week_num.iso_week_num_request_builder import IsoWeekNumRequestBuilder
    from .ispmt.ispmt_request_builder import IspmtRequestBuilder
    from .isref.isref_request_builder import IsrefRequestBuilder
    from .is_err.is_err_request_builder import IsErrRequestBuilder
    from .is_error.is_error_request_builder import IsErrorRequestBuilder
    from .is_even.is_even_request_builder import IsEvenRequestBuilder
    from .is_formula.is_formula_request_builder import IsFormulaRequestBuilder
    from .is_logical.is_logical_request_builder import IsLogicalRequestBuilder
    from .is_non_text.is_non_text_request_builder import IsNonTextRequestBuilder
    from .is_number.is_number_request_builder import IsNumberRequestBuilder
    from .is_n_a.is_n_a_request_builder import IsNARequestBuilder
    from .is_odd.is_odd_request_builder import IsOddRequestBuilder
    from .is_text.is_text_request_builder import IsTextRequestBuilder
    from .kurt.kurt_request_builder import KurtRequestBuilder
    from .large.large_request_builder import LargeRequestBuilder
    from .lcm.lcm_request_builder import LcmRequestBuilder
    from .left.left_request_builder import LeftRequestBuilder
    from .leftb.leftb_request_builder import LeftbRequestBuilder
    from .len.len_request_builder import LenRequestBuilder
    from .lenb.lenb_request_builder import LenbRequestBuilder
    from .ln.ln_request_builder import LnRequestBuilder
    from .log.log_request_builder import LogRequestBuilder
    from .log10.log10_request_builder import Log10RequestBuilder
    from .log_norm_dist.log_norm_dist_request_builder import LogNorm_DistRequestBuilder
    from .log_norm_inv.log_norm_inv_request_builder import LogNorm_InvRequestBuilder
    from .lookup.lookup_request_builder import LookupRequestBuilder
    from .lower.lower_request_builder import LowerRequestBuilder
    from .match.match_request_builder import MatchRequestBuilder
    from .max.max_request_builder import MaxRequestBuilder
    from .max_a.max_a_request_builder import MaxARequestBuilder
    from .mduration.mduration_request_builder import MdurationRequestBuilder
    from .median.median_request_builder import MedianRequestBuilder
    from .mid.mid_request_builder import MidRequestBuilder
    from .midb.midb_request_builder import MidbRequestBuilder
    from .min.min_request_builder import MinRequestBuilder
    from .minute.minute_request_builder import MinuteRequestBuilder
    from .min_a.min_a_request_builder import MinARequestBuilder
    from .mirr.mirr_request_builder import MirrRequestBuilder
    from .mod.mod_request_builder import ModRequestBuilder
    from .month.month_request_builder import MonthRequestBuilder
    from .mround.mround_request_builder import MroundRequestBuilder
    from .multi_nomial.multi_nomial_request_builder import MultiNomialRequestBuilder
    from .n.n_request_builder import NRequestBuilder
    from .na.na_request_builder import NaRequestBuilder
    from .neg_binom_dist.neg_binom_dist_request_builder import NegBinom_DistRequestBuilder
    from .network_days.network_days_request_builder import NetworkDaysRequestBuilder
    from .network_days_intl.network_days_intl_request_builder import NetworkDays_IntlRequestBuilder
    from .nominal.nominal_request_builder import NominalRequestBuilder
    from .norm_dist.norm_dist_request_builder import Norm_DistRequestBuilder
    from .norm_inv.norm_inv_request_builder import Norm_InvRequestBuilder
    from .norm_s_dist.norm_s_dist_request_builder import Norm_S_DistRequestBuilder
    from .norm_s_inv.norm_s_inv_request_builder import Norm_S_InvRequestBuilder
    from .not_.not_request_builder import NotRequestBuilder
    from .now.now_request_builder import NowRequestBuilder
    from .nper.nper_request_builder import NperRequestBuilder
    from .npv.npv_request_builder import NpvRequestBuilder
    from .number_value.number_value_request_builder import NumberValueRequestBuilder
    from .oct2_bin.oct2_bin_request_builder import Oct2BinRequestBuilder
    from .oct2_dec.oct2_dec_request_builder import Oct2DecRequestBuilder
    from .oct2_hex.oct2_hex_request_builder import Oct2HexRequestBuilder
    from .odd.odd_request_builder import OddRequestBuilder
    from .odd_f_price.odd_f_price_request_builder import OddFPriceRequestBuilder
    from .odd_f_yield.odd_f_yield_request_builder import OddFYieldRequestBuilder
    from .odd_l_price.odd_l_price_request_builder import OddLPriceRequestBuilder
    from .odd_l_yield.odd_l_yield_request_builder import OddLYieldRequestBuilder
    from .or_.or_request_builder import OrRequestBuilder
    from .pduration.pduration_request_builder import PdurationRequestBuilder
    from .percentile_exc.percentile_exc_request_builder import Percentile_ExcRequestBuilder
    from .percentile_inc.percentile_inc_request_builder import Percentile_IncRequestBuilder
    from .percent_rank_exc.percent_rank_exc_request_builder import PercentRank_ExcRequestBuilder
    from .percent_rank_inc.percent_rank_inc_request_builder import PercentRank_IncRequestBuilder
    from .permut.permut_request_builder import PermutRequestBuilder
    from .permutationa.permutationa_request_builder import PermutationaRequestBuilder
    from .phi.phi_request_builder import PhiRequestBuilder
    from .pi.pi_request_builder import PiRequestBuilder
    from .pmt.pmt_request_builder import PmtRequestBuilder
    from .poisson_dist.poisson_dist_request_builder import Poisson_DistRequestBuilder
    from .power.power_request_builder import PowerRequestBuilder
    from .ppmt.ppmt_request_builder import PpmtRequestBuilder
    from .price.price_request_builder import PriceRequestBuilder
    from .price_disc.price_disc_request_builder import PriceDiscRequestBuilder
    from .price_mat.price_mat_request_builder import PriceMatRequestBuilder
    from .product.product_request_builder import ProductRequestBuilder
    from .proper.proper_request_builder import ProperRequestBuilder
    from .pv.pv_request_builder import PvRequestBuilder
    from .quartile_exc.quartile_exc_request_builder import Quartile_ExcRequestBuilder
    from .quartile_inc.quartile_inc_request_builder import Quartile_IncRequestBuilder
    from .quotient.quotient_request_builder import QuotientRequestBuilder
    from .radians.radians_request_builder import RadiansRequestBuilder
    from .rand.rand_request_builder import RandRequestBuilder
    from .rand_between.rand_between_request_builder import RandBetweenRequestBuilder
    from .rank_avg.rank_avg_request_builder import Rank_AvgRequestBuilder
    from .rank_eq.rank_eq_request_builder import Rank_EqRequestBuilder
    from .rate.rate_request_builder import RateRequestBuilder
    from .received.received_request_builder import ReceivedRequestBuilder
    from .replace.replace_request_builder import ReplaceRequestBuilder
    from .replace_b.replace_b_request_builder import ReplaceBRequestBuilder
    from .rept.rept_request_builder import ReptRequestBuilder
    from .right.right_request_builder import RightRequestBuilder
    from .rightb.rightb_request_builder import RightbRequestBuilder
    from .roman.roman_request_builder import RomanRequestBuilder
    from .round.round_request_builder import RoundRequestBuilder
    from .round_down.round_down_request_builder import RoundDownRequestBuilder
    from .round_up.round_up_request_builder import RoundUpRequestBuilder
    from .rows.rows_request_builder import RowsRequestBuilder
    from .rri.rri_request_builder import RriRequestBuilder
    from .sec.sec_request_builder import SecRequestBuilder
    from .sech.sech_request_builder import SechRequestBuilder
    from .second.second_request_builder import SecondRequestBuilder
    from .series_sum.series_sum_request_builder import SeriesSumRequestBuilder
    from .sheet.sheet_request_builder import SheetRequestBuilder
    from .sheets.sheets_request_builder import SheetsRequestBuilder
    from .sign.sign_request_builder import SignRequestBuilder
    from .sin.sin_request_builder import SinRequestBuilder
    from .sinh.sinh_request_builder import SinhRequestBuilder
    from .skew.skew_request_builder import SkewRequestBuilder
    from .skew_p.skew_p_request_builder import Skew_pRequestBuilder
    from .sln.sln_request_builder import SlnRequestBuilder
    from .small.small_request_builder import SmallRequestBuilder
    from .sqrt.sqrt_request_builder import SqrtRequestBuilder
    from .sqrt_pi.sqrt_pi_request_builder import SqrtPiRequestBuilder
    from .standardize.standardize_request_builder import StandardizeRequestBuilder
    from .st_dev_a.st_dev_a_request_builder import StDevARequestBuilder
    from .st_dev_p.st_dev_p_request_builder import StDev_PRequestBuilder
    from .st_dev_p_a.st_dev_p_a_request_builder import StDevPARequestBuilder
    from .st_dev_s.st_dev_s_request_builder import StDev_SRequestBuilder
    from .substitute.substitute_request_builder import SubstituteRequestBuilder
    from .subtotal.subtotal_request_builder import SubtotalRequestBuilder
    from .sum.sum_request_builder import SumRequestBuilder
    from .sum_if.sum_if_request_builder import SumIfRequestBuilder
    from .sum_ifs.sum_ifs_request_builder import SumIfsRequestBuilder
    from .sum_sq.sum_sq_request_builder import SumSqRequestBuilder
    from .syd.syd_request_builder import SydRequestBuilder
    from .t.t_request_builder import TRequestBuilder
    from .tan.tan_request_builder import TanRequestBuilder
    from .tanh.tanh_request_builder import TanhRequestBuilder
    from .tbill_eq.tbill_eq_request_builder import TbillEqRequestBuilder
    from .tbill_price.tbill_price_request_builder import TbillPriceRequestBuilder
    from .tbill_yield.tbill_yield_request_builder import TbillYieldRequestBuilder
    from .text.text_request_builder import TextRequestBuilder
    from .time.time_request_builder import TimeRequestBuilder
    from .timevalue.timevalue_request_builder import TimevalueRequestBuilder
    from .today.today_request_builder import TodayRequestBuilder
    from .trim.trim_request_builder import TrimRequestBuilder
    from .trim_mean.trim_mean_request_builder import TrimMeanRequestBuilder
    from .true_.true_request_builder import TrueRequestBuilder
    from .trunc.trunc_request_builder import TruncRequestBuilder
    from .type.type_request_builder import TypeRequestBuilder
    from .t_dist.t_dist_request_builder import T_DistRequestBuilder
    from .t_dist_2_t.t_dist_2_t_request_builder import T_Dist_2TRequestBuilder
    from .t_dist_r_t.t_dist_r_t_request_builder import T_Dist_RTRequestBuilder
    from .t_inv.t_inv_request_builder import T_InvRequestBuilder
    from .t_inv_2_t.t_inv_2_t_request_builder import T_Inv_2TRequestBuilder
    from .unichar.unichar_request_builder import UnicharRequestBuilder
    from .unicode.unicode_request_builder import UnicodeRequestBuilder
    from .upper.upper_request_builder import UpperRequestBuilder
    from .usdollar.usdollar_request_builder import UsdollarRequestBuilder
    from .value.value_request_builder import ValueRequestBuilder
    from .var_a.var_a_request_builder import VarARequestBuilder
    from .var_p.var_p_request_builder import Var_PRequestBuilder
    from .var_p_a.var_p_a_request_builder import VarPARequestBuilder
    from .var_s.var_s_request_builder import Var_SRequestBuilder
    from .vdb.vdb_request_builder import VdbRequestBuilder
    from .vlookup.vlookup_request_builder import VlookupRequestBuilder
    from .weekday.weekday_request_builder import WeekdayRequestBuilder
    from .week_num.week_num_request_builder import WeekNumRequestBuilder
    from .weibull_dist.weibull_dist_request_builder import Weibull_DistRequestBuilder
    from .work_day.work_day_request_builder import WorkDayRequestBuilder
    from .work_day_intl.work_day_intl_request_builder import WorkDay_IntlRequestBuilder
    from .xirr.xirr_request_builder import XirrRequestBuilder
    from .xnpv.xnpv_request_builder import XnpvRequestBuilder
    from .xor.xor_request_builder import XorRequestBuilder
    from .year.year_request_builder import YearRequestBuilder
    from .year_frac.year_frac_request_builder import YearFracRequestBuilder
    from .yield_.yield_request_builder import YieldRequestBuilder
    from .yield_disc.yield_disc_request_builder import YieldDiscRequestBuilder
    from .yield_mat.yield_mat_request_builder import YieldMatRequestBuilder
    from .z_test.z_test_request_builder import Z_TestRequestBuilder

class FunctionsRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the functions property of the microsoft.graph.workbook entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new FunctionsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/drives/{drive%2Did}/items/{driveItem%2Did}/workbook/functions{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete navigation property functions for drives
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[FunctionsRequestBuilderGetQueryParameters]] = None) -> Optional[WorkbookFunctions]:
        """
        Get functions from drives
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WorkbookFunctions]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .......models.workbook_functions import WorkbookFunctions

        return await self.request_adapter.send_async(request_info, WorkbookFunctions, error_mapping)
    
    async def patch(self,body: WorkbookFunctions, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[WorkbookFunctions]:
        """
        Update the navigation property functions in drives
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WorkbookFunctions]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .......models.workbook_functions import WorkbookFunctions

        return await self.request_adapter.send_async(request_info, WorkbookFunctions, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete navigation property functions for drives
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[FunctionsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Get functions from drives
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: WorkbookFunctions, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property functions in drives
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PATCH, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> FunctionsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: FunctionsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return FunctionsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def abs(self) -> AbsRequestBuilder:
        """
        Provides operations to call the abs method.
        """
        from .abs.abs_request_builder import AbsRequestBuilder

        return AbsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def accr_int(self) -> AccrIntRequestBuilder:
        """
        Provides operations to call the accrInt method.
        """
        from .accr_int.accr_int_request_builder import AccrIntRequestBuilder

        return AccrIntRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def accr_int_m(self) -> AccrIntMRequestBuilder:
        """
        Provides operations to call the accrIntM method.
        """
        from .accr_int_m.accr_int_m_request_builder import AccrIntMRequestBuilder

        return AccrIntMRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def acos(self) -> AcosRequestBuilder:
        """
        Provides operations to call the acos method.
        """
        from .acos.acos_request_builder import AcosRequestBuilder

        return AcosRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def acosh(self) -> AcoshRequestBuilder:
        """
        Provides operations to call the acosh method.
        """
        from .acosh.acosh_request_builder import AcoshRequestBuilder

        return AcoshRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def acot(self) -> AcotRequestBuilder:
        """
        Provides operations to call the acot method.
        """
        from .acot.acot_request_builder import AcotRequestBuilder

        return AcotRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def acoth(self) -> AcothRequestBuilder:
        """
        Provides operations to call the acoth method.
        """
        from .acoth.acoth_request_builder import AcothRequestBuilder

        return AcothRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def amor_degrc(self) -> AmorDegrcRequestBuilder:
        """
        Provides operations to call the amorDegrc method.
        """
        from .amor_degrc.amor_degrc_request_builder import AmorDegrcRequestBuilder

        return AmorDegrcRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def amor_linc(self) -> AmorLincRequestBuilder:
        """
        Provides operations to call the amorLinc method.
        """
        from .amor_linc.amor_linc_request_builder import AmorLincRequestBuilder

        return AmorLincRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def and_(self) -> AndRequestBuilder:
        """
        Provides operations to call the and method.
        """
        from .and_.and_request_builder import AndRequestBuilder

        return AndRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def arabic(self) -> ArabicRequestBuilder:
        """
        Provides operations to call the arabic method.
        """
        from .arabic.arabic_request_builder import ArabicRequestBuilder

        return ArabicRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def areas(self) -> AreasRequestBuilder:
        """
        Provides operations to call the areas method.
        """
        from .areas.areas_request_builder import AreasRequestBuilder

        return AreasRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def asc(self) -> AscRequestBuilder:
        """
        Provides operations to call the asc method.
        """
        from .asc.asc_request_builder import AscRequestBuilder

        return AscRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def asin(self) -> AsinRequestBuilder:
        """
        Provides operations to call the asin method.
        """
        from .asin.asin_request_builder import AsinRequestBuilder

        return AsinRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def asinh(self) -> AsinhRequestBuilder:
        """
        Provides operations to call the asinh method.
        """
        from .asinh.asinh_request_builder import AsinhRequestBuilder

        return AsinhRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def atan(self) -> AtanRequestBuilder:
        """
        Provides operations to call the atan method.
        """
        from .atan.atan_request_builder import AtanRequestBuilder

        return AtanRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def atan2(self) -> Atan2RequestBuilder:
        """
        Provides operations to call the atan2 method.
        """
        from .atan2.atan2_request_builder import Atan2RequestBuilder

        return Atan2RequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def atanh(self) -> AtanhRequestBuilder:
        """
        Provides operations to call the atanh method.
        """
        from .atanh.atanh_request_builder import AtanhRequestBuilder

        return AtanhRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def ave_dev(self) -> AveDevRequestBuilder:
        """
        Provides operations to call the aveDev method.
        """
        from .ave_dev.ave_dev_request_builder import AveDevRequestBuilder

        return AveDevRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def average(self) -> AverageRequestBuilder:
        """
        Provides operations to call the average method.
        """
        from .average.average_request_builder import AverageRequestBuilder

        return AverageRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def average_a(self) -> AverageARequestBuilder:
        """
        Provides operations to call the averageA method.
        """
        from .average_a.average_a_request_builder import AverageARequestBuilder

        return AverageARequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def average_if(self) -> AverageIfRequestBuilder:
        """
        Provides operations to call the averageIf method.
        """
        from .average_if.average_if_request_builder import AverageIfRequestBuilder

        return AverageIfRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def average_ifs(self) -> AverageIfsRequestBuilder:
        """
        Provides operations to call the averageIfs method.
        """
        from .average_ifs.average_ifs_request_builder import AverageIfsRequestBuilder

        return AverageIfsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def baht_text(self) -> BahtTextRequestBuilder:
        """
        Provides operations to call the bahtText method.
        """
        from .baht_text.baht_text_request_builder import BahtTextRequestBuilder

        return BahtTextRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def base(self) -> BaseRequestBuilder_:
        """
        Provides operations to call the base method.
        """
        from .base.base_request_builder_ import BaseRequestBuilder_

        return BaseRequestBuilder_(self.request_adapter, self.path_parameters)
    
    @property
    def bessel_i(self) -> BesselIRequestBuilder:
        """
        Provides operations to call the besselI method.
        """
        from .bessel_i.bessel_i_request_builder import BesselIRequestBuilder

        return BesselIRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def bessel_j(self) -> BesselJRequestBuilder:
        """
        Provides operations to call the besselJ method.
        """
        from .bessel_j.bessel_j_request_builder import BesselJRequestBuilder

        return BesselJRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def bessel_k(self) -> BesselKRequestBuilder:
        """
        Provides operations to call the besselK method.
        """
        from .bessel_k.bessel_k_request_builder import BesselKRequestBuilder

        return BesselKRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def bessel_y(self) -> BesselYRequestBuilder:
        """
        Provides operations to call the besselY method.
        """
        from .bessel_y.bessel_y_request_builder import BesselYRequestBuilder

        return BesselYRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def beta_dist(self) -> Beta_DistRequestBuilder:
        """
        Provides operations to call the beta_Dist method.
        """
        from .beta_dist.beta_dist_request_builder import Beta_DistRequestBuilder

        return Beta_DistRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def beta_inv(self) -> Beta_InvRequestBuilder:
        """
        Provides operations to call the beta_Inv method.
        """
        from .beta_inv.beta_inv_request_builder import Beta_InvRequestBuilder

        return Beta_InvRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def bin2_dec(self) -> Bin2DecRequestBuilder:
        """
        Provides operations to call the bin2Dec method.
        """
        from .bin2_dec.bin2_dec_request_builder import Bin2DecRequestBuilder

        return Bin2DecRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def bin2_hex(self) -> Bin2HexRequestBuilder:
        """
        Provides operations to call the bin2Hex method.
        """
        from .bin2_hex.bin2_hex_request_builder import Bin2HexRequestBuilder

        return Bin2HexRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def bin2_oct(self) -> Bin2OctRequestBuilder:
        """
        Provides operations to call the bin2Oct method.
        """
        from .bin2_oct.bin2_oct_request_builder import Bin2OctRequestBuilder

        return Bin2OctRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def binom_dist(self) -> Binom_DistRequestBuilder:
        """
        Provides operations to call the binom_Dist method.
        """
        from .binom_dist.binom_dist_request_builder import Binom_DistRequestBuilder

        return Binom_DistRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def binom_dist_range(self) -> Binom_Dist_RangeRequestBuilder:
        """
        Provides operations to call the binom_Dist_Range method.
        """
        from .binom_dist_range.binom_dist_range_request_builder import Binom_Dist_RangeRequestBuilder

        return Binom_Dist_RangeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def binom_inv(self) -> Binom_InvRequestBuilder:
        """
        Provides operations to call the binom_Inv method.
        """
        from .binom_inv.binom_inv_request_builder import Binom_InvRequestBuilder

        return Binom_InvRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def bitand(self) -> BitandRequestBuilder:
        """
        Provides operations to call the bitand method.
        """
        from .bitand.bitand_request_builder import BitandRequestBuilder

        return BitandRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def bitlshift(self) -> BitlshiftRequestBuilder:
        """
        Provides operations to call the bitlshift method.
        """
        from .bitlshift.bitlshift_request_builder import BitlshiftRequestBuilder

        return BitlshiftRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def bitor(self) -> BitorRequestBuilder:
        """
        Provides operations to call the bitor method.
        """
        from .bitor.bitor_request_builder import BitorRequestBuilder

        return BitorRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def bitrshift(self) -> BitrshiftRequestBuilder:
        """
        Provides operations to call the bitrshift method.
        """
        from .bitrshift.bitrshift_request_builder import BitrshiftRequestBuilder

        return BitrshiftRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def bitxor(self) -> BitxorRequestBuilder:
        """
        Provides operations to call the bitxor method.
        """
        from .bitxor.bitxor_request_builder import BitxorRequestBuilder

        return BitxorRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def ceiling_math(self) -> Ceiling_MathRequestBuilder:
        """
        Provides operations to call the ceiling_Math method.
        """
        from .ceiling_math.ceiling_math_request_builder import Ceiling_MathRequestBuilder

        return Ceiling_MathRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def ceiling_precise(self) -> Ceiling_PreciseRequestBuilder:
        """
        Provides operations to call the ceiling_Precise method.
        """
        from .ceiling_precise.ceiling_precise_request_builder import Ceiling_PreciseRequestBuilder

        return Ceiling_PreciseRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def char(self) -> CharRequestBuilder:
        """
        Provides operations to call the char method.
        """
        from .char.char_request_builder import CharRequestBuilder

        return CharRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def chi_sq_dist(self) -> ChiSq_DistRequestBuilder:
        """
        Provides operations to call the chiSq_Dist method.
        """
        from .chi_sq_dist.chi_sq_dist_request_builder import ChiSq_DistRequestBuilder

        return ChiSq_DistRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def chi_sq_dist_r_t(self) -> ChiSq_Dist_RTRequestBuilder:
        """
        Provides operations to call the chiSq_Dist_RT method.
        """
        from .chi_sq_dist_r_t.chi_sq_dist_r_t_request_builder import ChiSq_Dist_RTRequestBuilder

        return ChiSq_Dist_RTRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def chi_sq_inv(self) -> ChiSq_InvRequestBuilder:
        """
        Provides operations to call the chiSq_Inv method.
        """
        from .chi_sq_inv.chi_sq_inv_request_builder import ChiSq_InvRequestBuilder

        return ChiSq_InvRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def chi_sq_inv_r_t(self) -> ChiSq_Inv_RTRequestBuilder:
        """
        Provides operations to call the chiSq_Inv_RT method.
        """
        from .chi_sq_inv_r_t.chi_sq_inv_r_t_request_builder import ChiSq_Inv_RTRequestBuilder

        return ChiSq_Inv_RTRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def choose(self) -> ChooseRequestBuilder:
        """
        Provides operations to call the choose method.
        """
        from .choose.choose_request_builder import ChooseRequestBuilder

        return ChooseRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def clean(self) -> CleanRequestBuilder:
        """
        Provides operations to call the clean method.
        """
        from .clean.clean_request_builder import CleanRequestBuilder

        return CleanRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def code(self) -> CodeRequestBuilder:
        """
        Provides operations to call the code method.
        """
        from .code.code_request_builder import CodeRequestBuilder

        return CodeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def columns(self) -> ColumnsRequestBuilder:
        """
        Provides operations to call the columns method.
        """
        from .columns.columns_request_builder import ColumnsRequestBuilder

        return ColumnsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def combin(self) -> CombinRequestBuilder:
        """
        Provides operations to call the combin method.
        """
        from .combin.combin_request_builder import CombinRequestBuilder

        return CombinRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def combina(self) -> CombinaRequestBuilder:
        """
        Provides operations to call the combina method.
        """
        from .combina.combina_request_builder import CombinaRequestBuilder

        return CombinaRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def complex(self) -> ComplexRequestBuilder:
        """
        Provides operations to call the complex method.
        """
        from .complex.complex_request_builder import ComplexRequestBuilder

        return ComplexRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def concatenate(self) -> ConcatenateRequestBuilder:
        """
        Provides operations to call the concatenate method.
        """
        from .concatenate.concatenate_request_builder import ConcatenateRequestBuilder

        return ConcatenateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def confidence_norm(self) -> Confidence_NormRequestBuilder:
        """
        Provides operations to call the confidence_Norm method.
        """
        from .confidence_norm.confidence_norm_request_builder import Confidence_NormRequestBuilder

        return Confidence_NormRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def confidence_t(self) -> Confidence_TRequestBuilder:
        """
        Provides operations to call the confidence_T method.
        """
        from .confidence_t.confidence_t_request_builder import Confidence_TRequestBuilder

        return Confidence_TRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def convert(self) -> ConvertRequestBuilder:
        """
        Provides operations to call the convert method.
        """
        from .convert.convert_request_builder import ConvertRequestBuilder

        return ConvertRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def cos(self) -> CosRequestBuilder:
        """
        Provides operations to call the cos method.
        """
        from .cos.cos_request_builder import CosRequestBuilder

        return CosRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def cosh(self) -> CoshRequestBuilder:
        """
        Provides operations to call the cosh method.
        """
        from .cosh.cosh_request_builder import CoshRequestBuilder

        return CoshRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def cot(self) -> CotRequestBuilder:
        """
        Provides operations to call the cot method.
        """
        from .cot.cot_request_builder import CotRequestBuilder

        return CotRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def coth(self) -> CothRequestBuilder:
        """
        Provides operations to call the coth method.
        """
        from .coth.coth_request_builder import CothRequestBuilder

        return CothRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def count(self) -> CountRequestBuilder:
        """
        Provides operations to call the count method.
        """
        from .count.count_request_builder import CountRequestBuilder

        return CountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def count_a(self) -> CountARequestBuilder:
        """
        Provides operations to call the countA method.
        """
        from .count_a.count_a_request_builder import CountARequestBuilder

        return CountARequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def count_blank(self) -> CountBlankRequestBuilder:
        """
        Provides operations to call the countBlank method.
        """
        from .count_blank.count_blank_request_builder import CountBlankRequestBuilder

        return CountBlankRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def count_if(self) -> CountIfRequestBuilder:
        """
        Provides operations to call the countIf method.
        """
        from .count_if.count_if_request_builder import CountIfRequestBuilder

        return CountIfRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def count_ifs(self) -> CountIfsRequestBuilder:
        """
        Provides operations to call the countIfs method.
        """
        from .count_ifs.count_ifs_request_builder import CountIfsRequestBuilder

        return CountIfsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def coup_day_bs(self) -> CoupDayBsRequestBuilder:
        """
        Provides operations to call the coupDayBs method.
        """
        from .coup_day_bs.coup_day_bs_request_builder import CoupDayBsRequestBuilder

        return CoupDayBsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def coup_days(self) -> CoupDaysRequestBuilder:
        """
        Provides operations to call the coupDays method.
        """
        from .coup_days.coup_days_request_builder import CoupDaysRequestBuilder

        return CoupDaysRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def coup_days_nc(self) -> CoupDaysNcRequestBuilder:
        """
        Provides operations to call the coupDaysNc method.
        """
        from .coup_days_nc.coup_days_nc_request_builder import CoupDaysNcRequestBuilder

        return CoupDaysNcRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def coup_ncd(self) -> CoupNcdRequestBuilder:
        """
        Provides operations to call the coupNcd method.
        """
        from .coup_ncd.coup_ncd_request_builder import CoupNcdRequestBuilder

        return CoupNcdRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def coup_num(self) -> CoupNumRequestBuilder:
        """
        Provides operations to call the coupNum method.
        """
        from .coup_num.coup_num_request_builder import CoupNumRequestBuilder

        return CoupNumRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def coup_pcd(self) -> CoupPcdRequestBuilder:
        """
        Provides operations to call the coupPcd method.
        """
        from .coup_pcd.coup_pcd_request_builder import CoupPcdRequestBuilder

        return CoupPcdRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def csc(self) -> CscRequestBuilder:
        """
        Provides operations to call the csc method.
        """
        from .csc.csc_request_builder import CscRequestBuilder

        return CscRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def csch(self) -> CschRequestBuilder:
        """
        Provides operations to call the csch method.
        """
        from .csch.csch_request_builder import CschRequestBuilder

        return CschRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def cum_i_pmt(self) -> CumIPmtRequestBuilder:
        """
        Provides operations to call the cumIPmt method.
        """
        from .cum_i_pmt.cum_i_pmt_request_builder import CumIPmtRequestBuilder

        return CumIPmtRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def cum_princ(self) -> CumPrincRequestBuilder:
        """
        Provides operations to call the cumPrinc method.
        """
        from .cum_princ.cum_princ_request_builder import CumPrincRequestBuilder

        return CumPrincRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def date(self) -> DateRequestBuilder:
        """
        Provides operations to call the date method.
        """
        from .date.date_request_builder import DateRequestBuilder

        return DateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def datevalue(self) -> DatevalueRequestBuilder:
        """
        Provides operations to call the datevalue method.
        """
        from .datevalue.datevalue_request_builder import DatevalueRequestBuilder

        return DatevalueRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def daverage(self) -> DaverageRequestBuilder:
        """
        Provides operations to call the daverage method.
        """
        from .daverage.daverage_request_builder import DaverageRequestBuilder

        return DaverageRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def day(self) -> DayRequestBuilder:
        """
        Provides operations to call the day method.
        """
        from .day.day_request_builder import DayRequestBuilder

        return DayRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def days(self) -> DaysRequestBuilder:
        """
        Provides operations to call the days method.
        """
        from .days.days_request_builder import DaysRequestBuilder

        return DaysRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def days360(self) -> Days360RequestBuilder:
        """
        Provides operations to call the days360 method.
        """
        from .days360.days360_request_builder import Days360RequestBuilder

        return Days360RequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def db(self) -> DbRequestBuilder:
        """
        Provides operations to call the db method.
        """
        from .db.db_request_builder import DbRequestBuilder

        return DbRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dbcs(self) -> DbcsRequestBuilder:
        """
        Provides operations to call the dbcs method.
        """
        from .dbcs.dbcs_request_builder import DbcsRequestBuilder

        return DbcsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dcount(self) -> DcountRequestBuilder:
        """
        Provides operations to call the dcount method.
        """
        from .dcount.dcount_request_builder import DcountRequestBuilder

        return DcountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dcount_a(self) -> DcountARequestBuilder:
        """
        Provides operations to call the dcountA method.
        """
        from .dcount_a.dcount_a_request_builder import DcountARequestBuilder

        return DcountARequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def ddb(self) -> DdbRequestBuilder:
        """
        Provides operations to call the ddb method.
        """
        from .ddb.ddb_request_builder import DdbRequestBuilder

        return DdbRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dec2_bin(self) -> Dec2BinRequestBuilder:
        """
        Provides operations to call the dec2Bin method.
        """
        from .dec2_bin.dec2_bin_request_builder import Dec2BinRequestBuilder

        return Dec2BinRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dec2_hex(self) -> Dec2HexRequestBuilder:
        """
        Provides operations to call the dec2Hex method.
        """
        from .dec2_hex.dec2_hex_request_builder import Dec2HexRequestBuilder

        return Dec2HexRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dec2_oct(self) -> Dec2OctRequestBuilder:
        """
        Provides operations to call the dec2Oct method.
        """
        from .dec2_oct.dec2_oct_request_builder import Dec2OctRequestBuilder

        return Dec2OctRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def decimal(self) -> DecimalRequestBuilder:
        """
        Provides operations to call the decimal method.
        """
        from .decimal.decimal_request_builder import DecimalRequestBuilder

        return DecimalRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def degrees(self) -> DegreesRequestBuilder:
        """
        Provides operations to call the degrees method.
        """
        from .degrees.degrees_request_builder import DegreesRequestBuilder

        return DegreesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def delta(self) -> DeltaRequestBuilder:
        """
        Provides operations to call the delta method.
        """
        from .delta.delta_request_builder import DeltaRequestBuilder

        return DeltaRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dev_sq(self) -> DevSqRequestBuilder:
        """
        Provides operations to call the devSq method.
        """
        from .dev_sq.dev_sq_request_builder import DevSqRequestBuilder

        return DevSqRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dget(self) -> DgetRequestBuilder:
        """
        Provides operations to call the dget method.
        """
        from .dget.dget_request_builder import DgetRequestBuilder

        return DgetRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def disc(self) -> DiscRequestBuilder:
        """
        Provides operations to call the disc method.
        """
        from .disc.disc_request_builder import DiscRequestBuilder

        return DiscRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dmax(self) -> DmaxRequestBuilder:
        """
        Provides operations to call the dmax method.
        """
        from .dmax.dmax_request_builder import DmaxRequestBuilder

        return DmaxRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dmin(self) -> DminRequestBuilder:
        """
        Provides operations to call the dmin method.
        """
        from .dmin.dmin_request_builder import DminRequestBuilder

        return DminRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dollar(self) -> DollarRequestBuilder:
        """
        Provides operations to call the dollar method.
        """
        from .dollar.dollar_request_builder import DollarRequestBuilder

        return DollarRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dollar_de(self) -> DollarDeRequestBuilder:
        """
        Provides operations to call the dollarDe method.
        """
        from .dollar_de.dollar_de_request_builder import DollarDeRequestBuilder

        return DollarDeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dollar_fr(self) -> DollarFrRequestBuilder:
        """
        Provides operations to call the dollarFr method.
        """
        from .dollar_fr.dollar_fr_request_builder import DollarFrRequestBuilder

        return DollarFrRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dproduct(self) -> DproductRequestBuilder:
        """
        Provides operations to call the dproduct method.
        """
        from .dproduct.dproduct_request_builder import DproductRequestBuilder

        return DproductRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dst_dev(self) -> DstDevRequestBuilder:
        """
        Provides operations to call the dstDev method.
        """
        from .dst_dev.dst_dev_request_builder import DstDevRequestBuilder

        return DstDevRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dst_dev_p(self) -> DstDevPRequestBuilder:
        """
        Provides operations to call the dstDevP method.
        """
        from .dst_dev_p.dst_dev_p_request_builder import DstDevPRequestBuilder

        return DstDevPRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dsum(self) -> DsumRequestBuilder:
        """
        Provides operations to call the dsum method.
        """
        from .dsum.dsum_request_builder import DsumRequestBuilder

        return DsumRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def duration(self) -> DurationRequestBuilder:
        """
        Provides operations to call the duration method.
        """
        from .duration.duration_request_builder import DurationRequestBuilder

        return DurationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dvar(self) -> DvarRequestBuilder:
        """
        Provides operations to call the dvar method.
        """
        from .dvar.dvar_request_builder import DvarRequestBuilder

        return DvarRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dvar_p(self) -> DvarPRequestBuilder:
        """
        Provides operations to call the dvarP method.
        """
        from .dvar_p.dvar_p_request_builder import DvarPRequestBuilder

        return DvarPRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def ecma_ceiling(self) -> Ecma_CeilingRequestBuilder:
        """
        Provides operations to call the ecma_Ceiling method.
        """
        from .ecma_ceiling.ecma_ceiling_request_builder import Ecma_CeilingRequestBuilder

        return Ecma_CeilingRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def edate(self) -> EdateRequestBuilder:
        """
        Provides operations to call the edate method.
        """
        from .edate.edate_request_builder import EdateRequestBuilder

        return EdateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def effect(self) -> EffectRequestBuilder:
        """
        Provides operations to call the effect method.
        """
        from .effect.effect_request_builder import EffectRequestBuilder

        return EffectRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def eo_month(self) -> EoMonthRequestBuilder:
        """
        Provides operations to call the eoMonth method.
        """
        from .eo_month.eo_month_request_builder import EoMonthRequestBuilder

        return EoMonthRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def erf(self) -> ErfRequestBuilder:
        """
        Provides operations to call the erf method.
        """
        from .erf.erf_request_builder import ErfRequestBuilder

        return ErfRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def erf_c(self) -> ErfCRequestBuilder:
        """
        Provides operations to call the erfC method.
        """
        from .erf_c.erf_c_request_builder import ErfCRequestBuilder

        return ErfCRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def erf_c_precise(self) -> ErfC_PreciseRequestBuilder:
        """
        Provides operations to call the erfC_Precise method.
        """
        from .erf_c_precise.erf_c_precise_request_builder import ErfC_PreciseRequestBuilder

        return ErfC_PreciseRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def erf_precise(self) -> Erf_PreciseRequestBuilder:
        """
        Provides operations to call the erf_Precise method.
        """
        from .erf_precise.erf_precise_request_builder import Erf_PreciseRequestBuilder

        return Erf_PreciseRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def error_type(self) -> Error_TypeRequestBuilder:
        """
        Provides operations to call the error_Type method.
        """
        from .error_type.error_type_request_builder import Error_TypeRequestBuilder

        return Error_TypeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def even(self) -> EvenRequestBuilder:
        """
        Provides operations to call the even method.
        """
        from .even.even_request_builder import EvenRequestBuilder

        return EvenRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def exact(self) -> ExactRequestBuilder:
        """
        Provides operations to call the exact method.
        """
        from .exact.exact_request_builder import ExactRequestBuilder

        return ExactRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def exp(self) -> ExpRequestBuilder:
        """
        Provides operations to call the exp method.
        """
        from .exp.exp_request_builder import ExpRequestBuilder

        return ExpRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def expon_dist(self) -> Expon_DistRequestBuilder:
        """
        Provides operations to call the expon_Dist method.
        """
        from .expon_dist.expon_dist_request_builder import Expon_DistRequestBuilder

        return Expon_DistRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def f_dist(self) -> F_DistRequestBuilder:
        """
        Provides operations to call the f_Dist method.
        """
        from .f_dist.f_dist_request_builder import F_DistRequestBuilder

        return F_DistRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def f_dist_r_t(self) -> F_Dist_RTRequestBuilder:
        """
        Provides operations to call the f_Dist_RT method.
        """
        from .f_dist_r_t.f_dist_r_t_request_builder import F_Dist_RTRequestBuilder

        return F_Dist_RTRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def f_inv(self) -> F_InvRequestBuilder:
        """
        Provides operations to call the f_Inv method.
        """
        from .f_inv.f_inv_request_builder import F_InvRequestBuilder

        return F_InvRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def f_inv_r_t(self) -> F_Inv_RTRequestBuilder:
        """
        Provides operations to call the f_Inv_RT method.
        """
        from .f_inv_r_t.f_inv_r_t_request_builder import F_Inv_RTRequestBuilder

        return F_Inv_RTRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def fact(self) -> FactRequestBuilder:
        """
        Provides operations to call the fact method.
        """
        from .fact.fact_request_builder import FactRequestBuilder

        return FactRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def fact_double(self) -> FactDoubleRequestBuilder:
        """
        Provides operations to call the factDouble method.
        """
        from .fact_double.fact_double_request_builder import FactDoubleRequestBuilder

        return FactDoubleRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def false_(self) -> FalseRequestBuilder:
        """
        Provides operations to call the false method.
        """
        from .false_.false_request_builder import FalseRequestBuilder

        return FalseRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def find(self) -> FindRequestBuilder:
        """
        Provides operations to call the find method.
        """
        from .find.find_request_builder import FindRequestBuilder

        return FindRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def find_b(self) -> FindBRequestBuilder:
        """
        Provides operations to call the findB method.
        """
        from .find_b.find_b_request_builder import FindBRequestBuilder

        return FindBRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def fisher(self) -> FisherRequestBuilder:
        """
        Provides operations to call the fisher method.
        """
        from .fisher.fisher_request_builder import FisherRequestBuilder

        return FisherRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def fisher_inv(self) -> FisherInvRequestBuilder:
        """
        Provides operations to call the fisherInv method.
        """
        from .fisher_inv.fisher_inv_request_builder import FisherInvRequestBuilder

        return FisherInvRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def fixed(self) -> FixedRequestBuilder:
        """
        Provides operations to call the fixed method.
        """
        from .fixed.fixed_request_builder import FixedRequestBuilder

        return FixedRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def floor_math(self) -> Floor_MathRequestBuilder:
        """
        Provides operations to call the floor_Math method.
        """
        from .floor_math.floor_math_request_builder import Floor_MathRequestBuilder

        return Floor_MathRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def floor_precise(self) -> Floor_PreciseRequestBuilder:
        """
        Provides operations to call the floor_Precise method.
        """
        from .floor_precise.floor_precise_request_builder import Floor_PreciseRequestBuilder

        return Floor_PreciseRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def fv(self) -> FvRequestBuilder:
        """
        Provides operations to call the fv method.
        """
        from .fv.fv_request_builder import FvRequestBuilder

        return FvRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def fvschedule(self) -> FvscheduleRequestBuilder:
        """
        Provides operations to call the fvschedule method.
        """
        from .fvschedule.fvschedule_request_builder import FvscheduleRequestBuilder

        return FvscheduleRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def gamma(self) -> GammaRequestBuilder:
        """
        Provides operations to call the gamma method.
        """
        from .gamma.gamma_request_builder import GammaRequestBuilder

        return GammaRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def gamma_dist(self) -> Gamma_DistRequestBuilder:
        """
        Provides operations to call the gamma_Dist method.
        """
        from .gamma_dist.gamma_dist_request_builder import Gamma_DistRequestBuilder

        return Gamma_DistRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def gamma_inv(self) -> Gamma_InvRequestBuilder:
        """
        Provides operations to call the gamma_Inv method.
        """
        from .gamma_inv.gamma_inv_request_builder import Gamma_InvRequestBuilder

        return Gamma_InvRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def gamma_ln(self) -> GammaLnRequestBuilder:
        """
        Provides operations to call the gammaLn method.
        """
        from .gamma_ln.gamma_ln_request_builder import GammaLnRequestBuilder

        return GammaLnRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def gamma_ln_precise(self) -> GammaLn_PreciseRequestBuilder:
        """
        Provides operations to call the gammaLn_Precise method.
        """
        from .gamma_ln_precise.gamma_ln_precise_request_builder import GammaLn_PreciseRequestBuilder

        return GammaLn_PreciseRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def gauss(self) -> GaussRequestBuilder:
        """
        Provides operations to call the gauss method.
        """
        from .gauss.gauss_request_builder import GaussRequestBuilder

        return GaussRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def gcd(self) -> GcdRequestBuilder:
        """
        Provides operations to call the gcd method.
        """
        from .gcd.gcd_request_builder import GcdRequestBuilder

        return GcdRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def ge_step(self) -> GeStepRequestBuilder:
        """
        Provides operations to call the geStep method.
        """
        from .ge_step.ge_step_request_builder import GeStepRequestBuilder

        return GeStepRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def geo_mean(self) -> GeoMeanRequestBuilder:
        """
        Provides operations to call the geoMean method.
        """
        from .geo_mean.geo_mean_request_builder import GeoMeanRequestBuilder

        return GeoMeanRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def har_mean(self) -> HarMeanRequestBuilder:
        """
        Provides operations to call the harMean method.
        """
        from .har_mean.har_mean_request_builder import HarMeanRequestBuilder

        return HarMeanRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def hex2_bin(self) -> Hex2BinRequestBuilder:
        """
        Provides operations to call the hex2Bin method.
        """
        from .hex2_bin.hex2_bin_request_builder import Hex2BinRequestBuilder

        return Hex2BinRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def hex2_dec(self) -> Hex2DecRequestBuilder:
        """
        Provides operations to call the hex2Dec method.
        """
        from .hex2_dec.hex2_dec_request_builder import Hex2DecRequestBuilder

        return Hex2DecRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def hex2_oct(self) -> Hex2OctRequestBuilder:
        """
        Provides operations to call the hex2Oct method.
        """
        from .hex2_oct.hex2_oct_request_builder import Hex2OctRequestBuilder

        return Hex2OctRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def hlookup(self) -> HlookupRequestBuilder:
        """
        Provides operations to call the hlookup method.
        """
        from .hlookup.hlookup_request_builder import HlookupRequestBuilder

        return HlookupRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def hour(self) -> HourRequestBuilder:
        """
        Provides operations to call the hour method.
        """
        from .hour.hour_request_builder import HourRequestBuilder

        return HourRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def hyp_geom_dist(self) -> HypGeom_DistRequestBuilder:
        """
        Provides operations to call the hypGeom_Dist method.
        """
        from .hyp_geom_dist.hyp_geom_dist_request_builder import HypGeom_DistRequestBuilder

        return HypGeom_DistRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def hyperlink(self) -> HyperlinkRequestBuilder:
        """
        Provides operations to call the hyperlink method.
        """
        from .hyperlink.hyperlink_request_builder import HyperlinkRequestBuilder

        return HyperlinkRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def if_(self) -> IfRequestBuilder:
        """
        Provides operations to call the if method.
        """
        from .if_.if_request_builder import IfRequestBuilder

        return IfRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def im_abs(self) -> ImAbsRequestBuilder:
        """
        Provides operations to call the imAbs method.
        """
        from .im_abs.im_abs_request_builder import ImAbsRequestBuilder

        return ImAbsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def im_argument(self) -> ImArgumentRequestBuilder:
        """
        Provides operations to call the imArgument method.
        """
        from .im_argument.im_argument_request_builder import ImArgumentRequestBuilder

        return ImArgumentRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def im_conjugate(self) -> ImConjugateRequestBuilder:
        """
        Provides operations to call the imConjugate method.
        """
        from .im_conjugate.im_conjugate_request_builder import ImConjugateRequestBuilder

        return ImConjugateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def im_cos(self) -> ImCosRequestBuilder:
        """
        Provides operations to call the imCos method.
        """
        from .im_cos.im_cos_request_builder import ImCosRequestBuilder

        return ImCosRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def im_cosh(self) -> ImCoshRequestBuilder:
        """
        Provides operations to call the imCosh method.
        """
        from .im_cosh.im_cosh_request_builder import ImCoshRequestBuilder

        return ImCoshRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def im_cot(self) -> ImCotRequestBuilder:
        """
        Provides operations to call the imCot method.
        """
        from .im_cot.im_cot_request_builder import ImCotRequestBuilder

        return ImCotRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def im_csc(self) -> ImCscRequestBuilder:
        """
        Provides operations to call the imCsc method.
        """
        from .im_csc.im_csc_request_builder import ImCscRequestBuilder

        return ImCscRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def im_csch(self) -> ImCschRequestBuilder:
        """
        Provides operations to call the imCsch method.
        """
        from .im_csch.im_csch_request_builder import ImCschRequestBuilder

        return ImCschRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def im_div(self) -> ImDivRequestBuilder:
        """
        Provides operations to call the imDiv method.
        """
        from .im_div.im_div_request_builder import ImDivRequestBuilder

        return ImDivRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def im_exp(self) -> ImExpRequestBuilder:
        """
        Provides operations to call the imExp method.
        """
        from .im_exp.im_exp_request_builder import ImExpRequestBuilder

        return ImExpRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def im_ln(self) -> ImLnRequestBuilder:
        """
        Provides operations to call the imLn method.
        """
        from .im_ln.im_ln_request_builder import ImLnRequestBuilder

        return ImLnRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def im_log10(self) -> ImLog10RequestBuilder:
        """
        Provides operations to call the imLog10 method.
        """
        from .im_log10.im_log10_request_builder import ImLog10RequestBuilder

        return ImLog10RequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def im_log2(self) -> ImLog2RequestBuilder:
        """
        Provides operations to call the imLog2 method.
        """
        from .im_log2.im_log2_request_builder import ImLog2RequestBuilder

        return ImLog2RequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def im_power(self) -> ImPowerRequestBuilder:
        """
        Provides operations to call the imPower method.
        """
        from .im_power.im_power_request_builder import ImPowerRequestBuilder

        return ImPowerRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def im_product(self) -> ImProductRequestBuilder:
        """
        Provides operations to call the imProduct method.
        """
        from .im_product.im_product_request_builder import ImProductRequestBuilder

        return ImProductRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def im_real(self) -> ImRealRequestBuilder:
        """
        Provides operations to call the imReal method.
        """
        from .im_real.im_real_request_builder import ImRealRequestBuilder

        return ImRealRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def im_sec(self) -> ImSecRequestBuilder:
        """
        Provides operations to call the imSec method.
        """
        from .im_sec.im_sec_request_builder import ImSecRequestBuilder

        return ImSecRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def im_sech(self) -> ImSechRequestBuilder:
        """
        Provides operations to call the imSech method.
        """
        from .im_sech.im_sech_request_builder import ImSechRequestBuilder

        return ImSechRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def im_sin(self) -> ImSinRequestBuilder:
        """
        Provides operations to call the imSin method.
        """
        from .im_sin.im_sin_request_builder import ImSinRequestBuilder

        return ImSinRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def im_sinh(self) -> ImSinhRequestBuilder:
        """
        Provides operations to call the imSinh method.
        """
        from .im_sinh.im_sinh_request_builder import ImSinhRequestBuilder

        return ImSinhRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def im_sqrt(self) -> ImSqrtRequestBuilder:
        """
        Provides operations to call the imSqrt method.
        """
        from .im_sqrt.im_sqrt_request_builder import ImSqrtRequestBuilder

        return ImSqrtRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def im_sub(self) -> ImSubRequestBuilder:
        """
        Provides operations to call the imSub method.
        """
        from .im_sub.im_sub_request_builder import ImSubRequestBuilder

        return ImSubRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def im_sum(self) -> ImSumRequestBuilder:
        """
        Provides operations to call the imSum method.
        """
        from .im_sum.im_sum_request_builder import ImSumRequestBuilder

        return ImSumRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def im_tan(self) -> ImTanRequestBuilder:
        """
        Provides operations to call the imTan method.
        """
        from .im_tan.im_tan_request_builder import ImTanRequestBuilder

        return ImTanRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def imaginary(self) -> ImaginaryRequestBuilder:
        """
        Provides operations to call the imaginary method.
        """
        from .imaginary.imaginary_request_builder import ImaginaryRequestBuilder

        return ImaginaryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def int(self) -> IntRequestBuilder:
        """
        Provides operations to call the int method.
        """
        from .int.int_request_builder import IntRequestBuilder

        return IntRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def int_rate(self) -> IntRateRequestBuilder:
        """
        Provides operations to call the intRate method.
        """
        from .int_rate.int_rate_request_builder import IntRateRequestBuilder

        return IntRateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def ipmt(self) -> IpmtRequestBuilder:
        """
        Provides operations to call the ipmt method.
        """
        from .ipmt.ipmt_request_builder import IpmtRequestBuilder

        return IpmtRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def irr(self) -> IrrRequestBuilder:
        """
        Provides operations to call the irr method.
        """
        from .irr.irr_request_builder import IrrRequestBuilder

        return IrrRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def is_err(self) -> IsErrRequestBuilder:
        """
        Provides operations to call the isErr method.
        """
        from .is_err.is_err_request_builder import IsErrRequestBuilder

        return IsErrRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def is_error(self) -> IsErrorRequestBuilder:
        """
        Provides operations to call the isError method.
        """
        from .is_error.is_error_request_builder import IsErrorRequestBuilder

        return IsErrorRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def is_even(self) -> IsEvenRequestBuilder:
        """
        Provides operations to call the isEven method.
        """
        from .is_even.is_even_request_builder import IsEvenRequestBuilder

        return IsEvenRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def is_formula(self) -> IsFormulaRequestBuilder:
        """
        Provides operations to call the isFormula method.
        """
        from .is_formula.is_formula_request_builder import IsFormulaRequestBuilder

        return IsFormulaRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def is_logical(self) -> IsLogicalRequestBuilder:
        """
        Provides operations to call the isLogical method.
        """
        from .is_logical.is_logical_request_builder import IsLogicalRequestBuilder

        return IsLogicalRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def is_n_a(self) -> IsNARequestBuilder:
        """
        Provides operations to call the isNA method.
        """
        from .is_n_a.is_n_a_request_builder import IsNARequestBuilder

        return IsNARequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def is_non_text(self) -> IsNonTextRequestBuilder:
        """
        Provides operations to call the isNonText method.
        """
        from .is_non_text.is_non_text_request_builder import IsNonTextRequestBuilder

        return IsNonTextRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def is_number(self) -> IsNumberRequestBuilder:
        """
        Provides operations to call the isNumber method.
        """
        from .is_number.is_number_request_builder import IsNumberRequestBuilder

        return IsNumberRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def is_odd(self) -> IsOddRequestBuilder:
        """
        Provides operations to call the isOdd method.
        """
        from .is_odd.is_odd_request_builder import IsOddRequestBuilder

        return IsOddRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def is_text(self) -> IsTextRequestBuilder:
        """
        Provides operations to call the isText method.
        """
        from .is_text.is_text_request_builder import IsTextRequestBuilder

        return IsTextRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def iso_ceiling(self) -> Iso_CeilingRequestBuilder:
        """
        Provides operations to call the iso_Ceiling method.
        """
        from .iso_ceiling.iso_ceiling_request_builder import Iso_CeilingRequestBuilder

        return Iso_CeilingRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def iso_week_num(self) -> IsoWeekNumRequestBuilder:
        """
        Provides operations to call the isoWeekNum method.
        """
        from .iso_week_num.iso_week_num_request_builder import IsoWeekNumRequestBuilder

        return IsoWeekNumRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def ispmt(self) -> IspmtRequestBuilder:
        """
        Provides operations to call the ispmt method.
        """
        from .ispmt.ispmt_request_builder import IspmtRequestBuilder

        return IspmtRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def isref(self) -> IsrefRequestBuilder:
        """
        Provides operations to call the isref method.
        """
        from .isref.isref_request_builder import IsrefRequestBuilder

        return IsrefRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def kurt(self) -> KurtRequestBuilder:
        """
        Provides operations to call the kurt method.
        """
        from .kurt.kurt_request_builder import KurtRequestBuilder

        return KurtRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def large(self) -> LargeRequestBuilder:
        """
        Provides operations to call the large method.
        """
        from .large.large_request_builder import LargeRequestBuilder

        return LargeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def lcm(self) -> LcmRequestBuilder:
        """
        Provides operations to call the lcm method.
        """
        from .lcm.lcm_request_builder import LcmRequestBuilder

        return LcmRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def left(self) -> LeftRequestBuilder:
        """
        Provides operations to call the left method.
        """
        from .left.left_request_builder import LeftRequestBuilder

        return LeftRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def leftb(self) -> LeftbRequestBuilder:
        """
        Provides operations to call the leftb method.
        """
        from .leftb.leftb_request_builder import LeftbRequestBuilder

        return LeftbRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def len(self) -> LenRequestBuilder:
        """
        Provides operations to call the len method.
        """
        from .len.len_request_builder import LenRequestBuilder

        return LenRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def lenb(self) -> LenbRequestBuilder:
        """
        Provides operations to call the lenb method.
        """
        from .lenb.lenb_request_builder import LenbRequestBuilder

        return LenbRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def ln(self) -> LnRequestBuilder:
        """
        Provides operations to call the ln method.
        """
        from .ln.ln_request_builder import LnRequestBuilder

        return LnRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def log(self) -> LogRequestBuilder:
        """
        Provides operations to call the log method.
        """
        from .log.log_request_builder import LogRequestBuilder

        return LogRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def log_norm_dist(self) -> LogNorm_DistRequestBuilder:
        """
        Provides operations to call the logNorm_Dist method.
        """
        from .log_norm_dist.log_norm_dist_request_builder import LogNorm_DistRequestBuilder

        return LogNorm_DistRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def log_norm_inv(self) -> LogNorm_InvRequestBuilder:
        """
        Provides operations to call the logNorm_Inv method.
        """
        from .log_norm_inv.log_norm_inv_request_builder import LogNorm_InvRequestBuilder

        return LogNorm_InvRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def log10(self) -> Log10RequestBuilder:
        """
        Provides operations to call the log10 method.
        """
        from .log10.log10_request_builder import Log10RequestBuilder

        return Log10RequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def lookup(self) -> LookupRequestBuilder:
        """
        Provides operations to call the lookup method.
        """
        from .lookup.lookup_request_builder import LookupRequestBuilder

        return LookupRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def lower(self) -> LowerRequestBuilder:
        """
        Provides operations to call the lower method.
        """
        from .lower.lower_request_builder import LowerRequestBuilder

        return LowerRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def match(self) -> MatchRequestBuilder:
        """
        Provides operations to call the match method.
        """
        from .match.match_request_builder import MatchRequestBuilder

        return MatchRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def max(self) -> MaxRequestBuilder:
        """
        Provides operations to call the max method.
        """
        from .max.max_request_builder import MaxRequestBuilder

        return MaxRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def max_a(self) -> MaxARequestBuilder:
        """
        Provides operations to call the maxA method.
        """
        from .max_a.max_a_request_builder import MaxARequestBuilder

        return MaxARequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mduration(self) -> MdurationRequestBuilder:
        """
        Provides operations to call the mduration method.
        """
        from .mduration.mduration_request_builder import MdurationRequestBuilder

        return MdurationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def median(self) -> MedianRequestBuilder:
        """
        Provides operations to call the median method.
        """
        from .median.median_request_builder import MedianRequestBuilder

        return MedianRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mid(self) -> MidRequestBuilder:
        """
        Provides operations to call the mid method.
        """
        from .mid.mid_request_builder import MidRequestBuilder

        return MidRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def midb(self) -> MidbRequestBuilder:
        """
        Provides operations to call the midb method.
        """
        from .midb.midb_request_builder import MidbRequestBuilder

        return MidbRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def min(self) -> MinRequestBuilder:
        """
        Provides operations to call the min method.
        """
        from .min.min_request_builder import MinRequestBuilder

        return MinRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def min_a(self) -> MinARequestBuilder:
        """
        Provides operations to call the minA method.
        """
        from .min_a.min_a_request_builder import MinARequestBuilder

        return MinARequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def minute(self) -> MinuteRequestBuilder:
        """
        Provides operations to call the minute method.
        """
        from .minute.minute_request_builder import MinuteRequestBuilder

        return MinuteRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mirr(self) -> MirrRequestBuilder:
        """
        Provides operations to call the mirr method.
        """
        from .mirr.mirr_request_builder import MirrRequestBuilder

        return MirrRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mod(self) -> ModRequestBuilder:
        """
        Provides operations to call the mod method.
        """
        from .mod.mod_request_builder import ModRequestBuilder

        return ModRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def month(self) -> MonthRequestBuilder:
        """
        Provides operations to call the month method.
        """
        from .month.month_request_builder import MonthRequestBuilder

        return MonthRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mround(self) -> MroundRequestBuilder:
        """
        Provides operations to call the mround method.
        """
        from .mround.mround_request_builder import MroundRequestBuilder

        return MroundRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def multi_nomial(self) -> MultiNomialRequestBuilder:
        """
        Provides operations to call the multiNomial method.
        """
        from .multi_nomial.multi_nomial_request_builder import MultiNomialRequestBuilder

        return MultiNomialRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def n(self) -> NRequestBuilder:
        """
        Provides operations to call the n method.
        """
        from .n.n_request_builder import NRequestBuilder

        return NRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def na(self) -> NaRequestBuilder:
        """
        Provides operations to call the na method.
        """
        from .na.na_request_builder import NaRequestBuilder

        return NaRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def neg_binom_dist(self) -> NegBinom_DistRequestBuilder:
        """
        Provides operations to call the negBinom_Dist method.
        """
        from .neg_binom_dist.neg_binom_dist_request_builder import NegBinom_DistRequestBuilder

        return NegBinom_DistRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def network_days(self) -> NetworkDaysRequestBuilder:
        """
        Provides operations to call the networkDays method.
        """
        from .network_days.network_days_request_builder import NetworkDaysRequestBuilder

        return NetworkDaysRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def network_days_intl(self) -> NetworkDays_IntlRequestBuilder:
        """
        Provides operations to call the networkDays_Intl method.
        """
        from .network_days_intl.network_days_intl_request_builder import NetworkDays_IntlRequestBuilder

        return NetworkDays_IntlRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def nominal(self) -> NominalRequestBuilder:
        """
        Provides operations to call the nominal method.
        """
        from .nominal.nominal_request_builder import NominalRequestBuilder

        return NominalRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def norm_dist(self) -> Norm_DistRequestBuilder:
        """
        Provides operations to call the norm_Dist method.
        """
        from .norm_dist.norm_dist_request_builder import Norm_DistRequestBuilder

        return Norm_DistRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def norm_inv(self) -> Norm_InvRequestBuilder:
        """
        Provides operations to call the norm_Inv method.
        """
        from .norm_inv.norm_inv_request_builder import Norm_InvRequestBuilder

        return Norm_InvRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def norm_s_dist(self) -> Norm_S_DistRequestBuilder:
        """
        Provides operations to call the norm_S_Dist method.
        """
        from .norm_s_dist.norm_s_dist_request_builder import Norm_S_DistRequestBuilder

        return Norm_S_DistRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def norm_s_inv(self) -> Norm_S_InvRequestBuilder:
        """
        Provides operations to call the norm_S_Inv method.
        """
        from .norm_s_inv.norm_s_inv_request_builder import Norm_S_InvRequestBuilder

        return Norm_S_InvRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def not_(self) -> NotRequestBuilder:
        """
        Provides operations to call the not method.
        """
        from .not_.not_request_builder import NotRequestBuilder

        return NotRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def now(self) -> NowRequestBuilder:
        """
        Provides operations to call the now method.
        """
        from .now.now_request_builder import NowRequestBuilder

        return NowRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def nper(self) -> NperRequestBuilder:
        """
        Provides operations to call the nper method.
        """
        from .nper.nper_request_builder import NperRequestBuilder

        return NperRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def npv(self) -> NpvRequestBuilder:
        """
        Provides operations to call the npv method.
        """
        from .npv.npv_request_builder import NpvRequestBuilder

        return NpvRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def number_value(self) -> NumberValueRequestBuilder:
        """
        Provides operations to call the numberValue method.
        """
        from .number_value.number_value_request_builder import NumberValueRequestBuilder

        return NumberValueRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def oct2_bin(self) -> Oct2BinRequestBuilder:
        """
        Provides operations to call the oct2Bin method.
        """
        from .oct2_bin.oct2_bin_request_builder import Oct2BinRequestBuilder

        return Oct2BinRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def oct2_dec(self) -> Oct2DecRequestBuilder:
        """
        Provides operations to call the oct2Dec method.
        """
        from .oct2_dec.oct2_dec_request_builder import Oct2DecRequestBuilder

        return Oct2DecRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def oct2_hex(self) -> Oct2HexRequestBuilder:
        """
        Provides operations to call the oct2Hex method.
        """
        from .oct2_hex.oct2_hex_request_builder import Oct2HexRequestBuilder

        return Oct2HexRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def odd(self) -> OddRequestBuilder:
        """
        Provides operations to call the odd method.
        """
        from .odd.odd_request_builder import OddRequestBuilder

        return OddRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def odd_f_price(self) -> OddFPriceRequestBuilder:
        """
        Provides operations to call the oddFPrice method.
        """
        from .odd_f_price.odd_f_price_request_builder import OddFPriceRequestBuilder

        return OddFPriceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def odd_f_yield(self) -> OddFYieldRequestBuilder:
        """
        Provides operations to call the oddFYield method.
        """
        from .odd_f_yield.odd_f_yield_request_builder import OddFYieldRequestBuilder

        return OddFYieldRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def odd_l_price(self) -> OddLPriceRequestBuilder:
        """
        Provides operations to call the oddLPrice method.
        """
        from .odd_l_price.odd_l_price_request_builder import OddLPriceRequestBuilder

        return OddLPriceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def odd_l_yield(self) -> OddLYieldRequestBuilder:
        """
        Provides operations to call the oddLYield method.
        """
        from .odd_l_yield.odd_l_yield_request_builder import OddLYieldRequestBuilder

        return OddLYieldRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def or_(self) -> OrRequestBuilder:
        """
        Provides operations to call the or method.
        """
        from .or_.or_request_builder import OrRequestBuilder

        return OrRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def pduration(self) -> PdurationRequestBuilder:
        """
        Provides operations to call the pduration method.
        """
        from .pduration.pduration_request_builder import PdurationRequestBuilder

        return PdurationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def percent_rank_exc(self) -> PercentRank_ExcRequestBuilder:
        """
        Provides operations to call the percentRank_Exc method.
        """
        from .percent_rank_exc.percent_rank_exc_request_builder import PercentRank_ExcRequestBuilder

        return PercentRank_ExcRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def percent_rank_inc(self) -> PercentRank_IncRequestBuilder:
        """
        Provides operations to call the percentRank_Inc method.
        """
        from .percent_rank_inc.percent_rank_inc_request_builder import PercentRank_IncRequestBuilder

        return PercentRank_IncRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def percentile_exc(self) -> Percentile_ExcRequestBuilder:
        """
        Provides operations to call the percentile_Exc method.
        """
        from .percentile_exc.percentile_exc_request_builder import Percentile_ExcRequestBuilder

        return Percentile_ExcRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def percentile_inc(self) -> Percentile_IncRequestBuilder:
        """
        Provides operations to call the percentile_Inc method.
        """
        from .percentile_inc.percentile_inc_request_builder import Percentile_IncRequestBuilder

        return Percentile_IncRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def permut(self) -> PermutRequestBuilder:
        """
        Provides operations to call the permut method.
        """
        from .permut.permut_request_builder import PermutRequestBuilder

        return PermutRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def permutationa(self) -> PermutationaRequestBuilder:
        """
        Provides operations to call the permutationa method.
        """
        from .permutationa.permutationa_request_builder import PermutationaRequestBuilder

        return PermutationaRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def phi(self) -> PhiRequestBuilder:
        """
        Provides operations to call the phi method.
        """
        from .phi.phi_request_builder import PhiRequestBuilder

        return PhiRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def pi(self) -> PiRequestBuilder:
        """
        Provides operations to call the pi method.
        """
        from .pi.pi_request_builder import PiRequestBuilder

        return PiRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def pmt(self) -> PmtRequestBuilder:
        """
        Provides operations to call the pmt method.
        """
        from .pmt.pmt_request_builder import PmtRequestBuilder

        return PmtRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def poisson_dist(self) -> Poisson_DistRequestBuilder:
        """
        Provides operations to call the poisson_Dist method.
        """
        from .poisson_dist.poisson_dist_request_builder import Poisson_DistRequestBuilder

        return Poisson_DistRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def power(self) -> PowerRequestBuilder:
        """
        Provides operations to call the power method.
        """
        from .power.power_request_builder import PowerRequestBuilder

        return PowerRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def ppmt(self) -> PpmtRequestBuilder:
        """
        Provides operations to call the ppmt method.
        """
        from .ppmt.ppmt_request_builder import PpmtRequestBuilder

        return PpmtRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def price(self) -> PriceRequestBuilder:
        """
        Provides operations to call the price method.
        """
        from .price.price_request_builder import PriceRequestBuilder

        return PriceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def price_disc(self) -> PriceDiscRequestBuilder:
        """
        Provides operations to call the priceDisc method.
        """
        from .price_disc.price_disc_request_builder import PriceDiscRequestBuilder

        return PriceDiscRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def price_mat(self) -> PriceMatRequestBuilder:
        """
        Provides operations to call the priceMat method.
        """
        from .price_mat.price_mat_request_builder import PriceMatRequestBuilder

        return PriceMatRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def product(self) -> ProductRequestBuilder:
        """
        Provides operations to call the product method.
        """
        from .product.product_request_builder import ProductRequestBuilder

        return ProductRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def proper(self) -> ProperRequestBuilder:
        """
        Provides operations to call the proper method.
        """
        from .proper.proper_request_builder import ProperRequestBuilder

        return ProperRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def pv(self) -> PvRequestBuilder:
        """
        Provides operations to call the pv method.
        """
        from .pv.pv_request_builder import PvRequestBuilder

        return PvRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def quartile_exc(self) -> Quartile_ExcRequestBuilder:
        """
        Provides operations to call the quartile_Exc method.
        """
        from .quartile_exc.quartile_exc_request_builder import Quartile_ExcRequestBuilder

        return Quartile_ExcRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def quartile_inc(self) -> Quartile_IncRequestBuilder:
        """
        Provides operations to call the quartile_Inc method.
        """
        from .quartile_inc.quartile_inc_request_builder import Quartile_IncRequestBuilder

        return Quartile_IncRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def quotient(self) -> QuotientRequestBuilder:
        """
        Provides operations to call the quotient method.
        """
        from .quotient.quotient_request_builder import QuotientRequestBuilder

        return QuotientRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def radians(self) -> RadiansRequestBuilder:
        """
        Provides operations to call the radians method.
        """
        from .radians.radians_request_builder import RadiansRequestBuilder

        return RadiansRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def rand(self) -> RandRequestBuilder:
        """
        Provides operations to call the rand method.
        """
        from .rand.rand_request_builder import RandRequestBuilder

        return RandRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def rand_between(self) -> RandBetweenRequestBuilder:
        """
        Provides operations to call the randBetween method.
        """
        from .rand_between.rand_between_request_builder import RandBetweenRequestBuilder

        return RandBetweenRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def rank_avg(self) -> Rank_AvgRequestBuilder:
        """
        Provides operations to call the rank_Avg method.
        """
        from .rank_avg.rank_avg_request_builder import Rank_AvgRequestBuilder

        return Rank_AvgRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def rank_eq(self) -> Rank_EqRequestBuilder:
        """
        Provides operations to call the rank_Eq method.
        """
        from .rank_eq.rank_eq_request_builder import Rank_EqRequestBuilder

        return Rank_EqRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def rate(self) -> RateRequestBuilder:
        """
        Provides operations to call the rate method.
        """
        from .rate.rate_request_builder import RateRequestBuilder

        return RateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def received(self) -> ReceivedRequestBuilder:
        """
        Provides operations to call the received method.
        """
        from .received.received_request_builder import ReceivedRequestBuilder

        return ReceivedRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def replace(self) -> ReplaceRequestBuilder:
        """
        Provides operations to call the replace method.
        """
        from .replace.replace_request_builder import ReplaceRequestBuilder

        return ReplaceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def replace_b(self) -> ReplaceBRequestBuilder:
        """
        Provides operations to call the replaceB method.
        """
        from .replace_b.replace_b_request_builder import ReplaceBRequestBuilder

        return ReplaceBRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def rept(self) -> ReptRequestBuilder:
        """
        Provides operations to call the rept method.
        """
        from .rept.rept_request_builder import ReptRequestBuilder

        return ReptRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def right(self) -> RightRequestBuilder:
        """
        Provides operations to call the right method.
        """
        from .right.right_request_builder import RightRequestBuilder

        return RightRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def rightb(self) -> RightbRequestBuilder:
        """
        Provides operations to call the rightb method.
        """
        from .rightb.rightb_request_builder import RightbRequestBuilder

        return RightbRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def roman(self) -> RomanRequestBuilder:
        """
        Provides operations to call the roman method.
        """
        from .roman.roman_request_builder import RomanRequestBuilder

        return RomanRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def round(self) -> RoundRequestBuilder:
        """
        Provides operations to call the round method.
        """
        from .round.round_request_builder import RoundRequestBuilder

        return RoundRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def round_down(self) -> RoundDownRequestBuilder:
        """
        Provides operations to call the roundDown method.
        """
        from .round_down.round_down_request_builder import RoundDownRequestBuilder

        return RoundDownRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def round_up(self) -> RoundUpRequestBuilder:
        """
        Provides operations to call the roundUp method.
        """
        from .round_up.round_up_request_builder import RoundUpRequestBuilder

        return RoundUpRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def rows(self) -> RowsRequestBuilder:
        """
        Provides operations to call the rows method.
        """
        from .rows.rows_request_builder import RowsRequestBuilder

        return RowsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def rri(self) -> RriRequestBuilder:
        """
        Provides operations to call the rri method.
        """
        from .rri.rri_request_builder import RriRequestBuilder

        return RriRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sec(self) -> SecRequestBuilder:
        """
        Provides operations to call the sec method.
        """
        from .sec.sec_request_builder import SecRequestBuilder

        return SecRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sech(self) -> SechRequestBuilder:
        """
        Provides operations to call the sech method.
        """
        from .sech.sech_request_builder import SechRequestBuilder

        return SechRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def second(self) -> SecondRequestBuilder:
        """
        Provides operations to call the second method.
        """
        from .second.second_request_builder import SecondRequestBuilder

        return SecondRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def series_sum(self) -> SeriesSumRequestBuilder:
        """
        Provides operations to call the seriesSum method.
        """
        from .series_sum.series_sum_request_builder import SeriesSumRequestBuilder

        return SeriesSumRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sheet(self) -> SheetRequestBuilder:
        """
        Provides operations to call the sheet method.
        """
        from .sheet.sheet_request_builder import SheetRequestBuilder

        return SheetRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sheets(self) -> SheetsRequestBuilder:
        """
        Provides operations to call the sheets method.
        """
        from .sheets.sheets_request_builder import SheetsRequestBuilder

        return SheetsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sign(self) -> SignRequestBuilder:
        """
        Provides operations to call the sign method.
        """
        from .sign.sign_request_builder import SignRequestBuilder

        return SignRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sin(self) -> SinRequestBuilder:
        """
        Provides operations to call the sin method.
        """
        from .sin.sin_request_builder import SinRequestBuilder

        return SinRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sinh(self) -> SinhRequestBuilder:
        """
        Provides operations to call the sinh method.
        """
        from .sinh.sinh_request_builder import SinhRequestBuilder

        return SinhRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def skew(self) -> SkewRequestBuilder:
        """
        Provides operations to call the skew method.
        """
        from .skew.skew_request_builder import SkewRequestBuilder

        return SkewRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def skew_p(self) -> Skew_pRequestBuilder:
        """
        Provides operations to call the skew_p method.
        """
        from .skew_p.skew_p_request_builder import Skew_pRequestBuilder

        return Skew_pRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sln(self) -> SlnRequestBuilder:
        """
        Provides operations to call the sln method.
        """
        from .sln.sln_request_builder import SlnRequestBuilder

        return SlnRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def small(self) -> SmallRequestBuilder:
        """
        Provides operations to call the small method.
        """
        from .small.small_request_builder import SmallRequestBuilder

        return SmallRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sqrt(self) -> SqrtRequestBuilder:
        """
        Provides operations to call the sqrt method.
        """
        from .sqrt.sqrt_request_builder import SqrtRequestBuilder

        return SqrtRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sqrt_pi(self) -> SqrtPiRequestBuilder:
        """
        Provides operations to call the sqrtPi method.
        """
        from .sqrt_pi.sqrt_pi_request_builder import SqrtPiRequestBuilder

        return SqrtPiRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def st_dev_a(self) -> StDevARequestBuilder:
        """
        Provides operations to call the stDevA method.
        """
        from .st_dev_a.st_dev_a_request_builder import StDevARequestBuilder

        return StDevARequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def st_dev_p(self) -> StDev_PRequestBuilder:
        """
        Provides operations to call the stDev_P method.
        """
        from .st_dev_p.st_dev_p_request_builder import StDev_PRequestBuilder

        return StDev_PRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def st_dev_p_a(self) -> StDevPARequestBuilder:
        """
        Provides operations to call the stDevPA method.
        """
        from .st_dev_p_a.st_dev_p_a_request_builder import StDevPARequestBuilder

        return StDevPARequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def st_dev_s(self) -> StDev_SRequestBuilder:
        """
        Provides operations to call the stDev_S method.
        """
        from .st_dev_s.st_dev_s_request_builder import StDev_SRequestBuilder

        return StDev_SRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def standardize(self) -> StandardizeRequestBuilder:
        """
        Provides operations to call the standardize method.
        """
        from .standardize.standardize_request_builder import StandardizeRequestBuilder

        return StandardizeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def substitute(self) -> SubstituteRequestBuilder:
        """
        Provides operations to call the substitute method.
        """
        from .substitute.substitute_request_builder import SubstituteRequestBuilder

        return SubstituteRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def subtotal(self) -> SubtotalRequestBuilder:
        """
        Provides operations to call the subtotal method.
        """
        from .subtotal.subtotal_request_builder import SubtotalRequestBuilder

        return SubtotalRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sum(self) -> SumRequestBuilder:
        """
        Provides operations to call the sum method.
        """
        from .sum.sum_request_builder import SumRequestBuilder

        return SumRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sum_if(self) -> SumIfRequestBuilder:
        """
        Provides operations to call the sumIf method.
        """
        from .sum_if.sum_if_request_builder import SumIfRequestBuilder

        return SumIfRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sum_ifs(self) -> SumIfsRequestBuilder:
        """
        Provides operations to call the sumIfs method.
        """
        from .sum_ifs.sum_ifs_request_builder import SumIfsRequestBuilder

        return SumIfsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sum_sq(self) -> SumSqRequestBuilder:
        """
        Provides operations to call the sumSq method.
        """
        from .sum_sq.sum_sq_request_builder import SumSqRequestBuilder

        return SumSqRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def syd(self) -> SydRequestBuilder:
        """
        Provides operations to call the syd method.
        """
        from .syd.syd_request_builder import SydRequestBuilder

        return SydRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def t(self) -> TRequestBuilder:
        """
        Provides operations to call the t method.
        """
        from .t.t_request_builder import TRequestBuilder

        return TRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def t_dist(self) -> T_DistRequestBuilder:
        """
        Provides operations to call the t_Dist method.
        """
        from .t_dist.t_dist_request_builder import T_DistRequestBuilder

        return T_DistRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def t_dist_2_t(self) -> T_Dist_2TRequestBuilder:
        """
        Provides operations to call the t_Dist_2T method.
        """
        from .t_dist_2_t.t_dist_2_t_request_builder import T_Dist_2TRequestBuilder

        return T_Dist_2TRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def t_dist_r_t(self) -> T_Dist_RTRequestBuilder:
        """
        Provides operations to call the t_Dist_RT method.
        """
        from .t_dist_r_t.t_dist_r_t_request_builder import T_Dist_RTRequestBuilder

        return T_Dist_RTRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def t_inv(self) -> T_InvRequestBuilder:
        """
        Provides operations to call the t_Inv method.
        """
        from .t_inv.t_inv_request_builder import T_InvRequestBuilder

        return T_InvRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def t_inv_2_t(self) -> T_Inv_2TRequestBuilder:
        """
        Provides operations to call the t_Inv_2T method.
        """
        from .t_inv_2_t.t_inv_2_t_request_builder import T_Inv_2TRequestBuilder

        return T_Inv_2TRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tan(self) -> TanRequestBuilder:
        """
        Provides operations to call the tan method.
        """
        from .tan.tan_request_builder import TanRequestBuilder

        return TanRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tanh(self) -> TanhRequestBuilder:
        """
        Provides operations to call the tanh method.
        """
        from .tanh.tanh_request_builder import TanhRequestBuilder

        return TanhRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tbill_eq(self) -> TbillEqRequestBuilder:
        """
        Provides operations to call the tbillEq method.
        """
        from .tbill_eq.tbill_eq_request_builder import TbillEqRequestBuilder

        return TbillEqRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tbill_price(self) -> TbillPriceRequestBuilder:
        """
        Provides operations to call the tbillPrice method.
        """
        from .tbill_price.tbill_price_request_builder import TbillPriceRequestBuilder

        return TbillPriceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tbill_yield(self) -> TbillYieldRequestBuilder:
        """
        Provides operations to call the tbillYield method.
        """
        from .tbill_yield.tbill_yield_request_builder import TbillYieldRequestBuilder

        return TbillYieldRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def text(self) -> TextRequestBuilder:
        """
        Provides operations to call the text method.
        """
        from .text.text_request_builder import TextRequestBuilder

        return TextRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def time(self) -> TimeRequestBuilder:
        """
        Provides operations to call the time method.
        """
        from .time.time_request_builder import TimeRequestBuilder

        return TimeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def timevalue(self) -> TimevalueRequestBuilder:
        """
        Provides operations to call the timevalue method.
        """
        from .timevalue.timevalue_request_builder import TimevalueRequestBuilder

        return TimevalueRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def today(self) -> TodayRequestBuilder:
        """
        Provides operations to call the today method.
        """
        from .today.today_request_builder import TodayRequestBuilder

        return TodayRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def trim(self) -> TrimRequestBuilder:
        """
        Provides operations to call the trim method.
        """
        from .trim.trim_request_builder import TrimRequestBuilder

        return TrimRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def trim_mean(self) -> TrimMeanRequestBuilder:
        """
        Provides operations to call the trimMean method.
        """
        from .trim_mean.trim_mean_request_builder import TrimMeanRequestBuilder

        return TrimMeanRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def true_(self) -> TrueRequestBuilder:
        """
        Provides operations to call the true method.
        """
        from .true_.true_request_builder import TrueRequestBuilder

        return TrueRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def trunc(self) -> TruncRequestBuilder:
        """
        Provides operations to call the trunc method.
        """
        from .trunc.trunc_request_builder import TruncRequestBuilder

        return TruncRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def type(self) -> TypeRequestBuilder:
        """
        Provides operations to call the type method.
        """
        from .type.type_request_builder import TypeRequestBuilder

        return TypeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def unichar(self) -> UnicharRequestBuilder:
        """
        Provides operations to call the unichar method.
        """
        from .unichar.unichar_request_builder import UnicharRequestBuilder

        return UnicharRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def unicode(self) -> UnicodeRequestBuilder:
        """
        Provides operations to call the unicode method.
        """
        from .unicode.unicode_request_builder import UnicodeRequestBuilder

        return UnicodeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def upper(self) -> UpperRequestBuilder:
        """
        Provides operations to call the upper method.
        """
        from .upper.upper_request_builder import UpperRequestBuilder

        return UpperRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def usdollar(self) -> UsdollarRequestBuilder:
        """
        Provides operations to call the usdollar method.
        """
        from .usdollar.usdollar_request_builder import UsdollarRequestBuilder

        return UsdollarRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def value(self) -> ValueRequestBuilder:
        """
        Provides operations to call the value method.
        """
        from .value.value_request_builder import ValueRequestBuilder

        return ValueRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def var_a(self) -> VarARequestBuilder:
        """
        Provides operations to call the varA method.
        """
        from .var_a.var_a_request_builder import VarARequestBuilder

        return VarARequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def var_p(self) -> Var_PRequestBuilder:
        """
        Provides operations to call the var_P method.
        """
        from .var_p.var_p_request_builder import Var_PRequestBuilder

        return Var_PRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def var_p_a(self) -> VarPARequestBuilder:
        """
        Provides operations to call the varPA method.
        """
        from .var_p_a.var_p_a_request_builder import VarPARequestBuilder

        return VarPARequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def var_s(self) -> Var_SRequestBuilder:
        """
        Provides operations to call the var_S method.
        """
        from .var_s.var_s_request_builder import Var_SRequestBuilder

        return Var_SRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def vdb(self) -> VdbRequestBuilder:
        """
        Provides operations to call the vdb method.
        """
        from .vdb.vdb_request_builder import VdbRequestBuilder

        return VdbRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def vlookup(self) -> VlookupRequestBuilder:
        """
        Provides operations to call the vlookup method.
        """
        from .vlookup.vlookup_request_builder import VlookupRequestBuilder

        return VlookupRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def week_num(self) -> WeekNumRequestBuilder:
        """
        Provides operations to call the weekNum method.
        """
        from .week_num.week_num_request_builder import WeekNumRequestBuilder

        return WeekNumRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def weekday(self) -> WeekdayRequestBuilder:
        """
        Provides operations to call the weekday method.
        """
        from .weekday.weekday_request_builder import WeekdayRequestBuilder

        return WeekdayRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def weibull_dist(self) -> Weibull_DistRequestBuilder:
        """
        Provides operations to call the weibull_Dist method.
        """
        from .weibull_dist.weibull_dist_request_builder import Weibull_DistRequestBuilder

        return Weibull_DistRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def work_day(self) -> WorkDayRequestBuilder:
        """
        Provides operations to call the workDay method.
        """
        from .work_day.work_day_request_builder import WorkDayRequestBuilder

        return WorkDayRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def work_day_intl(self) -> WorkDay_IntlRequestBuilder:
        """
        Provides operations to call the workDay_Intl method.
        """
        from .work_day_intl.work_day_intl_request_builder import WorkDay_IntlRequestBuilder

        return WorkDay_IntlRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def xirr(self) -> XirrRequestBuilder:
        """
        Provides operations to call the xirr method.
        """
        from .xirr.xirr_request_builder import XirrRequestBuilder

        return XirrRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def xnpv(self) -> XnpvRequestBuilder:
        """
        Provides operations to call the xnpv method.
        """
        from .xnpv.xnpv_request_builder import XnpvRequestBuilder

        return XnpvRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def xor(self) -> XorRequestBuilder:
        """
        Provides operations to call the xor method.
        """
        from .xor.xor_request_builder import XorRequestBuilder

        return XorRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def year(self) -> YearRequestBuilder:
        """
        Provides operations to call the year method.
        """
        from .year.year_request_builder import YearRequestBuilder

        return YearRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def year_frac(self) -> YearFracRequestBuilder:
        """
        Provides operations to call the yearFrac method.
        """
        from .year_frac.year_frac_request_builder import YearFracRequestBuilder

        return YearFracRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def yield_(self) -> YieldRequestBuilder:
        """
        Provides operations to call the yield method.
        """
        from .yield_.yield_request_builder import YieldRequestBuilder

        return YieldRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def yield_disc(self) -> YieldDiscRequestBuilder:
        """
        Provides operations to call the yieldDisc method.
        """
        from .yield_disc.yield_disc_request_builder import YieldDiscRequestBuilder

        return YieldDiscRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def yield_mat(self) -> YieldMatRequestBuilder:
        """
        Provides operations to call the yieldMat method.
        """
        from .yield_mat.yield_mat_request_builder import YieldMatRequestBuilder

        return YieldMatRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def z_test(self) -> Z_TestRequestBuilder:
        """
        Provides operations to call the z_Test method.
        """
        from .z_test.z_test_request_builder import Z_TestRequestBuilder

        return Z_TestRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class FunctionsRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class FunctionsRequestBuilderGetQueryParameters():
        """
        Get functions from drives
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
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
    class FunctionsRequestBuilderGetRequestConfiguration(RequestConfiguration[FunctionsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class FunctionsRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

