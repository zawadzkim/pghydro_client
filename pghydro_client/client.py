# client.py
from dataclasses import dataclass
from pandas import DataFrame
import requests

@dataclass
class WaterDataClient:
    """
    Class for connecting to the API.
    """
    base_url: str
    token: str
    headers: dict = None

    def __post_init__(self):
        self.headers = {'Authorization': f'Token {self.token}'}

    def fetch_data(self, 
                   url: str, 
                   params: dict = None) -> dict:
        
        """Fetches data from the API and returns it as a json object.

        Parameters
        ----------
        url : str
            URL to fetch data from.
        params : dict, optional
            Parameters to pass to the API. The default is None.

        Returns
        -------
        json
            JSON object containing the data.

        Raises
        ------
        HTTPError
            If the request fails.

        Examples
        --------
        >>> from pghydro_client import WaterDataClient
        >>> client = WaterDataClient(base_url='https://your-api-url.com', token='mytoken')
        """

        response = requests.get(url, params=params, headers=self.headers)
        response.raise_for_status()
        return response.json()

@dataclass
class GetData:
    """
    Class for getting data from the API.
    """
    client: WaterDataClient = None
    data: dict = None

    def get_groundwater_level(self) -> DataFrame:
        """Get groundwater level data from the API.
        Not implemented yet.
        """
        response = self.client.fetch_data(f"{self.client.base_url}/groundwaterlevel/")
        return response
    
    def get_physicochemical_parameters(self, 
                                       station: str | list = None, 
                                       parameter: str | list = None, 
                                       timestamp_start: str = None, 
                                       timestamp_end: str = None) -> DataFrame:
        """
        Get physicochemical parameter data from the API.

        Parameters
        ----------
        station : str or list of str, optional
            Station name(s) to filter by. If not specified, all stations are returned.
        parameter : str or list of str, optional
            Parameter name(s) to filter by. If not specified, all parameters are returned.
        timestamp_start : str, optional
            Start date to filter by. If not specified, all dates are returned.
        timestamp_end : str, optional
            End date to filter by. If not specified, all dates are returned.

        Returns
        -------
        DataFrame
            Pandas DataFrame containing the data.

        Examples
        --------
        >>> from pghydro_client import WaterDataClient, GetData
        >>> client = WaterDataClient(base_url='https://your-api-url.com', token='mytoken')
        >>> data = GetData(client)
        >>> # When parameters are not specified, that parameter is not used for filtering.
        >>> df = get_data.get_physicochemical_parameters(station='Piezometer 1', parameter=['pH', 'Temperature', 'Conductivity'])
        >>> df.head()
        """
        params = {}
        if station is not None:
            if isinstance(station, list):
                station = ','.join(station)
            params['station'] = station

        if parameter is not None:
            if isinstance(parameter, list):
                parameter = ','.join(parameter)
            params['parameter'] = parameter

        if timestamp_start is not None:
            params['timestamp_start'] = timestamp_start
        else:
            params['timestamp_start'] = '1900-01-01'

        if timestamp_end is not None:
            params['timestamp_end'] = timestamp_end
        else:
            params['timestamp_end'] = '2100-01-01'

        response = self.client.fetch_data(f"{self.client.base_url}/physicochemicalparameter/", params=params)

        df = DataFrame(response)
        return df
    
    def get_analyses(self, 
                     station: str | list = None, 
                     analyte: str | list = None, 
                     timestamp_start: str = None, 
                     timestamp_end: str = None) -> DataFrame:
        
        """
        Get physicochemical parameter data from the API.

        Parameters
        ----------
        station : str or list of str, optional
            Station name(s) to filter by. If not specified, all stations are returned.
        analyte : str or list of str, optional
            Analyte name(s) to filter by. If not specified, all parameters are returned.
        timestamp_start : str, optional
            Start date to filter by. If not specified, all dates are returned.
        timestamp_end : str, optional
            End date to filter by. If not specified, all dates are returned.

        Returns
        -------
        DataFrame
            Pandas DataFrame containing the data.

        Examples
        --------
        >>> from pghydro_client import WaterDataClient, GetData
        >>> client = WaterDataClient(base_url='https://your-api-url.com', token='mytoken')
        >>> data = GetData(client)
        >>> # When parameters are not specified, that parameter is not used for filtering.
        >>> df = get_data.get_analyses(station='Piezometer 1', analyte=['Ca', 'Cl', 'Na'])
        >>> df.head()
        """

        params = {}
        if station is not None:
            if isinstance(station, list):
                station = ','.join(station)
            params['station'] = station

        if analyte is not None:
            if isinstance(analyte, list):
                analyte = ','.join(analyte)
            params['analyte'] = analyte

        if timestamp_start is not None:
            params['timestamp_start'] = timestamp_start
        else:
            params['timestamp_start'] = '1900-01-01'

        if timestamp_end is not None:
            params['timestamp_end'] = timestamp_end
        else:
            params['timestamp_end'] = '2100-01-01'

        response = self.client.fetch_data(f"{self.client.base_url}/analysis/", params=params)
        
        df = DataFrame(response)
        return df
