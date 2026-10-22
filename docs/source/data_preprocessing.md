# Data preprocessing pipeline

All derivatives of data

## fmriprep
Input : raw data

algoritms and settings

>[!note] QA
>- Carpet plot
> - Movement timseries and assess trials/runs
> - FD treshold 

link annexe of the fmriprep text report (automated method description with all the method and references)


## Tedana
input : fmriprep

- Correlation with physiological measures? (PPG)
- make sure the removed component were inspected

- see tedana_call.sh for the exact command line ran

## GLM

input : Tedana (?)


## Physprep

Parameters + preprocessing steps

codebase + scripts : link



## EEG pipeline


## Temporal signal to noise ration (tSNR)

compare fmriprep, tedana-optimally-combined, tedana-denoise-opt-com

Codebase from [link ds_prep neuromod]

As part of pilot testing, we systematically computed tSNR across runs, to compare the effect of MRI parameters on data.

tSNR code can be found at `