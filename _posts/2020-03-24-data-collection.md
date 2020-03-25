---
layout: post
title: "data collection"
date: 2020-03-24
---

To employ ML in chemistry and materials science, first we need to gather sufficient amount of training data. A typical ML workflow is shown in this awesome figure below, credit to our senior group member [Ya Zhuo](https://scholar.google.com/citations?user=WacJk1sAAAAJ&hl=en&oi=ao). In this post, we will focus on the first step: **data collection**.

![ML workflow]({{ '/assets/images/ML_workflow.png' | relative_url }})
{: style="width: 300px; max-width: 100%;"}

# data sources

Depend on everyone's specific project, in our group we actually get our data from very different sources. So far, we have mainly two options:

*a. from DFT databases (you will see instructions of how to use these databases later)*

*b. from literature*

In practice, first thing you need to think about is always where to find sufficient amount of training data. For example, I use to work on building ML models to predict the formation energy of a certain composition. In this case, the formation energy data is available in DFT databases such as [Materials Project](https://materialsproject.org/), [AFLOW](http://aflowlib.org/) and [OQMD](http://oqmd.org/) since it can be easily calculated, so I can simply extract the formation energy data following the database's instruction. 

Another situation you will probably encounter is that you are working with more complex properties. For example, in Ya's recent work about [predicting the thermal quenching temperature of phosphors](https://pubs.acs.org/doi/abs/10.1021/acsami.9b16065), the thermal quenching temperature data is not available in the online DFT databases we mentioned above because it can only be measured experimentally. In her case, she extracted all the training data from literature by hand. That can be quite a challenge, but can also make your work unique and insightful.


# how to use Materials Project

We'll start with Materials Project because it is just so easy to work with. 

## First, go to the Materials Project [website](https://materialsproject.org/), and create your account.

![mp-1]({{ '/assets/images/mp_1.png' | relative_url }})
{: style="width: 100px; max-width: 50%;"}

After you have an account and logged in, go to "Dashboard" at the top right corner, and you will be able to see your **API keys**.
API is short for application programming interface, basically it allows third party (like us) to access and operate the database.

## How to use the python API

First, we need to install [pymatgen](https://pymatgen.org/index.html). It is the python library that Materials Project developed for materials analysis. Open the Anaconda Prompt:

![prompt]({{ '/assets/images/prompt.png' | relative_url }})
{: style="width: 300px; max-width: 10%;"}

And then simply type "pip install pymatgen" and hit enter, the installation will start.

After installing pymatgen, open jupyter notebook and create a new notebook.

![ju-1]({{ '/assets/images/jupyter_2.png' | relative_url }})
{: style="width: 300px; max-width: 100%;"}

Always name it before starting to put code in (remember to be organized, don't just leave it as "untitled").

![ju-1]({{ '/assets/images/jupyter_3.png' | relative_url }})
{: style="width: 300px; max-width: 100%;"}

Copy and paste the following code to your notebook, it is an example of how to extract formation energy from the database.

**from pymatgen import MPRester**

**MAPI_KEY = "your API key"**

**m = MPRester(MAPI_KEY)**

**data = m.query(criteria={"formation_energy_per_atom":{"$exists":True}}, properties=["pretty_formula", "formation_energy_per_atom"])**

Put your own API key here with the quotation marks. Then hit "Run" at the top menu bar, the code will start running.

*Tips*: there will be an asterisk mark in front of the code block when it is in progress. That means it's not done yet, wait until the asterisk mark disappear, that's when you're done.

![running code]({{ '/assets/images/running_code.png' | relative_url }})
{: style="width: 300px; max-width: 100%;"}

The code above will extract the composition and formation energy of all compounds in Materials Project. After extraction is done, now we can simply save the data to an excel file and view it. Copy and paste the following code to the next block:

**import pandas as pd**

**df=pd.DataFrame(data)**

**df.to_excel('your file name.xlsx', index=False)**

We haven't officially introduce pandas yet. It is the python library for data analysis, think of it as the excel for python. To install pandas, open your anaconda prompt and type "pip install pandas" and hit enter, very easy.

After installing pandas, you will be able to run the code above, and the excel file will be saved to the same folder where you keep your script. Now you have successfully extracted your first dataset.

## What if I want to extract something else?

You can check what else is available in the Materials Project [API documentation](https://materialsproject.org/docs/api#Resources_2). In this link you can find all the available keyword you can use to extract different materials properties. Explore it.

## More advanced search

You might notice that in the previous example, I extracted *everything* in the database, but in practice what if there are some criterias? In this line:

**data = m.query(criteria={"formation_energy_per_atom":{"$exists":True}}, properties=["pretty_formula", "formation_energy_per_atom"])**

You can see the criteria can be customized. In this example I just put "$exists: True" meaning that I want to extract every compound that have a formation energy value. Sometimes maybe you want only oxides or nitrides. In that case, I cannot provide the specific code solutions for all of your criterias, but I do recommend [a great resource, the MongoDB documentation](https://docs.mongodb.com/manual/reference/operator/query/) where you can look up what query operators you need, and they are all pretty straightforward once you understand the logic. 
