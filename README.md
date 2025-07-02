# Validation Workflow
## Introduction
Docking at its best, is a probabilistic heuristic which gives us a much better chance that the ligands we choose are going to prove to be a hit in the real world than if we were to do it by randomly choosing the ligands for the next stage. By running our docking pipeline for a receptor having a chemical library of known active and inactives derived from in vitro assays, we can get an estimate on how effective the scoring function, choice of hyperparameters, ligand preparation, receptor preparation etc. are at enriching the true actives/positives at the top of our predicted ranked list and to eliminate False Negatives and False Positives.
We do this with the help of a Receiver-Operating Characteristic curve(ROC). The value of the Area Under the ROC curve(AUC score). The AUC score ranges from 0 to 1 and is positively linked with the predictive power of our screening. Where a value of 0.5 means no bettter than random chance, 1 indicative of complete enrichment and 0 showing perfectly negative prediction, most docking workflows have an AUC score of []. 
The reason for choosing the ROC curve for our validation is because AUC values derived from the curve remain more or less unaffected of the ratios of inactives to actives in the testing dataset.

## Steps of the Valdation Workflow
### BindingDB
We want to look for a protein which loosely satisfies the following criteria: 
- Has many experimental data points of `Kd` or `IC50` values for various molecules.
- Has similarity with your essential gene and has the preferrably has the same source organism.

For our purposes, we will choose Beta-Lactamase, a hydrolase 
The rationale behind choosing this protein is evident - IC50 data pertaining to Beta Lactamase sourced from P. Aeruginosa is available with a large library of molecules. P. Aeruginosa is a pathogen of interest to us and is a member of the ESKAPE group of pathogens.
You can download the single 3D SDF file available ahead of it. This single SDF file contains all the molecules inside it with a plethora of meta-data along with just the 3D coordinates and the IC50 values.
> IC50 stands for 
