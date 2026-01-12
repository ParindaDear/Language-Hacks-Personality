# Language Hacks Personality 🔍🤔
## Project Overview   

## Dataset
- **Source:** [(MBTI) Myers-Briggs Personality Type Dataset (Kaggle)](https://www.kaggle.com/datasets/datasnaek/mbti-type)
- **Description:**   
  Each row contains a user's MBTI personality type and concatenated social media posts.
- **Acknowledgements:**   
  Data was collected through the [PersonalityCafe forum](https://www.personalitycafe.com/login/), as it provides a large selection of people and their MBTI personality type, as well as what they have written.
- **Rows:** 8675
- **Columns:** 2

## Tools & Tech
- JupyterLab
- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn
- NLTK

## Knowledge & Skills
- NLP with `NLTK` using **Stopwords** to filter out common words like 'is' and 'the' to resuce noise,
  **WordNet Lemmatizer** to convert words to base forms by part of speech, such as running → run or better → good,
  which is more accurate than simple stemming.
- Feature Engineering for Text Data via `TF-IDF` (Text Vectorization) which transforms text into numbers (TF-IDF matrix)
  so that ML model can use it, by calculating how often words appear in a document(TF) and reducing the weight of words that appear often across all documents(IDF)
- **ML Modeling:** Logistic Regression, Naive Bayes, Linear SVC, Random Forest
- Model Evaluation with `Confusion Matrix` for visualize true vs predicted labels, interpret errors (TP, FP, TN, FN),
  and use insights to improve model performance and handle class imbalance.
- Use `pickle` to save/load trained models and preprocessing pipelines for reproducible predictions and deployment in business scenarios.
- Data visualization using Matplotlib and Seaborn to communicate insights clearly and support decision-making for business teams.
- Translate model outputs into actionable recommendations for marketing, customer engagement, and sales strategy, showing business impact of ML.

## Project Structure
```
.
├── data/
│ ├── mbti_1.csv --> raw data
│ └── mbti_processed.csv --> cleaned data
│
├─ model/
│   ├─ lr_model.pkl --> Trained Logistic Regression model
│   └─ tfidf_vectorizer.pkl --> TF-IDF vectorizer
│
├── notebooks/
│ ├── 01_Modeling.ipynb --> Data cleaning, preprocessing, and ML model training
│ ├── 02_Visualization --> Exploratory data analysis and plotting insights
│ ├── 03_BU_Recommendation.ipynb --> Business recommendations based on model outputs
│ └── preprocess_utils.py --> Reusable preprocessing functions
│
├── .gitignore
└── README.md
```

## What I’m Most Proud Of in This Project
- **Problem**  
  - Social media posts contained noisy text, including URL, HTML tags, repeated delimiters,
    MBTI type words, and cognitive function abbreviations (e.g., ne, ti), making it difficult to train accurate ML models.
  - The dataset was imbalanced because Introvert (I) posts are more than Extrovert (E), which could bias the model. 

- **Solution**   
  - I use NLTK (stopwords, WordNet Lemmatizer) to clean and normalize text.
    Then implemented feature engineering with TF-IDF to convert text into numerical representations for ML models.
  - Use `class_weight='balanced'` to handling class imbalance with balanced weights, giving fair weight to smaller classes and making the model more reliable.

- **Result**   
  Logistic Regression model achieved 82% accuracy predicting Introvert vs Extrovert, with top predictive words for each class providing interpretable insights.

 
