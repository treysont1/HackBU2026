import json

data = """
[
  {
    "code": "AAAS",
    "description": "AAAS - Asian Asian Am Study"
  },
  {
    "code": "ACCT",
    "description": "ACCT - Accounting"
  },
  {
    "code": "AFST",
    "description": "AFST - Africana Studies"
  },
  {
    "code": "AMS",
    "description": "AMS - Ancient Mediterranean St"
  },
  {
    "code": "ANTH",
    "description": "ANTH - Anthropology"
  },
  {
    "code": "ARAB",
    "description": "ARAB - Arabic"
  },
  {
    "code": "ARTH",
    "description": "ARTH - Art History"
  },
  {
    "code": "ARTS",
    "description": "ARTS - Studio Art"
  },
  {
    "code": "ASTR",
    "description": "ASTR - Astronomy"
  },
  {
    "code": "BCHM",
    "description": "BCHM - Biochemistry"
  },
  {
    "code": "BIOL",
    "description": "BIOL - Biology"
  },
  {
    "code": "BLS",
    "description": "BLS - Business Law and Society"
  },
  {
    "code": "BME",
    "description": "BME - Biomedical Engineering"
  },
  {
    "code": "CCPA",
    "description": "CCPA-Col Comm &amp; Public Affairs"
  },
  {
    "code": "CDCI",
    "description": "CDCI-Career Dev Ctr Internship"
  },
  {
    "code": "CHEM",
    "description": "CHEM - Chemistry"
  },
  {
    "code": "CHIN",
    "description": "CHIN - Chinese"
  },
  {
    "code": "CINE",
    "description": "CINE - Cinema"
  },
  {
    "code": "COLI",
    "description": "COLI - Comparative Literatr"
  },
  {
    "code": "CQS",
    "description": "CQS - Comp and Quant Skills"
  },
  {
    "code": "CS",
    "description": "CS - Computer Science"
  },
  {
    "code": "CSC",
    "description": "CSC - Comm Schools Cert"
  },
  {
    "code": "CW",
    "description": "CW - Creative Writing"
  },
  {
    "code": "DATA",
    "description": "DATA - Data Analytics"
  },
  {
    "code": "DIDA",
    "description": "DIDA - Digital and Data Study"
  },
  {
    "code": "ECON",
    "description": "ECON - Economics"
  },
  {
    "code": "EDD",
    "description": "EDD - Engineering Design Div"
  },
  {
    "code": "EDUC",
    "description": "EDUC - Education"
  },
  {
    "code": "EECE",
    "description": "EECE - Elec Eng Comput Eng"
  },
  {
    "code": "EEES",
    "description": "EEES - E Europe &amp; Eurasian Std"
  },
  {
    "code": "ELED",
    "description": "ELED - Elementary Education"
  },
  {
    "code": "EML",
    "description": "EML - Eng for Multilinguals"
  },
  {
    "code": "ENG",
    "description": "ENG - English"
  },
  {
    "code": "ENT",
    "description": "ENT - Entrepreneurship"
  },
  {
    "code": "ENVI",
    "description": "ENVI - Environmental Study"
  },
  {
    "code": "ERED",
    "description": "ERED - Early Childhood Educ"
  },
  {
    "code": "EVOS",
    "description": "EVOS - Evolutionary Studies"
  },
  {
    "code": "FIN",
    "description": "FIN - Finance"
  },
  {
    "code": "FREN",
    "description": "FREN - French"
  },
  {
    "code": "GEOG",
    "description": "GEOG - Geography"
  },
  {
    "code": "GEOL",
    "description": "GEOL - Geology"
  },
  {
    "code": "GERM",
    "description": "GERM - German"
  },
  {
    "code": "GLST",
    "description": "GLST - Global Studies"
  },
  {
    "code": "GMAP",
    "description": "GMAP - Genocide&amp;Mass Atr Prev"
  },
  {
    "code": "GPH",
    "description": "GPH - Global Public Health"
  },
  {
    "code": "GRD",
    "description": "GRD - Graduate"
  },
  {
    "code": "GRK",
    "description": "GRK - Greek"
  },
  {
    "code": "HARP",
    "description": "HARP - Harpur College Wide"
  },
  {
    "code": "HDEV",
    "description": "HDEV - Human Development"
  },
  {
    "code": "HEBR",
    "description": "HEBR - Hebrew"
  },
  {
    "code": "HESA",
    "description": "HESA - Higher Ed &amp; Student Aff"
  },
  {
    "code": "HIST",
    "description": "HIST - History"
  },
  {
    "code": "HMRT",
    "description": "HMRT - Human Rights"
  },
  {
    "code": "HSCI",
    "description": "HSCI - Health Sciences"
  },
  {
    "code": "HWS",
    "description": "HWS - Health and Wellness St"
  },
  {
    "code": "INFO",
    "description": "INFO - Information Systm"
  },
  {
    "code": "ISE",
    "description": "ISE - Industr and Systm Engr"
  },
  {
    "code": "ISRL",
    "description": "ISRL - Israel Studies"
  },
  {
    "code": "ITAL",
    "description": "ITAL - Italian"
  },
  {
    "code": "JPN",
    "description": "JPN - Japanese"
  },
  {
    "code": "JUST",
    "description": "JUST - Judaic Studies"
  },
  {
    "code": "KOR",
    "description": "KOR - Korean"
  },
  {
    "code": "LACS",
    "description": "LACS -Lat Amer and Carib Study"
  },
  {
    "code": "LAT",
    "description": "LAT - Latin"
  },
  {
    "code": "LEAD",
    "description": "LEAD - Leadership"
  },
  {
    "code": "LING",
    "description": "LING - Linguistics"
  },
  {
    "code": "LTRC",
    "description": "LTRC - Literacy"
  },
  {
    "code": "MATH",
    "description": "MATH -Mathematics &amp; Statistics"
  },
  {
    "code": "MDVL",
    "description": "MDVL - Medieval Studies"
  },
  {
    "code": "ME",
    "description": "ME - Mechanical Engineering"
  },
  {
    "code": "MGMT",
    "description": "MGMT - Management"
  },
  {
    "code": "MIS",
    "description": "MIS - Mgmt Info Systems"
  },
  {
    "code": "MKTG",
    "description": "MKTG - Marketing"
  },
  {
    "code": "MSE",
    "description": "MSE - Material Science Eng"
  },
  {
    "code": "MSHR",
    "description": "MSHR - MS Human Rights"
  },
  {
    "code": "MUS",
    "description": "MUS - Music"
  },
  {
    "code": "MUSP",
    "description": "MUSP - Music Performance"
  },
  {
    "code": "NURS",
    "description": "NURS - Nursing"
  },
  {
    "code": "OCT",
    "description": "OCT - Occupational Therapy"
  },
  {
    "code": "OPM",
    "description": "OPM - Mgmt Operations"
  },
  {
    "code": "OUT",
    "description": "OUT - Outdoor Pursuits"
  },
  {
    "code": "PAFF",
    "description": "PAFF - Public Affairs"
  },
  {
    "code": "PERS",
    "description": "PERS - Persian"
  },
  {
    "code": "PH",
    "description": "PH - Public Health"
  },
  {
    "code": "PHIL",
    "description": "PHIL - Philosophy"
  },
  {
    "code": "PHRM",
    "description": "PHRM - Pharmacy"
  },
  {
    "code": "PHSC",
    "description": "PHSC - Pharmaceutical Sciences"
  },
  {
    "code": "PHYS",
    "description": "PHYS - Physics"
  },
  {
    "code": "PIC",
    "description": "PIC - Phil Interp Culture"
  },
  {
    "code": "PLSC",
    "description": "PLSC - Political Science"
  },
  {
    "code": "PPL",
    "description": "PPL - Phil Politics and Law"
  },
  {
    "code": "PSYC",
    "description": "PSYC - Psychology"
  },
  {
    "code": "PT",
    "description": "PT - Physical Therapy"
  },
  {
    "code": "RELG",
    "description": "RELG - Religious Studies"
  },
  {
    "code": "RHET",
    "description": "RHET - Rhetoric"
  },
  {
    "code": "ROML",
    "description": "ROML - Romance Langs and Lit"
  },
  {
    "code": "RUSS",
    "description": "RUSS - Russian"
  },
  {
    "code": "SAA",
    "description": "SAA - Student Affairs Admin"
  },
  {
    "code": "SCHL",
    "description": "SCHL - BUniv Scholars Courses"
  },
  {
    "code": "SCM",
    "description": "SCM - Supply Chain Management"
  },
  {
    "code": "SEC",
    "description": "SEC - Secondary Education"
  },
  {
    "code": "SLP",
    "description": "SLP - Speech &amp; Lang Pathology"
  },
  {
    "code": "SOC",
    "description": "SOC - Sociology"
  },
  {
    "code": "SPAN",
    "description": "SPAN - Spanish"
  },
  {
    "code": "SPED",
    "description": "SPED - Special Education"
  },
  {
    "code": "SSIE",
    "description": "SSIE - SS and Industrial Engr"
  },
  {
    "code": "SUST",
    "description": "SUST - Sustainable Communities"
  },
  {
    "code": "SW",
    "description": "SW - Social Work"
  },
  {
    "code": "THEA",
    "description": "THEA - Theater"
  },
  {
    "code": "THEP",
    "description": "THEP - Theater Performance"
  },
  {
    "code": "TRIP",
    "description": "TRIP - Translation Research"
  },
  {
    "code": "TURK",
    "description": "TURK - Turkish"
  },
  {
    "code": "UNIV",
    "description": "UNIV - Univ Wide Courses"
  },
  {
    "code": "WGSS",
    "description": "WGSS-Women, Gender &amp; Sexuality"
  },
  {
    "code": "WRIT",
    "description": "WRIT - Writing"
  },
  {
    "code": "WTSN",
    "description": "WTSN - Engineering Design"
  },
  {
    "code": "YIDD",
    "description": "YIDD - Yiddish"
  }
]

"""

parsed = json.loads(data)
 
SUBJECTS = [item["code"] for item in parsed]

print(SUBJECTS)