# seawater_crm

Certified values for seawater reference materials as pandas DataFrames.

## Installation

    pip install seawater_crm
    conda install conda-forge::seawater_crm

## Usage

See module and function docstrings for more detailed information.

### Dickson CO<sub>2</sub> CRMs

```python
    import seawater_crm as swcrm

    # Generate pandas DataFrame containing certified values
    crm = swcrm.dickson.get_crm_batches()

    # Access values for (a) given batch(es)
    batches = [205, 206, 208]
    dic_certified = crm.loc[batches].dic
    alkalinity_certified = crm.loc[batches].alkalinity
```

Nutrient, salinity, bottling date and flag columns are also available in the DataFrame, but the data in the nutrient columns are not yet complete.
