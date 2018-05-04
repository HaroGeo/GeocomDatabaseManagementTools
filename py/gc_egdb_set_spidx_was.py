# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        gc_egdb_set_spidx_was
# Purpose:
#
# Author:      Geocom Informatik AG
#
# Created:     01.04.2018
# Copyright:   (c) Geocom Informatik AG 2018
#-------------------------------------------------------------------------------




# Variables

def_array=[]

def_array.append(['/DIV/DIMENSION' , 'Polygon' , [100]])
def_array.append(['/DIV/KONSTRUKTION_FLA' , 'Polygon' , [1000]])
def_array.append(['/DIV/KONSTRUKTION_LIN' , 'Polyline' , [1000]])
def_array.append(['/DIV/KONSTRUKTION_PKT' , 'Point' , [500]])
def_array.append(['/DIV/MESSPUNKT' , 'Point' , [1000]])

def_array.append(['/WAS/WAS_ARMATUR' , 'Point' , [250]])
def_array.append(['/WAS/WAS_BAUMASSNAHMEN' , 'Point' , [1000]])
def_array.append(['/WAS/WAS_BMN_FLA' , 'Polygon' , [500]])
def_array.append(['/WAS/WAS_BMN_LIN' , 'Polyline' , [250]])
def_array.append(['/WAS/WAS_BMN_PKT' , 'Point' , [250]])
def_array.append(['/WAS/WAS_HAUSANSCHLUSS' , 'Point' , [250]])
def_array.append(['/WAS/WAS_HYDRANT' , 'Point' , [1000]])
def_array.append(['/WAS/WAS_HYDRAULIK_KNOTEN_PKT' , 'Point' , [1000]])
def_array.append(['/WAS/WAS_HYDRAULIK_STRANG_LIN' , 'Polyline' , [1000]])
def_array.append(['/WAS/WAS_KABEL' , 'Polyline' , [250]])
def_array.append(['/WAS/WAS_KABEL_PKT' , 'Point' , [1000]])
def_array.append(['/WAS/WAS_KKS' , 'Point' , [1000]])
def_array.append(['/WAS/WAS_LEITUNGSPUNKT' , 'Point' , [250]])
def_array.append(['/WAS/WAS_LINIE' , 'Polyline' , [500]])
def_array.append(['/WAS/WAS_ROHRLEITUNGSTEIL' , 'Point' , [250]])
def_array.append(['/WAS/WAS_SBW_FLA' , 'Polygon' , [500]])
def_array.append(['/WAS/WAS_SBW_LIN' , 'Polyline' , [500]])
def_array.append(['/WAS/WAS_SBW_PKT' , 'Point' , [500]])
def_array.append(['/WAS/WAS_SCHADEN' , 'Point' , [500]])
def_array.append(['/WAS/WAS_SPEZIALBAUWERK' , 'Point' , [1000]])
def_array.append(['/WAS/WAS_TOPO_LIN' , 'Polyline' , [250]])
def_array.append(['/WAS/WAS_UEBRIGE_PKT' , 'Point' , [250]])
def_array.append(['/WAS/WAS_LEITUNG' , 'Polyline' , [200]])
def_array.append(['/WAS/WAS_SCHUTZZONE_FLA' , 'Polygon' , [1000]])
def_array.append(['/WAS/WAS_NET_Junctions' , 'Point' , [200]])
def_array.append(['/WAS/WAS_DETAILPUNKT' , 'Point' , [500]])
def_array.append(['/WAS/WAS_DRUCKZONE_FLA' , 'Polygon' , [500]])
def_array.append(['/WAS/WAS_EINSTIEG' , 'Point' , [500]])
def_array.append(['/WAS/WAS_SCHUTZGEBIET_FLA' , 'Polygon' , [500]])
def_array.append(['/WAS/WAS_VERSORGUNGSBEZIRK' , 'Polygon' , [500]])

def_array.append(['/WAS_LABEL/WAST_BEMERKUNG_LTG' , 'Polyline' , [500]])
def_array.append(['/WAS_LABEL/WAST_MATDURCH_LTG' , 'Polyline' , [500]])
def_array.append(['/WAS_LABEL/WAST_NAME_SPEZIALBW' , 'Polyline' , [500]])
def_array.append(['/WAS_LABEL/WAST_SCHALT_ARMATUR' , 'Polyline' , [500]])
def_array.append(['/WAS_LABEL/WAST_TEXT' , 'Polyline' , [500]])
def_array.append(['/WAS_LABEL/WAST_UEBERDECKUNG_LTG' , 'Polyline' , [500]])
def_array.append(['/WAS_LABEL/WAST_MATTYPMESS_BMN' , 'Polyline' , [500]])
def_array.append(['/WAS_LABEL/WAST_TEXT_KABEL' , 'Polyline' , [500]])
def_array.append(['/WAS_LABEL/WAST_TEXT_KABEL_PKT' , 'Polyline' , [500]])
def_array.append(['/WAS_LABEL/WAST_NUMMER_ARMATUR' , 'Polyline' , [500]])
def_array.append(['/WAS_LABEL/WAST_NUMMER_HAUSAN' , 'Polyline' , [500]])
def_array.append(['/WAS_LABEL/WAST_NUMMER_HYD_STRANG' , 'Polyline' , [500]])
def_array.append(['/WAS_LABEL/WAST_NUMMER_HYDR' , 'Polyline' , [500]])
def_array.append(['/WAS_LABEL/WAST_NUMMER_ROHRT' , 'Polyline' , [500]])
def_array.append(['/WAS_LABEL/WASA_ccfb5cac6012b4518d788a13' , 'Annotation' , [500]])
def_array.append(['/WAS_LABEL/WASA_452b3c4af1eca2d4e5b1a7a5' , 'Annotation' , [500]])
def_array.append(['/WAS_LABEL/WASA_a40b27d48f822bbb659d9fc5' , 'Annotation' , [500]])
def_array.append(['/WAS_LABEL/WASA_5973d6d52521dfce094dde67' , 'Annotation' , [500]])
def_array.append(['/WAS_LABEL/WASA_67e0af784d2e4e3c862fb50e' , 'Annotation' , [500]])
def_array.append(['/WAS_LABEL/WASA_e3b39ac6571a6acfe1cf711a' , 'Annotation' , [500]])
def_array.append(['/WAS_LABEL/WASA_51c100585afe59d0e8897915' , 'Annotation' , [500]])
def_array.append(['/WAS_LABEL/WASA_4bfa9940ddd7205d171e2de1' , 'Annotation' , [500]])


def_array.append(['/WAS_PW2/WAS_PW2_LEITUNG' , 'Polyline' , [500]])
def_array.append(['/WAS_PW2/WAS_PW2_TOPO_LIN' , 'Polyline' , [500]])
def_array.append(['/WAS_PW2/WAS_PW2_HAUSANSCHLUSS' , 'Point' , [500]])
def_array.append(['/WAS_PW2/WAS_PW2_HYDRANT' , 'Point' , [500]])
def_array.append(['/WAS_PW2/WAS_PW2_KKS' , 'Point' , [500]])
def_array.append(['/WAS_PW2/WAS_PW2_ROHRLEITUNGSTEIL' , 'Point' , [500]])
def_array.append(['/WAS_PW2/WAS_PW2_SPEZIALBAUWERK' , 'Point' , [500]])
def_array.append(['/WAS_PW2/WAS_PW2_ARMATUR' , 'Point' , [500]])
def_array.append(['/WAS_PW2/WAS_PW2_UEBRIGE_PKT' , 'Point' , [500]])
def_array.append(['/WAS_PW2/WAS_PW2_KABEL' , 'Polyline' , [500]])
def_array.append(['/WAS_PW2/WAS_PW2_KABEL_PKT' , 'Point' , [500]])
def_array.append(['/WAS_PW2/WAS_PW2_SYMBOL_HYDRANT' , 'Point' , [500]])
def_array.append(['/WAS_PW2/WAST_PW2_DURCHM_LTG' , 'Polyline' , [500]])
def_array.append(['/WAS_PW2/WAST_PW2_NUMMER_HYDR' , 'Polyline' , [500]])
def_array.append(['/WAS_PW2/WAST_PW2_NAME_SPEZIALBW' , 'Polyline' , [500]])
def_array.append(['/WAS_PW2/WAST_PW2_NUMMER_ARMATUR' , 'Polyline' , [500]])
def_array.append(['/WAS_PW2/WAST_PW2_ENTNAHME_HYDR' , 'Polyline' , [500]])
def_array.append(['/WAS_PW2/WAST_PW2_FLIESSDRUCK_HYDR' , 'Polyline' , [500]])
def_array.append(['/WAS_PW2/WAST_PW2_TEXT_PUMPWERK' , 'Polyline' , [500]])
def_array.append(['/WAS_PW2/WAST_PW2_TEXT_RESERVOIR' , 'Polyline' , [500]])
def_array.append(['/WAS_PW2/WAST_PW2_VERSORGUNGSDRUCK_HYDR' , 'Polyline' , [500]])

def_array.append(['/WAS_PW3/WAS_PW3_TOPO_LIN' , 'Polyline' , [500]])
def_array.append(['/WAS_PW3/WAS_PW3_ARMATUR' , 'Point' , [500]])
def_array.append(['/WAS_PW3/WAS_PW3_HAUSANSCHLUSS' , 'Point' , [500]])
def_array.append(['/WAS_PW3/WAS_PW3_HYDRANT' , 'Point' , [500]])
def_array.append(['/WAS_PW3/WAS_PW3_LEITUNG' , 'Polyline' , [500]])
def_array.append(['/WAS_PW3/WAS_PW3_SPEZIALBAUWERK' , 'Point' , [500]])
def_array.append(['/WAS_PW3/WAS_PW3_KABEL' , 'Polyline' , [500]])
def_array.append(['/WAS_PW3/WAS_PW3_KABEL_PKT' , 'Point' , [500]])
def_array.append(['/WAS_PW3/WAS_PW3_KKS' , 'Point' , [500]])
def_array.append(['/WAS_PW3/WAS_PW3_ROHRLEITUNGSTEIL' , 'Point' , [500]])
def_array.append(['/WAS_PW3/WAS_PW3_UEBRIGE_PKT' , 'Point' , [500]])
def_array.append(['/WAS_PW3/WAST_PW3_DURCHM_LTG' , 'Polyline' , [500]])
def_array.append(['/WAS_PW3/WAST_PW3_NUMMER_HYDR' , 'Polyline' , [500]])
def_array.append(['/WAS_PW3/WAST_PW3_NAME_SPEZIALBW' , 'Polyline' , [500]])
def_array.append(['/WAS_PW3/WAST_PW3_NUMMER_ARMATUR' , 'Polyline' , [500]])
def_array.append(['/WAS_PW3/WAS_PW3_SYMBOL_HYDRANT' , 'Point' , [500]])
def_array.append(['/WAS_PW3/WAST_PW3_ENTNAHME_HYDR' , 'Polyline' , [500]])
def_array.append(['/WAS_PW3/WAST_PW3_FLIESSDRUCK_HYDR' , 'Polyline' , [500]])
def_array.append(['/WAS_PW3/WAST_PW3_TEXT_PUMPWERK' , 'Polyline' , [500]])
def_array.append(['/WAS_PW3/WAST_PW3_TEXT_RESERVOIR' , 'Polyline' , [500]])
def_array.append(['/WAS_PW3/WAST_PW3_VERSORGUNGSDRUCK_HYDR' , 'Polyline' , [500]])

def_array.append(['/WAS_PWD/GNPWD_URSPRUNG' , 'Polygon' , [500]])
def_array.append(['/WAS_PWD/GNPWD_ABBILD' , 'Polygon' , [500]])
def_array.append(['/WAS_PWD/GNPWD_VERBINDUNG' , 'Polyline' , [500]])
def_array.append(['/WAS_PWD/WAS_PWD_ARMATUR' , 'Point' , [500]])
def_array.append(['/WAS_PWD/WAS_PWD_HAUSANSCHLUSS' , 'Point' , [500]])
def_array.append(['/WAS_PWD/WAS_PWD_HYDRANT' , 'Point' , [500]])
def_array.append(['/WAS_PWD/WAS_PWD_KABEL' , 'Polyline' , [500]])
def_array.append(['/WAS_PWD/WAS_PWD_KABEL_PKT' , 'Point' , [500]])
def_array.append(['/WAS_PWD/WAS_PWD_KKS' , 'Point' , [500]])
def_array.append(['/WAS_PWD/WAS_PWD_LEITUNG' , 'Polyline' , [500]])
def_array.append(['/WAS_PWD/WAS_PWD_ROHRLEITUNGSTEIL' , 'Point' , [500]])
def_array.append(['/WAS_PWD/WAS_PWD_SBW_PKT' , 'Point' , [500]])
def_array.append(['/WAS_PWD/WAS_PWD_SBW_LIN' , 'Polyline' , [500]])
def_array.append(['/WAS_PWD/WAS_PWD_SBW_FLA' , 'Polygon' , [500]])
def_array.append(['/WAS_PWD/WAS_PWD_SPEZIALBAUWERK' , 'Point' , [500]])
def_array.append(['/WAS_PWD/WAS_PWD_UEBRIGE_PKT' , 'Point' , [500]])
def_array.append(['/WAS_PWD/WAST_PWD_BEMERKUNG_LTG' , 'Polyline' , [500]])
def_array.append(['/WAS_PWD/WAST_PWD_MATDURCH_LTG' , 'Polyline' , [500]])
def_array.append(['/WAS_PWD/WAST_PWD_NAME_SPEZIALBW' , 'Polyline' , [500]])
def_array.append(['/WAS_PWD/WAST_PWD_SCHALT_ARMATUR' , 'Polyline' , [500]])
def_array.append(['/WAS_PWD/WAST_PWD_UEBERDECKUNG_LTG' , 'Polyline' , [500]])
def_array.append(['/WAS_PWD/WAST_PWD_NUMMER_HYDR' , 'Polyline' , [500]])
def_array.append(['/WAS_PWD/WAST_PWD_NAME_ABBILD' , 'Polyline' , [500]])
def_array.append(['/WAS_PWD/WAST_PWD_NAME_URSPRUNG' , 'Polyline' , [500]])
def_array.append(['/WAS_PWD/WAST_PWD_NUMMER_ARMATUR' , 'Polyline' , [500]])
def_array.append(['/WAS_PWD/WAST_PWD_NUMMER_HAUSAN' , 'Polyline' , [500]])
def_array.append(['/WAS_PWD/WAST_PWD_NUMMER_ROHRT' , 'Polyline' , [500]])
def_array.append(['/WAS_PWD/WASA_ccd7346d01c59022d7d93ef4' , 'Annotation' , [500]])
def_array.append(['/WAS_PWD/WASA_987dad9d2fd8528dc3344c34' , 'Annotation' , [500]])
def_array.append(['/WAS_PWD/WASA_dd4100759eb32a8432c876c3' , 'Annotation' , [500]])
def_array.append(['/WAS_PWD/WASA_ef607a16f86dc68ce854efe3' , 'Annotation' , [500]])
def_array.append(['/WAS_PWD/WASA_90fa9bab3cc9c298b064248c' , 'Annotation' , [500]])
def_array.append(['/WAS_PWD/WASA_d29867866128f0bab3c39428' , 'Annotation' , [500]])
def_array.append(['/WAS_PWD/WASA_85bb4e46f9e987bfa8f1e80e' , 'Annotation' , [500]])
def_array.append(['/WAS_PWD/WASA_aaf44162386754cc2837fc0d' , 'Annotation' , [500]])