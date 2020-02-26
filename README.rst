ugly_csv_generator
=========================================================================================
|travis| |sonar_quality| |sonar_maintainability| |codacy|
|code_climate_maintainability| |pip| |downloads|

Python package to automatically uglify CSVs. Why?
To improve the testing capabilities of pipelines that
must be able to support strongly malformed input data.

All the malformation automated here are non-destructive,
meaning they introduce confusion in the data but do not
any information.

**The inspiration for the automated malformation are
all from real-life CSVs (sigh)**

Humans will always surprise us with the ever-new
malformed input data, but hey, we can try to best
ruining the test CSVs!

How do I install this package?
----------------------------------------------
As usual, just download it using pip:

.. code:: shell

    pip install ugly_csv_generator

Tests Coverage
----------------------------------------------
Since some software handling coverages sometime
get slightly different results, here's three of them:

|coveralls| |sonar_coverage| |code_climate_coverage|

Python package to generate ugly real-looking csvs.

Usage example
-----------------------------------
To ruin a CSV you can use the following snippet.
In the following example we use a tool to generate
a random sanitized csv.

.. code:: Python

    from random_csv_generator import random_csv
    from ugly_csv_generator import uglify

    csv = random_csv(5) # CSV with 5 lines
    csv = csv[csv.columns[:3]] # We will use only the first 3 columns for this example
    ugly = uglify(csv)

The initial CSV will look something like:

+----------------+---------------+-----------+
| region         | province      | surname   |
+================+===============+===========+
| Puglia         | Lecce         | Righetti  |
+----------------+---------------+-----------+
| Campania       | Napoli        | Govoni    |
+----------------+---------------+-----------+
| Emilia Romagna | Reggio Emilia | Vichi     |
+----------------+---------------+-----------+
| Lombardia      | Lecco         | Costa     |
+----------------+---------------+-----------+
| Umbria         | Perugia       | Fabbro    |
+----------------+---------------+-----------+

The result uglified CSV will look something like this:

+----------+----------------+----------+---------------+----------+-----+
| 0        | 1              | 2        | 3             | 4        |   5 |
+==========+================+==========+===============+==========+=====+
| nan      | nan            | nan      | nan           | nan      | nan |
+----------+----------------+----------+---------------+----------+-----+
| region-1 | region         | region 0 | province      | surname  | nan |
+----------+----------------+----------+---------------+----------+-----+
| nan      | nan            | nan      | nan           | nan      | nan |
+----------+----------------+----------+---------------+----------+-----+
| nan      | nan            | nan      | nan           | nan      | nan |
+----------+----------------+----------+---------------+----------+-----+
| nan      | nan            | nan      | nan           | nan      | nan |
+----------+----------------+----------+---------------+----------+-----+
| nan      | region         | nan      | province      | surname  | nan |
+----------+----------------+----------+---------------+----------+-----+
| nan      | region         | nan      | province      | surname  | nan |
+----------+----------------+----------+---------------+----------+-----+
| nan      | Puglia         | nan      | Lecce         | Righetti | nan |
+----------+----------------+----------+---------------+----------+-----+
| nan      | Campania       | nan      | Napoli        | Govoni   | nan |
+----------+----------------+----------+---------------+----------+-----+
| nan      | Emilia Romagna | nan      | Reggio Emilia | Vichi    | nan |
+----------+----------------+----------+---------------+----------+-----+
| nan      | Lombardia      | nan      | Lecco         | Costa    | nan |
+----------+----------------+----------+---------------+----------+-----+
| nan      | Umbria         | nan      | Perugia       | Fabbro   | nan |
+----------+----------------+----------+---------------+----------+-----+
| nan      | nan            | nan      | nan           | nan      | nan |
+----------+----------------+----------+---------------+----------+-----+
| nan      | nan            | nan      | nan           | nan      | nan |
+----------+----------------+----------+---------------+----------+-----+

The uglify method offers numerous keyword parameters,
since the library is currently in quick evolution
if you are interested in them just check out the
code documentation.


.. |travis| image:: https://travis-ci.org/LucaCappelletti94/ugly_csv_generator.png
   :target: https://travis-ci.org/LucaCappelletti94/ugly_csv_generator
   :alt: Travis CI build

.. |sonar_quality| image:: https://sonarcloud.io/api/project_badges/measure?project=LucaCappelletti94_ugly_csv_generator&metric=alert_status
    :target: https://sonarcloud.io/dashboard/index/LucaCappelletti94_ugly_csv_generator
    :alt: SonarCloud Quality

.. |sonar_maintainability| image:: https://sonarcloud.io/api/project_badges/measure?project=LucaCappelletti94_ugly_csv_generator&metric=sqale_rating
    :target: https://sonarcloud.io/dashboard/index/LucaCappelletti94_ugly_csv_generator
    :alt: SonarCloud Maintainability

.. |sonar_coverage| image:: https://sonarcloud.io/api/project_badges/measure?project=LucaCappelletti94_ugly_csv_generator&metric=coverage
    :target: https://sonarcloud.io/dashboard/index/LucaCappelletti94_ugly_csv_generator
    :alt: SonarCloud Coverage

.. |coveralls| image:: https://coveralls.io/repos/github/LucaCappelletti94/ugly_csv_generator/badge.svg?branch=master
    :target: https://coveralls.io/github/LucaCappelletti94/ugly_csv_generator?branch=master
    :alt: Coveralls Coverage

.. |pip| image:: https://badge.fury.io/py/ugly-csv-generator.svg
    :target: https://badge.fury.io/py/ugly-csv-generator
    :alt: Pypi project

.. |downloads| image:: https://pepy.tech/badge/ugly-csv-generator
    :target: https://pepy.tech/badge/ugly-csv-generator
    :alt: Pypi total project downloads

.. |codacy| image:: https://api.codacy.com/project/badge/Grade/8fc44d07742a47c1b77123b532f6f264
    :target: https://www.codacy.com/manual/LucaCappelletti94/ugly_csv_generator?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=LucaCappelletti94/ugly_csv_generator&amp;utm_campaign=Badge_Grade
    :alt: Codacy Maintainability

.. |code_climate_maintainability| image:: https://api.codeclimate.com/v1/badges/43f6565c8e36fd609252/maintainability
    :target: https://codeclimate.com/github/LucaCappelletti94/ugly_csv_generator/maintainability
    :alt: Maintainability

.. |code_climate_coverage| image:: https://api.codeclimate.com/v1/badges/43f6565c8e36fd609252/test_coverage
    :target: https://codeclimate.com/github/LucaCappelletti94/ugly_csv_generator/test_coverage
    :alt: Code Climate Coverate
