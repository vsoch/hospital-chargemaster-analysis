# Hospital Chargemaster Analysis

This is a small analysis using the [hospital chargemasters](https://www.github.com/vsoch/hospital-chargemasters)
Dinosaur Dataset.

<a target="_blank" href="https://camo.githubusercontent.com/d0eb19f161d4795a9c137b9b71c70b008d7c5e8e/68747470733a2f2f76736f63682e6769746875622e696f2f64617461736574732f6173736574732f696d672f61766f6361646f2e706e67"><img src="https://camo.githubusercontent.com/d0eb19f161d4795a9c137b9b71c70b008d7c5e8e/68747470733a2f2f76736f63682e6769746875622e696f2f64617461736574732f6173736574732f696d672f61766f6361646f2e706e67" alt="https://vsoch.github.io/datasets/assets/img/avocado.png" data-canonical-src="https://vsoch.github.io/datasets/assets/img/avocado.png" style="max-width:100%; float:right" width="100px"></a>

## General Goals

For this analysis, we want to try predicting price for a given item (possibly for 
a given hospital) based on the chargemaster data. For example, I would expect items
with the terms "brain" or "heart" to be more expensive than general medications
like Advil (ibuprofen). 

The approach we will take is to try a simple linear regression. I don't want to do the ultimate analysis, but rather to show you that the data is interesting.

 1. We first start with data from one hospital. This is to keep the data frame size reasonable to share on GitHub, and also speedy to run on my tiny local machine.
 2. We will then do stop word removal and make all terms lowercase.
 3. Then we will create a sparse data frame of words (columns) by the unique identifiers (rows). We can use [scikit-learn](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer) to create this data frame.
 4. The first model we will train is linear regression (possibly with lasso to get more zero entries).

Given over one hundred hospitals, there are definitely more interesting models to build and things
to try! And you need validation. I leave this up to you, dear data scientist.

### 1. Data Preparation

The data required for the dummy demo is provided in the repository, and here is
how I produced them:

```bash
git clone https://www.github.com/vsoch/hospital-chargemasters
cd hospital-chargemasters
```

And use the script [1.prepare-data.py](1.prepare-data.py) to read in the latest datasets

