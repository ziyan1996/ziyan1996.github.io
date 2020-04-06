---
layout: post
title: "data-representation"
date: 2020-04-06
---

## Fact: computers can not read chemical compositions like us

For example, we know Ca is calsium but it doesn't make any sense to computers. That's why in chemistry and materials science, researchers made a lot of effort in developing data representations for compounds that carry useful chemistry informations. There are several aspects of how we can develope representations for compounds:

*based on compositions*

*based on crystal structures*

*based on domain knowledge (this is where it gets very creative I guess)*

## compositional descriptors

Basic elemental properties can be used to develop compositional descriptors (*e.g.*, atomic numbers, electronegativity). To produce a set of compositional descriptors for a given composition, see the following steps:

First, download three files [here](https://github.com/ziyan1996/ziyan1996.github.io/tree/master/scripts%20and%20files), comp_descriptors.ipynb, MSE_ML_functionMod1.py and elementsnew.xlsx, place them in the same folder.

Then open comp_descriptors.ipynb in your jupyter notebook, follow each code block, you will be able to generate compositional descriptors for your compounds.
