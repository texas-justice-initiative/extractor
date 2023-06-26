"""
Pregnant Inmate Report
1. Add column names: 
    # - name: county_name
    # - name: p_code
    # - name: pregnant_female_count
    #   description: Pregnant individuals booked in jail and individuals found to be pregnant in jail
    # - name: data_date
    # - name: processed_at
    # - name: loaded_at
2. Parse data for columns:
County_name: Convert to titlecase, remove all (P) text
p_code: True if county name has (P), otherwise false
pregnant_female_count: numbers in second column
data_date: Extract month/year from first row - ex: APRIL 2023 PREGNANT INMATE REPORT
processed_at: datetime.now()
loaded_at: datetime.now()
3. Output data as a dictionary
"""

from typing import Dict

class XLSXConverter:
    """Turn Excel file into CSV file"""
    def __init__(self, report_type: str):
        self.report_type = report_type

    def convert(self) -> Dict:
        pass