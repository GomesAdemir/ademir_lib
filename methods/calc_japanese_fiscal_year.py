from .methods import fiscal
import pandas as pd

@pd.api.extensions.register_series_accessor("fiscal")
class FiscalAccessor:
    def __init__(self, pandas_obj):
        self._obj = pandas_obj

    def add_fy(self, dayfirst=True):
        """
        Retorna uma Series com o Ano Fiscal Japonês no formato FYxx
        """
        series = pd.to_datetime(self._obj, errors="coerce", dayfirst=dayfirst)

        def japanese_fiscal_year(dt):
            if pd.isna(dt):
                return None
            year = dt.year
            # Ano fiscal japonês: começa em 1º de abril e termina em 31 de março do ano seguinte
            if dt.month > 3 or (dt.month == 4 and dt.day >= 1):
                fiscal_year = year
            else:
                fiscal_year = year - 1
            return f"FY{str(fiscal_year)[-2:]}"
        
        return series.apply(japanese_fiscal_year)