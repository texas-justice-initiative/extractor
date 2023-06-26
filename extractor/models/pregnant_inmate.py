from typing import Optional

from sqlmodel import Field, SQLModel

# archive_url to get links: https://www.tcjs.state.tx.us/population-summary-reports/
# latest_url: https://www.tcjs.state.tx.us/population-reports/ (all are on there)
# report name on website: PregnantFemaleReportingCurrent.xslx / pdf
# base url format: https://www.tcjs.state.tx.us/wp-content/uploads/2023/03/PregnantFemaleReportingCurrent.xlsx
# page to get links: view-source:https://www.tcjs.state.tx.us/population-reports/
# formats: pdf has date (and filed incorrectly); xslx has month of report in words at top
class PregnantInmateCounty(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    # description: Monthly pregnant inmate counts by county
    # columns:
    # - name: county_name
    # - name: p_code
    # - name: pregnant_female_count
    #   description: Pregnant individuals booked in jail and individuals found to be pregnant in jail
    # - name: data_date
    # - name: processed_at
    # - name: loaded_at


class PregnantInmateTotal(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    # description: State-level pregnant inmate count by month
    # columns:
    # - name: pregnant_female_count
    #   description: Pregnant individuals booked in jail and individuals found to be pregnant in jail
    # - name: data_date
    # - name: processed_at
    # - name: loaded_at