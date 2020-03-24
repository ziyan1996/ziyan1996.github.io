---
layout: post
title: "data extraction"
date: 2020-03-24
---

To employ ML in chemistry and materials science, first we need to gather sufficient amount of training data. A typical ML workflow is shown in this awesome figure below, credit to our senior group member [Ya Zhuo](https://scholar.google.com/citations?user=WacJk1sAAAAJ&hl=en&oi=ao). In this post, we will focus on the first step: **data extraction**.

![ML workflow]({{ '/assets/images/ML_workflow.png' | relative_url }})
{: style="width: 300px; max-width: 100%;"}

# data sources



## materials project API

Materials Project is a DFT database that is easy to access. 

1. sign in with your account, get api key
2. example: extract formation energy data
3. be familiar with api documentation: what other properties are available
`(api keys)`
> blockquote
