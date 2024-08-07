# Charts-DL-SS2024

To try scripts in this repository in is necessary to install dependencies at first:

```bash
pip install -r requirements.txt
```

### Introduction

Repository can be described in 5 components: data gathering, data processing, prompt generation, prompt validation, final dataset.

### Data gathering

Data was collected from kaggle.com datasets and scraped from different sources. Code related to different datasets and sources placed in **/data** directory seperated inside. For each dataset there is code that reads, transforms/preprocesses, saves to output file in this folder.

### Data preprocessing
This part includes transforming initial 
dataset to meet our needs and make it representative for charts.

### Prompt generation
This step includes using **"microsoft/Phi-3-mini-128k-instruct"** model from 
huggingface.co. 
Basically flow looks like: composing default prompt for data instance by script -> ask the model to paraphrase it -> save it.
This code can be found in **/prompt_generator.ipynb** notebook.
Alternatively there is the **/prompt_generator_templates.ipynb** notebook which contains code that can be used to create prompts based on string templates.

### Prompt validation
A couple of functions were prepared for validation. Basically, these functions check for the presence of labels and values in the prompt and correct order of them.
Code related to validation can be found in **/validate.py** file.

### Final dataset
Final dataset with 1391 data rows with generated prompts is saved in **/final_validated.csv** file.

Columns definitions:
- **Data in JSON** - chart config in json format that we used in statistics, validations etc.
- **Chart in Natural language** - prompt generated by scripts
- **chart.js** - chart config which can be used immediately in chart.js library
- **LLM Generated** - prompt generated in Phi-3
- **LLM generated is valid** - boolean identifying whether Phi-3 generated prompt is valid or not. (validated by our own implemented validator functions)
