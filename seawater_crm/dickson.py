"""Seawater CRMs for dissolved inorganic carbon and total alkalinity prepared by the
laboratory of A.G. Dickson (Scripps Institution of Oceanography).

Functions
---------
get_crm_batches
    Generate a DataFrame containing all CRM batch information.
"""

import numpy as np
import pandas as pd


def _get_batches_raw():
    # Full table copied 26 September 2024
    return [
        [1, "Jan 29, 1990", 33.508, 2020.15, np.nan, "-"],
        [2, "Oct 01, 1990", 33.363, 1978.70, 2248.27, "A"],
        [3, "Jan 08, 1991", np.nan, np.nan, np.nan, "B"],
        [4, "Mar 20, 1991", np.nan, np.nan, np.nan, "B"],
        [5, "May 07, 1991", np.nan, np.nan, np.nan, "B"],
        [6, "May 22, 1991", 38.43, 2304.64, 2375.61, "A,C"],
        [7, "Aug 08, 1991", 37.12, 1926.63, np.nan, "C,D"],
        [8, "Aug 26, 1991", np.nan, np.nan, np.nan, "B"],
        [9, "Sep 20, 1991", np.nan, np.nan, np.nan, "B"],
        [10, "Nov 15, 1991", 34.572, 1960.61, 2257.50, "A"],
        [11, "Jan 07, 1992", 38.50, 2188.89, np.nan, "C,D"],
        [12, "Feb 27, 1992", 33.494, 1984.26, 2226.56, "A"],
        [13, "Jun 25, 1992", 32.864, 2015.13, 2203.79, "A"],
        [14, "Jul 23, 1992", np.nan, np.nan, np.nan, "E"],
        [15, "Nov 30, 1992", 33.199, 2031.65, 2202.38, "A"],
        [16, "Dec 04, 1992", 33.203, 2034.54, 2206.78, "A"],
        [17, "Apr 08, 1993", 33.226, 2044.54, 2219.15, "A"],
        [18, "Sep 10, 1993", 35.298, 2115.15, 2297.77, "A"],
        [19, "Sep 15, 1993", 33.705, 2004.08, np.nan, "D"],
        [20, "Nov 23, 1993", 33.145, 1983.40, 2211.53, "A"],
        [21, "Jan 28, 1994", 34.534, 1991.98, 2258.36, "A"],
        [22, "Apr 01, 1994", 33.561, 1995.19, 2217.16, "A"],
        [23, "May 04, 1994", 33.483, 1993.10, 2212.71, "A"],
        [24, "Aug 26, 1994", 33.264, 1987.53, 2215.51, "A"],
        [25, "Nov 10, 1994", 34.910, 2127.21, 2299.79, "A,F"],
        [26, "Dec 13, 1994", 33.258, 1978.34, 2176.59, "A"],
        [27, "Dec 21, 1994", 33.209, 1988.10, 2214.89, "A"],
        [28, "Feb 27, 1995", 33.407, 1994.64, 2223.47, "A"],
        [29, "Apr 19, 1995", 33.701, 1902.33, 2184.76, "A"],
        [30, "Jun 14, 1995", 33.420, 1988.78, 2201.88, "A"],
        [31, "Aug 16, 1995", 32.899, 1876.57, 2130.33, "A"],
        [32, "Oct 17, 1995", 33.745, 1997.57, 2221.48, "A"],
        [33, "Feb 27, 1996", 33.781, 2009.85, 2234.92, "-"],
        [34, "Apr 23, 1996", 34.514, 2061.52, 2284.35, "-"],
        [35, "Aug 06, 1996", 35.661, 2111.62, 2354.05, "-"],
        [36, "Nov 07, 1996", 35.368, 2050.21, 2283.83, "-"],
        [37, "Apr 02, 1997", 34.983, 2044.15, 2314.11, "-"],
        [38, "May 08, 1997", 34.932, 2089.99, 2300.89, "-"],
        [39, "Jul 24, 1997", np.nan, np.nan, np.nan, "B"],
        [40, "Sep 16, 1997", 33.383, 1985.76, 2196.41, "-"],
        [41, "Oct 31, 1997", 33.368, 1977.71, 2195.78, "-"],
        [42, "Dec 16, 1997", 33.364, 1985.10, 2210.54, "-"],
        [43, "Mar 25, 1998", 33.598, 1988.64, 2202.86, "-"],
        [44, "May 18, 1998", 34.271, 2030.66, 2258.24, "-"],
        [45, "Aug 19, 1998", 33.487, 1994.17, 2204.38, "-"],
        [46, "Oct 27, 1998", 33.769, 1992.92, 2191.27, "-"],
        [47, "Jan 26, 1999", 33.716, 2006.61, 2227.93, "-"],
        [48, "May 14, 1999", 33.442, 1999.91, 2189.62, "G"],
        [49, "Oct 07, 1999", 33.935, 1991.14, 2172.06, "G"],
        [50, "Jan 21, 2000", 33.411, 2006.21, 2211.11, "G"],
        [51, "Jun 08, 2000", 34.217, 2050.28, 2269.86, "G"],
        [52, "Aug 23, 2000", 33.608, 2005.57, 2224.72, "G"],
        [53, "Dec 13, 2000", 33.453, 2012.03, 2222.68, "G"],
        [54, "Apr 20, 2001", 35.228, 2107.35, 2342.09, "G"],
        [55, "May 15, 2001", 33.506, 2012.06, 2227.85, "G"],
        [56, "Sep 14, 2001", 33.408, 2014.16, 2219.69, "G,H"],
        [57, "Nov 29, 2001", 33.485, 2005.98, 2230.33, "G"],
        [58, "Feb 20, 2002", 33.487, 2010.94, 2223.66, "G"],
        [59, "May 3, 2002", 33.316, 2007.10, 2220.98, "G"],
        [60, "Aug 30, 2002", 33.012, 1991.24, 2199.55, "G"],
        [61, "Jun 23, 2003", 33.076, 1998.17, 2202.04, "G"],
        [62, "Aug 21, 2003", 35.224, 2126.46, 2338.20, "G"],
        [63, "Dec 12, 2003", 33.369, 2016.02, 2222.27, "G"],
        [64, "Jan 15, 2004", 37.339, 2090.89, 2427.60, "G"],
        [65, "Feb 20, 2004", 33.049, 1993.68, 2206.00, "G"],
        [66, "Jul 23, 2004", 32.962, 1969.57, 2193.27, "G"],
        [67, "Oct 15, 2004", 34.411, 1983.75, 2258.27, "G"],
        [68, "Dec 10, 2004", 33.758, 2003.78, 2233.71, "G"],
        [69, "Jan 4, 2005", 31.569, 1907.63, 2114.42, "G"],
        [70, "Apr 27, 2005", 33.016, 1989.53, 2160.46, "G"],
        [71, "May 19, 2005", 33.923, 2032.84, 2254.50, "G"],
        [72, "Jul 27, 2005", 35.015, 2091.61, 2312.79, "G"],
        [73, "Nov 17, 2005", 34.523, 2057.30, 2253.50, "G"],
        [74, "Dec 15, 2005", 34.739, 2085.53, 2305.34, "G"],
        [75, "Mar 2, 2006", 33.222, 2005.98, 2210.09, "G"],
        [76, "May 18, 2006", 34.835, 2101.69, 2314.49, "G"],
        [77, "Jul 13, 2006", 33.129, 1998.44, 2199.33, "G"],
        [78, "Sep 21, 2006", 33.285, 1991.93, 2185.57, "G"],
        [79, "Nov 21, 2006", 34.236, 2038.63, 2262.31, "G"],
        [80, "Jan 9, 2007", 33.357, 2006.50, 2214.49, "G"],
        [81, "Apr 26, 2007", 33.378, 2011.49, 2201.20, "G"],
        [82, "Jun 28, 2007", 35.356, 2118.25, 2335.02, "G"],
        [83, "Jul 26, 2007", 34.611, 2055.57, 2286.34, "G"],
        [84, "Sep 6, 2007", 33.391, 2001.23, 2201.01, "G"],
        [85, "Oct 12, 2007", 33.326, 2000.44, 2184.03, "G"],
        [86, "Dec 20, 2007", 33.097, 1998.37, 2175.56, "G"],
        [87, "Apr 15, 2008", 33.191, 2012.01, 2201.16, "G"],
        [88, "Jun 5, 2008", 33.328, 2013.42, 2205.41, "G"],
        [89, "Jul 17, 2008", 33.494, 2025.71, 2214.06, "G"],
        [90, "Sep 5, 2008", 33.390, 1985.61, 2216.00, "G"],
        [91, "Oct 10, 2008", 33.397, 2011.61, 2182.90, "G"],
        [92, "Nov 7, 2008", 33.321, 1996.35, 2201.91, "G"],
        [93, "Dec 18, 2008", 33.615, 2020.34, 2230.06, "G"],
        [94, "Jan 30, 2009", 33.424, 2015.92, 2222.39, "G"],
        [95, "Mar 2, 2009", 33.300, 2016.38, 2217.51, "G"],
        [96, "May 8, 2009", 33.081, 2005.36, 2212.40, "G"],
        [97, "Jun 26, 2009", 33.142, 2003.03, 2211.21, "G"],
        [98, "Aug 31, 2009", 33.366, 2013.85, 2231.11, "G"],
        [99, "Oct 9, 2009", 35.185, 2115.04, 2356.78, "G"],
        [100, "Nov 13, 2009", 33.351, 2021.65, 2232.36, "G"],
        [101, "Jan 15, 2010", 33.590, 2027.80, 2241.44, "G"],
        [102, "Feb 19, 2010", 33.310, 2012.24, 2227.46, "G"],
        [103, "Apr 9, 2010", 33.498, 2023.23, 2232.94, "G"],
        [104, "Jun 11, 2010", 33.300, 2020.10, 2222.61, "G"],
        [105, "Jul 23, 2010", 33.504, 2036.72, 2235.16, "G"],
        [106, "Sep 10, 2010", 33.274, 2004.90, 2219.68, "G"],
        [107, "Oct 8, 2010", 32.985, 1995.12, 2205.17, "G"],
        [108, "Nov 10, 2010", 33.224, 2022.70, 2218.00, "G"],
        [109, "Dec 9, 2010", 33.328, 2026.33, 2224.26, "G"],
        [110, "Jan 14, 2011", 33.418, 2018.28, 2229.04, "G"],
        [111, "Feb 18, 2011", 33.264, 2045.66, 2222.80, "G"],
        [112, "Jun 3, 2011", 33.305, 2011.09, 2223.26, "G"],
        [113, "Jul 8, 2011", 33.357, 2016.68, 2224.65, "G"],
        [114, "Aug 19, 2011", 33.208, 2000.93, 2217.91, "G"],
        [115, "Sep 16, 2011", 33.572, 2007.45, 2242.84, "G"],
        [116, "Oct 14, 2011", 33.451, 2014.18, 2232.76, "G"],
        [117, "Nov 10, 2011", 33.503, 2009.99, 2239.18, "G"],
        [118, "Dec 16, 2011", 33.377, 2013.33, 2229.75, "G"],
        [119, "Jan 20, 2012", 33.263, 2014.78, 2221.24, "G"],
        [120, "Feb 24, 2012", 33.072, 2002.61, 2208.43, "G"],
        [121, "Apr 6, 2012", 33.346, 2039.26, 2225.01, "G"],
        [122, "May 11, 2012", 33.435, 2042.29, 2233.32, "G"],
        [123, "Aug 16, 2012", 33.384, 2022.04, 2225.21, "G"],
        [124, "Oct 12, 2012", 33.190, 2015.72, 2215.08, "G"],
        [125, "Nov 6, 2012", 33.186, 2141.94, 2216.26, "G"],
        [126, "Dec 7, 2012", 33.460, 2007.64, 2232.55, "G"],
        [127, "Jan 18, 2013", 33.424, 2023.30, 2228.64, "G"],
        [128, "Feb 15, 2013", 33.442, 2013.54, 2240.28, "G"],
        [129, "Apr 26, 2013", 33.361, 2016.65, 2237.32, "G"],
        [130, "May 24, 2013", 33.661, 2072.58, 2238.04, "G"],
        [131, "Jun 28, 2013", 33.621, 2028.99, 2241.35, "G"],
        [132, "Jul 26, 2013", 33.441, 2032.65, 2229.24, "G"],
        [133, "Aug 30, 2013", 33.341, 2021.12, 2224.37, "G"],
        [134, "Sep 27, 2013", 33.651, 2026.91, 2236.51, "G"],
        [135, "Nov 1, 2013", 33.561, 2036.96, 2226.33, "G"],
        [136, "Dec 6, 2013", 33.678, 2021.15, 2246.74, "G"],
        [137, "Jan 17, 2014", 33.607, 2031.90, 2231.59, "G"],
        [138, "Feb 21, 2014", 33.398, 2033.98, 2221.75, "G"],
        [139, "Mar 27, 2014", 33.267, 2023.23, 2250.82, "G"],
        [140, "May 2, 2014", 33.471, 2040.94, 2232.58, "G"],
        [141, "Jun 13, 2014", 33.417, 2033.26, 2234.07, "G"],
        [142, "Jul 25, 2014", 33.389, 2038.07, 2227.59, "G"],
        [143, "Aug 29, 2014", 33.620, 2017.75, 2241.04, "G"],
        [144, "Oct 10, 2014", 33.571, 2031.53, 2238.60, "G"],
        [145, "Dec 4, 2014", 33.409, 2034.13, 2226.16, "G"],
        [146, "Jan 30, 2015", 33.122, 2002.92, 2214.11, "G"],
        [147, "Mar 13, 2015", 33.427, 2014.52, 2231.39, "G"],
        [148, "May 1, 2015", 33.624, 2024.12, 2241.13, "G"],
        [149, "Jun 12, 2015", 33.331, 2011.67, 2224.69, "G"],
        [150, "Jul 31, 2015", 33.343, 2017.88, 2214.71, "G"],
        [151, "Sep 4, 2015", 33.345, 2033.83, 2225.56, "G"],
        [152, "Oct 23, 2015", 33.371, 2020.88, 2216.94, "G"],
        [153, "Dec 4, 2015", 33.357, 2017.95, 2225.59, "G"],
        [154, "Jan 22, 2016", 33.347, 2037.68, 2224.30, "G"],
        [155, "Mar 4, 2016", 33.506, 2042.75, 2235.07, "G"],
        [156, "Apr 8, 2016", 33.455, 2052.72, 2236.51, "G"],
        [157, "May 20, 2016", 33.463, 2049.43, 2229.82, "G"],
        [158, "Jun 17, 2016", 33.516, 2043.54, 2226.55, "G"],
        [159, "Jul 22, 2016", 33.572, 2027.14, 2213.59, "G"],
        [160, "Sep 9, 2016", 33.414, 2030.39, 2212.44, "G"],
        [161, "Oct 14, 2016", 33.356, 2037.38, 2207.33, "G"],
        [162, "Nov 18, 2016", 33.312, 2177.27, 2403.72, "G"],
        [163, "Jan 13, 2017", 33.362, 2039.43, 2215.34, "G"],
        [164, "Feb 17, 2017", 33.247, 2238.89, 2309.32, "G"],
        [165, "Apr 14, 2017", 33.329, 2064.41, 2214.09, "G"],
        [166, "May 12, 2017", 33.477, 2053.48, 2212.56, "G"],
        [168, "Jun 30, 2017", 33.481, 2071.47, 2207.62, "G"],
        [169, "Aug 4, 2017", 33.518, 2063.31, 2207.03, "G"],
        [170, "Sep 8, 2017", 33.573, 1982.42, 2198.77, "G"],
        [171, "Oct 13, 2017", 33.434, 2029.19, 2217.40, "G"],
        [172, "Nov 17, 2017", 33.450, 2038.99, 2217.40, "G"],
        [173, "Dec 8, 2017", 33.414, 2042.41, 2210.77, "G"],
        [174, "Jan 26, 2018", 33.408, 2050.56, 2212.23, "G"],
        [175, "Mar 16, 2018", 33.458, 2067.06, 2224.53, "G"],
        [176, "May 4, 2018", 33.532, 2024.22, 2226.38, "G"],
        [177, "Jun 15, 2018", 33.641, 2067.67, 2223.89, "G"],
        [178, "Jul 20, 2018", 33.782, 1952.65, 2216.53, "G"],
        [179, "Sep 7, 2018", 33.841, 1941.92, 2219.26, "G"],
        [180, "Oct 19, 2018", 33.623, 2021.87, 2224.47, "G"],
        [181, "Dec 14, 2018", 33.582, 2030.77, 2222.71, "G"],
        [182, "Jan 25, 2019", 33.465, 2039.10, 2230.91, "G"],
        [183, "Mar 1, 2019", 33.420, 2040.25, 2230.52, "G"],
        [184, "Apr 12, 2019", 33.290, 2052.75, 2226.44, "G"],
        [185, "May 24, 2019", 33.418, 2029.88, 2220.67, "G"],
        [186, "Jun 28, 2019", 33.525, 2012.59, 2212.00, "G"],
        [187, "Aug 2, 2019", 33.602, 2002.85, 2204.98, "G"],
        [188, "Sep 27, 2019", 33.595, 2099.26, 2264.96, "G"],
        [189, "Nov 1, 2019", 33.494, 2009.48, 2205.26, "G"],
        [190, "Dec 20, 2019", 33.459, 2033.86, 2218.31, "G"],
        [191, "Feb 14, 2020", 33.316, 2051.40, 2225.50, "G"],
        [192, "Jan 14, 2021", 33.518, 2070.83, 2213.68, "G"],
        [193, "Feb 24, 2021", 33.425, 2048.36, 2193.07, "G"],
        [194, "Mar 24, 2021", 33.361, 2025.17, 2169.83, "G"],
        [195, "Apr 22, 2021", 33.485, 2024.96, 2213.51, "G"],
        [196, "May 20, 2021", 33.519, 2018.83, 2215.32, "G"],
        [197, "Jun 18, 2021", 33.529, 2115.23, 2256.77, "G"],
        [198, "Jul 5, 2021", 33.504, 2033.64, 2200.67, "G"],
        [199, "Oct 24, 2021", 33.473, 2021.66, 2202.75, "G"],
        [200, "Dec 2, 2021", 33.464, 2022.46, 2186.43, "G"],
        [201, "Jan 28, 2022", 33.302, 2048.19, 2207.56, "G"],
        [202, "Mar 18, 2022", 33.356, 2043.33, 2215.13, "G"],
        [203, "May 20, 2022", 33.464, 2029.92, 2214.54, "G"],
        [204, "Jul 22, 2022", 33.494, 2028.23, 2202.12, "G"],
        [205, "Sep 9, 2022", 33.443, 2011.85, 2202.05, "G"],
        [206, "Nov 22, 2022", 33.423, 2021.55, 2193.88, "G"],
        [207, "Jan 13, 2023", 33.237, 2040.33, 2199.32, "G"],
        [208, "Feb 24, 2023", 33.140, 2059.66, 2215.76, "G"],
        [209, "Apr 7, 2023", 33.147, 2060.05, 2210.40, "G"],
        [210, "May 19, 2023", 33.231, 2046.37, 2220.62, "G"],
        [211, "Jun 6, 2023", 33.272, 2057.02, 2218.40, "G"],
        [212, "Aug 10, 2023", 33.341, 2023.82, 2193.54, "G"],
        [213, "Sep 22, 2023", 33.232, 2024.67, 2203.56, "G"],
        [214, "Dec 01, 2023", 33.075, 2014.53, 2200.67, "G"],
        [215, "Feb 16, 2024", 32.942, 2024.29, 2191.30, "G"],
        [216, "Mar 22, 2024", 32.899, 2029.63, 2188.02, "G"],
    ]


def _get_nutrients_raw():
    # Column order: batch, phosphate, silicate, nitrite, nitrate
    return [
        [205, 0.4, 2.3, 0.09, 3.2],
        # TODO add values for other batches!
        # (These aren't nicely tabulated on the website)
    ]


def get_crm_batches():
    """Generate a DataFrame containing all CRM batch information.

    The data were most recently obtained from
    https://www.ncei.noaa.gov/access/ocean-carbon-acidification-data-system/oceans/Dickson_CRM/batches.html
    on 26 September 2024.

    The nutrient columns are incomplete; more values will be added in future updates.

    Returns
    -------
    batches : pd.DataFrame
        The certified values for the different variables and auxiliary information.
        The integer batch number is the DataFrame's index.
        The columns are
            date : datetime
                The bottling date.
            salinity : float
                Practical salinity (dimensionless).
            dic : float
                Dissolved inorganic carbon in µmol/kg-sw.
            alkalinity : float
                Total alkalinity in µmol/kg-sw.
            total_phosphate : float
                Total phosphate in µmol/kg-sw.
            total_silicate : float
                Total silicate in µmol/kg-sw.
            nitrite : float
                Nitrite in µmol/kg-sw.
            nitrate : float
                Nitrate in µmol/kg-sw.
            flag : str
                The 'NB' column from the data website, with values:
                    (A) Total alkalinity was not measured when the batch was originally
                        certified; the total alkalinity value is based on measurements
                        performed on archived samples of the batch.
                    (B) The measured values of total dissolved inorganic carbon and of
                        total alkalinity changed with time, probably due to the effects
                        of microbial growth in the bottles. This batch was not
                        certified as reference materials.
                    (C) This batch was a synthetic solution of sodium bicarbonate in
                        sodium chloride prepared directly in the holding tank by
                        diluting concentrated, filtered solutions of the two salts with
                        deionized (Milli-Q®) water. The salinity value was assigned so
                        as to allow the correct density at 20oC to be calculated using
                        the density-salinity relationship for sea water.
                    (D) Total alkalinity was not measured as archived samples were not
                        available; value is expected to have been stable.
                    (E) This batch was used as a basis of a collaborative study for the
                        analysis of total dissolved inorganic carbon by coulometry.
                    (F) This batch was prepared in England by using North Atlantic near
                        surface water. All analyses were performed, as with all
                        previous batches, in the laboratories of Andrew G. Dickson and
                        Charles D. Keeling.
                    (G) This batch was certified for total dissolved inorganic carbon
                        using a Ruska electronic constant-volume manometer rather than
                        the mercury column manometer for Batches 1 - 47.
                    (H) This batch was used in a collaborative study involving the
                        analysis of CO2 in air from glass ampoules.
    """
    batches_raw = _get_batches_raw()
    nutrients_raw = _get_nutrients_raw()
    batches = pd.DataFrame(
        [
            pd.Series(
                {
                    v: row[i]
                    for i, v in enumerate(
                        [
                            "batch",
                            "date",
                            "salinity",
                            "dic",
                            "alkalinity",
                            "flag",
                        ]
                    )
                }
            )
            for row in batches_raw
        ]
    ).set_index("batch")
    batches["date"] = pd.to_datetime(batches.date, format="%b %d, %Y")
    # Append nutrients
    nutrients_raw = pd.DataFrame(
        [
            pd.Series(
                {
                    v: row[i]
                    for i, v in enumerate(
                        [
                            "batch",
                            "total_phosphate",
                            "total_silicate",
                            "nitrite",
                            "nitrate",
                        ]
                    )
                }
            )
            for row in nutrients_raw
        ]
    ).set_index("batch")
    for c in nutrients_raw.columns:
        batches[c] = nutrients_raw[c]
    # Reorder columns
    batches = batches[
        [
            "date",
            "salinity",
            "dic",
            "alkalinity",
            "total_phosphate",
            "total_silicate",
            "nitrite",
            "nitrate",
            "flag",
        ]
    ]
    return batches
