'''
 # @ Create Time: 2022-11-05 16:58:58.526050
 # @ Create by：Zhidian Lin
'''

import pathlib
from dash import Dash
import dash_auth
from datetime import datetime
from dash import Dash, dcc, html, Input, Output, State, dash_table
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from buildChart import *
from dataSource import *
import openpyxl
import dash
import openpyxl
import flask
from dash.exceptions import PreventUpdate

本月合并底表 = 本月合并底表()
上月合并底表 = 上月合并底表()

上月WBS维度 = 上月WBS维度()
本月WBS维度 = 本月WBS维度()
actual上月WBS维度 = actual_wbs_tb(上月WBS维度)
actual本月WBS维度 = actual_wbs_tb(本月WBS维度)
type本月WBS维度 = wbs_type_number(本月WBS维度)
type上月WBS维度 = wbs_type_number(上月WBS维度)
cur_mon_staff = cleanCurMonStaff(本月人员维度())
last_mon_staff = cleanCurMonStaff(上月人员维度())

# indicator_Z_type_num_last = len(上月WBS维度[上月WBS维度['WBS类型'].isin(['Z'])])
# indicator_Z_type_num_cur = len(本月WBS维度[本月WBS维度['WBS类型'].isin(['Z'])])
# indicator_Z_type_act_last = 上月WBS维度[上月WBS维度['WBS类型'].isin(['Z'])]['实际人天'].sum()
# indicator_Z_type_act_cur = 本月WBS维度[本月WBS维度['WBS类型'].isin(['Z'])]['实际人天'].sum()
# others_numebr = indicator_wbs_number2(indicator_Z_type_num_cur, indicator_Z_type_num_last,'Others')
# z_act= indicator_wbs_number2(indicator_Z_type_act_cur, indicator_Z_type_act_last,'休假/非项目')

# indicator_scg_num_last = len(actual本月WBS维度[actual本月WBS维度['WBS所属部门'].isin(['新零售业务','创新业务部'])])
# indicator_scg_num_cur = len(actual本月WBS维度[actual本月WBS维度['WBS所属部门'].isin(['新零售业务','创新业务部'])])
# indicator_scg_act_last = actual本月WBS维度[actual本月WBS维度['WBS所属部门'].isin(['新零售业务','创新业务部'])]['实际人天'].sum()
# indicator_scg_act_cur = actual本月WBS维度[actual本月WBS维度['WBS所属部门'].isin(['新零售业务','创新业务部'])]['实际人天'].sum()
# scg_number = indicator_wbs_number2(indicator_scg_num_cur, indicator_scg_num_last,'SCG')
# scg_act = indicator_wbs_number2(indicator_scg_act_cur, indicator_scg_act_last,'SCG')


indicator_sxibg_num_last = 上月合并底表[
    上月合并底表['WBS所属部门'].isin(['中东云平台', '智慧综合体', '亚太云平台', '海外智慧生活与商业'])]
indicator_sxibg_num_last = indicator_sxibg_num_last[~indicator_sxibg_num_last['PM姓名'].isin(['谢乃玮'])]
indicator_sxibg_num_last = indicator_sxibg_num_last[indicator_sxibg_num_last['利润中心'].isin(['PL111'])]
indicator_sxibg_num_cur = 本月合并底表[
    本月合并底表['WBS所属部门'].isin(['中东云平台', '智慧综合体', '亚太云平台', '海外智慧生活与商业'])]
indicator_sxibg_num_cur = indicator_sxibg_num_cur[~indicator_sxibg_num_cur['PM姓名'].isin(['谢乃玮'])]
indicator_sxibg_num_cur = indicator_sxibg_num_cur[indicator_sxibg_num_cur['利润中心'].isin(['PL111'])]

indicator_sx_d_num_last = returnWBS_Bl_num(上月WBS维度, 'D',
                                           ['中东云平台', '智慧综合体', '亚太云平台', '海外智慧生活与商业'])
indicator_sx_d_num_cur = returnWBS_Bl_num(本月WBS维度, 'D',
                                          ['中东云平台', '智慧综合体', '亚太云平台', '海外智慧生活与商业'])
sx_d_number = indicator_wbs_number2(indicator_sx_d_num_cur, indicator_sx_d_num_last, 'SX')

indicator_sx_p_num_last = returnWBS_Bl_num(上月WBS维度, 'P',
                                           ['中东云平台', '智慧综合体', '亚太云平台', '海外智慧生活与商业'])
indicator_sx_p_num_cur = returnWBS_Bl_num(本月WBS维度, 'P',
                                          ['中东云平台', '智慧综合体', '亚太云平台', '海外智慧生活与商业'])
sx_p_number = indicator_wbs_number2(indicator_sx_p_num_cur, indicator_sx_p_num_last, 'SX')

indicator_sx_r_num_last = returnWBS_Bl_num(上月WBS维度, 'R',
                                           ['中东云平台', '智慧综合体', '亚太云平台', '海外智慧生活与商业'])
indicator_sx_r_num_cur = returnWBS_Bl_num(本月WBS维度, 'R',
                                          ['中东云平台', '智慧综合体', '亚太云平台', '海外智慧生活与商业'])
sx_r_number = indicator_wbs_number2(indicator_sx_r_num_cur, indicator_sx_r_num_last, 'SX')

indicator_sx_m_num_last = returnWBS_Bl_num(上月WBS维度, 'M',
                                           ['中东云平台', '智慧综合体', '亚太云平台', '海外智慧生活与商业'])
indicator_sx_m_num_cur = returnWBS_Bl_num(本月WBS维度, 'M',
                                          ['中东云平台', '智慧综合体', '亚太云平台', '海外智慧生活与商业'])
sx_m_number = indicator_wbs_number2(indicator_sx_m_num_cur, indicator_sx_m_num_last, 'SX')

indicator_sx_d_act_last = returnWBS_Bl_act(indicator_sxibg_num_last, 'D')
indicator_sx_d_act_cur = returnWBS_Bl_act(indicator_sxibg_num_cur, 'D')
sx_d_act = indicator_wbs_number2(indicator_sx_d_act_cur, indicator_sx_d_act_last, 'SX')

indicator_sx_p_act_last = returnWBS_Bl_act(indicator_sxibg_num_last, 'P')
indicator_sx_p_act_cur = returnWBS_Bl_act(indicator_sxibg_num_cur, 'P')
sx_p_act = indicator_wbs_number2(indicator_sx_p_act_cur, indicator_sx_p_act_last, 'SX')

indicator_sx_r_act_last = returnWBS_Bl_act(indicator_sxibg_num_last, 'R')
indicator_sx_r_act_cur = returnWBS_Bl_act(indicator_sxibg_num_cur, 'R')
sx_r_act = indicator_wbs_number2(indicator_sx_r_act_cur, indicator_sx_r_act_last, 'SX')

indicator_sx_m_act_last = returnWBS_Bl_act(indicator_sxibg_num_last, 'M')
indicator_sx_m_act_cur = returnWBS_Bl_act(indicator_sxibg_num_cur, 'M')
sx_m_act = indicator_wbs_number2(indicator_sx_m_act_cur, indicator_sx_m_act_last, 'SX')

# indicator_ssxibg_act_last = actual本月WBS维度[actual本月WBS维度['WBS所属部门'].isin(['中东云平台','亚太云平台'])]['实际人天'].sum()
# indicator_sxibg_act_cur = actual本月WBS维度[actual本月WBS维度['WBS所属部门'].isin(['中东云平台','亚太云平台'])]['实际人天'].sum()
# sx_act = indicator_wbs_number2(indicator_sxibg_act_cur, indicator_ssxibg_act_last,'SX')

indicator_ir_num_last = 上月合并底表[上月合并底表['WBS所属部门'].isin(['智慧娱乐', '亚太云平台'])]
indicator_ir_num_last = indicator_ir_num_last[~indicator_ir_num_last['PM姓名'].isin(['张赛'])]
indicator_ir_num_cur = 本月合并底表[本月合并底表['WBS所属部门'].isin(['智慧娱乐', '亚太云平台'])]
indicator_ir_num_cur = indicator_ir_num_cur[~indicator_ir_num_cur['PM姓名'].isin(['张赛'])]

indicator_ir_d_num_last = returnWBS_Bl_num(上月WBS维度, 'D', ['智慧娱乐'])
indicator_ir_d_num_cur = returnWBS_Bl_num(本月WBS维度, 'D', ['智慧娱乐'])
ir_d_number = indicator_wbs_number2(indicator_ir_d_num_cur, indicator_ir_d_num_last, 'IR')

indicator_ir_p_num_last = returnWBS_Bl_num(上月WBS维度, 'P', ['智慧娱乐'])
indicator_ir_p_num_cur = returnWBS_Bl_num(本月WBS维度, 'P', ['智慧娱乐'])
ir_p_number = indicator_wbs_number2(indicator_ir_p_num_cur, indicator_ir_p_num_last, 'IR')

indicator_ir_r_num_last = returnWBS_Bl_num(上月WBS维度, 'R', ['智慧娱乐'])
indicator_ir_r_num_cur = returnWBS_Bl_num(本月WBS维度, 'R', ['智慧娱乐'])
ir_r_number = indicator_wbs_number2(indicator_ir_r_num_cur, indicator_ir_r_num_last, 'IR')

indicator_ir_m_num_last = returnWBS_Bl_num(上月WBS维度, 'M', ['智慧娱乐'])
indicator_ir_m_num_cur = returnWBS_Bl_num(本月WBS维度, 'M', ['智慧娱乐'])
ir_m_number = indicator_wbs_number2(indicator_ir_m_num_cur, indicator_ir_m_num_last, 'IR')

indicator_ir_d_act_last = returnWBS_Bl_act(indicator_ir_num_last, 'D')
indicator_ir_d_act_cur = returnWBS_Bl_act(indicator_ir_num_cur, 'D')
ir_d_act = indicator_wbs_number2(indicator_ir_d_act_cur, indicator_ir_d_act_last, 'IR')

indicator_ir_p_act_last = returnWBS_Bl_act(indicator_ir_num_last, 'P')
indicator_ir_p_act_cur = returnWBS_Bl_act(indicator_ir_num_cur, 'P')
ir_p_act = indicator_wbs_number2(indicator_ir_p_act_cur, indicator_ir_p_act_last, 'IR')

indicator_ir_r_act_last = returnWBS_Bl_act(indicator_ir_num_last, 'R')
indicator_ir_r_act_cur = returnWBS_Bl_act(indicator_ir_num_cur, 'R')
ir_r_act = indicator_wbs_number2(indicator_ir_r_act_cur, indicator_ir_r_act_last, 'IR')

indicator_ir_m_act_last = returnWBS_Bl_act(indicator_ir_num_last, 'M')
indicator_ir_m_act_cur = returnWBS_Bl_act(indicator_ir_num_cur, 'M')
ir_m_act = indicator_wbs_number2(indicator_ir_m_act_cur, indicator_ir_m_act_last, 'IR')

#
# indicator_ir_act_last = actual本月WBS维度[actual本月WBS维度['WBS所属部门'].isin(['智慧娱乐'])]['实际人天'].sum()
# indicator_ir_act_cur = actual本月WBS维度[actual本月WBS维度['WBS所属部门'].isin(['智慧娱乐'])]['实际人天'].sum()
# ir_number = indicator_wbs_number2(indicator_ir_num_cur, indicator_ir_num_last,'IR')
# ir_act = indicator_wbs_number2(indicator_ir_act_cur, indicator_ir_act_last,'IR')

indicator_dx_num_last = 上月合并底表[上月合并底表['WBS所属部门'].isin(['运营与赋能中心'])]
indicator_dx_num_last = indicator_dx_num_last[~indicator_dx_num_last['PM姓名'].isin(['徐浩'])]
indicator_dx_num_cur = 本月合并底表[本月合并底表['WBS所属部门'].isin(['运营与赋能中心'])]
indicator_dx_num_cur = indicator_dx_num_cur[~indicator_dx_num_cur['PM姓名'].isin(['徐浩'])]

indicator_dx_d_num_last = returnWBS_Bl_num3(上月WBS维度, 'D', ['运营与赋能中心'], ['徐浩'])
indicator_dx_d_num_cur = returnWBS_Bl_num3(本月WBS维度, 'D', ['运营与赋能中心'], ['徐浩'])
dx_d_number = indicator_wbs_number2(indicator_dx_d_num_cur, indicator_dx_d_num_last, 'DX-TY')

indicator_dx_p_num_last = returnWBS_Bl_num3(上月WBS维度, 'P', ['运营与赋能中心'], ['徐浩'])
indicator_dx_p_num_cur = returnWBS_Bl_num3(本月WBS维度, 'P', ['运营与赋能中心'], ['徐浩'])
dx_p_number = indicator_wbs_number2(indicator_dx_p_num_cur, indicator_dx_p_num_last, 'DX-TY')

indicator_dx_r_num_last = returnWBS_Bl_num3(上月WBS维度, 'R', ['运营与赋能中心'], ['徐浩'])
indicator_dx_r_num_cur = returnWBS_Bl_num3(本月WBS维度, 'R', ['运营与赋能中心'], ['徐浩'])
dx_r_number = indicator_wbs_number2(indicator_dx_r_num_cur, indicator_dx_r_num_last, 'DX-TY')

indicator_dx_m_num_last = returnWBS_Bl_num3(上月WBS维度, 'M', ['运营与赋能中心'], ['徐浩'])
indicator_dx_m_num_cur = returnWBS_Bl_num3(本月WBS维度, 'M', ['运营与赋能中心'], ['徐浩'])
dx_m_number = indicator_wbs_number2(indicator_dx_m_num_cur, indicator_dx_m_num_last, 'DX-TY')

indicator_dx_d_act_last = returnWBS_Bl_act(indicator_dx_num_last, 'D')
indicator_dx_d_act_cur = returnWBS_Bl_act(indicator_dx_num_cur, 'D')
dx_d_act = indicator_wbs_number2(indicator_dx_d_act_cur, indicator_dx_d_act_last, 'DX-TY')

indicator_dx_p_act_last = returnWBS_Bl_act(indicator_dx_num_last, 'P')
indicator_dx_p_act_cur = returnWBS_Bl_act(indicator_dx_num_cur, 'P')
dx_p_act = indicator_wbs_number2(indicator_dx_p_act_cur, indicator_dx_p_act_last, 'DX-TY')

indicator_dx_r_act_last = returnWBS_Bl_act(indicator_dx_num_last, 'R')
indicator_dx_r_act_cur = returnWBS_Bl_act(indicator_dx_num_cur, 'R')
dx_r_act = indicator_wbs_number2(indicator_dx_r_act_cur, indicator_dx_r_act_last, 'DX-TY')

indicator_dx_m_act_last = returnWBS_Bl_act(indicator_dx_num_last, 'M')
indicator_dx_m_act_cur = returnWBS_Bl_act(indicator_dx_num_cur, 'M')
dx_m_act = indicator_wbs_number2(indicator_dx_m_act_cur, indicator_dx_m_act_last, 'DX-TY')

# indicator_innova_num_last = 上月合并底表[~上月合并底表['利润中心'].isin(['PL111'])]
# indicator_innova_num_cur = 本月合并底表[~本月合并底表['利润中心'].isin(['PL111'])]


indicator_innova_num_last = 上月合并底表[~上月合并底表['利润中心'].isin(['PL111'])]
# indicator_innova_num_last = indicator_innova_num_last[~indicator_innova_num_last['WBS所属部门'].isin(['中东云平台','智慧综合体','亚太云平台','海外智慧生活与商业'])]
indicator_innova_num_cur = 本月合并底表[~本月合并底表['利润中心'].isin(['PL111'])]
# indicator_innova_num_cur = indicator_innova_num_cur[~indicator_innova_num_cur['WBS所属部门'].isin(['中东云平台','智慧综合体','亚太云平台','海外智慧生活与商业'])]


indicator_innova_d_num_last = returnWBS_Bl_num2(上月WBS维度, 'D')
indicator_innova_d_num_cur = returnWBS_Bl_num2(本月WBS维度, 'D')
innova_d_number = indicator_wbs_number2(indicator_innova_d_num_cur, indicator_innova_d_num_last, '其他部门')

indicator_innova_p_num_last = returnWBS_Bl_num2(上月WBS维度, 'P')
indicator_innova_p_num_cur = returnWBS_Bl_num2(本月WBS维度, 'P')
innova_p_number = indicator_wbs_number2(indicator_innova_p_num_cur, indicator_innova_p_num_last, '其他部门')

indicator_innova_r_num_last = returnWBS_Bl_num2(上月WBS维度, 'R')
indicator_innova_r_num_cur = returnWBS_Bl_num2(本月WBS维度, 'R')
innova_r_number = indicator_wbs_number2(indicator_innova_r_num_cur, indicator_innova_r_num_last, '其他部门')

indicator_innova_m_num_last = returnWBS_Bl_num2(上月WBS维度, 'M')
indicator_innova_m_num_cur = returnWBS_Bl_num2(本月WBS维度, 'M')
innova_m_number = indicator_wbs_number2(indicator_innova_m_num_cur, indicator_innova_m_num_last, '其他部门')

indicator_innova_d_act_last = returnWBS_Bl_act(indicator_innova_num_last, 'D')
indicator_innova_d_act_cur = returnWBS_Bl_act(indicator_innova_num_cur, 'D')
innova_d_act = indicator_wbs_number2(indicator_innova_d_act_cur, indicator_innova_d_act_last, '其他部门')

indicator_innova_p_act_last = returnWBS_Bl_act(indicator_innova_num_last, 'P')
indicator_innova_p_act_cur = returnWBS_Bl_act(indicator_innova_num_cur, 'P')
innova_p_act = indicator_wbs_number2(indicator_innova_p_act_cur, indicator_innova_p_act_last, '其他部门')

indicator_innova_r_act_last = returnWBS_Bl_act(indicator_innova_num_last, 'R')
indicator_innova_r_act_cur = returnWBS_Bl_act(indicator_innova_num_cur, 'R')
innova_r_act = indicator_wbs_number2(indicator_innova_r_act_cur, indicator_innova_r_act_last, '其他部门')

indicator_innova_m_act_last = returnWBS_Bl_act(indicator_innova_num_last, 'M')
indicator_innova_m_act_cur = returnWBS_Bl_act(indicator_innova_num_cur, 'M')
innova_m_act = indicator_wbs_number2(indicator_innova_m_act_cur, indicator_innova_m_act_last, '其他部门')

# indicator_innova_act_last = actual本月WBS维度[actual本月WBS维度['WBS所属部门'].isin(['创新与赋能中心','创新业务'])]['实际人天'].sum()
# indicator_innova_act_cur = actual本月WBS维度[actual本月WBS维度['WBS所属部门'].isin(['创新与赋能中心','创新业务'])]['实际人天'].sum()
# chuangxin_number = indicator_wbs_number2(indicator_innova_num_cur, indicator_innova_num_last,'创新')
# chuangxin_act = indicator_wbs_number2(indicator_innova_act_cur, indicator_innova_act_last,'创新')

indicator_oac_num_last = 上月合并底表[上月合并底表['WBS所属部门'].isin(['运营与赋能中心'])]
indicator_oac_num_last = indicator_oac_num_last[~indicator_oac_num_last['PM姓名'].isin(['林智钿'])]
indicator_oac_num_cur = 本月合并底表[本月合并底表['WBS所属部门'].isin(['运营与赋能中心'])]
indicator_oac_num_cur = indicator_oac_num_cur[~indicator_oac_num_cur['PM姓名'].isin(['林智钿'])]

indicator_oac_d_num_last = returnWBS_Bl_num3(indicator_oac_num_last, 'D', ['运营与赋能中心'], ['林智钿'])
indicator_oac_d_num_cur = returnWBS_Bl_num3(indicator_oac_num_cur, 'D', ['运营与赋能中心'], ['林智钿'])
oac_d_number = indicator_wbs_number2(indicator_oac_d_num_cur, indicator_oac_d_num_last, '运赋')

indicator_oac_p_num_last = returnWBS_Bl_num3(indicator_oac_num_last, 'P', ['运营与赋能中心'], ['林智钿'])
indicator_oac_p_num_cur = returnWBS_Bl_num3(indicator_oac_num_cur, 'P', ['运营与赋能中心'], ['林智钿'])
oac_p_number = indicator_wbs_number2(indicator_oac_p_num_cur, indicator_oac_p_num_last, '运赋')

indicator_oac_r_num_last = returnWBS_Bl_num3(indicator_oac_num_last, 'R', ['运营与赋能中心'], ['林智钿'])
indicator_oac_r_num_cur = returnWBS_Bl_num3(indicator_oac_num_cur, 'R', ['运营与赋能中心'], ['林智钿']) - 1
oac_r_number = indicator_wbs_number2(indicator_oac_r_num_cur, indicator_oac_r_num_last, '运赋')

indicator_oac_m_num_last = returnWBS_Bl_num3(indicator_oac_num_last, 'M', ['运营与赋能中心'], ['林智钿'])
indicator_oac_m_num_cur = returnWBS_Bl_num3(indicator_oac_num_cur, 'M', ['运营与赋能中心'], ['林智钿']) - 1
oac_m_number = indicator_wbs_number2(indicator_oac_m_num_cur, indicator_oac_m_num_last, '运赋')

indicator_oac_d_act_last = returnWBS_Bl_act(indicator_oac_num_last, 'D')
indicator_oac_d_act_cur = returnWBS_Bl_act(indicator_oac_num_cur, 'D')
oac_d_act = indicator_wbs_number2(indicator_oac_d_act_cur, indicator_oac_d_act_last, '运赋')

indicator_oac_p_act_last = returnWBS_Bl_act(indicator_oac_num_last, 'P')
indicator_oac_p_act_cur = returnWBS_Bl_act(indicator_oac_num_cur, 'P')
oac_p_act = indicator_wbs_number2(indicator_oac_p_act_cur, indicator_oac_p_act_last, '运赋')

indicator_oac_r_act_last = returnWBS_Bl_act(indicator_oac_num_last, 'R')
indicator_oac_r_act_cur = returnWBS_Bl_act(indicator_oac_num_cur, 'R')
oac_r_act = indicator_wbs_number2(indicator_oac_r_act_cur, indicator_oac_r_act_last, '运赋')

indicator_oac_m_act_last = returnWBS_Bl_act(indicator_oac_num_last, 'M')
indicator_oac_m_act_cur = returnWBS_Bl_act(indicator_oac_num_cur, 'M')
oac_m_act = indicator_wbs_number2(indicator_oac_m_act_cur, indicator_oac_m_act_last, '运赋')

# indicator_oac_act_last = actual本月WBS维度[actual本月WBS维度['WBS所属部门'].isin(['运营与赋能中心'])]['实际人天'].sum()
# indicator_oac_act_cur = actual本月WBS维度[actual本月WBS维度['WBS所属部门'].isin(['运营与赋能中心'])]['实际人天'].sum()
# yunfu_number = indicator_wbs_number2(indicator_oac_num_cur, indicator_oac_num_last,'运赋')
# yunfu_act = indicator_wbs_number2(indicator_oac_act_cur, indicator_oac_act_last,'运赋')

indicator_mkt_num_last = 上月合并底表[上月合并底表['WBS所属部门'].isin(['产品方案与市场拓展'])]
indicator_mkt_num_cur = 本月合并底表[本月合并底表['WBS所属部门'].isin(['产品方案与市场拓展'])]

indicator_mkt_d_num_last = returnWBS_Bl_num(indicator_mkt_num_last, 'D', ['产品方案与市场拓展'])
indicator_mkt_d_num_cur = returnWBS_Bl_num(indicator_mkt_num_cur, 'D', ['产品方案与市场拓展'])
mkt_d_number = indicator_wbs_number2(indicator_mkt_d_num_cur, indicator_mkt_d_num_last, 'MKT')

indicator_mkt_p_num_last = returnWBS_Bl_num(indicator_mkt_num_last, 'P', ['产品方案与市场拓展'])
indicator_mkt_p_num_cur = returnWBS_Bl_num(indicator_mkt_num_cur, 'P', ['产品方案与市场拓展'])
mkt_p_number = indicator_wbs_number2(indicator_mkt_p_num_cur, indicator_mkt_p_num_last, 'MKT')

indicator_mkt_r_num_last = returnWBS_Bl_num(indicator_mkt_num_last, 'R', ['产品方案与市场拓展'])
indicator_mkt_r_num_cur = returnWBS_Bl_num(indicator_mkt_num_cur, 'R', ['产品方案与市场拓展'])
mkt_r_number = indicator_wbs_number2(indicator_mkt_r_num_cur, indicator_mkt_r_num_last, 'MKT')

indicator_mkt_m_num_last = returnWBS_Bl_num(indicator_mkt_num_last, 'M', ['产品方案与市场拓展'])
indicator_mkt_m_num_cur = returnWBS_Bl_num(indicator_mkt_num_cur, 'M', ['产品方案与市场拓展'])
mkt_m_number = indicator_wbs_number2(indicator_mkt_m_num_cur, indicator_mkt_m_num_last, 'MKT')

indicator_mkt_d_act_last = returnWBS_Bl_act(indicator_mkt_num_last, 'D')
indicator_mkt_d_act_cur = returnWBS_Bl_act(indicator_mkt_num_cur, 'D')
mkt_d_act = indicator_wbs_number2(indicator_mkt_d_act_cur, indicator_mkt_d_act_last, 'MKT')

indicator_mkt_p_act_last = returnWBS_Bl_act(indicator_mkt_num_last, 'P')
indicator_mkt_p_act_cur = returnWBS_Bl_act(indicator_mkt_num_cur, 'P')
mkt_p_act = indicator_wbs_number2(indicator_mkt_p_act_cur, indicator_mkt_p_act_last, 'MKT')

indicator_mkt_r_act_last = returnWBS_Bl_act(indicator_mkt_num_last, 'R')
indicator_mkt_r_act_cur = returnWBS_Bl_act(indicator_mkt_num_cur, 'R')
mkt_r_act = indicator_wbs_number2(indicator_mkt_r_act_cur, indicator_mkt_r_act_last, 'MKT')

indicator_mkt_m_act_last = returnWBS_Bl_act(indicator_mkt_num_last, 'M')
indicator_mkt_m_act_cur = returnWBS_Bl_act(indicator_mkt_num_cur, 'M')
mkt_m_act = indicator_wbs_number2(indicator_mkt_m_act_cur, indicator_mkt_m_act_last, 'MKT')

# indicator_mkt_act_last = actual本月WBS维度[actual本月WBS维度['WBS所属部门'].isin(['产品方案与市场拓展'])]['实际人天'].sum()
# indicator_mkt_act_cur = actual本月WBS维度[actual本月WBS维度['WBS所属部门'].isin(['产品方案与市场拓展'])]['实际人天'].sum()
# mkt_number = indicator_wbs_number2(indicator_mkt_num_cur, indicator_mkt_num_last,'MKT')
# mkt_act = indicator_wbs_number2(indicator_mkt_act_cur, indicator_mkt_act_last,'MKT')

# wbs_chuangfu_percentage = indicator_wbs_percentage(actual本月WBS维度,actual上月WBS维度, '创新与赋能中心','WBS所属部门','预估人天','实际人天','创新赋能填报率')
# wbs_sx_percentage = indicator_wbs_percentage(actual本月WBS维度,actual上月WBS维度, '中东云平台','WBS所属部门','预估人天','实际人天','SX填报率')
# wbs_ir_percentage = indicator_wbs_percentage(actual本月WBS维度,actual上月WBS维度, '智慧娱乐','WBS所属部门','预估人天','实际人天','IR填报率')
# wbs_aiot_percentage = indicator_wbs_percentage(actual本月WBS维度,actual上月WBS维度, '海外智能终端与应用','WBS所属部门','预估人天','实际人天','AIoT填报率')

# indicator_abg_num_last = len(wbs_abg(actual上月WBS维度, 'AB'))
# indicator_abg_num_cur = len(wbs_abg(actual本月WBS维度, 'AB'))
# indicator_abg_act_last = wbs_abg(actual上月WBS维度, 'AB')['实际人天'].sum()
# indicator_abg_act_cur = wbs_abg(actual本月WBS维度, 'AB')['实际人天'].sum()
# abg_number = indicator_wbs_number2(indicator_abg_num_cur, indicator_abg_num_last,'ABG')
# abg_act = indicator_wbs_number2(indicator_abg_act_cur, indicator_abg_act_last,'ABG')
#
# indicator_ibg_num_last = len(wbs_abg(actual上月WBS维度, 'IB'))
# indicator_ibg_num_cur = len(wbs_abg(actual本月WBS维度, 'IB'))
# indicator_ibg_act_last = wbs_abg(actual上月WBS维度, 'IB')['实际人天'].sum()
# indicator_ibg_act_cur = wbs_abg(actual本月WBS维度, 'IB')['实际人天'].sum()
# ibg_number = indicator_wbs_number2(indicator_ibg_num_cur, indicator_ibg_num_last,'IBG')
# ibg_act = indicator_wbs_number2(indicator_ibg_act_cur, indicator_ibg_act_last,'IBG')


external_stylesheets = ['https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/sandstone/bootstrap.min.css']
layout = dict(
    autosize=True,
    automargin=True,
    margin=dict(l=3, r=3, b=5, t=2),
    hovermode="closest",
    plot_bgcolor="#F9F9F9",
    paper_bgcolor="#F9F9F9",
    legend=dict(font=dict(size=10), orientation="h"),
)
# server = flask.Flask(__name__)
app = Dash(__name__, title="IRDC - 资源看板", external_stylesheets=[dbc.themes.SANDSTONE],
           update_title='刷新中，请稍等哦...',
           meta_tags=[{'name': 'viewport',
                       'content': 'width=device-width, initial-scale=1.0'}])

server = app.server

html.Img(src=app.get_asset_url('img/IRDC_removed_bg.png'), style={'width': '100%'})
VALID_USERNAME_PASSWORD_PAIRS = {
    cyber(
        'Vm0wd2VHUXhUWGRPVldScFVtMW9WRll3WkRSV2JGbDNXa1JTV0ZKdGVEQmFWVll3VmpGS2RHVkdXbFpOYmtKVVZqQmFTMlJIVmtsalJtaG9UV3N3ZUZkV1dsWmxSbGw1Vkd0a2FGSnRVbGhaYkdSdlpWWmFjMVp0UmxkTlZuQlhWRlpXVjJGSFZuRlJWR3M5'): cyber(
        'Vm0wd2QyVkZOVWRXV0doVVYwZG9jRlZ0TVZOV2JGbDNXa2M1VjFadGVIbFhhMXBQVmpGS2RHVkdiR0ZXVjJoeVZqQmFZV015VGtsaVJtUnBWa1phZVZadE1UUlRNbEpIVm01R1UySklRbTlaV0hCWFpWWmFjMVp0UmxkTlZuQlhWRlpXVjJGSFZuRlJWR3M5'),
    cyber(
        'Vm0wd2VHUXhUWGRPVldSWVYwZDRWVll3Wkc5WFZsbDNXa1JTVjFac2JETlhhMk0xWVd4S2MxZHFRbFZXYlUweFZtMTRZV014WkhWaVJtUlhUVEZLVFZac1ZtRldNVnBXVFZWV2FHVnFRVGs9'): cyber(
        'Vm0wd2QyVkhVWGhVV0dST1ZsZG9WRll3Wkc5V1ZsbDNXa1pPVmxKc2JETldNblF3VmpGS2RHVkdXbFpOYWtFeFdWWlZlRmRXUm5OaVJuQk9VbXh3VFZac1ZtRldNVnBXVFZWV2FHVnFRVGs9')
}
auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)

app.config.suppress_callback_exceptions = True

tabs_styles = {
    'height': '65px',
    'backgroundColor': '#F9F9F9',
    # 'borderBottom': '1px solid #d6d6d6',
    'borderLeft': 'None',
    'borderTop': 'None',
    'borderRight': 'None'
}
tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '10px',
    'fontWeight': 'bold'
}

tab_selected_style = {
    'borderTop': 'None',
    'borderRight': 'None',
    'borderLeft': 'None',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#d6d6d6',
    'color': 'black',
    'padding': '10px'
}

# indicator summary for irdc
cur_in_staff_number = len(cur_mon_staff[cur_mon_staff['员工组'] == "正式员工"])
last_in_staff_number = len(last_mon_staff[last_mon_staff['员工组'] == "正式员工"])
cur_out_staff_number = len(cur_mon_staff[cur_mon_staff['员工组'] == "外包员工"])
last_out_staff_number = len(last_mon_staff[last_mon_staff['员工组'] == "外包员工"])
cur_intern_staff_number = len(cur_mon_staff[cur_mon_staff['员工组'] == "实习生"])
last_intern_staff_number = len(last_mon_staff[last_mon_staff['员工组'] == "实习生"])
last_in_actual_day = last_mon_staff[last_mon_staff['员工组'] == "正式员工"]['实际人天'].sum()
cur_in_actual_day = cur_mon_staff[cur_mon_staff['员工组'] == "正式员工"]['实际人天'].sum()
last_out_actual_day = last_mon_staff[last_mon_staff['员工组'] == "外包员工"]['实际人天'].sum()
cur_out_actual_day = cur_mon_staff[cur_mon_staff['员工组'] == "外包员工"]['实际人天'].sum()
last_intern_actual_day = last_mon_staff[last_mon_staff['员工组'] == "实习生"]['实际人天'].sum()
cur_intern_actual_day = cur_mon_staff[cur_mon_staff['员工组'] == "实习生"]['实际人天'].sum()

last_in_lo_day = last_mon_staff[last_mon_staff['员工组'] == "正式员工"]['理论人天'].sum()
cur_in_lo_day = cur_mon_staff[cur_mon_staff['员工组'] == "正式员工"]['理论人天'].sum()
last_out_lo_day = last_mon_staff[last_mon_staff['员工组'] == "外包员工"]['理论人天'].sum()
cur_out_lo_day = cur_mon_staff[cur_mon_staff['员工组'] == "外包员工"]['理论人天'].sum()
last_intern_lo_day = last_mon_staff[last_mon_staff['员工组'] == "实习生"]['理论人天'].sum()
cur_intern_lo_day = cur_mon_staff[cur_mon_staff['员工组'] == "实习生"]['理论人天'].sum()

本月未填工时 = 本月未填工时名单()
上月未填工时 = 上月未填工时名单()
本月未填正式num = len(本月未填工时[本月未填工时['员工组'] == '正式员工'])
本月未填外包num = len(本月未填工时[本月未填工时['员工组'] == '外包员工'])
本月未填实习num = len(本月未填工时[本月未填工时['员工组'] == '实习生'])
上月未填正式num = len(上月未填工时[上月未填工时['员工组'] == '正式员工'])
上月未填外包num = len(上月未填工时[上月未填工时['员工组'] == '外包员工'])
上月未填实习num = len(上月未填工时[上月未填工时['员工组'] == '实习生'])

# staff_number_indicator = indicator_large_ppl(len(cur_mon_staff)+len(本月未填工时), len(last_mon_staff)+len(上月未填工时), "员工数")
# staff_in_indicator = indicator_ppl(cur_in_staff_number+本月未填正式num, last_in_staff_number+上月未填正式num, "正式")
# staff_out_indicator = indicator_ppl(cur_out_staff_number+本月未填外包num, last_out_staff_number+上月未填外包num, "外包")
# staff_intern_indicator = indicator_ppl(cur_intern_staff_number+本月未填实习num, last_intern_staff_number+上月未填实习num, "实习")

staff_number_indicator = indicator_large_ppl(len(本月人员维度()),
                                             len(上月人员维度()), "员工数")
staff_in_indicator = indicator_ppl(cur_in_staff_number, last_in_staff_number, "正式")
staff_out_indicator = indicator_ppl(cur_out_staff_number, last_out_staff_number, "外包")
staff_intern_indicator = indicator_ppl(cur_intern_staff_number, last_intern_staff_number, "实习")

# actual all day
act_allday = indicator_irdc_sum(本月合并底表, 上月合并底表, "实际人天", "实际人天")
act_in_day = indicator_ppl(cur_in_actual_day, last_in_actual_day, "正式")
act_out_day = indicator_ppl(cur_out_actual_day, last_out_actual_day, "外包")
act_intern_day = indicator_ppl(cur_intern_actual_day, cur_intern_actual_day, "实习")

# attendance
attend_allday = indicator_irdc_sum(cur_mon_staff, last_mon_staff, "实际人天", "考勤人天")
attend_in_day = indicator_ppl(cur_in_actual_day, last_in_actual_day, "正式")
attend_out_day = indicator_ppl(cur_out_actual_day, last_out_actual_day, "外包")
attend_intern_day = indicator_ppl(cur_intern_actual_day, cur_intern_actual_day, "实习")

# actural per day
act_perday = indicator_irdc_per(本月合并底表, 上月合并底表, "实际人天", "员工姓名", "实际人均")
act_in_perday = indicator_irdc_type_per(cur_in_actual_day, cur_in_staff_number, last_in_actual_day,
                                        last_in_staff_number, "正式")
act_out_perday = indicator_irdc_type_per(cur_out_actual_day, cur_out_staff_number, last_out_actual_day,
                                         last_out_staff_number, "外包")
act_intern_perday = indicator_irdc_type_per(cur_intern_actual_day, cur_intern_staff_number, last_intern_actual_day,
                                            last_intern_staff_number, "实习")

# est all day
est_allday = indicator_irdc_sum(cur_mon_staff, last_mon_staff, "预估人天", "预估人天")
est_percentage = indicator_irdc_rate(cur_mon_staff, last_mon_staff, "实际人天", "预估人天", "预估填报率")

# logic all day
logic_allday = indicator_irdc_sum(cur_mon_staff, last_mon_staff, "理论人天", "理论人天")
logic_percentage = indicator_irdc_rate(cur_mon_staff, last_mon_staff, "实际人天", "理论人天", "填报率")

# wbs
wbs_all_number = indicator_wbs_sum_wide(actual本月WBS维度, actual上月WBS维度, '项目编号', "WBS个数")
wbs_p_numebr = indicator_wbs_number(type本月WBS维度, type上月WBS维度, 'P', 'P类总个数')
wbs_m_numebr = indicator_wbs_number(type本月WBS维度, type上月WBS维度, 'M', 'M类总个数')
wbs_r_numebr = indicator_wbs_number(type本月WBS维度, type上月WBS维度, 'R', 'R类总个数')
wbs_d_numebr = indicator_wbs_number(type本月WBS维度, type上月WBS维度, 'D', 'D类总个数')

# wbs_p_numebr_sx = indicator_wbs_number_sm(type本月WBS维度, type上月WBS维度,'P','P类总数')
# wbs_m_numebr_sx = indicator_wbs_number_sm(type本月WBS维度, type上月WBS维度,'M','M类总数')
# wbs_r_numebr_sx = indicator_wbs_number_sm(type本月WBS维度, type上月WBS维度,'R','R类总数')
# wbs_d_numebr_sx = indicator_wbs_number_sm(type本月WBS维度, type上月WBS维度,'D','D类总数')

wbs_more_numebr = indicator_wbs_number2(len(本月WBS维度), len(上月WBS维度), '增加')
wbs_less_numebr = indicator_wbs_number2(len(上月WBS维度), len(本月WBS维度), '减少')

wbs_actual_hrs = indicator_wbs_act_wide(本月合并底表, 上月合并底表, '实际人天', '实际人天')
# wbs_p_act_percentage = indicator_wbs_type(actual本月WBS维度, actual上月WBS维度, 'P','WBS类型','实际人天','P占比')
# wbs_m_act_percentage = indicator_wbs_type(actual本月WBS维度, actual上月WBS维度, 'M','WBS类型','实际人天','M占比')
# wbs_r_act_percentage = indicator_wbs_type(actual本月WBS维度, actual上月WBS维度, 'R','WBS类型','实际人天','R占比')
# wbs_d_act_percentage = indicator_wbs_type(actual本月WBS维度, actual上月WBS维度, 'D','WBS类型','实际人天','D占比')

wbs_p_act = indicator_wbs_type_sum(本月合并底表, 上月合并底表, 'P', 'WBS类型', '实际人天', 'P类总人天')
wbs_m_act = indicator_wbs_type_sum(本月合并底表, 上月合并底表, 'M', 'WBS类型', '实际人天', 'M类总人天')
wbs_r_act = indicator_wbs_type_sum(本月合并底表, 上月合并底表, 'R', 'WBS类型', '实际人天', 'R类总人天')
wbs_d_act = indicator_wbs_type_sum(本月合并底表, 上月合并底表, 'D', 'WBS类型', '实际人天', 'D类总人天')

logic_in_percentage = indicator_logic_percentage(cur_in_actual_day, cur_in_lo_day, last_in_actual_day, last_in_lo_day,
                                                 "正式")
logic_out_percentage = indicator_logic_percentage(cur_out_actual_day, cur_out_lo_day, last_out_actual_day,
                                                  last_out_lo_day, "外包")
logic_intern_percentage = indicator_logic_percentage(cur_intern_actual_day, cur_intern_lo_day, last_intern_actual_day,
                                                     last_intern_lo_day, "实习")

# gpu usage
gpu_abud_avg_usage = indicator_gpu_percentage_large(gpu_monthly_usage(本年(), 本月(), 'SH1024/IRDC_A100_40G'),
                                                    gpu_monthly_usage(上年(), 上月(), 'SH1024/IRDC_A100_40G'),
                                                    'IRDC_A100_40G<br>平均使用率')
gpu_abud_10_usage = indicator_gpu_percentage_small(gpu_monthly_usage_time(本年(), 本月(), 'SH1024/IRDC_A100_40G', 10),
                                                   gpu_monthly_usage_time(上年(), 上月(), 'SH1024/IRDC_A100_40G', 10),
                                                   '10点')
gpu_abud_14_usage = indicator_gpu_percentage_small(gpu_monthly_usage_time(本年(), 本月(), 'SH1024/IRDC_A100_40G', 14),
                                                   gpu_monthly_usage_time(上年(), 上月(), 'SH1024/IRDC_A100_40G', 14),
                                                   '14点')
gpu_abud_18_usage = indicator_gpu_percentage_small(gpu_monthly_usage_time(本年(), 本月(), 'SH1024/IRDC_A100_40G', 18),
                                                   gpu_monthly_usage_time(上年(), 上月(), 'SH1024/IRDC_A100_40G', 18),
                                                   '18点')
gpu_abud_22_usage = indicator_gpu_percentage_small(gpu_monthly_usage_time(本年(), 本月(), 'SH1024/IRDC_A100_40G', 22),
                                                   gpu_monthly_usage_time(上年(), 上月(), 'SH1024/IRDC_A100_40G', 22),
                                                   '22点')

gpu_sg2_avg_usage = indicator_gpu_percentage_large(gpu_monthly_usage(本年(), 本月(), 'SH40/IRDC_1080Ti'),
                                                   gpu_monthly_usage(上年(), 上月(), 'SH40/IRDC_1080Ti'),
                                                   'IRDC_1080Ti<br>平均使用率')
gpu_sg2_10_usage = indicator_gpu_percentage_small(gpu_monthly_usage_time(本年(), 本月(), 'SH40/IRDC_1080Ti', 10),
                                                  gpu_monthly_usage_time(上年(), 上月(), 'SH40/IRDC_1080Ti', 10),
                                                  '10点')
gpu_sg2_14_usage = indicator_gpu_percentage_small(gpu_monthly_usage_time(本年(), 本月(), 'SH40/IRDC_1080Ti', 14),
                                                  gpu_monthly_usage_time(上年(), 上月(), 'SH40/IRDC_1080Ti', 14),
                                                  '14点')
gpu_sg2_18_usage = indicator_gpu_percentage_small(gpu_monthly_usage_time(本年(), 本月(), 'SH40/IRDC_1080Ti', 18),
                                                  gpu_monthly_usage_time(上年(), 上月(), 'SH40/IRDC_1080Ti', 18),
                                                  '18点')
gpu_sg2_22_usage = indicator_gpu_percentage_small(gpu_monthly_usage_time(本年(), 本月(), 'SH40/IRDC_1080Ti', 22),
                                                  gpu_monthly_usage_time(上年(), 上月(), 'SH40/IRDC_1080Ti', 22),
                                                  '22点')

gpu_sh40_avg_usage = indicator_gpu_percentage_large(gpu_monthly_usage(本年(), 本月(), 'SH40/IRDC_Share'),
                                                    gpu_monthly_usage(上年(), 上月(), 'SH40/IRDC_Share'),
                                                    'IRDC_Share<br>平均使用率')
gpu_sh40_10_usage = indicator_gpu_percentage_small(gpu_monthly_usage_time(本年(), 本月(), 'SH40/IRDC_Share', 10),
                                                   gpu_monthly_usage_time(上年(), 上月(), 'SH40/IRDC_Share', 10),
                                                   '10点')
gpu_sh40_14_usage = indicator_gpu_percentage_small(gpu_monthly_usage_time(本年(), 本月(), 'SH40/IRDC_Share', 14),
                                                   gpu_monthly_usage_time(上年(), 上月(), 'SH40/IRDC_Share', 14),
                                                   '14点')
gpu_sh40_18_usage = indicator_gpu_percentage_small(gpu_monthly_usage_time(本年(), 本月(), 'SH40/IRDC_Share', 18),
                                                   gpu_monthly_usage_time(上年(), 上月(), 'SH40/IRDC_Share', 18),
                                                   '18点')
gpu_sh40_22_usage = indicator_gpu_percentage_small(gpu_monthly_usage_time(本年(), 本月(), 'SH40/IRDC_Share', 22),
                                                   gpu_monthly_usage_time(上年(), 上月(), 'SH40/IRDC_Share', 22),
                                                   '22点')

gpu_sh1988_avg_usage = indicator_gpu_percentage_large(gpu_monthly_usage(本年(), 本月(), 'SH1988/IRDC_V100_16G'),
                                                      gpu_monthly_usage(上年(), 上月(), 'SH1988/IRDC_V100_16G'),
                                                      'IRDC_V100_16G<br>平均使用率')
gpu_sh1988_10_usage = indicator_gpu_percentage_small(gpu_monthly_usage_time(本年(), 本月(), 'SH1988/IRDC_V100_16G', 10),
                                                     gpu_monthly_usage_time(上年(), 上月(), 'SH1988/IRDC_V100_16G', 10),
                                                     '10点')
gpu_sh1988_14_usage = indicator_gpu_percentage_small(gpu_monthly_usage_time(本年(), 本月(), 'SH1988/IRDC_V100_16G', 14),
                                                     gpu_monthly_usage_time(上年(), 上月(), 'SH1988/IRDC_V100_16G', 14),
                                                     '14点')
gpu_sh1988_18_usage = indicator_gpu_percentage_small(gpu_monthly_usage_time(本年(), 本月(), 'SH1988/IRDC_V100_16G', 18),
                                                     gpu_monthly_usage_time(上年(), 上月(), 'SH1988/IRDC_V100_16G', 18),
                                                     '18点')
gpu_sh1988_22_usage = indicator_gpu_percentage_small(gpu_monthly_usage_time(本年(), 本月(), 'SH1988/IRDC_V100_16G', 22),
                                                     gpu_monthly_usage_time(上年(), 上月(), 'SH1988/IRDC_V100_16G', 22),
                                                     '22点')

biaozhuTask = 标注任务()
caijiTask = 采集任务()
budgetDf = 预算单()
monthly_bz_cur = monthly_bzcj(biaozhuTask, 1)
monthly_bz_last = monthly_bzcj(biaozhuTask, 2)
monthly_cj_cur = monthly_bzcj(caijiTask, 1)
monthly_cj_last = monthly_bzcj(caijiTask, 2)

# 标注
if len(monthly_bz_cur) != 0 and len(monthly_bz_last) != 0:
    dataBZ_indicator = indicator_large_ppl(len(tryExcept0(monthly_bz_cur)), len(tryExcept0(monthly_bz_last)), "标注数")
    dataBZ_bill_indicator = indicator_databz(tryExcept0(monthly_bz_cur), tryExcept0(monthly_bz_last), '费用（元）',
                                             '标注总账单')
else:
    dataBZ_indicator = indicator_large_forNA(tryExcept0(len(monthly_bz_cur)), tryExcept0(len(monthly_bz_last)),
                                             "标注数")
    dataBZ_bill_indicator = indicator_databz_forNA(tryExcept0(len(monthly_bz_cur)), tryExcept0(len(monthly_bz_last)),
                                                   '标注总账单')

dataBZ_done_indicator = indicator_ppl(tryExcept0(len(monthly_bz_cur[monthly_bz_cur['任务状态'] == '任务完成'])),
                                      tryExcept0(len(monthly_bz_last[monthly_bz_last['任务状态'] == '任务完成'])),
                                      "Done")
dataBZ_ing_indicator = indicator_ppl(tryExcept0(len(monthly_bz_cur[monthly_bz_cur['任务状态'] != '任务完成'])),
                                     tryExcept0(len(monthly_bz_last[monthly_bz_last['任务状态'] != '任务完成'])), "ING")
dataBZ_back_indicator = indicator_logic_percentage(
    tryExcept0(len(monthly_bz_cur[monthly_bz_cur['是否有数据包被打回'] == True])), tryExcept0(len(monthly_bz_cur)),
    tryExcept0(len(monthly_bz_last[monthly_bz_last['是否有数据包被打回'] == True])), tryExcept0(len(monthly_bz_last)),
    "返工比例")

dataBZ_sx_indicator = indicator_ppl(tryExcept0(len(monthly_bz_cur[monthly_bz_cur['业务线'] == 'SX'])),
                                    tryExcept0(len(monthly_bz_last[monthly_bz_last['业务线'] == 'SX'])), "SX")
dataBZ_dx_indicator = indicator_ppl(tryExcept0(len(monthly_bz_cur[monthly_bz_cur['业务线'] == 'DX'])),
                                    tryExcept0(len(monthly_bz_last[monthly_bz_last['业务线'] == 'DX'])), "DX")
dataBZ_ir_indicator = indicator_ppl(tryExcept0(len(monthly_bz_cur[monthly_bz_cur['业务线'] == 'IR'])),
                                    tryExcept0(len(monthly_bz_last[monthly_bz_last['业务线'] == 'IR'])), "IR")

dataBZ_bill_confirm = indicator_ppl(
    tryExcept0(monthly_bz_cur[monthly_bz_cur['账单确认'] == '已确认']['费用（元）'].sum()),
    tryExcept0(monthly_bz_last[monthly_bz_last['账单确认'] == '已确认']['费用（元）'].sum()), "已确认")
dataBZ_bill_onhold = indicator_ppl(tryExcept0(monthly_bz_cur[monthly_bz_cur['账单确认'] == '待确认']['费用（元）'].sum()),
                                   tryExcept0(
                                       monthly_bz_last[monthly_bz_last['账单确认'] == '待确认']['费用（元）'].sum()),
                                   "待确认")

# 采集
if len(monthly_cj_cur) != 0 and len(monthly_cj_last) != 0:
    dataCJ_indicator = indicator_large_ppl(len(tryExcept0(monthly_cj_cur)), len(tryExcept0(monthly_cj_last)), "采集数")
    dataCJ_bill_indicator = indicator_databz(tryExcept0(monthly_cj_cur), tryExcept0(monthly_cj_last), '费用（元）',
                                             '采集总账单')
    dataCJ_done_indicator = indicator_ppl(tryExcept0(len(monthly_cj_cur[monthly_cj_cur['任务状态'] == '任务完成'])),
                                          tryExcept0(len(monthly_cj_last[monthly_cj_last['任务状态'] == '任务完成'])),
                                          "Done")
    dataCJ_ing_indicator = indicator_ppl(tryExcept0(len(monthly_cj_cur[monthly_cj_cur['任务状态'] != '任务完成'])),
                                         tryExcept0(len(monthly_cj_last[monthly_cj_last['任务状态'] != '任务完成'])),
                                         "ING")
    dataCJ_back_indicator = indicator_ppl(0,
                                          tryExcept0(len(monthly_cj_last[monthly_cj_last['任务状态'] != '任务完成'])),
                                          "ING")

    dataCJ_sx_indicator = indicator_ppl(tryExcept0(len(monthly_cj_cur[monthly_cj_cur['业务线'] == 'SX'])),
                                        tryExcept0(len(monthly_cj_last[monthly_cj_last['业务线'] == 'SX'])), "SX")
    dataCJ_dx_indicator = indicator_ppl(tryExcept0(len(monthly_cj_cur[monthly_cj_cur['业务线'] == 'DX'])),
                                        tryExcept0(len(monthly_cj_last[monthly_cj_last['业务线'] == 'DX'])), "DX")
    dataCJ_ir_indicator = indicator_ppl(tryExcept0(len(monthly_cj_cur[monthly_cj_cur['业务线'] == 'IR'])),
                                        tryExcept0(len(monthly_cj_last[monthly_cj_last['业务线'] == 'IR'])), "IR")

    dataCJ_bill_confirm = indicator_ppl(
        tryExcept0(monthly_cj_cur[monthly_cj_cur['账单确认'] == '已确认']['费用（元）'].sum()),
        tryExcept0(monthly_cj_last[monthly_cj_last['账单确认'] == '已确认']['费用（元）'].sum()),
        "已确认")
    dataCJ_bill_onhold = indicator_ppl(
        tryExcept0(monthly_cj_cur[monthly_cj_cur['账单确认'] == '待确认']['费用（元）'].sum()),
        tryExcept0(monthly_cj_last[monthly_cj_last['账单确认'] == '待确认']['费用（元）'].sum()),
        "待确认")

elif len(monthly_cj_cur) != 0:
    dataCJ_indicator = indicator_large_forNA(tryExcept0(len(monthly_cj_cur)), 0, "采集数")
    dataCJ_bill_indicator = indicator_databz_forNA(tryExcept0(monthly_cj_cur['费用（元）'].sum()), 0, '采集总账单')
    dataCJ_done_indicator = indicator_ppl(tryExcept0(len(monthly_cj_cur[monthly_cj_cur['任务状态'] == '任务完成'])), 0,
                                          "Done")
    dataCJ_ing_indicator = indicator_ppl(tryExcept0(len(monthly_cj_cur[monthly_cj_cur['任务状态'] != '任务完成'])), 0,
                                         "ING")
    dataCJ_back_indicator = indicator_ppl(tryExcept0(len(monthly_cj_cur[monthly_cj_cur['任务状态'] != '任务完成'])), 0,
                                          "ING")

    dataCJ_sx_indicator = indicator_ppl(tryExcept0(len(monthly_cj_cur[monthly_cj_cur['业务线'] == 'SX'])), 0, "SX")
    dataCJ_dx_indicator = indicator_ppl(tryExcept0(len(monthly_cj_cur[monthly_cj_cur['业务线'] == 'DX'])), 0, "DX")
    dataCJ_ir_indicator = indicator_ppl(tryExcept0(len(monthly_cj_cur[monthly_cj_cur['业务线'] == 'IR'])), 0, "IR")

    dataCJ_bill_confirm = indicator_ppl(
        tryExcept0(monthly_cj_cur[monthly_cj_cur['账单确认'] == '已确认']['费用（元）'].sum()), 0,
        "已确认")
    dataCJ_bill_onhold = indicator_ppl(
        tryExcept0(monthly_cj_cur[monthly_cj_cur['账单确认'] == '待确认']['费用（元）'].sum()), 0,
        "待确认")

elif len(monthly_cj_last) != 0:
    dataCJ_indicator = indicator_large_forNA(0, tryExcept0(len(monthly_cj_last)), "采集数")
    dataCJ_bill_indicator = indicator_databz_forNA(0, tryExcept0(monthly_cj_last['费用（元）'].sum()), '采集总账单')
    dataCJ_done_indicator = indicator_ppl(0,
                                          tryExcept0(len(monthly_cj_last[monthly_cj_last['任务状态'] == '任务完成'])),
                                          "Done")
    dataCJ_ing_indicator = indicator_ppl(0,
                                         tryExcept0(len(monthly_cj_last[monthly_cj_last['任务状态'] != '任务完成'])),
                                         "ING")
    dataCJ_back_indicator = indicator_ppl(0,
                                          tryExcept0(len(monthly_cj_last[monthly_cj_last['任务状态'] != '任务完成'])),
                                          "ING")

    dataCJ_sx_indicator = indicator_ppl(0,
                                        tryExcept0(len(monthly_cj_last[monthly_cj_last['业务线'] == 'SX'])), "SX")
    dataCJ_dx_indicator = indicator_ppl(0,
                                        tryExcept0(len(monthly_cj_last[monthly_cj_last['业务线'] == 'DX'])), "DX")
    dataCJ_ir_indicator = indicator_ppl(0,
                                        tryExcept0(len(monthly_cj_last[monthly_cj_last['业务线'] == 'IR'])), "IR")

    dataCJ_bill_confirm = indicator_ppl(0,
                                        tryExcept0(
                                            monthly_cj_last[monthly_cj_last['账单确认'] == '已确认']['费用（元）'].sum()),
                                        "已确认")
    dataCJ_bill_onhold = indicator_ppl(0,
                                       tryExcept0(
                                           monthly_cj_last[monthly_cj_last['账单确认'] == '待确认']['费用（元）'].sum()),
                                       "待确认")

sxData = filDataApartment(本月合并底表, '智慧综合体')
irData = filDataApartment(本月合并底表, '智慧娱乐')
dxSkuData = filDataApartment(本月合并底表, '创新孵化-冰箱')
dxTyData = filDataApartment(本月合并底表, '创新孵化-体育')
mktData = filDataApartment(本月合并底表, '市场拓展部')
oacData = filDataApartment(本月合并底表, '运营与赋能中心')

sxDataLast = filDataApartment(上月合并底表, '智慧综合体')
irDataLast = filDataApartment(上月合并底表, '智慧娱乐')
dxSkuDataLast = filDataApartment(上月合并底表, '创新孵化-冰箱')
dxTyDataLast = filDataApartment(上月合并底表, '创新孵化-体育')
mktDataLast = filDataApartment(上月合并底表, '市场拓展部')
oacDataLast = filDataApartment(上月合并底表, '运营与赋能中心')

sxDataTotal = int(sxData['实际人天'].sum())
sxDataTotalLast = int(sxDataLast['实际人天'].sum())

irDataTotal = int(irData['实际人天'].sum())
irDataTotalLast = int(irDataLast['实际人天'].sum())

dxSkuDataTotal = int(dxSkuData['实际人天'].sum())
dxSkuDataTotalLast = int(dxSkuDataLast['实际人天'].sum())

dxTyDataTotal = int(dxTyData['实际人天'].sum())
dxTyDataTotalLast = int(dxTyDataLast['实际人天'].sum())

mktDataTotal = int(mktData['实际人天'].sum())
mktDataTotalLast = int(mktDataLast['实际人天'].sum())

oacDataTotal = int(oacData['实际人天'].sum())
oacDataTotalLast = int(oacDataLast['实际人天'].sum())

sxGroup算法 = tryExceptNone(blGroupByTitle(sxData, '资源池', '算法SDK资源池'))
sxGroup开发 = tryExceptNone(blGroupByTitle(sxData, '资源池', '业务开发资源池'))
sxGroup架构 = tryExceptNone(blGroupByTitle(sxData, '资源池', '架构平台资源池'))
sxGroup测试 = tryExceptNone(blGroupByTitle(sxData, '资源池', '测试运维资源池'))
sxGroup非 = tryExceptNone(blGroupByTitle(sxData, '资源池', '非资源池'))
sxGroup非per = tryExceptNone(blGroupByTitlePer(sxGroup非, sxData))
sxGroup算法per = tryExceptNone(blGroupByTitlePer(sxGroup算法, sxData))
sxGroup开发per = tryExceptNone(blGroupByTitlePer(sxGroup开发, sxData))
sxGroup架构per = tryExceptNone(blGroupByTitlePer(sxGroup架构, sxData))
sxGroup测试per = tryExceptNone(blGroupByTitlePer(sxGroup测试, sxData))

sxGroup算法last = tryExceptNone(blGroupByTitle(sxDataLast, '资源池', '算法SDK资源池'))
sxGroup开发last = tryExceptNone(blGroupByTitle(sxDataLast, '资源池', '业务开发资源池'))
sxGroup架构last = tryExceptNone(blGroupByTitle(sxDataLast, '资源池', '架构平台资源池'))
sxGroup测试last = tryExceptNone(blGroupByTitle(sxDataLast, '资源池', '测试运维资源池'))
sxGroup非last = tryExceptNone(blGroupByTitle(sxDataLast, '资源池', '非资源池'))
sxGroup非perLast = tryExceptNone(blGroupByTitlePer(sxGroup非last, sxDataLast))
sxGroup算法perLast = tryExceptNone(blGroupByTitlePer(sxGroup算法last, sxDataLast))
sxGroup开发perLast = tryExceptNone(blGroupByTitlePer(sxGroup开发last, sxDataLast))
sxGroup架构perLast = tryExceptNone(blGroupByTitlePer(sxGroup架构last, sxDataLast))
sxGroup测试perLast = tryExceptNone(blGroupByTitlePer(sxGroup测试last, sxDataLast))

irGroup算法 = tryExceptNone(blGroupByTitle(irData, '资源池', '算法SDK资源池'))
irGroup开发 = tryExceptNone(blGroupByTitle(irData, '资源池', '业务开发资源池'))
irGroup架构 = tryExceptNone(blGroupByTitle(irData, '资源池', '架构平台资源池'))
irGroup测试 = tryExceptNone(blGroupByTitle(irData, '资源池', '测试运维资源池'))
irGroup非 = tryExceptNone(blGroupByTitle(irData, '资源池', '非资源池'))
irGroup非per = tryExceptNone(blGroupByTitlePer(irGroup非, irData))
irGroup算法per = tryExceptNone(blGroupByTitlePer(irGroup算法, irData))
irGroup开发per = tryExceptNone(blGroupByTitlePer(irGroup开发, irData))
irGroup架构per = tryExceptNone(blGroupByTitlePer(irGroup架构, irData))
irGroup测试per = tryExceptNone(blGroupByTitlePer(irGroup测试, irData))

irGroup算法last = tryExceptNone(blGroupByTitle(irDataLast, '资源池', '算法SDK资源池'))
irGroup开发last = tryExceptNone(blGroupByTitle(irDataLast, '资源池', '业务开发资源池'))
irGroup架构last = tryExceptNone(blGroupByTitle(irDataLast, '资源池', '架构平台资源池'))
irGroup测试last = tryExceptNone(blGroupByTitle(irDataLast, '资源池', '测试运维资源池'))
irGroup非last = tryExceptNone(blGroupByTitle(irDataLast, '资源池', '非资源池'))
irGroup非perLast = tryExceptNone(blGroupByTitlePer(irGroup非last, irDataLast))
irGroup算法perLast = tryExceptNone(blGroupByTitlePer(irGroup算法last, irDataLast))
irGroup开发perLast = tryExceptNone(blGroupByTitlePer(irGroup开发last, irDataLast))
irGroup架构perLast = tryExceptNone(blGroupByTitlePer(irGroup架构last, irDataLast))
irGroup测试perLast = tryExceptNone(blGroupByTitlePer(irGroup测试last, irDataLast))

dxSkuGroup算法 = tryExceptNone(blGroupByTitle(dxSkuData, '资源池', '算法SDK资源池'))
dxSkuGroup开发 = tryExceptNone(blGroupByTitle(dxSkuData, '资源池', '业务开发资源池'))
dxSkuGroup架构 = tryExceptNone(blGroupByTitle(dxSkuData, '资源池', '架构平台资源池'))
dxSkuGroup测试 = tryExceptNone(blGroupByTitle(dxSkuData, '资源池', '测试运维资源池'))
dxSkuGroup非 = tryExceptNone(blGroupByTitle(dxSkuData, '资源池', '非资源池'))
dxSkuGroup非per = tryExceptNone(blGroupByTitlePer(dxSkuGroup非, dxSkuData))
dxSkuGroup算法per = tryExceptNone(blGroupByTitlePer(dxSkuGroup算法, dxSkuData))
dxSkuGroup开发per = tryExceptNone(blGroupByTitlePer(dxSkuGroup开发, dxSkuData))
dxSkuGroup架构per = tryExceptNone(blGroupByTitlePer(dxSkuGroup架构, dxSkuData))
dxSkuGroup测试per = tryExceptNone(blGroupByTitlePer(dxSkuGroup测试, dxSkuData))

dxSkuGroup算法last = tryExceptNone(blGroupByTitle(dxSkuDataLast, '资源池', '算法SDK资源池'))
dxSkuGroup开发last = tryExceptNone(blGroupByTitle(dxSkuDataLast, '资源池', '业务开发资源池'))
dxSkuGroup架构last = tryExceptNone(blGroupByTitle(dxSkuDataLast, '资源池', '架构平台资源池'))
dxSkuGroup测试last = tryExceptNone(blGroupByTitle(dxSkuDataLast, '资源池', '测试运维资源池'))
dxSkuGroup非last = tryExceptNone(blGroupByTitle(dxSkuDataLast, '资源池', '非资源池'))
dxSkuGroup非perLast = tryExceptNone(blGroupByTitlePer(dxSkuGroup非last, dxSkuDataLast))
dxSkuGroup算法perLast = tryExceptNone(blGroupByTitlePer(dxSkuGroup算法last, dxSkuDataLast))
dxSkuGroup开发perLast = tryExceptNone(blGroupByTitlePer(dxSkuGroup开发last, dxSkuDataLast))
dxSkuGroup架构perLast = tryExceptNone(blGroupByTitlePer(dxSkuGroup架构last, dxSkuDataLast))
dxSkuGroup测试perLast = tryExceptNone(blGroupByTitlePer(dxSkuGroup测试last, dxSkuDataLast))

dxTyGroup算法 = tryExceptNone(blGroupByTitle(dxTyData, '资源池', '算法SDK资源池'))
dxTyGroup开发 = tryExceptNone(blGroupByTitle(dxTyData, '资源池', '业务开发资源池'))
dxTyGroup架构 = tryExceptNone(blGroupByTitle(dxTyData, '资源池', '架构平台资源池'))
dxTyGroup测试 = tryExceptNone(blGroupByTitle(dxTyData, '资源池', '测试运维资源池'))
dxTyGroup非 = tryExceptNone(blGroupByTitle(dxTyData, '资源池', '非资源池'))
dxTyGroup非per = tryExceptNone(blGroupByTitlePer(dxTyGroup非, dxTyData))
dxTyGroup算法per = tryExceptNone(blGroupByTitlePer(dxTyGroup算法, dxTyData))
dxTyGroup开发per = tryExceptNone(blGroupByTitlePer(dxTyGroup开发, dxTyData))
dxTyGroup架构per = tryExceptNone(blGroupByTitlePer(dxTyGroup架构, dxTyData))
dxTyGroup测试per = tryExceptNone(blGroupByTitlePer(dxTyGroup测试, dxTyData))

dxTyGroup算法last = tryExceptNone(blGroupByTitle(dxTyDataLast, '资源池', '算法SDK资源池'))
dxTyGroup开发last = tryExceptNone(blGroupByTitle(dxTyDataLast, '资源池', '业务开发资源池'))
dxTyGroup架构last = tryExceptNone(blGroupByTitle(dxTyDataLast, '资源池', '架构平台资源池'))
dxTyGroup测试last = tryExceptNone(blGroupByTitle(dxTyDataLast, '资源池', '测试运维资源池'))
dxTyGroup非last = tryExceptNone(blGroupByTitle(dxTyDataLast, '资源池', '非资源池'))
dxTyGroup非perLast = tryExceptNone(blGroupByTitlePer(dxTyGroup非last, dxTyDataLast))
dxTyGroup算法perLast = tryExceptNone(blGroupByTitlePer(dxTyGroup算法last, dxTyDataLast))
dxTyGroup开发perLast = tryExceptNone(blGroupByTitlePer(dxTyGroup开发last, dxTyDataLast))
dxTyGroup架构perLast = tryExceptNone(blGroupByTitlePer(dxTyGroup架构last, dxTyDataLast))
dxTyGroup测试perLast = tryExceptNone(blGroupByTitlePer(dxTyGroup测试last, dxTyDataLast))

mktGroup算法 = tryExceptNone(blGroupByTitle(mktData, '资源池', '算法SDK资源池'))
mktGroup开发 = tryExceptNone(blGroupByTitle(mktData, '资源池', '业务开发资源池'))
mktGroup架构 = tryExceptNone(blGroupByTitle(mktData, '资源池', '架构平台资源池'))
mktGroup测试 = tryExceptNone(blGroupByTitle(mktData, '资源池', '测试运维资源池'))
mktGroup非 = tryExceptNone(blGroupByTitle(mktData, '资源池', '非资源池'))
mktGroup非per = tryExceptNone(blGroupByTitlePer(mktGroup非, mktData))
mktGroup算法per = tryExceptNone(blGroupByTitlePer(mktGroup算法, mktData))
mktGroup开发per = tryExceptNone(blGroupByTitlePer(mktGroup开发, mktData))
mktGroup架构per = tryExceptNone(blGroupByTitlePer(mktGroup架构, mktData))
mktGroup测试per = tryExceptNone(blGroupByTitlePer(mktGroup测试, mktData))

mktGroup算法last = tryExceptNone(blGroupByTitle(mktDataLast, '资源池', '算法SDK资源池'))
mktGroup开发last = tryExceptNone(blGroupByTitle(mktDataLast, '资源池', '业务开发资源池'))
mktGroup架构last = tryExceptNone(blGroupByTitle(mktDataLast, '资源池', '架构平台资源池'))
mktGroup测试last = tryExceptNone(blGroupByTitle(mktDataLast, '资源池', '测试运维资源池'))
mktGroup非last = tryExceptNone(blGroupByTitle(mktDataLast, '资源池', '非资源池'))
mktGroup非perLast = tryExceptNone(blGroupByTitlePer(mktGroup非last, mktDataLast))
mktGroup算法perLast = tryExceptNone(blGroupByTitlePer(mktGroup算法last, mktDataLast))
mktGroup开发perLast = tryExceptNone(blGroupByTitlePer(mktGroup开发last, mktDataLast))
mktGroup架构perLast = tryExceptNone(blGroupByTitlePer(mktGroup架构last, mktDataLast))
mktGroup测试perLast = tryExceptNone(blGroupByTitlePer(mktGroup测试last, mktDataLast))

oacGroup算法 = tryExceptNone(blGroupByTitle(oacData, '资源池', '算法SDK资源池'))
oacGroup开发 = tryExceptNone(blGroupByTitle(oacData, '资源池', '业务开发资源池'))
oacGroup架构 = tryExceptNone(blGroupByTitle(oacData, '资源池', '架构平台资源池'))
oacGroup测试 = tryExceptNone(blGroupByTitle(oacData, '资源池', '测试运维资源池'))
oacGroup非 = tryExceptNone(blGroupByTitle(oacData, '资源池', '非资源池'))
oacGroup算法per = tryExceptNone(blGroupByTitlePer(oacGroup算法, oacData))
oacGroup开发per = tryExceptNone(blGroupByTitlePer(oacGroup开发, oacData))
oacGroup架构per = tryExceptNone(blGroupByTitlePer(oacGroup架构, oacData))
oacGroup测试per = tryExceptNone(blGroupByTitlePer(oacGroup测试, oacData))
oacGroup非per = tryExceptNone(blGroupByTitlePer(oacGroup非, oacData))

oacGroup算法last = tryExceptNone(blGroupByTitle(oacDataLast, '资源池', '算法SDK资源池'))
oacGroup开发last = tryExceptNone(blGroupByTitle(oacDataLast, '资源池', '业务开发资源池'))
oacGroup架构last = tryExceptNone(blGroupByTitle(oacDataLast, '资源池', '架构平台资源池'))
oacGroup测试last = tryExceptNone(blGroupByTitle(oacDataLast, '资源池', '测试运维资源池'))
oacGroup非last = tryExceptNone(blGroupByTitle(oacDataLast, '资源池', '非资源池'))
oacGroup算法perLast = tryExceptNone(blGroupByTitlePer(oacGroup算法last, oacDataLast))
oacGroup开发perLast = tryExceptNone(blGroupByTitlePer(oacGroup开发last, oacDataLast))
oacGroup架构perLast = tryExceptNone(blGroupByTitlePer(oacGroup架构last, oacDataLast))
oacGroup测试perLast = tryExceptNone(blGroupByTitlePer(oacGroup测试last, oacDataLast))
oacGroup非perLast = tryExceptNone(blGroupByTitlePer(oacGroup非last, oacDataLast))

sx_wh_total = indicator_bl_total(sxDataTotal, sxDataTotalLast, "SX 总人天")
ir_wh_total = indicator_bl_total(irDataTotal, irDataTotalLast, "IR 总人天")
dxSku_wh_total = indicator_bl_total(dxSkuDataTotal, dxSkuDataTotalLast, "DX-SKU 总人天")
dxTy_wh_total = indicator_bl_total(dxTyDataTotal, dxTyDataTotalLast, "DX-TY 总人天")
mkt_wh_total = indicator_bl_total(mktDataTotal, mktDataTotalLast, "MKT 总人天")
oac_wh_total = indicator_bl_total(oacDataTotal, oacDataTotalLast, "运赋 总人天")

sx_算法资源池 = indicator_bl_total_mid(sxGroup算法, sxGroup算法last, '算法')
ir_算法资源池 = indicator_bl_total_mid(irGroup算法, irGroup算法last, '算法')
dxSku_算法资源池 = indicator_bl_total_mid(dxSkuGroup算法, dxSkuGroup算法last, '算法')
dxTy_算法资源池 = indicator_bl_total_mid(dxTyGroup算法, dxTyGroup算法last, '算法')
mkt_算法资源池 = indicator_bl_total_mid(mktGroup算法, mktGroup算法last, '算法')
oac_算法资源池 = indicator_bl_total_mid(oacGroup算法, oacGroup算法last, '算法')

sx_算法资源池per = indicator_bl_total_mid_rate(sxGroup算法per, sxGroup算法perLast, '占比')
ir_算法资源池per = indicator_bl_total_mid_rate(irGroup算法per, irGroup算法perLast, '占比')
dxSku_算法资源池per = indicator_bl_total_mid_rate(dxSkuGroup算法per, dxSkuGroup算法perLast, '占比')
dxTy_算法资源池per = indicator_bl_total_mid_rate(dxTyGroup算法per, dxTyGroup算法perLast, '占比')
mkt_算法资源池per = indicator_bl_total_mid_rate(mktGroup算法per, mktGroup算法perLast, '占比')
oac_算法资源池per = indicator_bl_total_mid_rate(oacGroup算法per, oacGroup算法perLast, '占比')

sx_开发资源池 = indicator_bl_total_mid(sxGroup开发, sxGroup开发last, '开发')
ir_开发资源池 = indicator_bl_total_mid(irGroup开发, irGroup开发last, '开发')
dxSku_开发资源池 = indicator_bl_total_mid(dxSkuGroup开发, dxSkuGroup开发last, '开发')
dxTy_开发资源池 = indicator_bl_total_mid(dxTyGroup开发, dxTyGroup开发last, '开发')
mkt_开发资源池 = indicator_bl_total_mid(mktGroup开发, mktGroup开发last, '开发')
oac_开发资源池 = indicator_bl_total_mid(oacGroup开发, oacGroup开发last, '开发')

sx_开发资源池per = indicator_bl_total_mid_rate(sxGroup开发per, sxGroup开发perLast, '占比')
ir_开发资源池per = indicator_bl_total_mid_rate(irGroup开发per, irGroup开发perLast, '占比')
dxSku_开发资源池per = indicator_bl_total_mid_rate(dxSkuGroup开发per, dxSkuGroup开发perLast, '占比')
dxTy_开发资源池per = indicator_bl_total_mid_rate(dxTyGroup开发per, dxTyGroup开发perLast, '占比')
mkt_开发资源池per = indicator_bl_total_mid_rate(mktGroup开发per, mktGroup开发perLast, '占比')
oac_开发资源池per = indicator_bl_total_mid_rate(oacGroup开发per, oacGroup开发perLast, '占比')

sx_架构资源池 = indicator_bl_total_mid(sxGroup架构, sxGroup架构last, '架构')
ir_架构资源池 = indicator_bl_total_mid(irGroup架构, irGroup架构last, '架构')
dxSku_架构资源池 = indicator_bl_total_mid(dxSkuGroup架构, dxSkuGroup架构last, '架构')
dxTy_架构资源池 = indicator_bl_total_mid(dxTyGroup架构, dxTyGroup架构last, '架构')
mkt_架构资源池 = indicator_bl_total_mid(mktGroup架构, mktGroup架构last, '架构')
oac_架构资源池 = indicator_bl_total_mid(oacGroup架构, oacGroup架构last, '架构')

sx_架构资源池per = indicator_bl_total_mid_rate(sxGroup架构per, sxGroup架构perLast, '占比')
ir_架构资源池per = indicator_bl_total_mid_rate(irGroup架构per, irGroup架构perLast, '占比')
dxSku_架构资源池per = indicator_bl_total_mid_rate(dxSkuGroup架构per, dxSkuGroup架构perLast, '占比')
dxTy_架构资源池per = indicator_bl_total_mid_rate(dxTyGroup架构per, dxTyGroup架构perLast, '占比')
mkt_架构资源池per = indicator_bl_total_mid_rate(mktGroup架构per, mktGroup架构perLast, '占比')
oac_架构资源池per = indicator_bl_total_mid_rate(oacGroup架构per, oacGroup架构perLast, '占比')

sx_测试资源池 = indicator_bl_total_mid(sxGroup测试, sxGroup测试last, '测试')
ir_测试资源池 = indicator_bl_total_mid(irGroup测试, irGroup测试last, '测试')
dxSku_测试资源池 = indicator_bl_total_mid(dxSkuGroup测试, dxSkuGroup测试last, '测试')
dxTy_测试资源池 = indicator_bl_total_mid(dxTyGroup测试, dxTyGroup测试last, '测试')
mkt_测试资源池 = indicator_bl_total_mid(mktGroup测试, mktGroup测试last, '测试')
oac_测试资源池 = indicator_bl_total_mid(oacGroup测试, oacGroup测试last, '测试')

sx_测试资源池per = indicator_bl_total_mid_rate(sxGroup测试per, sxGroup测试perLast, '占比')
ir_测试资源池per = indicator_bl_total_mid_rate(irGroup测试per, irGroup测试perLast, '占比')
dxSku_测试资源池per = indicator_bl_total_mid_rate(dxSkuGroup测试per, dxSkuGroup测试perLast, '占比')
dxTy_测试资源池per = indicator_bl_total_mid_rate(dxTyGroup测试per, dxTyGroup测试perLast, '占比')
mkt_测试资源池per = indicator_bl_total_mid_rate(mktGroup测试per, mktGroup测试perLast, '占比')
oac_测试资源池per = indicator_bl_total_mid_rate(oacGroup测试per, oacGroup测试perLast, '占比')

sx_非资源池 = indicator_bl_total_mid(sxGroup非, sxGroup非last, '非资源池')
sx_非资源池per = indicator_bl_total_mid_rate(sxGroup非per, sxGroup非perLast, '占比')

ir_非资源池 = indicator_bl_total_mid(irGroup非, irGroup非last, '非资源池')
ir_非资源池per = indicator_bl_total_mid_rate(irGroup非per, irGroup非perLast, '占比')

dxSku_非资源池 = indicator_bl_total_mid(dxSkuGroup非, dxSkuGroup非last, '非资源池')
dxSku_非资源池per = indicator_bl_total_mid_rate(dxSkuGroup非per, dxSkuGroup非perLast, '占比')

dxTy_非资源池 = indicator_bl_total_mid(dxTyGroup非, dxTyGroup非last, '非资源池')
dxTy_非资源池per = indicator_bl_total_mid_rate(dxTyGroup非per, dxTyGroup非perLast, '占比')

mkt_非资源池 = indicator_bl_total_mid(mktGroup非, mktGroup非last, '非资源池')
mkt_非资源池per = indicator_bl_total_mid_rate(mktGroup非per, mktGroup非perLast, '占比')

oac_非资源池 = indicator_bl_total_mid(oacGroup非, oacGroup非last, '非资源池')
oac_非资源池per = indicator_bl_total_mid_rate(oacGroup非per, oacGroup非perLast, '占比')

sxWbsD = tryExceptNone(blGroupByTitle(sxData, 'WBS类型', 'D'))
sxWbsDLast = tryExceptNone(blGroupByTitle(sxDataLast, 'WBS类型', 'D'))
irWbsD = tryExceptNone(blGroupByTitle(irData, 'WBS类型', 'D'))
irWbsDLast = tryExceptNone(blGroupByTitle(irDataLast, 'WBS类型', 'D'))
dxSkuWbsD = tryExceptNone(blGroupByTitle(dxSkuData, 'WBS类型', 'D'))
dxSkuWbsDLast = tryExceptNone(blGroupByTitle(dxSkuDataLast, 'WBS类型', 'D'))
dxTyWbsD = tryExceptNone(blGroupByTitle(dxTyData, 'WBS类型', 'D'))
dxTyWbsDLast = tryExceptNone(blGroupByTitle(dxTyDataLast, 'WBS类型', 'D'))
mktWbsD = tryExceptNone(blGroupByTitle(mktData, 'WBS类型', 'D'))
mktWbsDLast = tryExceptNone(blGroupByTitle(mktDataLast, 'WBS类型', 'D'))
oacWbsD = tryExceptNone(blGroupByTitle(oacData, 'WBS类型', 'D'))
oacWbsDLast = tryExceptNone(blGroupByTitle(oacDataLast, 'WBS类型', 'D'))

sxWbsDper = tryExceptNone(blGroupByTitlePer(sxWbsD, sxData))
sxWbsDperLast = tryExceptNone(blGroupByTitlePer(sxWbsDLast, sxDataLast))
irWbsDper = tryExceptNone(blGroupByTitlePer(irWbsD, irData))
irWbsDperLast = tryExceptNone(blGroupByTitlePer(irWbsDLast, irDataLast))
dxSkuWbsDper = tryExceptNone(blGroupByTitlePer(dxSkuWbsD, dxSkuData))
dxSkuWbsDperLast = tryExceptNone(blGroupByTitlePer(dxSkuWbsDLast, dxSkuDataLast))
dxTyWbsDper = tryExceptNone(blGroupByTitlePer(dxTyWbsD, dxTyData))
dxTyWbsDperLast = tryExceptNone(blGroupByTitlePer(dxTyWbsDLast, dxTyDataLast))
mktWbsDper = tryExceptNone(blGroupByTitlePer(mktWbsD, mktData))
mktWbsDperLast = tryExceptNone(blGroupByTitlePer(mktWbsDLast, mktDataLast))
oacWbsDper = tryExceptNone(blGroupByTitlePer(oacWbsD, oacData))
oacWbsDperLast = tryExceptNone(blGroupByTitlePer(oacWbsDLast, oacDataLast))

sx_wbsD = indicator_bl_total_mid(sxWbsD, sxWbsDLast, 'D类')
ir_wbsD = indicator_bl_total_mid(irWbsD, irWbsDLast, 'D类')
dxSku_wbsD = indicator_bl_total_mid(dxSkuWbsD, dxSkuWbsDLast, 'D类')
dxTy_wbsD = indicator_bl_total_mid(dxTyWbsD, dxTyWbsDLast, 'D类')
mkt_wbsD = indicator_bl_total_mid(mktWbsD, mktWbsDLast, 'D类')
oac_wbsD = indicator_bl_total_mid(oacWbsD, oacWbsDLast, 'D类')

sx_wbsDper = indicator_bl_total_mid_rate(sxWbsDper, sxWbsDperLast, '占比')
ir_wbsDper = indicator_bl_total_mid_rate(irWbsDper, irWbsDperLast, '占比')
dxSku_wbsDper = indicator_bl_total_mid_rate(dxSkuWbsDper, dxSkuWbsDperLast, '占比')
dxTy_wbsDper = indicator_bl_total_mid_rate(dxTyWbsDper, dxTyWbsDperLast, '占比')
mkt_wbsDper = indicator_bl_total_mid_rate(mktWbsDper, mktWbsDperLast, '占比')
oac_wbsDper = indicator_bl_total_mid_rate(oacWbsDper, oacWbsDperLast, '占比')

sxWbsX = tryExceptNone(blGroupByFilter(sxData, 'PL111', '利润中心'))
sxWbsXLast = tryExceptNone(blGroupByFilter(sxDataLast, 'PL111', '利润中心'))
irWbsX = tryExceptNone(blGroupByFilter(irData, 'PL111', '利润中心'))
irWbsXLast = tryExceptNone(blGroupByFilter(irDataLast, 'PL111', '利润中心'))
dxSkuWbsX = tryExceptNone(blGroupByFilter(dxSkuData, 'PL111', '利润中心'))
dxSkuWbsXLast = tryExceptNone(blGroupByFilter(dxSkuDataLast, 'PL111', '利润中心'))
dxTyWbsX = tryExceptNone(blGroupByFilter(dxTyData, 'PL111', '利润中心'))
dxTyWbsXLast = tryExceptNone(blGroupByFilter(dxTyDataLast, 'PL111', '利润中心'))
mktWbsX = tryExceptNone(blGroupByFilter(mktData, 'PL111', '利润中心'))
mktWbsXLast = tryExceptNone(blGroupByFilter(mktDataLast, 'PL111', '利润中心'))
oacWbsX = tryExceptNone(blGroupByFilter(oacData, 'PL111', '利润中心'))
oacWbsXLast = tryExceptNone(blGroupByFilter(oacDataLast, 'PL111', '利润中心'))

sxWbsXper = tryExceptNone(blGroupByTitlePer(sxWbsX, sxData))
sxWbsXperLast = tryExceptNone(blGroupByTitlePer(sxWbsXLast, sxDataLast))
irWbsXper = tryExceptNone(blGroupByTitlePer(irWbsX, irData))
irWbsXperLast = tryExceptNone(blGroupByTitlePer(irWbsXLast, irDataLast))
dxSkuWbsXper = tryExceptNone(blGroupByTitlePer(dxSkuWbsX, dxSkuData))
dxSkuWbsXperLast = tryExceptNone(blGroupByTitlePer(dxSkuWbsXLast, dxSkuDataLast))
dxTyWbsXper = tryExceptNone(blGroupByTitlePer(dxTyWbsX, dxTyData))
dxTyWbsXperLast = tryExceptNone(blGroupByTitlePer(dxTyWbsXLast, dxTyDataLast))
mktWbsXper = tryExceptNone(blGroupByTitlePer(mktWbsX, mktData))
mktWbsXperLast = tryExceptNone(blGroupByTitlePer(mktWbsXLast, mktDataLast))
oacWbsXper = tryExceptNone(blGroupByTitlePer(oacWbsX, oacData))
oacWbsXperLast = tryExceptNone(blGroupByTitlePer(oacWbsXLast, oacDataLast))

sx_wbsX = indicator_bl_total_mid(sxWbsX, sxWbsXLast, '其他部门')
ir_wbsX = indicator_bl_total_mid(irWbsX, irWbsXLast, '其他部门')
dxSku_wbsX = indicator_bl_total_mid(dxSkuWbsX, dxSkuWbsXLast, '其他部门')
dxTy_wbsX = indicator_bl_total_mid(dxTyWbsX, dxTyWbsXLast, '其他部门')
mkt_wbsX = indicator_bl_total_mid(mktWbsX, mktWbsXLast, '其他部门')
oac_wbsX = indicator_bl_total_mid(oacWbsX, oacWbsXLast, '其他部门')

sx_wbsXper = indicator_bl_total_mid_rate(sxWbsXper, sxWbsXperLast, '占比')
ir_wbsXper = indicator_bl_total_mid_rate(irWbsXper, irWbsXperLast, '占比')
dxSku_wbsXper = indicator_bl_total_mid_rate(dxSkuWbsXper, dxSkuWbsXperLast, '占比')
dxTy_wbsXper = indicator_bl_total_mid_rate(dxTyWbsXper, dxTyWbsXperLast, '占比')
mkt_wbsXper = indicator_bl_total_mid_rate(mktWbsXper, mktWbsXperLast, '占比')
oac_wbsXper = indicator_bl_total_mid_rate(oacWbsXper, oacWbsXperLast, '占比')

wbs_d_days = round(本月合并底表[本月合并底表['WBS类型'] == 'D']['实际人天'].sum(), 1)
wbs_notPL111_days = round(本月合并底表[~本月合并底表['利润中心'].isin(['PL111'])]['实际人天'].sum(), 1)
wbs_total_out = round(
    本月合并底表[本月合并底表['WBS类型'] == 'D'].append(本月合并底表[~本月合并底表['利润中心'].isin(['PL111'])],
                                                        ignore_index=True).drop_duplicates().reset_index(drop=True)[
        '实际人天'].sum(), 1)

modal = html.Div(
    [
        dbc.Button("Open modal", id="open", n_clicks=0),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle("Header")),
                dbc.ModalBody("This is the content of the modal"),
                dbc.ModalFooter(
                    dbc.Button(
                        "Close", id="close", className="ms-auto", n_clicks=0,
                    )
                ),
            ],
            id="modal",
            is_open=False,
        ),
    ]
)

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(
            dbc.Row([
                html.Img(src=app.get_asset_url("img/dash-logo.png"), id="plotly-image",
                         style={"height": "60px", "width": "auto"}),
            ]),
        ),
        dbc.Col([
            dbc.Row([html.Div([
                dbc.Button("数据说明", id="open", n_clicks=0, color="transparent", ),
                dbc.Modal([
                    dbc.ModalBody(
                        html.Div(
                            className="markdown-text",
                            children=dcc.Markdown(
                                children=(
                                    """
                            ###### 【 ⏰ 工时数据说明】 
                            ###### 1、数据来源
                            上月26日-本月25日内OA工时填报已报送工时;
                            ###### 2、人员构成
                            部门正式员工、人力外包、实习生（不含外部门人员、项目外包成员、当月入离职员工）;
                            ###### 3、数据定义
                            理论工时：部门填写工时人数*当月工作日天数；
                            实际工时：OA工时填报中的已报送工时；
                            预计工时：PM对项目当月做出的[工时预估](https://docs.qq.com/sheet/DVkVZRUNseGJ4Q0tl?tab=7bdo9o)。
                            合理预估填报率：80% < 实际人天/预估人天 < 120%；
                            合理理论填报率：90% < 实际人天/理论人天 < 120%。
                            ###### 
                            ###### 【 💎 资源数据说明】 
                            ###### 1、GPU
                            数据来源于各集群每日10点、14点、18点与22点GPU卡使用情况，可关注企微群 ` IRDC内部GPU资源调度群`  每日推送；
                            ###### 2、数据采标
                            数据爬取自Sensebee各采集标注任务，可关注企微群 ` IRDC数据采标任务群`  每日推送；
                            ###### 3、Open Cloud、DCP存储
                            ###### 4、固定资产

                        """
                                )), ), ),
                    dbc.ModalFooter(
                        dbc.Button(
                            "Close", id="close", className="ms-auto", n_clicks=0
                        )
                    ),
                ],
                    id="modal",
                    size="lg",
                    is_open=False,
                ),
            ])]),
        ]),
        dbc.Col([
            dcc.Tabs(id="tabs-title", value='工时', children=[
                # dcc.Tab(label='工时', value='工时', style=tab_style, selected_style=tab_selected_style),
                dcc.Tab(label='资源', value='资源', style=tab_style, selected_style=tab_selected_style),
                dcc.Tab(label='产品线/资源池', value='产品线/资源池', style=tab_style,
                        selected_style=tab_selected_style),
            ]),
        ], width=9)
    ]),
    dbc.Row([
        dbc.Col([
            html.Div(id='tabs-content')
        ])
    ])
], fluid=True)


@app.callback(
    Output("modal", "is_open"),
    [Input("open", "n_clicks"), Input("close", "n_clicks")],
    [State("modal", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


@app.callback(
    Output('pandas-output-container-1', 'value'),
    Input('产品线详细', 'value')
)
def select_bl(value):
    return value


@app.callback(
    Output("collapse", "is_open"),
    [Input("collapse-button", "n_clicks")],
    [State("collapse", "is_open")],
)
@app.callback(
    Output("collapse2", "is_open"),
    [Input("collapse-button2", "n_clicks")],
    [State("collapse2", "is_open")],
)
@app.callback(
    Output("collapse3", "is_open"),
    [Input("collapse-button3", "n_clicks")],
    [State("collapse3", "is_open")],
)
@app.callback(
    Output("collapse4", "is_open"),
    [Input("collapse-button4", "n_clicks")],
    [State("collapse4", "is_open")],
)
@app.callback(
    Output("collapse6", "is_open"),
    [Input("collapse-button6", "n_clicks")],
    [State("collapse6", "is_open")],
)
@app.callback(
    Output("collapse7", "is_open"),
    [Input("collapse-button7", "n_clicks")],
    [State("collapse7", "is_open")],
)
@app.callback(
    Output("collapse8", "is_open"),
    [Input("collapse-button8", "n_clicks")],
    [State("collapse8", "is_open")],
)
@app.callback(
    Output("collapse9", "is_open"),
    [Input("collapse-button9", "n_clicks")],
    [State("collapse9", "is_open")],
)
@app.callback(
    Output("collapse10", "is_open"),
    [Input("collapse-button10", "n_clicks")],
    [State("collapse10", "is_open")],
)
@app.callback(
    Output("collapse11", "is_open"),
    [Input("collapse-button11", "n_clicks")],
    [State("collapse11", "is_open")],
)
@app.callback(
    Output("collapse12", "is_open"),
    [Input("collapse-button12", "n_clicks")],
    [State("collapse12", "is_open")],
)
@app.callback(
    Output("collapse13", "is_open"),
    [Input("collapse-button13", "n_clicks")],
    [State("collapse13", "is_open")],
)
@app.callback(
    Output("collapse14", "is_open"),
    [Input("collapse-button14", "n_clicks")],
    [State("collapse14", "is_open")],
)
@app.callback(
    Output("collapse15", "is_open"),
    [Input("collapse-button15", "n_clicks")],
    [State("collapse15", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


def dfExist(df, dfNoStr, collbtn, coll):
    if len(df) > 1:
        return dbc.Row([collapse_btn_table(collbtn, "df", df,
                                           coll), ])
    else:
        return html.P(dfNoStr, style={"fontSize": 25, "color": "red"})


def dfExistDfStr(df, dfStr):
    if len(df) > 0:
        return dbc.Row([
            html.P(dfStr + str(len(df)),
                   style={"fontSize": 25}),
        ])
    else:
        return dbc.Row([])


def dfExistDf(df, dfStr):
    try:
        data = df
        if len(data) > 0:
            return dbc.Row([
                dbc.Col([
                    dash_table_not_collapse(dfStr, data)
                ]),
            ])
        else:
            return dbc.Row([])
    except:
        return dbc.Row([])


@app.callback(Output('tabs-content', 'children'),
              Input('tabs-title', 'value'))
def render_content(tab):
    # if tab == '工时':
    #     return dbc.Container([
    #         html.P(
    #             "人员维度工时 ( Data {}; 国内全勤 {} 人天, 新加坡全勤 {} 人天, 本月入离职共 {} 人, 未填工时共 {} 人)".format(
    #                 人员维度更新时间(), 国内全勤人天(), 新加坡全勤人天(), str(len(本月入离职名单())),
    #                 str(len(tryExcept0(本月未填工时名单()))))),
    #         dbc.Row([
    #             dbc.Col([
    #                 irdc_summary_large_ppl("staff_number_indicator", staff_number_indicator)
    #             ]),
    #             dbc.Col([
    #                 dbc.Row([
    #                     irdc_summary_smWider_ppl("staff_in_indicator", staff_in_indicator),
    #                     irdc_summary_smWider_ppl("staff_out_indicator", staff_out_indicator),
    #                     irdc_summary_smWider_ppl("staff_intern_indicator", staff_intern_indicator),
    #                 ])
    #             ]),
    #             dbc.Col([
    #                 irdc_summary_large_ppl("logic_percentage", logic_percentage),
    #             ]),
    #             dbc.Col([
    #                 dbc.Row([
    #                     irdc_summary_smWider_ppl("logic_in_percentage", logic_in_percentage),
    #                     irdc_summary_smWider_ppl("logic_out_percentage", logic_out_percentage),
    #                     irdc_summary_smWider_ppl("logic_intern_percentage", logic_intern_percentage),
    #                 ])
    #             ]),
    #             dbc.Col([
    #                 irdc_summary_large_ppl("act_allday", act_allday)
    #             ]),
    #             dbc.Col([
    #                 dbc.Row([
    #                     irdc_summary_smWider_ppl("act_in_day", act_in_day),
    #                     irdc_summary_smWider_ppl("act_out_day", act_out_day),
    #                     irdc_summary_smWider_ppl("act_intern_day", act_intern_day),
    #                 ])
    #             ]),
    #             dbc.Col([
    #                 irdc_summary_large_ppl("act_perday", act_perday)
    #             ]),
    #             dbc.Col([
    #                 dbc.Row([
    #                     irdc_summary_smWider_ppl("act_in_perday", act_in_perday),
    #                     irdc_summary_smWider_ppl("act_out_perday", act_out_perday),
    #                     irdc_summary_smWider_ppl("act_intern_perday", act_intern_perday),
    #                 ])
    #             ]),
    #             dbc.Col([
    #                 irdc_summary_large_ppl("attend_allday", attend_allday)
    #             ]),
    #             dbc.Col([
    #                 dbc.Row([
    #                     irdc_summary_smWider_ppl("attend_in_day", attend_in_day),
    #                     irdc_summary_smWider_ppl("attend_out_day", attend_out_day),
    #                     irdc_summary_smWider_ppl("attend_intern_day", attend_intern_day),
    #                 ])
    #             ]),
    #         ]),
    #         html.Br(),
    #         html.Br(),
    #         dbc.Row([
    #             dbc.Col([
    #                 dbc.Row([
    #                     irdc_wh_large("sx_total_indicator", sx_wh_total)
    #                 ]),
    #                 dbc.Row([
    #                     irdc_wh_middle("sx_算法资源池_indicator", sx_算法资源池),
    #                     irdc_wh_middle("sx_算法资源池per_indicator", sx_算法资源池per)
    #                 ]),
    #                 dbc.Row([
    #                     irdc_wh_middle("sx_开发资源池_indicator", sx_开发资源池),
    #                     irdc_wh_middle("sx_开发资源池per_indicator", sx_开发资源池per)
    #                 ]),
    #                 dbc.Row([
    #                     irdc_wh_middle("sx_架构资源池_indicator", sx_架构资源池),
    #                     irdc_wh_middle("sx_架构资源池per_indicator", sx_架构资源池per)
    #                 ]),
    #                 dbc.Row([
    #                     irdc_wh_middle("sx_测试资源池_indicator", sx_测试资源池),
    #                     irdc_wh_middle("sx_测试资源池per_indicator", sx_测试资源池per)
    #                 ]),
    #                 dbc.Row([
    #                     irdc_wh_middle("sx_非资源池_indicator", sx_非资源池),
    #                     irdc_wh_middle("sx_非资源池per_indicator", sx_非资源池per)
    #                 ]),
    #
    #             ]),
    #             dbc.Col([
    #                 dbc.Row([
    #                     irdc_wh_large("ir_total_indicator", ir_wh_total)
    #                 ]),
    #                 dbc.Row([
    #                     irdc_wh_middle("ir_算法资源池_indicator", ir_算法资源池),
    #                     irdc_wh_middle("ir_算法资源池per_indicator", ir_算法资源池per)
    #                 ]),
    #                 dbc.Row([
    #                     irdc_wh_middle("ir_开发资源池_indicator", ir_开发资源池),
    #                     irdc_wh_middle("ir_开发资源池per_indicator", ir_开发资源池per)
    #                 ]),
    #                 dbc.Row([
    #                     irdc_wh_middle("ir_架构资源池_indicator", ir_架构资源池),
    #                     irdc_wh_middle("ir_架构资源池per_indicator", ir_架构资源池per)
    #                 ]),
    #                 dbc.Row([
    #                     irdc_wh_middle("ir_测试资源池_indicator", ir_测试资源池),
    #                     irdc_wh_middle("ir_测试资源池per_indicator", ir_测试资源池per)
    #                 ]),
    #                 dbc.Row([
    #                     irdc_wh_middle("ir_非资源池_indicator", ir_非资源池),
    #                     irdc_wh_middle("ir_非资源池per_indicator", ir_非资源池per)
    #                 ]),
    #             ]),
    #             dbc.Col([
    #                 dbc.Row([
    #                     irdc_wh_large("dxSku_total_indicator", dxSku_wh_total)
    #                 ]),
    #                 dbc.Row([
    #                     irdc_wh_middle("dxSku_算法资源池_indicator", dxSku_算法资源池),
    #                     irdc_wh_middle("dxSku_算法资源池per_indicator", dxSku_算法资源池per)
    #                 ]),
    #                 dbc.Row([
    #                     irdc_wh_middle("dxSku_开发资源池_indicator", dxSku_开发资源池),
    #                     irdc_wh_middle("dxSku_开发资源池per_indicator", dxSku_开发资源池per)
    #                 ]),
    #                 dbc.Row([
    #                     irdc_wh_middle("dxSku_架构资源池_indicator", dxSku_架构资源池),
    #                     irdc_wh_middle("dxSku_架构资源池per_indicator", dxSku_架构资源池per)
    #                 ]),
    #                 dbc.Row([
    #                     irdc_wh_middle("dxSku_测试资源池_indicator", dxSku_测试资源池),
    #                     irdc_wh_middle("dxSku_测试资源池per_indicator", dxSku_测试资源池per)
    #                 ]),
    #                 dbc.Row([
    #                     irdc_wh_middle("dxSku_非资源池_indicator", dxSku_非资源池),
    #                     irdc_wh_middle("dxSku_非资源池per_indicator", dxSku_非资源池per)
    #                 ]),
    #             ]),
    #             dbc.Col([
    #                 dbc.Row([
    #                     irdc_wh_large("dxTy_total_indicator", dxTy_wh_total)
    #                 ]),
    #                 dbc.Row([
    #                     irdc_wh_middle("dxTy_算法资源池_indicator", dxTy_算法资源池),
    #                     irdc_wh_middle("dxTy_算法资源池per_indicator", dxTy_算法资源池per)
    #                 ]),
    #                 dbc.Row([
    #                     irdc_wh_middle("dxTy_开发资源池_indicator", dxTy_开发资源池),
    #                     irdc_wh_middle("dxTy_开发资源池per_indicator", dxTy_开发资源池per)
    #                 ]),
    #                 dbc.Row([
    #                     irdc_wh_middle("dxTy_架构资源池_indicator", dxTy_架构资源池),
    #                     irdc_wh_middle("dxTy_架构资源池per_indicator", dxTy_架构资源池per)
    #                 ]),
    #                 dbc.Row([
    #                     irdc_wh_middle("dxTy_测试资源池_indicator", dxTy_测试资源池),
    #                     irdc_wh_middle("dxTy_测试资源池per_indicator", dxTy_测试资源池per)
    #                 ]),
    #                 dbc.Row([
    #                     irdc_wh_middle("dxTy_非资源池_indicator", dxTy_非资源池),
    #                     irdc_wh_middle("dxTy_非资源池per_indicator", dxTy_非资源池per)
    #                 ]),
    #             ]),
    #             dbc.Col([
    #                 dbc.Row([
    #                     irdc_wh_large("mkt_total_indicator", mkt_wh_total)
    #                 ]),
    #                 dbc.Row([
    #                     irdc_wh_middle("mkt_算法资源池_indicator", mkt_算法资源池),
    #                     irdc_wh_middle("mkt_算法资源池per_indicator", mkt_算法资源池per)
    #                 ]),
    #                 dbc.Row([
    #                     irdc_wh_middle("mkt_开发资源池_indicator", mkt_开发资源池),
    #                     irdc_wh_middle("mkt_开发资源池per_indicator", mkt_开发资源池per)
    #                 ]),
    #                 dbc.Row([
    #                     irdc_wh_middle("mkt_架构资源池_indicator", mkt_架构资源池),
    #                     irdc_wh_middle("mkt_架构资源池per_indicator", mkt_架构资源池per)
    #                 ]),
    #                 dbc.Row([
    #                     irdc_wh_middle("mkt_测试资源池_indicator", mkt_测试资源池),
    #                     irdc_wh_middle("mkt_测试资源池per_indicator", mkt_测试资源池per)
    #                 ]),
    #                 dbc.Row([
    #                     irdc_wh_middle("mkt_非资源池_indicator", mkt_非资源池),
    #                     irdc_wh_middle("mkt_非资源池per_indicator", mkt_非资源池per)
    #                 ]),
    #             ]),
    #             dbc.Col([
    #                 dbc.Row([
    #                     irdc_wh_large("oac_total_indicator", oac_wh_total)
    #                 ]),
    #                 dbc.Row([
    #                     irdc_wh_middle("oac_算法资源池_indicator", oac_算法资源池),
    #                     irdc_wh_middle("oac_算法资源池per_indicator", oac_算法资源池per)
    #                 ]),
    #                 dbc.Row([
    #                     irdc_wh_middle("oac_开发资源池_indicator", oac_开发资源池),
    #                     irdc_wh_middle("oac_开发资源池per_indicator", oac_开发资源池per)
    #                 ]),
    #                 dbc.Row([
    #                     irdc_wh_middle("oac_架构资源池_indicator", oac_架构资源池),
    #                     irdc_wh_middle("oac_架构资源池per_indicator", oac_架构资源池per)
    #                 ]),
    #                 dbc.Row([
    #                     irdc_wh_middle("oac_测试资源池_indicator", oac_测试资源池),
    #                     irdc_wh_middle("oac_测试资源池per_indicator", oac_测试资源池per)
    #                 ]),
    #                 dbc.Row([
    #                     irdc_wh_middle("oac_非资源池_indicator", oac_非资源池),
    #                     irdc_wh_middle("oac_非资源池per_indicator", oac_非资源池per)
    #                 ]),
    #             ]),
    #         ]),
    #         html.Br(),
    #         html.Div(
    #             dbc.Accordion([
    #                 dbc.AccordionItem([
    #                     dbc.Row([
    #                         dbc.Col([
    #                             irdc_graph('员工所属部门汇总-summary', fig员工所属部门汇总())
    #                         ], xs=12, sm=12, md=6, lg=6, xl=6),
    #                         dbc.Col([
    #                             irdc_graph('员工所属部门汇总-bar', fig员工所属部门人均人天())
    #                         ], xs=12, sm=12, md=6, lg=6, xl=6),
    #                         html.Br(),
    #                     ]),
    #                     dbc.Col([
    #                         dash_table_not_collapse("apartment_wh", staff_apartment_tb.iloc[:, 0:-2]),
    #                     ]),
    #                     html.Br(),
    #                     dbc.Row([
    #                         dbc.Col([
    #                             dcc.RadioItems(
    #                                 id='radio_actual_per',
    #                                 options=[
    #                                     {'label': 'IRDC', 'value': 'graph_actual_per_irdc'},
    #                                     {'label': '员工所属部门', 'value': 'graph_actual_per_all'},
    #                                 ],
    #                                 value='graph_actual_per_all',
    #                                 style={"width": "60%"},
    #                                 inline=True),
    #                         ]),
    #                     ]),
    #                     dbc.Row([
    #                         dbc.Col([
    #                             dcc.Graph(id='graph_actual_per',
    #                                       style={'height': 500,
    #                                              'width': '100%',
    #                                              "border-radius": "5px",
    #                                              "background-color": "#f9f9f9",
    #                                              "box-shadow": "2px 2px 2px lightgrey",
    #                                              "position": "relative",
    #                                              "margin-bottom": "15px"
    #                                              },
    #                                       config={'displayModeBar': False},
    #                                       ),
    #                         ]),
    #                     ]),
    #                     dbc.Row([
    #                         dbc.Col([
    #                             irdc_graph('业务线汇总-pie', fig业务线pie()),
    #                         ])
    #                     ]),
    #
    #                     # html.Br(),
    #                     # html.Br(),
    #                     # dbc.Row([
    #                     #     dbc.Col([
    #                     #         html.Div([
    #                     #             html.Div([
    #                     #                 dcc.RadioItems(
    #                     #                     id='radio_logic_rate',
    #                     #                     options=[
    #                     #                         {'label': 'IRDC', 'value': 'graph_logic_rate_irdc'},
    #                     #                         {'label': '员工所属部门', 'value': 'graph_logic_rate_all'},
    #                     #                     ],
    #                     #                     value='graph_logic_rate_irdc',
    #                     #                     style={"width": "60%"},
    #                     #                     inline=True),
    #                     #             ]),
    #                     #             html.Div(
    #                     #                 dcc.Graph(id='graph_logic_rate',
    #                     #                           style={'height': 500,
    #                     #                                  "border-radius": "5px",
    #                     #                                  "background-color": "#f9f9f9",
    #                     #                                  "box-shadow": "2px 2px 2px lightgrey",
    #                     #                                  "position": "relative",
    #                     #                                  "margin-bottom": "15px"
    #                     #                                  },
    #                     #                           config={'displayModeBar': False},
    #                     #                           ),
    #                     #             ),
    #                     #
    #                     #         ])
    #                     #     ]),
    #                     # ]),
    #                     html.Br(),
    #                     dbc.Row([
    #                         dbc.Col([
    #                             html.Div([
    #                                 html.Div([
    #                                     dcc.RadioItems(
    #                                         id='radio_产品线工时投入',
    #                                         options=[
    #                                             {'label': '员工组', 'value': 'graph_员工组人天'},
    #                                             {'label': '资源池', 'value': 'graph_资源池人天'},
    #                                             {'label': '岗位名称', 'value': 'graph_岗位名称人天'},
    #                                         ],
    #                                         value='graph_员工组人天',
    #                                         style={"width": "60%"},
    #                                         inline=True),
    #                                 ]),
    #                                 html.Div([
    #                                     dcc.Graph(id='graph_产品线工时投入',
    #                                               style={'height': 500,
    #                                                      "border-radius": "5px",
    #                                                      "background-color": "#f9f9f9",
    #                                                      "box-shadow": "2px 2px 2px lightgrey",
    #                                                      "position": "relative",
    #                                                      "margin-bottom": "15px"
    #                                                      },
    #                                               config={'displayModeBar': False},
    #                                               )]),
    #                                 html.Br(),
    #                                 html.Div([
    #                                     dash_table.DataTable(
    #                                         id='table_产品线工时投入', )
    #                                 ]),
    #                                 html.Br(),
    #                             ])
    #                         ], xs=12, sm=12, md=6, lg=6, xl=6),
    #                         dbc.Col([
    #                             html.Div([
    #                                 html.Div([
    #                                     dcc.RadioItems(
    #                                         id='radio_资源池工时投入',
    #                                         options=[
    #                                             {'label': '员工组', 'value': 'graph_资源池员工组人天'},
    #                                             {'label': '员工所属部门', 'value': 'graph_资源池员工所属部门人天'},
    #                                             {'label': '岗位名称', 'value': 'graph_资源池岗位名称人天'},
    #                                         ],
    #                                         value='graph_资源池员工组人天',
    #                                         style={"width": "60%"},
    #                                         inline=True),
    #                                 ]),
    #                                 html.Div([
    #                                     dcc.Graph(id='graph_资源池工时投入',
    #                                               style={'height': 500,
    #                                                      "border-radius": "5px",
    #                                                      "background-color": "#f9f9f9",
    #                                                      "box-shadow": "2px 2px 2px lightgrey",
    #                                                      "position": "relative",
    #                                                      "margin-bottom": "15px"
    #                                                      },
    #                                               config={'displayModeBar': False},
    #                                               )]),
    #                                 html.Br(),
    #                                 html.Div([
    #                                     dash_table.DataTable(
    #                                         id='table_资源池工时投入', )
    #                                 ]),
    #                                 html.Br(),
    #                             ])
    #                         ], xs=12, sm=12, md=6, lg=6, xl=6),
    #                     ]),
    #                     html.Br(),
    #                     dbc.Row([
    #                         dbc.Col([
    #                             irdc_graph('资源池汇总-bar', fig资源池汇总()),
    #                         ], xs=12, sm=12, md=6, lg=6, xl=6),
    #                         dbc.Col([
    #                             irdc_graph('岗位名称汇总-bar', fig岗位名称汇总()),
    #                         ], xs=12, sm=12, md=6, lg=6, xl=6),
    #                     ]),
    #                     # dbc.Row([
    #                     #     irdc_graph('资源池汇总-pie', fig资源池pie()),
    #                     # ]),
    #                     html.Br(),
    #                     dbc.Row([
    #                         dbc.Col([
    #                             dfExistDfStr(logic_rate_abnormal_tb(), '本月工时填报异常人数：'),
    #                             dfExistDf(logic_rate_abnormal_tb(), 'logic_distribution_tb_id'),
    #                         ]),
    #                         dbc.Col([
    #                             dfExistDfStr(本月未填工时名单(), '本月未填工时人数（连续两月未填已标蓝）：'),
    #                             dfExistDf(not_fill_workHour_twice(), 'no_actual_list_tb_id'),
    #                         ]),
    #                     ]),
    #                     html.Br(),
    #                     dbc.Row([
    #                         dbc.Col([
    #                             dfExistDfStr(本月入离职名单(), '本月入离职人数：'),
    #                             dfExistDf(本月入离职名单().iloc[:, 0:-2], 'inOut_staff_tb_id'),
    #                         ]),
    #                         html.Br(),
    #                         dbc.Col([
    #                             # dfExistDfStr(cur_mon_staff[cur_mon_staff['缺填日期'] != np.nan].append(cur_mon_staff[cur_mon_staff['多填日期'] != np.nan]),
    #                             #              '本月非正常工作日填报工时：'),
    #                             html.P(
    #                                 '本月非正常工作日填报工时(以"员工工作地点"与"行政放假安排"判定是否为当地工作日)'),
    #                             dfExistDf(not_fill_wh(), 'wired_date_tb_id'),
    #                         ]),
    #                     ]),
    #                     html.Br(),
    #                     dbc.Row([
    #                         html.P('本月工时填报人员明细', style={"fontSize": 25}),
    #                     ]),
    #                     dbc.Col([
    #                         dash_table_not_collapse("cur_mon_staff_detailed",
    #                                                 cur_mon_staff.iloc[:, 0:-4]),
    #                     ]),
    #                     html.Br(),
    #                     dbc.Row([
    #                         dbc.Col([
    #                             dcc.RadioItems(
    #                                 id='radio_实际vs预估',
    #                                 options=[
    #                                     {'label': '员工所属部门', 'value': '员工所属部门'},
    #                                     {'label': '资源池', 'value': '资源池'},
    #                                 ],
    #                                 value='员工所属部门',
    #                                 style={"width": "60%"},
    #                                 inline=True),
    #                         ], xs=12, sm=12, md=6, lg=6, xl=6),
    #                         dbc.Col([
    #                             dcc.RadioItems(
    #                                 id='radio_实际vs理论',
    #                                 options=[
    #                                     {'label': '员工所属部门', 'value': '员工所属部门'},
    #                                     {'label': '资源池', 'value': '资源池'},
    #                                 ],
    #                                 value='员工所属部门',
    #                                 style={"width": "60%"},
    #                                 inline=True),
    #
    #                         ], xs=12, sm=12, md=6, lg=6, xl=6),
    #
    #                     ]),
    #                     html.Br(),
    #                     dbc.Row([
    #                         dbc.Col([
    #                             dbc.Row([
    #                                 dbc.Col([
    #                                     html.P("预估填报率:"),
    #                                 ], xs=4, sm=4, md=3, lg=3, xl=3),
    #                                 dbc.Col([
    #                                     dcc.RangeSlider(
    #                                         id='range-slider实际vs预估',
    #                                         min=cur_mon_staff.预估填报率.min(), max=cur_mon_staff.预估填报率.max(),
    #                                         step=1,
    #                                         marks={
    #                                             cur_mon_staff.预估填报率.min(): {
    #                                                 'label': str(cur_mon_staff.预估填报率.min()),
    #                                                 'style': {'color': 'orange'}},
    #                                             80: {'label': '80%', 'style': {'color': 'green'}},
    #                                             120: {'label': '120%', 'style': {'color': 'green'}},
    #                                             cur_mon_staff.预估填报率.max(): {
    #                                                 'label': str(cur_mon_staff.预估填报率.max()),
    #                                                 'style': {'color': 'red'}}},
    #                                         value=[cur_mon_staff.预估填报率.min(), cur_mon_staff.预估填报率.max()],
    #                                         allowCross=False, tooltip={"placement": "bottom", "always_visible": True}
    #                                     ),
    #                                 ], xs=8, sm=8, md=9, lg=9, xl=9),
    #                             ]),
    #                             dbc.Row([
    #                                 dcc.Graph(id='fig全量实际vs预估人天-scatter', figure=fig全量实际vs预估人天(),
    #                                           config={'displayModeBar': False},
    #                                           style={"border-radius": "5px",
    #                                                  "background-color": "#f9f9f9",
    #                                                  "box-shadow": "2px 2px 2px lightgrey",
    #                                                  "position": "relative",
    #                                                  "margin-bottom": "15px"
    #                                                  }
    #                                           ),
    #                             ]),
    #                         ], xs=12, sm=12, md=6, lg=6, xl=6),
    #                         dbc.Col([
    #                             dbc.Row([
    #                                 dbc.Col([
    #                                     html.P("理论填报率:"),
    #                                 ], xs=4, sm=4, md=3, lg=3, xl=3),
    #                                 dbc.Col([
    #                                     dcc.RangeSlider(
    #                                         id='range-slider实际vs理论',
    #                                         min=cur_mon_staff.理论填报率.min(), max=cur_mon_staff.理论填报率.max(),
    #                                         step=1,
    #                                         marks={
    #                                             cur_mon_staff.理论填报率.min(): {
    #                                                 'label': str(cur_mon_staff.理论填报率.min()),
    #                                                 'style': {'color': 'orange'}},
    #                                             90: {'label': '90%', 'style': {'color': 'green'}},
    #                                             120: {'label': '120%', 'style': {'color': 'green'}},
    #                                             cur_mon_staff.理论填报率.max(): {
    #                                                 'label': str(cur_mon_staff.理论填报率.max()),
    #                                                 'style': {'color': 'red'}}},
    #                                         value=[cur_mon_staff.理论填报率.min(), cur_mon_staff.理论填报率.max()],
    #                                         allowCross=False,
    #                                         tooltip={"placement": "bottom", "always_visible": True}
    #                                     ),
    #                                 ], xs=8, sm=8, md=9, lg=9, xl=9),
    #                             ]),
    #                             dbc.Row([
    #                                 dcc.Graph(id='fig全量实际vs理论人天-scatter', figure=fig全量实际vs理论人天(),
    #                                           config={'displayModeBar': False},
    #                                           style={"border-radius": "5px",
    #                                                  "background-color": "#f9f9f9",
    #                                                  "box-shadow": "2px 2px 2px lightgrey",
    #                                                  "position": "relative",
    #                                                  "margin-bottom": "15px"
    #                                                  }
    #                                           ),
    #                             ]),
    #
    #                         ], xs=12, sm=12, md=6, lg=6, xl=6)
    #                     ]),
    #                     html.Br(),
    #                     dbc.Row([
    #                         dbc.Col([
    #                             html.P(id="sameDaysWithStaff"),
    #                         ], xs=12, sm=12, md=6, lg=6, xl=6),
    #                         dbc.Col([
    #                             html.P(id="sameDaysWithStaff2"),
    #                         ], xs=12, sm=12, md=6, lg=6, xl=6),
    #                     ]),
    #                     html.Br(),
    #                     dbc.Row([
    #                         dbc.Col([
    #                             html.P('员工姓名'),
    #                         ], xs=12, sm=12, md=2, lg=2, xl=2),
    #                         dbc.Col([
    #                             dcc.Input(
    #                                 id="input_userName",
    #                                 type="text",
    #                                 style={'width': '100%'},
    #                                 placeholder="输入【员工姓名】查看历史工时",
    #                             ),
    #
    #                         ], xs=12, sm=12, md=10, lg=10, xl=10),
    #                     ]),
    #                     html.Div(id="staffNameRemind"),
    #                     html.Br(),
    #                     dbc.Row([
    #                         dbc.Col([
    #                             dcc.Graph(id='historical_days', config={'displayModeBar': False}, )
    #                         ])
    #                     ]),
    #                     html.Br(),
    #                     dbc.Row([
    #                         dbc.Col([
    #                             dcc.Graph(id='historical_wbs_days', config={'displayModeBar': False}, )
    #                         ])
    #                     ]),
    #
    #                     # dbc.Row([
    #                     #     dcc.Graph(id="staff_3d_graph",config={'displayModeBar': False},
    #                     #               style={"border-radius": "5px",
    #                     #                      "background-color": "#f9f9f9",
    #                     #                      "box-shadow": "2px 2px 2px lightgrey",
    #                     #                      "position": "relative",
    #                     #                      "margin-bottom": "15px",
    #                     #                      "height":'800px'
    #                     #                      }
    #                     # ),
    #                     #     html.P("理论填报率:"),
    #                     #     dcc.RangeSlider(
    #                     #         id='range-slider',
    #                     #         min=min(cur_mon_staff['理论填报率']), max=max(cur_mon_staff['理论填报率']), step=5,
    #                     #         marks={min(cur_mon_staff['理论填报率']): min(cur_mon_staff['理论填报率']), max(cur_mon_staff['理论填报率']): max(cur_mon_staff['理论填报率'])},
    #                     #         value = [0, 120]
    #                     #     ),
    #                     # ]),
    #                     # html.Br(),
    #
    #                     # dbc.Row([
    #                     #     dbc.Col([
    #                     #         irdc_graph('fig全量实际vs理论人天-scatter', fig全量实际vs理论人天),
    #                     #         html.P("理论填报率:"),
    #                     #         dcc.RangeSlider(
    #                     #             id='range-slider实际vs理论',
    #                     #             min=cur_mon_staff.理论填报率.min(), max=cur_mon_staff.理论填报率.max(), step=1,
    #                     #             marks={
    #                     #                 cur_mon_staff.理论填报率.min(): {'label': str(cur_mon_staff.理论填报率.min()),
    #                     #                                                  'style': {'color': 'orange'}},
    #                     #                 90: {'label': '90%', 'style': {'color': 'green'}},
    #                     #                 120: {'label': '120%', 'style': {'color': 'green'}},
    #                     #                 cur_mon_staff.理论填报率.max(): {'label': str(cur_mon_staff.理论填报率.max()),
    #                     #                                                  'style': {'color': 'red'}}},
    #                     #             value=[cur_mon_staff.理论填报率.min(), cur_mon_staff.理论填报率.max()], allowCross=False,
    #                     #             tooltip={"placement": "bottom", "always_visible": True}
    #                     #         ),
    #                     #     ], xs=12, sm=12, md=6, lg=6, xl=6)
    #                     # ]),
    #
    #                 ], title='点击查看人员维度详细', )
    #             ], flush=True, start_collapsed=True, id="accordtion-staff")),
    #         html.Br(),
    #
    #         html.P("WBS维度工时 ( Data " + 人员维度更新时间() + ' , 其他部门为利润中心非PL111的WBS。)'),
    #         dbc.Row([
    #             dbc.Col([
    #                 dbc.Row([
    #                     irdc_summary_large_wbs("wbs_all_number", wbs_all_number)
    #                 ]),
    #                 dbc.Row([
    #                     irdc_summary_smWider("wbs_d_numebr", wbs_d_numebr),
    #                     irdc_summary_sm("sx_d_number", sx_d_number),
    #                     irdc_summary_sm("ir_d_number", ir_d_number),
    #                     irdc_summary_sm("dx_d_number", dx_d_number),
    #                     irdc_summary_sm("mkt_d_number", mkt_d_number),
    #                     irdc_summary_sm("oac_d_number", oac_d_number),
    #                     irdc_summary_sm("innova_d_number", innova_d_number),
    #                 ]),
    #                 dbc.Row([
    #                     irdc_summary_smWider("wbs_p_numebr", wbs_p_numebr),
    #                     irdc_summary_sm("sx_p_number", sx_p_number),
    #                     irdc_summary_sm("ir_p_number", ir_p_number),
    #                     irdc_summary_sm("dx_p_number", dx_p_number),
    #                     irdc_summary_sm("mkt_p_number", mkt_p_number),
    #                     irdc_summary_sm("oac_p_number", oac_p_number),
    #                     irdc_summary_sm("innova_p_number", innova_p_number),
    #
    #                 ]),
    #                 dbc.Row([
    #                     irdc_summary_smWider("wbs_r_numebr", wbs_r_numebr),
    #                     irdc_summary_sm("sx_r_number", sx_r_number),
    #                     irdc_summary_sm("ir_r_number", ir_r_number),
    #                     irdc_summary_sm("dx_r_number", dx_r_number),
    #                     irdc_summary_sm("mkt_r_number", mkt_r_number),
    #                     irdc_summary_sm("oac_r_number", oac_r_number),
    #                     irdc_summary_sm("innova_r_number", innova_r_number),
    #
    #                 ]),
    #                 dbc.Row([
    #                     irdc_summary_smWider("wbs_m_numebr", wbs_m_numebr),
    #                     irdc_summary_sm("sx_m_number", sx_m_number),
    #                     irdc_summary_sm("ir_m_number", ir_m_number),
    #                     irdc_summary_sm("dx_m_number", dx_m_number),
    #                     irdc_summary_sm("mkt_m_number", mkt_m_number),
    #                     irdc_summary_sm("oac_m_number", oac_m_number),
    #                     irdc_summary_sm("innova_m_number", innova_m_number),
    #
    #                 ]),
    #             ]),
    #             dbc.Col([
    #                 dbc.Row([
    #                     irdc_summary_large_wbs("wbs_actual_hrs", wbs_actual_hrs)
    #                 ]),
    #                 dbc.Row([
    #                     irdc_summary_smWider("wbs_d_act", wbs_d_act),
    #                     irdc_summary_sm("sx_d_act", sx_d_act),
    #                     irdc_summary_sm("ir_d_act", ir_d_act),
    #                     irdc_summary_sm("dx_d_act", dx_d_act),
    #                     irdc_summary_sm("mkt_d_act", mkt_d_act),
    #                     irdc_summary_sm("oac_d_act", oac_d_act),
    #                     irdc_summary_sm("innova_d_act", innova_d_act),
    #
    #                 ]),
    #                 dbc.Row([
    #                     irdc_summary_smWider("wbs_p_act", wbs_p_act),
    #                     irdc_summary_sm("sx_p_act", sx_p_act),
    #                     irdc_summary_sm("ir_p_act", ir_p_act),
    #                     irdc_summary_sm("dx_p_act", dx_p_act),
    #                     irdc_summary_sm("mkt_p_act", mkt_p_act),
    #                     irdc_summary_sm("oac_p_act", oac_p_act),
    #                     irdc_summary_sm("innova_p_act", innova_p_act),
    #
    #                 ]),
    #                 dbc.Row([
    #                     irdc_summary_smWider("wbs_r_act", wbs_r_act),
    #                     irdc_summary_sm("sx_r_act", sx_r_act),
    #                     irdc_summary_sm("ir_r_act", ir_r_act),
    #                     irdc_summary_sm("dx_r_act", dx_r_act),
    #                     irdc_summary_sm("mkt_r_act", mkt_r_act),
    #                     irdc_summary_sm("oac_r_act", oac_r_act),
    #                     irdc_summary_sm("innova_r_act", innova_r_act),
    #
    #                 ]),
    #                 dbc.Row([
    #                     irdc_summary_smWider("wbs_m_act", wbs_m_act),
    #                     irdc_summary_sm("sx_m_act", sx_m_act),
    #                     irdc_summary_sm("ir_m_act", ir_m_act),
    #                     irdc_summary_sm("dx_m_act", dx_m_act),
    #                     irdc_summary_sm("mkt_m_act", mkt_m_act),
    #                     irdc_summary_sm("oac_m_act", oac_m_act),
    #                     irdc_summary_sm("innova_m_act", innova_m_act),
    #
    #                 ]),
    #             ]),
    #         ]),
    #         html.Br(),
    #         html.P(
    #             "产品线员工投入D类总实际人天 {}; 投入其他部门(利润中心非PL111)的总实际人天 {}: 转出WBS共 {} 人天, 转出占比 {}% ".format(
    #                 str(wbs_d_days), str(wbs_notPL111_days), str(wbs_total_out),
    #                 str(round(((wbs_total_out / (round(本月合并底表['实际人天'].sum(), 1))) * 100), 1)))),
    #         dbc.Row([
    #             dbc.Col([
    #                 dbc.Row([
    #                     irdc_wh_large("sx_total_indicator", sx_wh_total)
    #                 ]),
    #                 dbc.Row([
    #                     irdc_wh_middle("sx_wbsD_indicator", sx_wbsD),
    #                     irdc_wh_middle("sx_wbsDper_indicator", sx_wbsDper)
    #                 ]),
    #                 dbc.Row([
    #                     irdc_wh_middle("sx_wbsX_indicator", sx_wbsX),
    #                     irdc_wh_middle("sx_wbsXper_indicator", sx_wbsXper)
    #                 ]),
    #
    #             ]),
    #             dbc.Col([
    #                 dbc.Row([
    #                     irdc_wh_large("ir_total_indicator", ir_wh_total)
    #                 ]),
    #                 dbc.Row([
    #                     irdc_wh_middle("ir_算法资源池_indicator", ir_wbsD),
    #                     irdc_wh_middle("ir_算法资源池per_indicator", ir_wbsDper)
    #                 ]),
    #                 dbc.Row([
    #                     irdc_wh_middle("ir_开发资源池_indicator", ir_wbsX),
    #                     irdc_wh_middle("ir_开发资源池per_indicator", ir_wbsXper)
    #                 ]),
    #
    #             ]),
    #             dbc.Col([
    #                 dbc.Row([
    #                     irdc_wh_large("dxSku_total_indicator", dxSku_wh_total)
    #                 ]),
    #                 dbc.Row([
    #                     irdc_wh_middle("dxSku_算法资源池_indicator", dxSku_wbsD),
    #                     irdc_wh_middle("dxSku_算法资源池per_indicator", dxSku_wbsDper)
    #                 ]),
    #                 dbc.Row([
    #                     irdc_wh_middle("dxSku_开发资源池_indicator", dxSku_wbsX),
    #                     irdc_wh_middle("dxSku_开发资源池per_indicator", dxSku_wbsXper)
    #                 ]),
    #
    #             ]),
    #             dbc.Col([
    #                 dbc.Row([
    #                     irdc_wh_large("dxTy_total_indicator", dxTy_wh_total)
    #                 ]),
    #                 dbc.Row([
    #                     irdc_wh_middle("dxTy_算法资源池_indicator", dxTy_wbsD),
    #                     irdc_wh_middle("dxTy_算法资源池per_indicator", dxTy_wbsDper)
    #                 ]),
    #                 dbc.Row([
    #                     irdc_wh_middle("dxTy_开发资源池_indicator", dxTy_wbsX),
    #                     irdc_wh_middle("dxTy_开发资源池per_indicator", dxTy_wbsXper)
    #                 ]),
    #
    #             ]),
    #             dbc.Col([
    #                 dbc.Row([
    #                     irdc_wh_large("mkt_total_indicator", mkt_wh_total)
    #                 ]),
    #                 dbc.Row([
    #                     irdc_wh_middle("mkt_算法资源池_indicator", mkt_wbsD),
    #                     irdc_wh_middle("mkt_算法资源池per_indicator", mkt_wbsDper)
    #                 ]),
    #                 dbc.Row([
    #                     irdc_wh_middle("mkt_开发资源池_indicator", mkt_wbsX),
    #                     irdc_wh_middle("mkt_开发资源池per_indicator", mkt_wbsXper)
    #                 ]),
    #
    #             ]),
    #             dbc.Col([
    #                 dbc.Row([
    #                     irdc_wh_large("oac_total_indicator", oac_wh_total)
    #                 ]),
    #                 dbc.Row([
    #                     irdc_wh_middle("oac_算法资源池_indicator", oac_wbsD),
    #                     irdc_wh_middle("oac_算法资源池per_indicator", oac_wbsDper)
    #                 ]),
    #                 dbc.Row([
    #                     irdc_wh_middle("oac_开发资源池_indicator", oac_wbsX),
    #                     irdc_wh_middle("oac_开发资源池per_indicator", oac_wbsXper)
    #                 ]),
    #
    #             ]),
    #         ]),
    #         html.Br(),
    #         html.Div(
    #             dbc.Accordion([
    #                 dbc.AccordionItem([
    #                     dbc.Row([
    #                         dbc.Col([
    #                             irdc_graph('WBS部门Top5-bar', figWBS部门Top5())
    #                         ], xs=12, sm=12, md=6, lg=6, xl=6),
    #                         dbc.Col([
    #                             irdc_graph('WBS实际人天Top5-pie', figWBStop5填报分布())
    #                         ], xs=12, sm=12, md=6, lg=6, xl=6),
    #                     ]),
    #                     # dbc.Row([
    #                     #     dbc.Col([
    #                     #         irdc_graph('WBS实际人天Top5-pie', figWBStop5填报分布())
    #                     #     ], xs=12, sm=12, md=6, lg=6, xl=6),
    #                     #     dbc.Col([
    #                     #         irdc_graph('WBS类型Top5-pie', figWBStop5填报类型分布())
    #                     #     ], xs=12, sm=12, md=6, lg=6, xl=6),
    #                     # ]),
    #                     dbc.Col([
    #                         dash_table_not_collapse("WBS部门Top5_id",
    #                                                 wbs_top5_actual().iloc[:, 0:-2]),
    #                     ]),
    #                     html.Br(),
    #                     dbc.Row([
    #                         dbc.Col([
    #                             irdc_graph('历史WBS类型-line', fig历史WBS类型())
    #                         ]),
    #                     ]),
    #                     html.Br(),
    #                     html.Br(),
    #                     dbc.Row([
    #                         dbc.Col([
    #                             dbc.Row([
    #                                 dbc.Col([
    #                                     html.P('WBS类型'),
    #                                 ], xs=6, sm=6, md=2, lg=2, xl=2),
    #                                 dbc.Col([
    #                                     dcc.Dropdown(
    #                                         id='dropDown_wbs类型',
    #                                         options=list(set(本月WBS维度['WBS类型'])),
    #                                         value='D',
    #                                         clearable=False,
    #                                         style={"width": "100%"},
    #                                         placeholder='WBS类型'
    #                                     ),
    #                                 ], xs=6, sm=6, md=4, lg=4, xl=4),
    #                             ]),
    #                         ]),
    #                         dbc.Col([
    #                             dbc.Row([
    #                                 dbc.Col([
    #                                     html.P('WBS类型'),
    #                                 ], xs=6, sm=6, md=2, lg=2, xl=2),
    #                                 dbc.Col([
    #                                     dcc.Dropdown(
    #                                         id='dropDown_wbs类型2',
    #                                         options=list(set(本月WBS维度['WBS类型'])),
    #                                         value='D',
    #                                         clearable=False,
    #                                         style={"width": "100%"},
    #                                         placeholder='WBS类型'
    #                                     ),
    #                                 ], xs=6, sm=6, md=4, lg=4, xl=4),
    #                             ]),
    #
    #                         ])
    #                     ]),
    #                     dbc.Row([
    #                         dbc.Col([
    #                             html.Div([
    #                                 html.Div([
    #                                     dcc.RadioItems(
    #                                         id='radio_产品线wbsD工时投入',
    #                                         options=[
    #                                             {'label': '员工组', 'value': 'graph_wbs员工组人天'},
    #                                             {'label': '资源池', 'value': 'graph_wbs资源池人天'},
    #                                             {'label': '岗位名称', 'value': 'graph_wbs岗位名称人天'},
    #                                             {'label': '员工姓名', 'value': 'graph_wbs员工姓名人天'},
    #                                         ],
    #                                         value='graph_wbs员工组人天',
    #                                         style={"width": "60%"},
    #                                         inline=True),
    #                                 ]),
    #                                 html.Div([
    #                                     dcc.Graph(id='graph_产品线wbsD工时投入',
    #                                               style={'height': 500,
    #                                                      "border-radius": "5px",
    #                                                      "background-color": "#f9f9f9",
    #                                                      "box-shadow": "2px 2px 2px lightgrey",
    #                                                      "position": "relative",
    #                                                      "margin-bottom": "15px"
    #                                                      },
    #                                               config={'displayModeBar': False},
    #                                               ),
    #                                 ]),
    #                             ])
    #                         ]
    #                             , xs=12, sm=12, md=6, lg=6, xl=6),
    #                         dbc.Col([
    #                             html.Div([
    #                                 html.Div([
    #                                     dcc.RadioItems(
    #                                         id='radio_产品线wbsD工时投入2',
    #                                         options=[
    #                                             {'label': '员工组', 'value': 'graph_wbs员工组人天2'},
    #                                             {'label': '员工所属部门', 'value': 'graph_wbs员工所属部门人天2'},
    #                                             {'label': '岗位名称', 'value': 'graph_wbs岗位名称人天2'},
    #                                             {'label': '员工姓名', 'value': 'graph_wbs员工姓名人天2'},
    #                                         ],
    #                                         value='graph_wbs员工组人天2',
    #                                         style={"width": "60%"},
    #                                         inline=True),
    #                                 ]),
    #                                 html.Div([
    #                                     dcc.Graph(id='graph_产品线wbsD工时投入2',
    #                                               style={'height': 500,
    #                                                      "border-radius": "5px",
    #                                                      "background-color": "#f9f9f9",
    #                                                      "box-shadow": "2px 2px 2px lightgrey",
    #                                                      "position": "relative",
    #                                                      "margin-bottom": "15px"
    #                                                      },
    #                                               config={'displayModeBar': False},
    #                                               ),
    #                                 ]),
    #                             ])
    #                         ]
    #                             , xs=12, sm=12, md=6, lg=6, xl=6),
    #                     ]),
    #                     html.Br(),
    #                     html.P("D类WBS的工时投入明细（按照实际人天倒序排序）"),
    #                     dash_table_not_collapse_showAll("wbsD类工时投入明细table",
    #                                                     wbsType('D').iloc[:, 0:-2].sort_values(by=['实际人天'],
    #                                                                                            ascending=False).reset_index(
    #                                                         drop=True)),
    #                     html.Br(),
    #                     html.Br(),
    #                     dbc.Row([
    #                         dbc.Col([
    #                             html.Div([
    #                                 html.Div([
    #                                     dcc.RadioItems(
    #                                         id='radio_产品线wbsX工时投入',
    #                                         options=[
    #                                             {'label': '员工组', 'value': 'graph_wbsX员工组人天'},
    #                                             {'label': '资源池', 'value': 'graph_wbsX资源池人天'},
    #                                             {'label': '岗位名称', 'value': 'graph_wbsX岗位名称人天'},
    #                                             {'label': '员工姓名', 'value': 'graph_wbsX员工姓名人天'},
    #                                         ],
    #                                         value='graph_wbsX员工组人天',
    #                                         style={"width": "60%"},
    #                                         inline=True),
    #                                 ]),
    #                                 html.Div(
    #                                     dcc.Graph(id='graph_产品线wbsX工时投入',
    #                                               style={'height': 500,
    #                                                      "border-radius": "5px",
    #                                                      "background-color": "#f9f9f9",
    #                                                      "box-shadow": "2px 2px 2px lightgrey",
    #                                                      "position": "relative",
    #                                                      "margin-bottom": "15px"
    #                                                      },
    #                                               config={'displayModeBar': False},
    #                                               ),
    #                                 ),
    #
    #                             ])
    #                         ], xs=12, sm=12, md=6, lg=6, xl=6),
    #                         dbc.Col([
    #                             html.Div([
    #                                 html.Div([
    #                                     dcc.RadioItems(
    #                                         id='radio_产品线wbsX工时投入2',
    #                                         options=[
    #                                             {'label': '员工组', 'value': 'graph_wbsX员工组人天2'},
    #                                             {'label': '员工所属部门', 'value': 'graph_wbsX员工所属部门人天2'},
    #                                             {'label': '岗位名称', 'value': 'graph_wbsX岗位名称人天2'},
    #                                             {'label': '员工姓名', 'value': 'graph_wbsX员工姓名人天2'},
    #                                         ],
    #                                         value='graph_wbsX员工组人天2',
    #                                         style={"width": "60%"},
    #                                         inline=True),
    #                                 ]),
    #                                 html.Div(
    #                                     dcc.Graph(id='graph_产品线wbsX工时投入2',
    #                                               style={'height': 500,
    #                                                      "border-radius": "5px",
    #                                                      "background-color": "#f9f9f9",
    #                                                      "box-shadow": "2px 2px 2px lightgrey",
    #                                                      "position": "relative",
    #                                                      "margin-bottom": "15px"
    #                                                      },
    #                                               config={'displayModeBar': False},
    #                                               ),
    #                                 ),
    #
    #                             ])
    #                         ], xs=12, sm=12, md=6, lg=6, xl=6),
    #                     ]),
    #                     html.Br(),
    #                     html.P("非PL111WBS的工时投入明细（按照实际人天倒序排序）"),
    #                     dash_table_not_collapse_showAll("wbsX类工时投入明细table",
    #                                                     notPL111wbsType().iloc[:, 0:-2].sort_values(by=['实际人天'],
    #                                                                                                 ascending=False).reset_index(
    #                                                         drop=True)),
    #
    #                     html.Br(),
    #                     dfExistDfStr(list(set(list(sku_to_PL111()['员工姓名']))), '冰箱填到PL111的员工个数：'),
    #                     dfExistDf(sortWBS(sku_to_PL111()), 'logic_distribution_tb_WBS_id'),
    #                     html.Br(),
    #
    #                     # dbc.Row([
    #                     #     irdc_graph('WBS汇总类型-pie', figWBS类型pie()),
    #                     # ]),
    #                     # dbc.Row([
    #                     #     irdc_graph('WBS汇总部门-pie', figWBS部门pie()),
    #                     # ]),
    #                     # dbc.Row([
    #                     #     dbc.Col([
    #                     #         irdc_graph('wbs预估填报分布-pie', figWBS预估填报分布())
    #                     #     ], xs=12, sm=12, md=6, lg=6, xl=6),
    #                     #     dbc.Col([
    #                     #         dbc.Row([
    #                     #             irdc_graph('WBS预估填报异常部门-pie', figWBS预估填报异常部门分布())
    #                     #         ]),
    #                     #     ], xs=12, sm=12, md=6, lg=6, xl=6),
    #                     # ]),
    #
    #                     dfExistDfStr(logic_rate_abnormal_tb_WBS(), 'WBS填报异常个数：'),
    #                     dfExistDf(sortWBS(logic_rate_abnormal_tb_WBS()).sort_values(by=['实际人天'],
    #                                                                                 ascending=False).reset_index(
    #                         drop=True), 'logic_distribution_tb_WBS_id'),
    #
    #                     # dbc.Row([
    #                     #     collapse_btn_table2("collapse-button6", "wbs总表_table",
    #                     #                         本月WBS维度.sort_values(by='实际人天', ascending=False).iloc[:,0:-2],
    #                     #                         'collapse6', '实际人天'),
    #                     # ]),
    #                     # dbc.Row([
    #                     #     dbc.Col([
    #                     #         dfExistDfStr(est_no_act_df(),'预估并未实际填写WBS个数：'),
    #                     #     ]),
    #                     #     dbc.Col([
    #                     #         dfExistDfStr(act_no_est_df(),'实际填写并未预估WBS个数：'),
    #                     #     ]),
    #                     # ]),
    #                     # dbc.Row([
    #                     #     dbc.Col([
    #                     #         irdc_graph('WBS预估未填报-pie', figWBS预估无实际分布())
    #                     #     ], xs=12, sm=12, md=6, lg=6, xl=6),
    #                     #     dbc.Col([
    #                     #         irdc_graph('WBS实际未填报-pie', figWBS实际未预估填报分布())
    #                     #     ], xs=12, sm=12, md=6, lg=6, xl=6),
    #                     # ]),
    #                     # dbc.Row([
    #                     #     dbc.Col([
    #                     #         dfExistDf(est_no_act_df(), "WBS预估未填报-table")
    #                     #     ]),
    #                     #     dbc.Col([
    #                     #         dfExistDf(act_no_est_df(), "WBS实际未填报-table")
    #                     #     ]),
    #                     # ]),
    #
    #                     # dbc.Row([
    #                     #         # dbc.Col([
    #                     #         #     dfExistDfStr(est_twice_wbs(), '连续两月预估无实际填写WBS个数：'),
    #                     #         # ]),
    #                     #     dbc.Col([
    #                     #         dfExistDfStr(get_more_than1yr_wbs(), '建立超过1年WBS个数：'),
    #                     #     ]),
    #                     # ]),
    #                     # dbc.Row([
    #                     #     # dbc.Col([
    #                     #     #     dfExistDf(est_twice_wbs(), '连续两月预估无实际填写WBS-table')
    #                     #     # ]),
    #                     #     dbc.Col([
    #                     #         dfExistDf(get_more_than1yr_wbs(), '超过1年WBS-table'),
    #                     #     ]),
    #                     # ]),
    #                     html.Br(),
    #
    #                     # dbc.Row([
    #                     #     dbc.Col([
    #                     #         irdc_graph('连续两月预估无实际填写WBS-pie', figWBS连续预估2月未填写分布())
    #                     #     ], xs=12, sm=12, md=6, lg=6, xl=6),
    #                     #     dbc.Col([
    #                     #         dbc.Row([
    #                     #             html.P('连续两月预估无实际填写WBS个数：' + str(
    #                     #                 len(est_twice_wbs())),
    #                     #                    style={"fontSize": 25}),
    #                     #         ]),
    #                     #         dbc.Row([
    #                     #             dbc.Col([
    #                     #                 dash_table_not_collapse('连续两月预估无实际填写WBS-table',est_twice_wbs()[['项目编号','项目名称','PM姓名','上月预估','本月预估']])
    #                     #             ]),
    #                     #         ]),
    #                     #     ], xs=12, sm=12, md=6, lg=6, xl=6),
    #                     # ]),
    #                     # dbc.Row([
    #                     #     dbc.Col([
    #                     #         irdc_graph('超过1年WBS-pie', figWBS超过1年分布())
    #                     #     ], xs=12, sm=12, md=6, lg=6, xl=6),
    #                     #     dbc.Col([
    #                     #         dbc.Row([
    #                     #             html.P('建立超过1年WBS个数：' + str(
    #                     #                 len(get_more_than1yr_wbs())),
    #                     #                    style={"fontSize": 25}),
    #                     #         ]),
    #                     #         dbc.Row([
    #                     #             dbc.Col([
    #                     #                 dash_table_not_collapse('超过1年WBS-table', get_more_than1yr_wbs())
    #                     #             ]),
    #                     #         ]),
    #                     #     ], xs=12, sm=12, md=6, lg=6, xl=6),
    #                     # ]),
    #                     dfExistDfStr(新增wbs(actual_wbs_tb(本月WBS维度), actual_wbs_tb(上月WBS维度)),
    #                                  '同比新增WBS个数(本月WBS明细)：'),
    #                     dfExistDf(sortWBS(新增wbs_tb(actual_wbs_tb(本月WBS维度), actual_wbs_tb(上月WBS维度), "项目编号",
    #                                                  "实际人天").iloc[:, :-2]), 'wbs新增table'),
    #                     html.Br(),
    #                     dfExistDfStr(减少wbs(actual_wbs_tb(本月WBS维度), actual_wbs_tb(上月WBS维度)),
    #                                  '同比减少WBS个数(上月WBS明细)：'),
    #                     dfExistDf(sortWBS(减少wbs_tb(actual_wbs_tb(本月WBS维度), actual_wbs_tb(上月WBS维度), "项目编号",
    #                                                  "实际人天").iloc[:, :-2]), 'wbs减少table'),
    #                     html.Br(),
    #                     html.Br(),
    #                     dbc.Col([
    #                         html.P('本月填报的全部WBS(各WBS类型按照实际人天倒序排序)：' + str(
    #                             len(actual_wbs_tb(本月WBS维度))), style={"fontSize": 25})
    #                     ]),
    #                     dbc.Col([
    #                         dash_table_not_collapse_showAll("all_tb_WBS_id",
    #                                                         sortWBS(actual_wbs_tb(本月WBS维度).iloc[:, :-2].sort_values(
    #                                                             by=['实际人天'], ascending=False).reset_index(
    #                                                             drop=True)))
    #
    #                     ]),
    #                     html.Br(),
    #                     html.Br(),
    #                     dbc.Row([
    #                         # dbc.Col([
    #                         #     dcc.RadioItems(
    #                         #         id='radio_利润中心wbs部门',
    #                         #         options=[
    #                         #             {'label': 'WBS所属部门', 'value': 'WBS所属部门'},
    #                         #             # {'label': 'WBS类型', 'value': 'WBS类型'},
    #                         #             # {'label': '利润中心', 'value': '利润中心'},
    #                         #         ],
    #                         #         value='WBS所属部门',
    #                         #         style={"width": "60%"},
    #                         #         inline=True),
    #                         # ], xs=12, sm=12, md=4, lg=4, xl=4),
    #                         dbc.Col([
    #                             html.P('WBS所属部门'),
    #                         ], xs=12, sm=12, md=2, lg=2, xl=2),
    #                         dbc.Col([
    #                             dcc.Dropdown(
    #                                 id='dropDown_利润中心wbs部门',
    #                                 options=[{'label': opt, 'value': opt} for opt in list(set(list(
    #                                     getAllWBS().sort_values(by='WBS所属部门', ascending=False)['WBS所属部门'])))],
    #                                 value=list(set(list(getAllWBS()['WBS所属部门'])))[0],
    #                                 placeholder="选择WBS所属部门",
    #                                 clearable=False,
    #                                 style={"width": "100%"},
    #                                 # multi=True
    #                             ),
    #                         ], xs=12, sm=12, md=10, lg=10, xl=10),
    #                     ]),
    #                     html.Br(),
    #                     dbc.Row([
    #                         dbc.Col([
    #                             html.P('项目名称'),
    #                         ], xs=12, sm=12, md=2, lg=2, xl=2),
    #                         dbc.Col([
    #                             dcc.Dropdown(
    #                                 id='dropDown_wbs名称',
    #                                 # options=[{'label': opt, 'value': opt} for opt in
    #                                 #          list(set(list(getAllWBS()['项目名称'])))],
    #                                 # value=list(set(list(getAllWBS()['项目名称'])))[0],
    #                                 clearable=False,
    #                                 placeholder="选择项目名称",
    #                                 style={"width": "100%"},
    #                                 # multi=True
    #                             ),
    #                         ], xs=12, sm=12, md=10, lg=10, xl=10),
    #                     ]),
    #                     html.Br(),
    #                     dbc.Row([
    #                         dcc.RadioItems(
    #                             id='radio_资源池岗位名称员工姓名',
    #                             options=[
    #                                 {'label': '资源池', 'value': '资源池'},
    #                                 {'label': '岗位名称', 'value': '岗位名称'},
    #                                 {'label': '员工组', 'value': '员工组'},
    #                                 {'label': '员工姓名', 'value': '员工姓名'},
    #                             ],
    #                             value='资源池',
    #                             style={"width": "60%"},
    #                             inline=True),
    #                     ]),
    #                     dbc.Row([
    #                         dbc.Col([
    #                             dcc.Graph(id='wbsHistorical_days', config={'displayModeBar': False}, )
    #                         ])
    #                     ]),
    #                     html.Br(),
    #                     html.Br(),
    #                     html.P('上诉wbs的历史工时投入'),
    #                     html.Div([
    #                         dash_table.DataTable(
    #                             id='table_历史wbs工时投入', )
    #                     ]),
    #                     html.Br(),
    #
    #                 ], title='点击查看WBS维度详细')
    #             ], flush=True, start_collapsed=True, id="accordtion-wbs")),
    #     ], fluid=True, id="accordtion-wh")

    if tab == '资源':
        return dbc.Container([
            html.P("GPU使用情况 ( Update at " + GPU使用更新时间() + ' )'),
            dbc.Row([
                dbc.Col([
                    irdc_summary_large("gpu_sh40_avg_usage", gpu_sh40_avg_usage)
                ]),
                dbc.Col([
                    dbc.Row([
                        irdc_summary_smWider("gpu_sh40_10_usage", gpu_sh40_10_usage),
                        irdc_summary_smWider("gpu_sh40_14_usage", gpu_sh40_14_usage),
                        irdc_summary_smWider("gpu_sh40_18_usage", gpu_sh40_18_usage),
                        irdc_summary_smWider("gpu_sh40_22_usage", gpu_sh40_22_usage),
                    ])]),

                dbc.Col([
                    irdc_summary_large("gpu_sg2_avg_usage", gpu_sg2_avg_usage)
                ]),
                dbc.Col([
                    dbc.Row([
                        irdc_summary_smWider("gpu_sg2_10_usage", gpu_sg2_10_usage),
                        irdc_summary_smWider("gpu_sg2_14_usage", gpu_sg2_14_usage),
                        irdc_summary_smWider("gpu_sg2_18_usage", gpu_sg2_18_usage),
                        irdc_summary_smWider("gpu_sg2_22_usage", gpu_sg2_22_usage),
                    ])]),

                dbc.Col([
                    irdc_summary_large("gpu_sh1988_avg_usage", gpu_sh1988_avg_usage)
                ]),
                dbc.Col([
                    dbc.Row([
                        irdc_summary_smWider("gpu_sh1988_10_usage", gpu_sh1988_10_usage),
                        irdc_summary_smWider("gpu_sh1988_14_usage", gpu_sh1988_14_usage),
                        irdc_summary_smWider("gpu_sh1988_18_usage", gpu_sh1988_18_usage),
                        irdc_summary_smWider("gpu_sh1988_22_usage", gpu_sh1988_22_usage),
                    ])]),

                dbc.Col([
                    irdc_summary_large("gpu_abud_avg_usage", gpu_abud_avg_usage)
                ]),
                dbc.Col([
                    dbc.Row([
                        irdc_summary_smWider("gpu_abud_10_usage", gpu_abud_10_usage),
                        irdc_summary_smWider("gpu_abud_14_usage", gpu_abud_14_usage),
                        irdc_summary_smWider("gpu_abud_18_usage", gpu_abud_18_usage),
                        irdc_summary_smWider("gpu_abud_22_usage", gpu_abud_22_usage),
                    ])]),

            ]),
            html.Br(),
            html.Div(
                dbc.Accordion(
                    [
                        dbc.AccordionItem([
                            html.Div([
                                html.Div([
                                    dcc.RadioItems(
                                        id='radio_gpu_filter',
                                        options=[
                                            {'label': '使用率', 'value': '使用率'},
                                            {'label': '累计使用节点', 'value': '累计使用节点'},
                                            {'label': '累计使用时长', 'value': '累计使用时长'},
                                        ],
                                        value='使用率',
                                        style={"width": "60%"},
                                        inline=True),

                                ]),
                                html.Div([
                                    dcc.RadioItems(
                                        id='radio_gpu_use',
                                        options=[
                                            {'label': 'Avg', 'value': 'graph_gpu_avg'},
                                            {'label': '10点', 'value': 'graph_gpu_10'},
                                            {'label': '14点', 'value': 'graph_gpu_14'},
                                            {'label': '18点', 'value': 'graph_gpu_18'},
                                            {'label': '22点', 'value': 'graph_gpu_22'},
                                        ],
                                        value='graph_gpu_avg',
                                        style={"width": "60%"},
                                        inline=True),
                                ]),
                                html.Div(
                                    dcc.Graph(id='graph_gpu_use',
                                              style={'height': 500,
                                                     "border-radius": "5px",
                                                     "background-color": "#f9f9f9",
                                                     "box-shadow": "2px 2px 2px lightgrey",
                                                     "position": "relative",
                                                     "margin-bottom": "15px"
                                                     },
                                              config={'displayModeBar': False},
                                              ),
                                ),

                                html.Div([
                                    dcc.RadioItems(
                                        id='radio_gpu_user_filter',
                                        options=[
                                            {'label': '累计使用节点', 'value': '累计使用节点'},
                                            {'label': '累计使用时长', 'value': '累计使用时长'},
                                        ],
                                        value='累计使用节点',
                                        style={"width": "60%"},
                                        inline=True),
                                ]),
                                html.Div(
                                    dcc.Graph(id='graph_gpu_user_use',
                                              style={'height': 500,
                                                     "border-radius": "5px",
                                                     "background-color": "#f9f9f9",
                                                     "box-shadow": "2px 2px 2px lightgrey",
                                                     "position": "relative",
                                                     "margin-bottom": "15px"
                                                     },
                                              config={'displayModeBar': False},
                                              ),
                                ),

                            ]),
                            dbc.Row([
                                dbc.Col([
                                    irdc_graph('gpuTop10userNodes-bar', figGpuUserTop10())
                                ], xs=12, sm=12, md=6, lg=6, xl=6),
                                dbc.Col([
                                    irdc_graph('gpuTop10userTime-bar', figGpuUserTimeTop10())
                                ], xs=12, sm=12, md=6, lg=6, xl=6),
                            ]),
                            dbc.Col([
                                dash_table_not_collapse("gpuTop10userNodes_id", monthly_gpu()),
                            ]),
                            html.Br(),
                            html.Br(),
                        ],
                            title='点击查看GPU使用详细',
                        )
                    ],

                    flush=True, start_collapsed=True, id="accordtion-gpu"
                ),
            ),

            html.Br(),
            html.P("OC存储  ( Update at " + OC存储更新时间() + ' )'),
            dbc.Row([
            ]),
            html.Br(),
            html.Div(
                dbc.Accordion(
                    [
                        dbc.AccordionItem([

                        ],
                            title='点击查看OC存储详细',
                        )
                    ],
                    flush=True, start_collapsed=True, id="accordtion-oc"
                ),
            ),

            html.Br(),
            html.P("DCP存储 ( Update at " + DCP存储更新时间() + ' )'),
            dbc.Row([
            ]),
            html.Br(),
            html.Div(
                dbc.Accordion(
                    [
                        dbc.AccordionItem([
                        ],
                            title='点击查看DCP存储详细',
                        )
                    ],
                    flush=True, start_collapsed=True, id="accordtion-dcp"
                ),
            ),

            html.Br(),
            html.P("数据采标 ( Update at " + 数据采标更新时间() + ' )'),
            dbc.Row([
                dbc.Col([
                    dbc.Col([
                        irdc_summary_large_ppl("dataBZ_indicator", dataBZ_indicator)
                    ]),
                    dbc.Col([
                        dbc.Row([
                            irdc_summary_smWider_ppl("dataBZ_done_indicator", dataBZ_done_indicator),
                            irdc_summary_smWider_ppl("dataBZ_ing_indicator", dataBZ_ing_indicator),
                            irdc_summary_smWider_ppl("dataBZ_back_indicator", dataBZ_back_indicator),
                        ])
                    ]),
                    dbc.Col([
                        dbc.Row([
                            irdc_summary_smWider_ppl("dataBZ_sx_indicator", dataBZ_sx_indicator),
                            irdc_summary_smWider_ppl("dataBZ_dx_indicator", dataBZ_dx_indicator),
                            irdc_summary_smWider_ppl("dataBZ_ir_indicator", dataBZ_ir_indicator),
                        ])
                    ]),
                ]),
                dbc.Col([
                    dbc.Col([
                        irdc_summary_large_ppl("dataBZ_bill_indicator", dataBZ_bill_indicator)
                    ]),
                    dbc.Col([
                        dbc.Row([
                            irdc_summary_smWider_ppl("dataBZ_bill_confirm", dataBZ_bill_confirm),
                            irdc_summary_smWider_ppl("dataBZ_bill_onhold", dataBZ_bill_onhold),
                        ])]),
                ]),
                dbc.Col([
                    dbc.Col([
                        irdc_summary_large_ppl("dataCJ_indicator", dataCJ_indicator)
                    ]),
                    dbc.Col([
                        dbc.Row([
                            irdc_summary_smWider_ppl("dataCJ_done_indicator", dataCJ_done_indicator),
                            irdc_summary_smWider_ppl("dataCJ_ing_indicator", dataCJ_ing_indicator),
                            irdc_summary_smWider_ppl("dataCJ_back_indicator", dataCJ_back_indicator),
                        ]),
                    ]),
                    dbc.Col([
                        dbc.Row([
                            irdc_summary_smWider_ppl("dataCJ_sx_indicator", dataCJ_sx_indicator),
                            irdc_summary_smWider_ppl("dataCJ_dx_indicator", dataCJ_dx_indicator),
                            irdc_summary_smWider_ppl("dataCJ_ir_indicator", dataCJ_ir_indicator),
                        ])
                    ]),
                ]),
                dbc.Col([
                    dbc.Col([
                        irdc_summary_large_ppl("dataCJ_bill_indicator", dataCJ_bill_indicator)
                    ]),
                    dbc.Col([
                        dbc.Row([
                            irdc_summary_smWider_ppl("dataCJ_bill_confirm", dataCJ_bill_confirm),
                            irdc_summary_smWider_ppl("dataCJ_bill_onhold", dataCJ_bill_onhold),
                        ])]),
                ]),

            ]),
            html.Br(),
            html.Div(
                dbc.Accordion(
                    [
                        dbc.AccordionItem([
                            dbc.Row([
                                irdc_graph('fig历史业务线标注费-id',
                                           fig历史业务线采标费用(历史标注费用(), '业务线历史标注费用'))
                            ]),
                            html.Br(),
                            dbc.Row([
                                dbc.Col([
                                    irdc_graph('figBZBillTop5-bar', figBZBillTop5())
                                ], xs=12, sm=12, md=6, lg=6, xl=6),
                                dbc.Col([
                                    irdc_graph('figBZBillTop5-pie', figBZBilltop5分布())
                                ], xs=12, sm=12, md=6, lg=6, xl=6),
                            ]),
                            # dbc.Col([
                            #     dash_table_not_collapse("bzBill_top5_id",
                            #                             bzBill_top5()),
                            # ]),
                            html.Br(),
                            dbc.Row([
                                dfExist(monthly_bz_cur, "上月无标注任务", "collapse-button9", 'collapse9'),
                                html.Br(),
                            ]),

                            dbc.Row([
                                dbc.Col([
                                    dbc.Row([
                                        html.P('验收数据包打回任务数：' + str(
                                            len(data_back_biaozhu())),
                                               style={"fontSize": 25}),
                                    ]),
                                    dbc.Row([
                                        irdc_graph('数据包打回任务-pie', fig标注数据包打回())
                                    ]),

                                ], xs=12, sm=12, md=6, lg=6, xl=6),
                                dbc.Col([
                                    dbc.Row([
                                        html.P('标注延期超过5天任务数：' + str(
                                            len(data_delay_biaozhu())),
                                               style={"fontSize": 25}),
                                    ]),
                                    dbc.Row([
                                        irdc_graph('标注任务延期超过5天-pie', fig标注任务延期())
                                    ])
                                ], xs=12, sm=12, md=6, lg=6, xl=6),
                            ]),

                            dbc.Row([
                                dbc.Col([
                                    collapse_btn_table("collapse-button11", "验收数据包打回任务_id",
                                                       data_back_biaozhu(),
                                                       'collapse11'),
                                ], xs=12, sm=12, md=6, lg=6, xl=6),
                                dbc.Col([
                                    collapse_btn_table("collapse-button12", "标注任务延期超过5天_id",
                                                       data_delay_biaozhu(),
                                                       'collapse12'),
                                ], xs=12, sm=12, md=6, lg=6, xl=6),
                            ]),

                            dbc.Row([
                                irdc_graph('fig历史业务线采集费-id',
                                           fig历史业务线采标费用(历史采集费用(), '业务线历史采集费用'))
                            ]),
                            dbc.Row([
                                dfExist(monthly_cj_cur, "上月无采集任务", "collapse-button10", 'collapse10'),
                                html.Br(),
                            ]),
                        ],
                            title='点击查看数据采标任务详细'
                        )
                    ],
                    flush=True, start_collapsed=True, id="accordtion-data"
                ),
            ),

            html.Br(),
            html.P("固定资产 ( Update at " + 固定资产更新时间() + ' )'),
            dbc.Row([
            ]),
            html.Br(),
            html.Div(
                dbc.Accordion(
                    [
                        dbc.AccordionItem([

                        ],
                            title='点击查看固定资产详细',
                        )
                    ],
                    flush=True, start_collapsed=True, id="accordtion-computers"
                ),
            ),

        ], fluid=True, id="accordtion-res")

    elif tab == '产品线/资源池':
        return dbc.Container([
            html.Br(),
            html.Br(),
            html.P("产品线（点击跳转，账号密码相同）"),
            dbc.NavItem(
                dbc.NavLink(
                    "智慧综合体",
                    href="http://irdc-sx.onrender.com",
                    external_link='True',
                    target='_blank'
                )
            ),
            dbc.NavItem(
                dbc.NavLink(
                    "智慧娱乐",
                    href="http://irdc-ir.onrender.com",
                    external_link='True',
                    target='_blank'
                )
            ),
            dbc.NavItem(
                dbc.NavLink(
                    "创新孵化",
                    href="http://irdc-dx.onrender.com",
                    external_link='True',
                    target='_blank'
                )
            ),
            html.P("资源池（点击跳转，账号密码相同）"),
            dbc.Row([
                dbc.NavItem(
                    dbc.NavLink(
                        "算法SDK资源池",
                        href="http://irdc-alg.onrender.com",
                        external_link='True',
                        target='_blank'
                    )
                ),
                dbc.NavItem(
                    dbc.NavLink(
                        "业务开发资源池",
                        href="http://irdc-eng.onrender.com",
                        external_link='True',
                        target='_blank'
                    )
                ),
                dbc.NavItem(
                    dbc.NavLink(
                        "平台架构资源池",
                        href="http://irdc-sar.onrender.com",
                        external_link='True',
                        target='_blank'
                    )
                ),
                dbc.NavItem(
                    dbc.NavLink(
                        "运维测试资源池",
                        href="http://irdc-ops.onrender.com",
                        external_link='True',
                        target='_blank'
                    )
                ),
            ]),
        ], fluid=True, id="accordtion-jumpList")


@app.callback(
    Output("fig全量实际vs理论人天-scatter", "figure"),
    [Input("range-slider实际vs理论", "value"),
     Input("radio_实际vs理论", "value")])
def update_bar_chart(slider_range, radio_domain):
    if radio_domain == '员工所属部门':
        low, high = slider_range
        mask = (cur_mon_staff.理论填报率 >= low) & (cur_mon_staff.理论填报率 <= high)
        fig = px.scatter(cur_mon_staff[mask],
                         title='员工"实际人天"v."理论人天"',
                         x="实际人天", y="理论人天",
                         color="员工所属部门", size="实际人天", hover_data=['员工姓名', '员工组', '资源池', '岗位名称'])
        return fig
    elif radio_domain == '资源池':
        low, high = slider_range
        mask = (cur_mon_staff.理论填报率 >= low) & (cur_mon_staff.理论填报率 <= high)
        fig = px.scatter(cur_mon_staff[mask],
                         title='员工"实际人天"v."理论人天"',
                         x="实际人天", y="理论人天",
                         color="资源池", size="实际人天", hover_data=['员工姓名', '员工组', '员工所属部门', '岗位名称'])
        return fig


@app.callback(
    Output("fig全量实际vs预估人天-scatter", "figure"),
    [Input("range-slider实际vs预估", "value"),
     Input("radio_实际vs预估", "value")])
def update_bar_chart2(slider_range, radio_domain):
    if radio_domain == '员工所属部门':
        low, high = slider_range
        mask = (cur_mon_staff.预估填报率 >= low) & (cur_mon_staff.预估填报率 <= high)
        fig = px.scatter(cur_mon_staff[mask],
                         title='员工"实际人天"v."预估人天"',
                         x="实际人天", y="预估人天",
                         color="员工所属部门", size="实际人天", hover_data=['员工姓名', '员工组', '资源池', '岗位名称'])
        return fig
    elif radio_domain == '资源池':
        low, high = slider_range
        mask = (cur_mon_staff.预估填报率 >= low) & (cur_mon_staff.预估填报率 <= high)
        fig = px.scatter(cur_mon_staff[mask],
                         title='员工"实际人天"v."预估人天"',
                         x="实际人天", y="预估人天",
                         color="资源池", size="实际人天", hover_data=['员工姓名', '员工组', '员工所属部门', '岗位名称'])
        return fig


@app.callback(
    [Output("historical_days", "figure"),
     Output("historical_wbs_days", "figure"),
     Output('staffNameRemind', 'children'),
     Output('sameDaysWithStaff', 'children'),
     Output('sameDaysWithStaff2', 'children')],
    [Input('input_userName', 'value'),
     Input('fig全量实际vs理论人天-scatter', 'clickData'),
     Input('fig全量实际vs预估人天-scatter', 'clickData')]
)
def update_outputLogic(input_userName, clickDatalogic, clickDataestim):
    ctx = dash.callback_context
    click_id = ctx.triggered[0]['prop_id'].split('.')[0]
    try:
        if click_id == 'fig全量实际vs预估人天-scatter':
            user = clickDataestim['points'][0]['customdata'][0]
            actDays = clickDataestim['points'][0]['x']
            estDays = clickDataestim['points'][0]['y']
            temp = cur_mon_staff[cur_mon_staff['实际人天'] == actDays]
            temp = temp[temp['预估人天'] == estDays].copy().reset_index(drop=True)
            sameDaysStaff = list(set(temp['员工姓名']))
            if len(sameDaysStaff) > 1:
                sameDaysStaff.remove(user)
                sameDaysStaff = '"实际人天"和"预估人天" 与【{}】 一致的员工有： '.format(user) + str(sameDaysStaff)
                sameDaysStaff2 = ""
            else:
                sameDaysStaff = "没有其他员工与 【{}】 一致".format(user)
                sameDaysStaff2 = ""

        elif click_id == 'fig全量实际vs理论人天-scatter':
            user = clickDatalogic['points'][0]['customdata'][0]
            actDays = clickDatalogic['points'][0]['x']
            logicDays = clickDatalogic['points'][0]['y']
            temp = cur_mon_staff[cur_mon_staff['实际人天'] == int(actDays)]
            temp = temp[temp['理论人天'] == int(logicDays)].copy().reset_index(drop=True)
            sameDaysStaff2 = list(set(temp['员工姓名']))
            if len(sameDaysStaff2) > 1:
                sameDaysStaff2.remove(user)
                sameDaysStaff2 = '"实际人天"和"理论人天" 与【{}】一致的员工有： '.format(user) + str(sameDaysStaff2)
                sameDaysStaff = ""
            else:
                sameDaysStaff2 = "没有其他员工与 【{}】 一致".format(user)
                sameDaysStaff = ""

        elif len(input_userName) > 0:
            user = input_userName
            sameDaysStaff = ""
            sameDaysStaff2 = ""

        data1 = getCertainUserDays(user).reset_index(drop=True)
        for i in range(len(data1)):
            data1.loc[i, '工时月份'] = str(data1.loc[i, '工时年份']) + '年' + str(data1.loc[i, '工时月份']) + '月'
        figure = fig员工历史人天(data1)
        staff_apartment = data1['员工所属部门'][0]
        staff_title = data1['岗位名称'][0]
        staff_res = data1['资源池'][0]
        staff_type = data1['员工组'][0]

        data2 = getCertainUserWBS(user).reset_index(drop=True)
        for i in range(len(data2)):
            data2.loc[i, '工时月份'] = str(data2.loc[i, '工时年份']) + '年' + str(data2.loc[i, '工时月份']) + '月'
        figure2 = fig员工历史wbs人天(data2)
        return figure, figure2, '{} ( 部门：{}-{}，岗位：{}-{} ) 的历史工时如下'.format(user, staff_apartment, staff_type,
                                                                                     staff_res,
                                                                                     staff_title), sameDaysStaff, sameDaysStaff2
    except:
        user = None
        figure = go.Figure()
        figure2 = go.Figure()
        return figure, figure2, '{} 员工不存在 or 姓名输入错误 or 该员工没有数据！'.format(user), "", ""


@app.callback(
    Output('graph_actual_per', 'figure'),
    [Input(component_id='radio_actual_per', component_property='value')]
)
def build_graph_actual_per(value_actual_per):
    if value_actual_per == 'graph_actual_per_all':
        return fig历史实际人均人天()
    else:
        return fig历史实际人均人天_irdc()


@app.callback(
    Output('graph_logic_rate', 'figure'),
    [Input(component_id='radio_logic_rate', component_property='value')]
)
def build_graph_logic_rate(value_logic_rate):
    if value_logic_rate == 'graph_logic_rate_irdc':
        return fig历史理论填报率_irdc()

    else:
        return fig历史理论填报率()


@app.callback(
    Output('graph_产品线工时投入', 'figure'),
    Input(component_id='radio_产品线工时投入', component_property='value')
)
def build_graph_bl_wl(attri):
    if attri == 'graph_员工组人天':
        return fig员工部门员工组()
    elif attri == 'graph_资源池人天':
        return fig员工部门资源池()
    elif attri == 'graph_岗位名称人天':
        return fig员工部门岗位名称()


@app.callback(
    Output('graph_资源池工时投入', 'figure'),
    Input(component_id='radio_资源池工时投入', component_property='value')
)
def build_graph_rpl_wl(attri):
    if attri == 'graph_资源池员工组人天':
        return fig资源池员工部门员工组()
    elif attri == 'graph_资源池员工所属部门人天':
        return fig资源池员工部门资源池()
    elif attri == 'graph_资源池岗位名称人天':
        return fig资源池员工部门岗位名称()


@app.callback(
    Output('table_产品线工时投入', 'data'),
    Input(component_id='radio_产品线工时投入', component_property='value')
)
def build_table_bl_wl(attri):
    if attri == 'graph_员工组人天':
        return df0Beautfy(groupByWl(本月人员维度(),
                                    {'创新孵化-体育': [],
                                     '创新孵化-冰箱': [],
                                     '市场拓展部': [],
                                     '智慧娱乐': [],
                                     '智慧综合体': [],
                                     '运营与赋能中心': []},
                                    ['正式员工', '外包员工', '实习生'],
                                    '员工所属部门', '员工组')).to_dict('records')
    elif attri == 'graph_资源池人天':
        return df0Beautfy(groupByWl(本月人员维度(),
                                    {'创新孵化-体育': [],
                                     '创新孵化-冰箱': [],
                                     '市场拓展部': [],
                                     '智慧娱乐': [],
                                     '智慧综合体': [],
                                     '运营与赋能中心': []},
                                    ['算法SDK资源池', '业务开发资源池', '架构平台资源池', '测试运维资源池', '非资源池'],
                                    '员工所属部门', '资源池')).to_dict('records')
    elif attri == 'graph_岗位名称人天':
        return df0Beautfy(groupByWl(本月人员维度(),
                                    {'创新孵化-体育': [],
                                     '创新孵化-冰箱': [],
                                     '市场拓展部': [],
                                     '智慧娱乐': [],
                                     '智慧综合体': [],
                                     '运营与赋能中心': []},
                                    ['RPL', '算法研究', '算法开发', '前端开发', '后端开发', '平台开发', '架构师',
                                     '测试', 'DevOps', '产品方案', '产品管理', '项目管理', ],
                                    '员工所属部门', '岗位名称')).to_dict('records')


@app.callback(
    Output('table_资源池工时投入', 'data'),
    Input(component_id='radio_资源池工时投入', component_property='value')
)
def build_table_rpl_wl(attri):
    if attri == 'graph_资源池员工组人天':
        return df0Beautfy(groupByWl(本月人员维度(),
                                    {'业务开发资源池': [],
                                     '架构平台资源池': [],
                                     '测试运维资源池': [],
                                     '算法SDK资源池': [],
                                     '非资源池': []},
                                    ['正式员工', '外包员工', '实习生'],
                                    '资源池', '员工组')).to_dict('records')
    elif attri == 'graph_资源池员工所属部门人天':
        return df0Beautfy(groupByWl(本月人员维度(),
                                    {'业务开发资源池': [],
                                     '架构平台资源池': [],
                                     '测试运维资源池': [],
                                     '算法SDK资源池': [],
                                     '非资源池': []},
                                    ['创新孵化-体育', '创新孵化-冰箱', '市场拓展部', '智慧娱乐', '智慧综合体',
                                     '运营与赋能中心'],
                                    '资源池', '员工所属部门')).to_dict('records')
    elif attri == 'graph_资源池岗位名称人天':
        return df0Beautfy(groupByWl(本月人员维度(),
                                    {'业务开发资源池': [],
                                     '架构平台资源池': [],
                                     '测试运维资源池': [],
                                     '算法SDK资源池': [],
                                     '非资源池': []},
                                    ['RPL', '算法研究', '算法开发', '前端开发', '后端开发', '平台开发', '架构师',
                                     '测试', 'DevOps', '产品方案', '产品管理', '项目管理', ],
                                    '资源池', '岗位名称')).to_dict('records')


@app.callback(
    Output('table_历史wbs工时投入', 'data'),
    Input('dropDown_wbs名称', 'value')
)
def build_table_wbs_historical_days(value):
    data = readhistroyData(工时历史总表汇总(), '合并底表')
    data = data[data['员工所属部门'] != 0]
    return data[data['项目名称'] == value].reset_index(drop=True).to_dict('records')


@app.callback(
    Output('graph_产品线wbsD工时投入', 'figure'),
    [Input('dropDown_wbs类型', 'value'),
     Input(component_id='radio_产品线wbsD工时投入', component_property='value')]
)
def build_WBSgraph_bl_wl(type, attri):
    if attri == 'graph_wbs员工组人天':
        data = wbsType(type)
        return fig员工部门不同维度wbs(对比部门汇总2(data, '实际人天', "员工组"), "员工组",
                                      '员工所属部门员工组投入' + type + '类WBS实际人天')
    elif attri == 'graph_wbs资源池人天':
        data = wbsType(type)
        return fig员工部门不同维度wbs(对比部门汇总2(data, '实际人天', "资源池"), "资源池",
                                      '员工所属部门资源池投入' + type + '类WBS实际人天')
    elif attri == 'graph_wbs岗位名称人天':
        data = wbsType(type)
        return fig员工部门不同维度wbs(对比部门汇总2(data, '实际人天', "岗位名称"), "岗位名称",
                                      '员工所属部门岗位名称投入' + type + '类WBS实际人天')
    elif attri == 'graph_wbs员工姓名人天':
        data = wbsType(type)
        return fig员工部门不同维度wbs(对比部门汇总2(data, '实际人天', "员工姓名"), "员工姓名",
                                      '员工所属部门员工姓名投入' + type + '类WBS实际人天')


@app.callback(
    Output('graph_产品线wbsD工时投入2', 'figure'),
    [Input('dropDown_wbs类型2', 'value'),
     Input(component_id='radio_产品线wbsD工时投入2', component_property='value')]
)
def build_WBSgraph_bl_wl2(type, attri):
    if attri == 'graph_wbs员工组人天2':
        data = wbsType(type)
        return fig员工部门不同维度wbs2(对比部门汇总3(data, '实际人天', "员工组"), "员工组",
                                       '资源池员工组投入' + type + '类WBS实际人天')
    elif attri == 'graph_wbs员工所属部门人天2':
        data = wbsType(type)
        return fig员工部门不同维度wbs2(对比部门汇总3(data, '实际人天', "员工所属部门"), "员工所属部门",
                                       '资源池员工所属部门投入' + type + '类WBS实际人天')
    elif attri == 'graph_wbs岗位名称人天2':
        data = wbsType(type)
        return fig员工部门不同维度wbs2(对比部门汇总3(data, '实际人天', "岗位名称"), "岗位名称",
                                       '资源池岗位名称投入' + type + '类WBS实际人天')
    elif attri == 'graph_wbs员工姓名人天2':
        data = wbsType(type)
        return fig员工部门不同维度wbs2(对比部门汇总3(data, '实际人天', "员工姓名"), "员工姓名",
                                       '资源池员工姓名投入' + type + '类WBS实际人天')


@app.callback(
    Output('graph_产品线wbsX工时投入', 'figure'),
    [Input(component_id='radio_产品线wbsX工时投入', component_property='value')]
)
def build_WBSgraph_bl_wl(attri):
    if attri == 'graph_wbsX员工组人天':
        return fig员工部门不同维度wbs(对比部门汇总2(notPL111wbsType(), '实际人天', "员工组"), "员工组",
                                      '员工所属部门员工组投入非PL111WBS实际人天')
    elif attri == 'graph_wbsX资源池人天':
        return fig员工部门不同维度wbs(对比部门汇总2(notPL111wbsType(), '实际人天', "资源池"), "资源池",
                                      '员工所属部门资源池投入非PL111WBS实际人天')
    elif attri == 'graph_wbsX岗位名称人天':
        return fig员工部门不同维度wbs(对比部门汇总2(notPL111wbsType(), '实际人天', "岗位名称"), "岗位名称",
                                      '员工所属部门岗位名称投入非PL111WBS实际人天')
    elif attri == 'graph_wbsX员工姓名人天':
        return fig员工部门不同维度wbs(对比部门汇总2(notPL111wbsType(), '实际人天', "员工姓名"), "员工姓名",
                                      '员工所属部门员工姓名投入非PL111WBS实际人天')


@app.callback(
    Output('graph_产品线wbsX工时投入2', 'figure'),
    [Input(component_id='radio_产品线wbsX工时投入2', component_property='value')]
)
def build_WBSgraph_bl_wl2(attri):
    if attri == 'graph_wbsX员工组人天2':
        return fig员工部门不同维度wbs2(对比部门汇总3(notPL111wbsType(), '实际人天', "员工组"), "员工组",
                                       '资源池员工组投入非PL111WBS实际人天')
    elif attri == 'graph_wbsX员工所属部门人天2':
        return fig员工部门不同维度wbs2(对比部门汇总3(notPL111wbsType(), '实际人天', "员工所属部门"), "员工所属部门",
                                       '资源池员工所属部门投入非PL111WBS实际人天')
    elif attri == 'graph_wbsX岗位名称人天2':
        return fig员工部门不同维度wbs2(对比部门汇总3(notPL111wbsType(), '实际人天', "岗位名称"), "岗位名称",
                                       '资源池岗位名称投入非PL111WBS实际人天')
    elif attri == 'graph_wbsX员工姓名人天2':
        return fig员工部门不同维度wbs2(对比部门汇总3(notPL111wbsType(), '实际人天', "员工姓名"), "员工姓名",
                                       '资源池员工姓名投入非PL111WBS实际人天')


# @app.callback(
#     [Output('dropDown_利润中心wbs部门', 'options'),
#     Output('dropDown_利润中心wbs部门', 'value')],
#     Input(component_id='radio_利润中心wbs部门', component_property='value')
# )
# def buildWbsHistoryGraph(value):
#     if value == '利润中心':
#         opts = list(set(getAllWBS()['利润中心']))
#         options = [{'label': opt, 'value': opt} for opt in opts]
#         return options, value
#     elif value == 'WBS类型':
#         opts = list(set(getAllWBS()['WBS类型']))
#         options = [{'label': opt, 'value': opt} for opt in opts]
#         value = opts[0]
#         return options, value
#     elif value == 'WBS所属部门':
#         opts = list(set(getAllWBS()['WBS所属部门']))
#         options = [{'label': opt, 'value': opt} for opt in opts]
#         value = opts[0]
#         return options, value


@app.callback(
    [Output('dropDown_wbs名称', 'options'),
     Output('dropDown_wbs名称', 'value')],
    Input('dropDown_利润中心wbs部门', 'value')
)
def buildWbsNameList(value):
    # if value == '利润中心':
    #     data = getAllWBS()[getAllWBS()['利润中心'] in [listValue]]
    #     opts = list(set(data['项目名称']))
    #     options = [{'label': opt, 'value': opt} for opt in opts]
    #     value = opts[0]
    #     return options, value
    # elif value == 'WBS类型':
    #     data = getAllWBS()[getAllWBS()['WBS类型'] in [listValue]]
    #     opts = list(set(data['项目名称']))
    #     options = [{'label': opt, 'value': opt} for opt in opts]
    #     value = opts[0]
    #     return options, value
    data = getAllWBS()[getAllWBS()['WBS所属部门'] == value]
    opts = list(set(data['项目名称']))
    options = [{'label': opt, 'value': opt} for opt in opts]
    value = opts[0]
    return options, value


@app.callback(
    Output('wbsHistorical_days', 'figure'),
    [Input('dropDown_wbs名称', 'value'),
     Input(component_id='radio_资源池岗位名称员工姓名', component_property='value')]
)
def build_wbsGraph(wbsName, groupByValue):
    data = getCertainWBS(wbsName).reset_index(drop=True)
    groupBy = groupByValue
    for i in range(len(data)):
        data.loc[i, '工时月份'] = str(data.loc[i, '工时年份']) + '年' + str(data.loc[i, '工时月份']) + '月'
    return fig历史wbs人天(data, groupBy)


# @app.callback(
#     Output(component_id='radio_gpu_filter', component_property='value'),
#     Input(component_id='radio_gpu_use', component_property='value'))
# def filterGpuRadio(value):


@app.callback(
    Output('graph_gpu_use', 'figure'),
    [Input(component_id='radio_gpu_filter', component_property='value'),
     Input(component_id='radio_gpu_use', component_property='value')]
)
def build_graph_gpu_use(radio_gpu_filter, value_gpu_use):
    if radio_gpu_filter == '使用率':
        if value_gpu_use == 'graph_gpu_avg':
            return fig历史gpu使用(clean_gpu_avg_usage(), "日期", '使用率', 'GPU历史使用率', '分区')
        if value_gpu_use == 'graph_gpu_10':
            return fig历史gpu使用具体时间点(历史GPU使用情况(), 10, "日期", '使用率', 'GPU历史使用率')
        if value_gpu_use == 'graph_gpu_14':
            return fig历史gpu使用具体时间点(历史GPU使用情况(), 14, "日期", '使用率', 'GPU历史使用率')
        if value_gpu_use == 'graph_gpu_18':
            return fig历史gpu使用具体时间点(历史GPU使用情况(), 18, "日期", '使用率', 'GPU历史使用率')
        if value_gpu_use == 'graph_gpu_22':
            return fig历史gpu使用具体时间点(历史GPU使用情况(), 22, "日期", '使用率', 'GPU历史使用率')

    elif radio_gpu_filter == '累计使用节点':
        if value_gpu_use == 'graph_gpu_avg':
            return fig历史gpu使用(gpu_avg_sum_nodes(历史GPU用户使用情况()), '日期', '使用节点数', 'GPU累计使用节点数',
                                  '分区')
        if value_gpu_use == 'graph_gpu_10':
            return fig历史gpu使用具体时间点(历史GPU用户使用情况(), 10, '日期', '使用节点数', 'GPU累计使用节点数')
        if value_gpu_use == 'graph_gpu_14':
            return fig历史gpu使用具体时间点(历史GPU用户使用情况(), 14, '日期', '使用节点数', 'GPU累计使用节点数')
        if value_gpu_use == 'graph_gpu_18':
            return fig历史gpu使用具体时间点(历史GPU用户使用情况(), 18, '日期', '使用节点数', 'GPU累计使用节点数')
        if value_gpu_use == 'graph_gpu_22':
            return fig历史gpu使用具体时间点(历史GPU用户使用情况(), 22, '日期', '使用节点数', 'GPU累计使用节点数')

    elif radio_gpu_filter == '累计使用时长':
        if value_gpu_use == 'graph_gpu_avg':
            return fig历史gpu使用(gpu_avg_sum_time(历史GPU用户使用情况()), '日期', '累计使用时长',
                                  'GPU累计使用时长(小时)', '分区')
        if value_gpu_use == 'graph_gpu_10':
            return fig历史gpu使用具体时间点(历史GPU用户使用情况(), 10, '日期', '累计使用时长', 'GPU累计使用时长(小时)')
        if value_gpu_use == 'graph_gpu_14':
            return fig历史gpu使用具体时间点(历史GPU用户使用情况(), 14, '日期', '累计使用时长', 'GPU累计使用时长(小时)')
        if value_gpu_use == 'graph_gpu_18':
            return fig历史gpu使用具体时间点(历史GPU用户使用情况(), 18, '日期', '累计使用时长', 'GPU累计使用时长(小时)')
        if value_gpu_use == 'graph_gpu_22':
            return fig历史gpu使用具体时间点(历史GPU用户使用情况(), 22, '日期', '累计使用时长', 'GPU累计使用时长(小时)')


@app.callback(
    Output('graph_gpu_user_use', 'figure'),
    [Input(component_id='radio_gpu_user_filter', component_property='value')]
)
def build_graph_gpu_user_user(value):
    if value == '累计使用节点':
        return fig历史gpu使用(clean_gpu_user(), "日期", '使用节点数', '历史用户累计使用节点', '用户')
    elif value == '累计使用时长':
        return fig历史gpu使用(clean_gpu_user(), "日期", '累计使用时长', '历史用户累计使用时长', '用户')


# @app.callback(
#     Output('graph_actual_per', 'figure'),
#     [Input(component_id='radio_actual_per', component_property='value')]
# )
# def build_graph_actual_per(value):
#     if value == 'graph_irdc_actual_per':
#         return irdc_graph('1', fig历史实际人均人天_irdc())
#
#     else:
#         return irdc_graph('2', fig历史实际人均人天())
#

#
if __name__ == "__main__":
    app.run_server(debug=True, port=8090)

# app.callback 里加上prevent_initial_callback=True,为了不要一开始就call back
# 用判断条件来看是是否要trigger，用state，然后def里的参数需要input 和state 几个
# return 记得用component_property 来放在def里return
# 用df作图，永远先copy 成新df来做！！！
# PreventUpdate 用来避免output update
# 有很多output，但有些不想update 用Dash.no_update
