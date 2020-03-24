---
layout: post
title: "prerequisites"
date: 2020-03-23
---

first, let's install some stuff

## download Python 3.8.2 for windows
Unlike most Unix systems and services, Windows does not include a system supported installation of Python. To make Python available on Windows, first download the installer [here](https://www.python.org/downloads/windows/).

select the "windows x86-64 excecutable installer"

![1]({{ '/assets/images/py_1.png' | relative_url }})
{: style="width: 300px; max-width: 100%;"}

start the installation, and for the "optional features", you can select all of them, pip will be extremely useful since it allows you to easily install other python packages in the future.

![2]({{ '/assets/images/py_2.png' | relative_url }})
{: style="width: 300px; max-width: 100%;"}

then you will see "advanced features", here we don't need to select all of them.

![3]({{ '/assets/images/py_3.png' | relative_url }})
{: style="width: 300px; max-width: 100%;"}

done!

## install anaconda on windows
Anaconda will allow us to easily manage python libraries and perform machine learning on windows. They have very detailed documentation for installation [here](https://docs.anaconda.com/anaconda/install/windows/), just follow this step by step.

After installation, you will be able to lunch anaconda navigator.

![4]({{ '/assets/images/anaconda_1.png' | relative_url }})
{: style="width: 300px; max-width: 100%;"}

and you can open jupyter notebook from here

![5]({{ '/assets/images/anaconda_2.png' | relative_url }})
{: style="width: 300px; max-width: 100%;"}

Alternatively, you can lunch jupyter notebook directly without opening anaconda, simply type "jupyter notebook" in the searching area, and you will be able to see it.

![6]({{ '/assets/images/anaconda_3.png' | relative_url }})
{: style="width: 300px; max-width: 100%;"}

After you click it, you should see this page pops up in your browser.

![7]({{ '/assets/images/jupyter_1.png' | relative_url }})
{: style="width: 300px; max-width: 100%;"}

You can see "Desktop", "Download" folders here, and you should pick a place where you want to save all your machine learning files. It is very important to be organized, my suggestion is create one main folder "ML_yourname" on Desktop or wherever you like, and they build subfolders for different projects from there.

After you create your working folders, you have completed the basic setup.
