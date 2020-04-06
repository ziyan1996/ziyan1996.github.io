---
layout: post
title: "matminer data retrieval"
date: 2020-04-03
---

## Data collection from other DFT databases

When I want to extract data from OQMD or AFLOW databases, I often use [matminer](https://hackingmaterials.lbl.gov/matminer/). This is a Python library developed for data mining the properties of materials, also include automated featurization. In this post I will only introduce how to use their data retrieval tools, if you are interested in their other functions, please check the documentation.

The installation of matminer:

![matminer install]({{ '/assets/images/matminer_1.png' | relative_url }})
{: style="width: 300px; max-width: 100%;"}

Example 1: extract formation energy from OQMD

**from matminer.data_retrieval.retrieve_MDF import MDFDataRetrieval**
**mdf=MDFDataRetrieval(anonymous=True)**
**query_string='mdf.source_name:oqmd AND (oqmd.configuration:static OR oqmd.configuration:standard) AND dft.converged:True'**
**data_oqmd=mdf.get_data(query_string, unwind_arrays=False)**

Example 2: extract formation energy from AFLOW

**from matminer.data_retrieval.retrieve_AFLOW import AFLOWDataRetrieval**
**mdf=AFLOWDataRetrieval()**
**data=mdf.get_dataframe(criteria={"energy_atom":{"$lt":0}}, properties=["energy_atom", "compound"])**

You can see matminer is very convinient for data retrieval, and you can check the database's documentation to see what other properties you can extract.
