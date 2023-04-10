# Domino-Code-Assistant-Workshop
An introductory workshop to [Domino's Code Assistant](https://dominodatalab.github.io/domino-code-assist-docs/latest/)

### Data Source

[Balancing Mechanism Reporting Service](https://www.bmreports.com/bmrs/?q=help/about-us) is the primary channel for providing operational data relating to the GB Electricity Balancing and Settlement arrangements. It is used extensively by market participants to help make trading decisions and understanding market dynamics and acts as a prompt reporting platform as well as a means of accessing historic data. 

#### In this workshop you will work through an end-to-end workflow to ingest, clean & vizualize data from BMRS:

* Set up Domino Code Assist in your Project & Workspace
* Explore Data Ingest with Code Assist
* Work through pre-built Transforms to your data
* Create plots using pre-built visualizations
* Load and create code snippets for future re-use
* Build an app using Domino Code Assistant 

## Section 1 - Setting Up Domimno Code Assistant (DCA)

### 1.1 Installing Domimno Code Assistant (DCA)

Domino Code Assistant is simply a Python packae or R package running in a Domino Workspace. 

There are four distinct approaches to installing Domino Code Assist (DCA) for either Python or R:

* Install in a Workspace
* Install in a Project
* Install in a Compute Environment or
* Install from Source.

The first approach is the easiest way to get started with DCA. But if you restart you workspace, then you will need to reinstall DCA. The second and third approaches will enable DCA more permanently.

For this lab, we'll use a Compute Environment  with DCA already installed, which will be a Domino Standard Environment for Domino 5.5 or later. To ensure all workspaces have DCA pre-installed, go into the settings tab in your Project. Ensure the compute environment is set to a Domino 5.5+ environment: 

<p align="center">
<img src = readme_images/default_env.png width="800">
</p>

For details on how to install Domino Code Assistant in a Workspace or Project rather than environment, see the [DCA Install Documentation](https://dominodatalab.github.io/domino-code-assist-docs/latest/install/#install-in-a-workspace)

### 1.2 Initializing DCA in a Notebook: Python

Now that we have a default Project environment with DCA pre-installed, create a new workspace.  

In your Project, navigate to the Workspaces tab on the left, and select “Create New Workspace”. Leave the default Hardware Tier and Environment. 

Select the IDE of your choice, and click Launch. The images in this tutorial use JupyterLab, so you may want to select JupyterLab to make it easier to  follow along. 

Once your IDE is started up, craete a new Notebook and rename it "DCA_Tutorial"

<p align="center">
<img src = readme_images/new_workspace.png width="800">
</p>

Then click on the blue Domino Code Assist button on the toolbar to initialize the Code Assistant. 

<p align="center">
<img src = readme_images/DCA_init.png width="800">
</p>

When you hover over the next cell in your Notebook, a blue DCA icon should appear on the left. This is where we’ll access the DCA tools.

<p align="center">
<img src = readme_images/DCA-icon.png width="800">
</p>

### 1.2 Initializing DCA in a Notebook: R Studio

DCA works similarly between Python notebooks and R Notebooks, but the UI is different. 

Create a new Workspace, but choose R Studio as your IDE. 

Once R Studio is up and running, there is no need to initialize DCA, the DCA tools are already available in the Addins menu:

<p align="center">
<img src = readme_images/R_Init.png width="800">
</p>

## Section 2 - Expore Data Ingest

There are many ways to load a dataset into your notebook using Code Assist. To get started, in the DCA Menu, select Load Data from the DCA menu ("DCA Load Data" for R Studio Users): 

<p align="center">
<img src = readme_images/DCA_menu_load_data.png width="800">
</p>




