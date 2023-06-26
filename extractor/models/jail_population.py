from typing import Optional

from sqlmodel import Field, SQLModel

# archive_url to get links: https://www.tcjs.state.tx.us/population-summary-reports/
# latest_url: https://www.tcjs.state.tx.us/population-reports/ (all are on there)
# report name on website: AbbreRptCurrent.xslx / pdf
# base url format: https://www.tcjs.state.tx.us/wp-content/uploads/2023/03/AbbreRptCurrent.xlsx
# page to get links: view-source:https://www.tcjs.state.tx.us/population-reports/
# formats: pdf has date (and filed incorrectly); xslx has no date on the report so we need to rely on url
class JailPopulationCounty(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    # - name: county_name
    # - name: p_code
    # - name: report_date
    # - name: pretrial_felons
    # - name: convicted_felons
    # - name: convicted_felons_sentenced_county
    # - name: parole_violators
    # - name: parole_violators_new_charge
    # - name: pretrial_misdemeanor
    # - name: convicted_misdemeanor
    # - name: bench_warrants
    # - name: federal
    # - name: pretrial_sjf
    # - name: convicted_sjf_sentenced_county
    # - name: convicted_sjf_sentenced_state
    # - name: total_others
    # - name: total_local
    # - name: total_contract
    # - name: total_population
    # - name: total_capacity
    # - name: pct_capacity
    # - name: available_beds
    # - name: processed_at
    # - name: loaded_at
    # - name: document_id
    # - name: source_filename

class JailPopulationTotal(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    # - name: pretrial_felons
    # - name: convicted_felons
    # - name: convicted_felons_sentenced_county
    # - name: parole_violators
    # - name: parole_violators_new_charge
    # - name: pretrial_misdemeanor
    # - name: convicted_misdemeanor
    # - name: bench_warrants
    # - name: federal
    # - name: pretrial_sjf
    # - name: convicted_sjf_sentenced_county
    # - name: convicted_sjf_sentenced_state
    # - name: total_others
    # - name: total_local
    # - name: total_contract
    # - name: total_population
    # - name: total_capacity
    # - name: pct_capacity
    # - name: available_beds
    # - name: processed_at
    # - name: loaded_at
