---
layout: post
title: "data extraction"
date: 2020-03-24
---

To employ ML in chemistry and materials science, first we need to gather sufficient amount of training data. A typical ML workflow is shown in this awesome figure below, credit to our senior group member [Ya Zhuo](https://scholar.google.com/citations?user=WacJk1sAAAAJ&hl=en&oi=ao). In this post, we will focus on the first step: **data extraction**.

![ML workflow]({{ '/assets/images/ML_workflow.png' | relative_url }})
{: style="width: 300px; max-width: 100%;"}

## data sources

Depend on everyone's specific project, in our group we actually get our data from very different sources. So far, we have mainly two options:

- from DFT databases (you will see instructions of how to use these databases later)
- from literature

In practice, first thing you need to think about is always where to find sufficient amount of training data. For example, I use to work on building ML models to predict the formation energy of a certain composition. In this case, the formation energy data is available in DFT databases such as [Materials Project](https://materialsproject.org/), [AFLOW](http://aflowlib.org/) and [OQMD](http://oqmd.org/) since it can be easily calculated, so I can simply extract the formation energy data following the database's instruction. 

Another situation you will probably encounter is that you are working with more complex properties. For example, in Ya's recent work about [predicting the thermal quenching temperature of phosphors](https://pubs.acs.org/doi/abs/10.1021/acsami.9b16065), the thermal quenching temperature data is not available in the online DFT databases we mentioned above because it can only be measured experimentally. In her case, she extracted all the training data from literature by hand. That can be quite a challenge, but can also make your work unique and insightful.


## how to use Materials Project

We'll start with Materials Project because it is just so easy to work with. 

- First, go to the Materials Project [website](https://materialsproject.org/), and create your account.

![mp-1]({{ '/assets/images/mp_1.png' | relative_url }})
{: style="width: 100px; max-width: 50%;"}

After you have an account and logged in, go to "Dashboard" at the top right corner, and you will be able to see your **API keys**.
API is short for application programming interface, basically it allows third party (like us) to access and operate the database.

- How to use the python API

Open jupyter notebook and create a new notebook.

![ju-1]({{ '/assets/images/jupyter_2.png' | relative_url }})
{: style="width: 300px; max-width: 100%;"}

Always name it before starting to put code in (remember to be organized, don't just leave it as "untitled").

![ju-1]({{ '/assets/images/jupyter_3.png' | relative_url }})
{: style="width: 300px; max-width: 100%;"}

Copy and paste the following code to your notebook
`from pymatgen import MPRester
MAPI_KEY = "your api key"
m = MPRester(MAPI_KEY)
data = m.query(criteria={"formation_energy_per_atom":{"$exists":True}}, properties=["pretty_formula", "formation_energy_per_atom"])`


3. be familiar with api documentation: what other properties are available

> blockquote
