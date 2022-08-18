

![Austin Animals](https://firehouseroundrock.com/client-logo/austin-animal-center/)




# <a name="top"></a>Individual_Project_Austin_Animals

### Saving our Austin Animals
by: Glady Barrios

<p>
  <a href="https://github.com/GladyBarrios" target="_blank">
    <img alt="Glady" src="https://img.shields.io/github/followers/GladyBarrios?label=Follow_Glady&style=social" />
  </a>
</p>


***
[[Project Description](#project_description)]
[[Project Planning](#planning)]
[[Key Findings](#findings)]
[[Data Dictionary](#dictionary)]
[[Data Acquire and Prep](#wrangle)]
[[Data Exploration](#explore)]
[[Statistical Analysis](#stats)]
[[Modeling](#model)]
[[Conclusion](#conclusion)]
___

<img src="https://docs.google.com/drawings/d/e/2PACX-1vR19fsVfxHvzjrp0kSMlzHlmyU0oeTTAcnTUT9dNe4wAEXv_2WJNViUa9qzjkvcpvkFeUCyatccINde/pub?w=1389&amp;h=410">

## <a name="project_description"></a>Project Description:
[[Back to top](#top)]


There are sevral diffrent attributes as to why our animals get euthanized, using this dataset from the City of Austin website we will explore the diffrent attributes and use our best model to predict weather an animals certain characteristics will lead them to be euthanized. The attributes we will be exploring are the animals, age, sex, type of animal and year the animal was released.***


## <a name="planning"></a>Project Planning: 
[[Back to top](#top)]

### Project Outline:
Checking the database 

        
### Initial Questions 

- what sex of animals is more likely to get euthanasia?
- what animal type is more likely to get euthinized?
- Does the age of the animal determine the euthinization?
- Is there some sort of relationship between animal color and Euthinization? 
- Is there some sort of relationship between animal Breed and Euthinization? 

### Target variable
 Use a Macine learning Classsification model to be able to predict the diffrent freatues of the animals coming into the center and deternmine euthanization 

### Need to haves (Deliverables):
Need to have acces to jupyter notebook and all of the imoprtant libraries such as
-numpy
-pandas
-matplotlib
-seaborn 
 more information in final notebook 
 
Need to dowload this  csv from website [https://dev.socrata.com/foundry/data.austintexas.gov/9t4d-g238]

Austin_Animal_Center_Outcomes.csv

### Nice to haves (With more time):
 - Due to time crunch i would love to explore the variables of "breed" and "Color", since they are so many categories of the variables this would take some time to sift through 


***

## <a name="findings"></a>Key Findings:
[[Back to top](#top)]

- A few of the biggest drivers of euthanization is age, sex, and animal_type


***

## <a name="dictionary"></a>Data Dictionary  
[[Back to top](#top)]

### Data Used
	
  
---
| Attribute | Definition | Data Type |
| ----- | ----- | ----- |
|MonthYear| Month and year the animal was reeased| datetime64|
|DOB	|Date of birth of the animal| datetime64|
|outcome  | What was the outcome of the animal leaving the center | object|
|animal_type |What is the type of animal, dog, cat, other |object|
|Age_upon_out | Age as the animal leaves the center|timedelta64 |
|days_old |The age of the animals in days|int64|

***

## <a name="wrangle"></a>Data Acquisition and Preparation
[[Back to top](#top)]

### Aquire steps:

aquird the data from City of austin public databases dowloadable .csv file 

 
### Wrangle steps: 

- changin the collumn name so that it would be easier to run data such as ('date of birth, to DOB)

-  there are some nulls in the name collumn so i changed it to "no_name" 
- Since the collumn "subtype" has many nuls i decided to drop the whole collumn 
- Then some collumns still had a few nulls i ddecied to drop the nulls and still had a large enough dataset 
- when looking at age_upon_outcome there are some years that are negative, I belive this is a mistake and I decided to replace it with a positive 
- created a few collumns 'year_born', 'current_age','age_bin'(this will bin the age into difffrent categories),'year_released','age_out_years'(this is the age upon outcome in just years),'age_upon_out'(age upon outcome in days and time),'days_old' 
- Created dummy varables for collumns, outcome, animal_type, sex.

*********************

## <a name="explore"></a>Data Exploration:
[[Back to top](#top)]
- Python files used for exploration:
    - prepare.py 

### Questions and Takeaways:

Question 1- Is there a relationship between animal_type and Euthanization?

- looking at the visualization looks there is a relationship with the animal_type and Euthinasia
- The animal type category `other` has the most animals being euthinzed, the second largest animal set is cats and lastly dog
- The statistical test also shows that there is a relationship between animal type and euthinasia

Question 2- What sex of animals is more likely to get euthinized?

- concluding from the statistical test and the visualization we can see that there is a relationship between the animals sex and euthinization 
- from the visualization and looking at the numbers we can see that intact male and femailes are more lilky to get euthinized than a nutered male or female
- an unknown sex is more likely able to get euthanized than any other category

Question 3- At what age are animals more likely to get euthanized ?

- to look at the visualization we can see that the majority of animals that are leading to be euthinized are animals that are one year old
- the statistical test will show that the ages from the animals that are euthinized are not equal to the number of the animalsa are not euthinized 

Question 4 - Is there some sort of relationship between color and Euthinization 

- to look at the visualization we can see that the majority of animals that are leading to be euthinized are animals that are one year old
- the statistical test will show that the ages from the animals that are euthinized are not equal to the number of the animalsa are not euthinized 

Question 5 - Is there some relationship between color and Euthinization

- from running the statistical test we can see that there is a relationship between animal type and Euthanasia
 
***

## <a name="model"></a>Modeling:
[[Back to top](#top)]

### Model Preparation:

### Baseline
    
- Baseline Results: 
    93% accuracy 

- Selected features to input into models:
    - features = [year_born,	year_released,	days_old,	animal_type_Bird,	animal_type_Cat,	animal_type_Dog,	animal_type_Livestock,	animal_type_Other,	sex_Intact Female,	sex_Intact Male,	sex_Neutered Male,	sex_Spayed Female,	sex_Unknown]

***

### Models and accuracy Values:
- Will run the following classifiation models:
  - Random forest
  - KNN modeling
  - Random forest
  - Logistic Regression model
    

- Other indicators of model performance with breif description and why it's important:

    
    
#### Model 1: Decision Tree


- Model 1 results:

Decision Tree, max depth 3| train: 96% |Validate: 96%
This is the best model, since all of my models worked with 96% accuracy this model gave me the fastest result and will be less costly to compute

### Model 2 : Random forest

- Model 2 results:

max depth 3| train: 96% |Validate: 96%

### Model 3 : KNN modeling

- Model 3 results: all measured with accuracy

max depth 3| train: 96% |Validate: 96%


### Model 4: Logistic Regression model

- Model 4 results:
at C= 0.05 | train: 96%


## Selecting the Best Model:
- all of the models used they where all around the same range in accuracy so `Decision tree` was the fastes and easiest to use so this idealy would be the best model 

***

## <a name="conclusion"></a>Conclusion:
[[Back to top](#top)]

In conclusion these models will help deternmin with 96% accuracy if the animal has certain characterisics that would lead to euthinization 

- our goal from the start is to use classification models to detrmine predictions as to when a animal will be euthinized and how we can reduce that 


### Recomendations

- from the looks of the data animals that are not nutered or spayed are more likly to be euthinized, if there was a way we can workout the public the impotrance of nutering anmals and being spayed and how this will decrease euthinization and save our animals lives 

- Having the City of Austin explain to the public the types of animals in they "put down" its not only cats and dogs and find ways to explain the actual numbers for the adoptible animals i.e the numbers of the animals cats and dogs that have been euthinized.

- I think this dataset is amazing it had so much information on the animals, I just think, looking though this data there is alot I had to deep dive and look for and I think that the City of Austin should invest more time making the dataset more specific so that the public has a easier time reading the dataset 

