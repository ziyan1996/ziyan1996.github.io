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

Basic elemental properties can be used to develop compositional descriptors (*e.g.*, atomic numbers, electronegativity, et al. forming muti-dimensional vectors). To produce a set of compositional descriptors for a given composition, see the following steps:

First, download three files [here](https://github.com/ziyan1996/ziyan1996.github.io/tree/master/scripts%20and%20files), comp_descriptors.ipynb, MSE_ML_functionMod1.py and elementsnew.xlsx, place them in the same folder.

Then open comp_descriptors.ipynb in your jupyter notebook, follow each code block, you will be able to generate compositional descriptors for your compounds.

## structural descriptors

There are two ways to incorporate structural information in descriptors. First is you can use properties like space group numbers, lattice parameters as descriptors, similar as compositional descriptors mentioned above. The other ways is use crystal structures completely, use the cif files as data representation.

The first approach requires gathering related information and form them into muti-dimentional vectors same as compositional descriptors, and the second approach is a bit more tricky because reading cif files is not as straightforward as constructing a data frame that simply contain numerous structural informations.

[Crystal Graph Convolutional Neutal Network](https://github.com/txie-93/cgcnn)
