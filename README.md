# Ugly CSV generator
[![Pypi project](https://badge.fury.io/py/ugly-csv-generator.svg)](https://badge.fury.io/py/ugly-csv-generator)
[![Pypi total project downloads](https://pepy.tech/badge/ugly-csv-generator)](https://pepy.tech/projects/ugly-csv-generator)
[![LICENSE](https://img.shields.io/pypi/l/ugly-csv-generator)](https://github.com/LucaCappelletti94/ugly-csv-generator/blob/main/LICENSE)
[![Python version](https://img.shields.io/pypi/pyversions/ugly-csv-generator)](https://img.shields.io/pypi/pyversions/ugly-csv-generator)
[![Github Actions](https://github.com/LucaCappelletti94/ugly_csv_generator/actions/workflows/python.yml/badge.svg)](https://github.com/LucaCappelletti94/ugly_csv_generator/actions/)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/e6fe64db1c9042bbaa4c0a20bde585dc)](https://app.codacy.com/gh/LucaCappelletti94/ugly_csv_generator/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)

Python package to automatically uglify CSVs. Why? To improve the testing capabilities of pipelines that must be able to support strongly malformed input data.

All the malformation automated here are non-destructive, meaning they introduce confusion in the data but do not mangle or destroy information.

**The inspiration for the automated malformation are all from real-life CSVs (sigh)**

Humans will always surprise us with the ever-new malformed input data, but hey, we can try to best ruining the test CSVs!

## How do I install this package?
As usual, just download it using pip:

```shell
pip install ugly_csv_generator
```

## Usage example

To ruin a CSV you can use the following snippet. In the following example we use a [random_csv_generator](https://github.com/LucaCappelletti94/random_csv_generator) to generate a random "healthy" csv.

```python
from random_csv_generator import random_csv
from ugly_csv_generator import uglify

csv = random_csv(5) # CSV with 5 lines
csv = csv[csv.columns[:3]] # We will use only the first 3 columns for this example
ugly = uglify(csv)
```

The initial CSV will look something like:

| region    | province  | surname  |
|-----------|-----------|----------|
| Calabria  | Catanzaro | Rossi    |
| Sicilia   | Ragusa    | Pinna    |
| Lombardia | Varese    | Sbrana   |
| Lazio     | Roma      | Mair     |
| Sicilia   | Messina   | Ferrari  |

The result uglified CSV will look something like this:

|     | 1                                     | 2                   | 3        | 4        | 5                                      | 6    |
|-----|---------------------------------------|---------------------|----------|----------|----------------------------------------|------|
| 0   | ////                                  | #RIF!               | #RIF!    | 0        | ....                                   | 0    |
| 1   | "('surname',)('.',)(0,)"              | region              | province | surname  | "('province',)('_',)(1,)"              |      |
| 2   | ////////                              | region              | "province                                   " | "surname                                   " | 0                                      | 0    |
| 3   | ///////                               | "region                                         " | "province                                   " | "surname                                     " | #RIF!                                   | #RIF!     |
| 4   |                                       | Calabria            | "Catanzaro                                   " | "Rossi                                     " | 0                                      | -------- |
| 5   | "                                     " | Sicilia            | Ragusa   | "Pinna                                     " | "                                            " |          |
| 6   | -------                               |                     | #RIF!    | #RIF!    | 0                                      | "                                        " |
| 7   | /////////                             | "Lombardia                                      " | "Varese                                     " | Sbrana                                  | ///////////                             |          |
| 8   | ---------                             | "Lazio                                         " | "Roma                                       " | "Mair                                       " |                                        |          |
| 9   | --------                              | 0                   | /////    | ---      | 0                                      | ///// |
| 10  | #RIF!                                 | "Sicilia                                     " | Messina  | "Ferrari                                     " | 0                                      |          |
| 11  | 0                                     |                     | -----    | "                                             " | --------                                | 0    |

## Available uglifications
Let's take a look at the available uglifications! All of these options are available as keyword arguments in the `uglify` function.

We start by taking a look at the same example from before, but now we expand all of the available options:

```python
from random_csv_generator import random_csv
from ugly_csv_generator import uglify

csv = random_csv(5) # CSV with 5 lines
csv = csv[csv.columns[:3]] # We will use only the first 3 columns for this example

ugly = uglify(
    csv,
    empty_columns = True,
    empty_rows = True,
    duplicate_schema = True,
    empty_padding = True,
    nan_like_artefacts = True,
    replace_zeros = True,
    replace_ones = True,
    satellite_artefacts = False,
    random_spaces = True,
    include_unicode = True,
    verbose = True,
    seed = 42,
)
```

Let's break down all of the available options with adequate examples. In all cases, we will use the following CSV as a starting point,
obtained from the `random_csv_generator` package:

```python
from random_csv_generator import random_csv

csv = random_csv(5) # CSV with 5 lines
csv = csv[csv.columns[:3]] # We will use only the first 3 columns for this example
```

The initial CSV will look something like:

|   | region  | province   | surname |
|---|---------|------------|---------|
| 0 | Veneto  | Vicenza    | Sacco   |
| 1 | Abruzzo | L' Aquila  | Sala    |
| 2 | Sicilia | Messina    | Sanna   |
| 3 | Marche  | Ancona     | Gallo   |
| 4 | Lazio   | Frosinone  | Gallo   |

### Empty columns
In the following example we will solely add empty columns to the CSV. This phenomenon is common when the data-entry person leaves empty columns in the middle of the table.

```python
from random_csv_generator import random_csv
from ugly_csv_generator import uglify

csv = random_csv(5) # CSV with 5 lines
csv = csv[csv.columns[:3]] # We will use only the first 3 columns for this example
ugly = uglify(
    csv,
    empty_columns = True,
    empty_rows = False,
    duplicate_schema = False,
    empty_padding = False,
    nan_like_artefacts = False,
    satellite_artefacts = False,
    random_spaces = False,
    seed = 424,
)
```

The result will look something like:

|   | region_2 | region_0 1 | region  | region_0 | province   | surname |
|---|----------|------------|---------|----------|------------|---------|
| 0 |          |            | Veneto  |          | Vicenza    | Sacco   |
| 1 |          |            | Abruzzo |          | L Aquila   | Sala    |
| 2 |          |            | Sicilia |          | Messina    | Sanna   |
| 3 |          |            | Marche  |          | Ancona     | Gallo   |
| 4 |          |            | Lazio   |          | Frosinone  | Gallo   |

### Empty rows
In the following example we will solely add empty rows to the CSV. This phenomenon is common when the data-entry person leaves empty rows in the middle of the table.

```python
from random_csv_generator import random_csv
from ugly_csv_generator import uglify

csv = random_csv(5) # CSV with 5 lines
csv = csv[csv.columns[:3]] # We will use only the first 3 columns for this example
ugly = uglify(
    csv,
    empty_columns = False,
    empty_rows = True,
    duplicate_schema = False,
    empty_padding = False,
    nan_like_artefacts = False,
    satellite_artefacts = False,
    random_spaces = False,
    seed = 424,
)
```

The result will look something like:

|   | region  | province   | surname |
|---|---------|------------|---------|
| 0 | Veneto  | Vicenza    | Sacco   |
| 1 | Abruzzo | L Aquila   | Sala    |
| 2 | Sicilia | Messina    | Sanna   |
| 3 |         |            |         |
| 4 | Marche  | Ancona     | Gallo   |
| 5 | Lazio   | Frosinone  | Gallo   |
| 6 |         |            |         |

### Duplicate schema
In the following example we will solely duplicate the schema of the CSV. This phenomenon is common when the data-entry person copies the header of the table multiple times, or several CSVs are concatenated together without removing the header.

```python
from random_csv_generator import random_csv
from ugly_csv_generator import uglify

csv = random_csv(5) # CSV with 5 lines
csv = csv[csv.columns[:3]] # We will use only the first 3 columns for this example
ugly = uglify(
    csv,
    empty_columns = False,
    empty_rows = False,
    duplicate_schema = True,
    empty_padding = False,
    nan_like_artefacts = False,
    satellite_artefacts = False,
    random_spaces = False,
    seed = 424,
)
```

The result will look something like:

|   | region  | province   | surname |
|---|---------|------------|---------|
| 0 | Veneto  | Vicenza    | Sacco   |
| 1 | Abruzzo | L Aquila   | Sala    |
| 2 | Sicilia | Messina    | Sanna   |
| 3 | region  | province   | surname |
| 4 | Marche  | Ancona     | Gallo   |
| 5 | Lazio   | Frosinone  | Gallo   |
| 6 | region  | province   | surname |

### Empty padding
In the following example we will solely add empty padding to the CSV. Padding in this context means adding empty cells around the CSV, represing when the data-entry person started the table somewhere in the middle of a sheet document.

```python
from random_csv_generator import random_csv
from ugly_csv_generator import uglify

csv = random_csv(5) # CSV with 5 lines
csv = csv[csv.columns[:3]] # We will use only the first 3 columns for this example
ugly = uglify(
    csv,
    empty_columns = False,
    empty_rows = False,
    duplicate_schema = False,
    empty_padding = True,
    nan_like_artefacts = False,
    satellite_artefacts = False,
    random_spaces = False,
    seed = 424,
)
```

The result will look something like:

|   |   0 | 1       | 2        | 3       | 4  | 5  |
|---|-----|---------|----------|---------|----|----|
| 0 |     | region  | province | surname |    |    |
| 1 |     | Veneto  | Vicenza  | Sacco   |    |    |
| 2 |     | Abruzzo | L Aquila | Sala    |    |    |
| 3 |     | Sicilia | Messina  | Sanna   |    |    |
| 4 |     | Marche  | Ancona   | Gallo   |    |    |
| 5 |     | Lazio   | Frosinone| Gallo   |    |    |
| 6 |     |         |          |         |    |    |
| 7 |     |         |          |         |    |    |
| 8 |     |         |          |         |    |    |
| 9 |     |         |          |         |    |    |
| 10|     |         |          |         |    |    |
| 11|     |         |          |         |    |    |

### NaN-like artefacts
In the following example we will solely add NaN-like artefacts to the CSV. This phenomenon is common when the data-entry person follows some custom notation, which may be their own or office standard, to represent missing values. In some cases, this may be a string like "N/A", "NaN", "NULL", or even (one or more) "-", "\n", or "\t". Since the objective of this package is to not destroy information, it will solely replace NaN values with NaN-like artefacts.

In the example we considered earlier, we do not have any NaN values, so we will add some to the CSV by also enabling the `empty_rows` option.

```python
from random_csv_generator import random_csv
from ugly_csv_generator import uglify

csv = random_csv(5) # CSV with 5 lines
csv = csv[csv.columns[:3]] # We will use only the first 3 columns for this example
ugly = uglify(
    csv,
    empty_columns = False,
    empty_rows = True,
    duplicate_schema = False,
    empty_padding = False,
    nan_like_artefacts = True,
    satellite_artefacts = False,
    random_spaces = False,
    seed = 424,
)
```

The result will look something like:

|   | region  | province   | surname |
|---|---------|------------|---------|
| 0 | Veneto  | Vicenza    | Sacco   |
| 1 | Abruzzo | L Aquila   | Sala    |
| 2 | Sicilia | Messina    | Sanna   |
| 3 | " "     | ...        | ----    |
| 4 | Marche  | Ancona     | Gallo   |
| 5 | Lazio   | Frosinone  | Gallo   |
| 6 |         | "          | ------- |


#### Unicode variant
The NaN-like artefacts can also be applied with unicode characters. This is useful to test the robustness of the CSV reader to unicode characters.

```python
from random_csv_generator import random_csv
from ugly_csv_generator import uglify

csv = random_csv(5) # CSV with 5 lines
csv = csv[csv.columns[:3]] # We will use only the first 3 columns for this example

ugly = uglify(
    csv,
    empty_columns = False,
    empty_rows = True,
    duplicate_schema = False,
    empty_padding = False,
    nan_like_artefacts = True,
    satellite_artefacts = False,
    random_spaces = False,
    include_unicode = True,
    seed = 424,
)
```

The result will look something like:

|    | region    | province   | surname   |
|---:|:----------|:-----------|:----------|
|  0 | Calabria  | Catanzaro  | Rossi     |
|  1 | Sicilia   | Ragusa     | Pinna     |
|  2 | Lombardia | Varese     | Sbrana    |
|  3 | .         | ᴑ          | 0         |
|  4 | Lazio     | Roma       | Mair      |
|  5 | Sicilia   | Messina    | Ferrari   |
|  6 | ₀         | ________   | ᪐         |

### Replace zeros
In the following example we will solely replace zeros with a custom value. In different places in the word and different offices, zeros may be represented in different ways. Characters for zero from different alphabets, or even different symbols, may be used to represent zero. Note that this latter functionality is only enabled if the `include_unicode` option is set to `True`.

```python
from random_csv_generator import random_csv
from ugly_csv_generator import uglify

csv = random_csv(5) # CSV with 5 lines
csv = csv[csv.columns[:3]] # We will use only the first 3 columns for this example

# We add a column with zeros
csv["zero"] = 0

ugly = uglify(
    csv,
    empty_columns = False,
    empty_rows = False,
    duplicate_schema = False,
    empty_padding = False,
    nan_like_artefacts = False,
    satellite_artefacts = False,
    random_spaces = False,
    replace_zeros = True,
    include_unicode = False,
    seed = 424,
)
```

The result will look something like:

|    | region    | province   | surname   | zero   |
|---:|:----------|:-----------|:----------|:-------|
|  0 | Calabria  | Catanzaro  | Rossi     | 0      |
|  1 | Sicilia   | Ragusa     | Pinna     | o      |
|  2 | Lombardia | Varese     | Sbrana    | 0      |
|  3 | Lazio     | Roma       | Mair      | 0      |
|  4 | Sicilia   | Messina    | Ferrari   | O      |

#### Unicode variant
The replace zeros can also be applied with unicode characters. This is useful to test the robustness of the CSV reader to unicode characters.

```python
from random_csv_generator import random_csv
from ugly_csv_generator import uglify

csv = random_csv(5) # CSV with 5 lines
csv = csv[csv.columns[:3]] # We will use only the first 3 columns for this example

# We add a column with zeros
csv["zero"] = 0

ugly = uglify(
    csv,
    empty_columns = False,
    empty_rows = False,
    duplicate_schema = False,
    empty_padding = False,
    nan_like_artefacts = False,
    satellite_artefacts = False,
    random_spaces = False,
    replace_zeros = True,
    include_unicode = True,
    seed = 424,
)
```

The result will look something like:

|    | region    | province   | surname   | zero   |
|---:|:----------|:-----------|:----------|:-------|
|  0 | Calabria  | Catanzaro  | Rossi     | o      |
|  1 | Sicilia   | Ragusa     | Pinna     | ᪐      |
|  2 | Lombardia | Varese     | Sbrana    | ο      |
|  3 | Lazio     | Roma       | Mair      | 𝟘      |
|  4 | Sicilia   | Messina    | Ferrari   | ᥆      |

### Replace ones
In the following example we will solely replace ones with a custom value. In different places in the word and different offices, ones may be represented in different ways. Characters for one from different alphabets, or even different symbols, may be used to represent one. Note that this latter functionality is only enabled if the `include_unicode` option is set to `True`.

```python
from random_csv_generator import random_csv
from ugly_csv_generator import uglify

csv = random_csv(5) # CSV with 5 lines
csv = csv[csv.columns[:3]] # We will use only the first 3 columns for this example

# We add a column with ones
csv["one"] = 1

ugly = uglify(
    csv,
    empty_columns = False,
    empty_rows = False,
    duplicate_schema = False,
    empty_padding = False,
    nan_like_artefacts = False,
    satellite_artefacts = False,
    random_spaces = False,
    replace_ones = True,
    include_unicode = False,
    seed = 424,
)
```

The result will look something like:

|    | region    | province   | surname   | one   |
|---:|:----------|:-----------|:----------|:------|
|  0 | Calabria  | Catanzaro  | Rossi     | 1     |
|  1 | Sicilia   | Ragusa     | Pinna     | l     |
|  2 | Lombardia | Varese     | Sbrana    | 1     |
|  3 | Lazio     | Roma       | Mair      | 1     |
|  4 | Sicilia   | Messina    | Ferrari   | I     |

#### Unicode variant
The replace ones can also be applied with unicode characters. This is useful to test the robustness of the CSV reader to unicode characters.

```python
from random_csv_generator import random_csv
from ugly_csv_generator import uglify

csv = random_csv(5) # CSV with 5 lines
csv = csv[csv.columns[:3]] # We will use only the first 3 columns for this example

# We add a column with ones
csv["one"] = 1

ugly = uglify(
    csv,
    empty_columns = False,
    empty_rows = False,
    duplicate_schema = False,
    empty_padding = False,
    nan_like_artefacts = False,
    satellite_artefacts = False,
    random_spaces = False,
    replace_ones = True,
    include_unicode = True,
    seed = 424,
)
```

The result will look something like:

|    | region    | province   | surname   | one   |
|---:|:----------|:-----------|:----------|:------|
|  0 | Calabria  | Catanzaro  | Rossi     | ¹     |
|  1 | Sicilia   | Ragusa     | Pinna     | ₁     |
|  2 | Lombardia | Varese     | Sbrana    | l     |
|  3 | Lazio     | Roma       | Mair      | 1     |
|  4 | Sicilia   | Messina    | Ferrari   | ⓵     |


### Satellite artefacts
In the following example we will solely add satellite artefacts to the CSV. A satellite artefact is likely the quirkiest and most annoying artefact to deal with. It represents the situation where the data-entry person adds some notes on the side of the table. A real-world example of this which I have encountered is when the data-entry person adds the office lunch order on the side of the table and forgets to remove it.

The package offers a few satellite artefacts encountered in the wild.

```python
from random_csv_generator import random_csv
from ugly_csv_generator import uglify

csv = random_csv(5) # CSV with 5 lines
csv = csv[csv.columns[:3]] # We will use only the first 3 columns for this example
ugly = uglify(
    csv,
    empty_columns = False,
    empty_rows = True,
    duplicate_schema = False,
    empty_padding = False,
    nan_like_artefacts = False,
    satellite_artefacts = True,
    random_spaces = False,
    seed = 424,
)
```

The result will look something like:

|    | 0       | 1         | 2                | 3       | 4  |
|----|---------|-----------|------------------|---------|----|
| 0  |         |           |                  | random  |    |
| 1  |         |           | random           |         |    |
| 2  |         | caso      |                  |         |    |
| 3  | region  | province  | surname          |         |    |
| 4  | Veneto  | Vicenza   | Sacco            |         |    |
| 5  | Abruzzo | L Aquila  | Sala             |         |    |
| 6  | Sicilia | Messina   | Sanna            |         |    |
| 7  | Marche  | Ancona    | Gallo            |         |    |
| 8  | Lazio   | Frosinone | Gallo            |         |    |
| 9  |         |           |                  |         |    |
| 10 |         |           |                  |         |    |
| 11 |         |           |                  |         |    |
| 12 |         |           |                  |         |    |
| 13 |         |           |                  |         |    |
| 14 |         |           |                  |         |    |
| 15 | person  | food      |                  |         |    |
| 16 | Jerry   | kebab     |                  |         |    |
| 17 | Steven  | rice with paprika |          |         |    |
| 18 | Vale    | pizza mit ananas |          |         |    |

### Random spaces
In the following example we will solely add random spaces around the values in the CSV. This phenomenon is common when the data-entry person is not careful with the spaces around the values in the table and adds some random spaces, for instance to visually align the values.

```python
from random_csv_generator import random_csv
from ugly_csv_generator import uglify

csv = random_csv(5) # CSV with 5 lines
csv = csv[csv.columns[:3]] # We will use only the first 3 columns for this example
ugly = uglify(
    csv,
    empty_columns = False,
    empty_rows = False,
    duplicate_schema = False,
    empty_padding = False,
    nan_like_artefacts = False,
    satellite_artefacts = False,
    random_spaces = True,
    seed = 424,
)
```

The result will look something like:

|   | region               | province         | surname         |
|---|----------------------|------------------|-----------------|
| 0 | "    Veneto          " | "  Vicenza      " | " Sacco        " |
| 1 | " Abruzzo            " | " L Aquila      " | " Sala         " |
| 2 | " Sicilia            " | " Messina       " | " Sanna        " |
| 3 | " Marche             " | " Ancona        " | " Gallo        " |
| 4 | " Lazio              " | " Frosinone     " | " Gallo        " |


#### Unicode variant
The random spaces uglification can also be applied with unicode characters. This is useful to test the robustness of the CSV reader to unicode characters.

```python
from random_csv_generator import random_csv
from ugly_csv_generator import uglify

csv = random_csv(5) # CSV with 5 lines
csv = csv[csv.columns[:3]] # We will use only the first 3 columns for this example
ugly = uglify(
    csv,
    empty_columns = False,
    empty_rows = False,
    duplicate_schema = False,
    empty_padding = False,
    nan_like_artefacts = False,
    satellite_artefacts = False,
    random_spaces = True,
    include_unicode = True,
    seed = 424,
)
```

Due to limitations of the markdown rendering, we cannot show the result here. You can run the code snippet to see the result. It's just that damn cursed!

## Contributing
You have encountered a new type of uglification that you would like to add to the package? You have a suggestion for a new feature or improvement? You have found a bug? Open an issue or a pull request, I will be happy to help you!

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/LucaCappelletti94/ugly_csv_generator/blob/master/LICENSE) file for details.
