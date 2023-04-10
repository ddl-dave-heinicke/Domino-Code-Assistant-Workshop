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

## Section 1 - Setting Up Domimno Code Assistant

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

For details on how to install Domino Code Assistant in a Workspace or Project rather than environment, see the [DCA Documentation](https://dominodatalab.github.io/domino-code-assist-docs/latest/install/#install-in-a-workspace)