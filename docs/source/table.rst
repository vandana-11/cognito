:orphan:


Table
=========


correlation
^^^^^^^^^^^^

.. code-block:: python

		>> table = Table('filename.csv')
		>> table.correlation()
		>> dataframe

convert_to_bin
^^^^^^^^^^^^^^^^

.. code-block:: python

		>> table = Table('filename.csv')
		>> table.convert_to_bin('column_name')
		>> list


binning
^^^^^^^^

.. code-block:: python

		>> table = Table('filename.csv')
		>> table.binningn('column_name', bins)
		>> dataframe


slice
^^^^^^

.. code-block:: python

		>> table = Table('filename.csv')
		>> table.slice([column_names])
		>> dataframe


scale
^^^^^^

covariance
^^^^^^^^^^^

.. code-block:: python

		>> table = Table('filename.csv')

		>> table.scale([column_names],mode)
		>> dataframe

		>> table.covariance()
		>> dataframe


		
