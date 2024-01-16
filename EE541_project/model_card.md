# Model card for "K means and Restricted Boltzman Machines"

Jump to section:

- [Model details](#model-details)
- [Context](#Context)
- [Metrics](#metrics)
- [Preprocessing](#Preprocessing)
- [Performance](#Performance)
- [Conclusion](#Conclusion)

## Model details

_Basic information about the model._

Report regarding model is found in [link](#https://drive.google.com/file/d/1NHy3TYOmCJoWaYOsJu6u9FoxkevK2ETv/view?usp=sharing)

- Belongs to Praburam K Varadharajan and Raksheka Rajakumar
- Model Name: MovieRecSys-RBM-KMeans
- Model Version: 1.0
- Date: 2nd December 2023
- Where to send questions or comments about the model

## Context

**Project Summary:** This project explores advanced models—RBMs and KMeans Clustering—for movie recommendation systems. The goal is to provide users with accurate, diverse, and personalized movie recommendations by leveraging collaborative filtering and clustering techniques.

## Intended use

_Can be used by streaming companies like Netflix, Prime video and Hulu for better training and evaluation_


### Primary intended uses
Serves as a performance anaysis for streaming companies  to check which model performs better under given circumstances.

### Primary intended users
Serves as a research for Netflix, Amazon, Sony, Disney and etc.

### Out-of-scope use cases
With a slight modifications to code, it can be used by students for course recommendations, Food recommendations and travel recommendations


### Evaluation factors
We consider that all the input features that the model was trained on is available so that the prediction can be done.

## Metrics

Evaluation metrics used in this paper Mean squared error, Accuracy and Human evaluation. The metrics are discussed more detail in the 6th Chapter of the submitted report

## Models in Focus

1. **Restricted Boltzmann Machines (RBMs):**
   - Strengths: Captures complex patterns, handles sparse data, and provides personalized recommendations.
   - Evaluation Metric: Mean Squared Error (MSE).
   - Tradeoff: Computational complexity for training.

2. **KMeans Clustering:**
   - Strengths: Efficient content-based clustering, computationally less demanding.
   - Evaluation Metric: Silhouette score.
   - Tradeoff: Sacrifices intricacy in user preference modeling for faster processing.

### Data Used

- **Movies Dataset:**
  - 45,466 entries with detailed movie information.
  - Attributes include genres, ratings, and user interactions.

- **Ratings Dataset:**
  - 26,024,289 entries with user-specific movie ratings.


### Motivation
In the dynamic landscape of machine learning, the importance of transparent and accountable model documentation cannot be overstated. The motivation behind creating this model card lies in our commitment to fostering transparency, trust, and responsible AI practices in the development and deployment of our movie recommendation system.

### User Empowerment
We recognize the profound impact that recommendation systems can have on user experiences. By providing a detailed model card, we aim to empower users with the knowledge they need to understand how our system works, what factors influence its recommendations, and the potential implications for their content consumption.

## Preprocessing

### Data Cleaning and Integration

Our movie recommendation system relies on two major datasets: the "Movies" dataset and the "Ratings" dataset. A meticulous data cleaning process was undertaken to ensure the quality and reliability of the information.

#### Movies Dataset (45,466 entries)

- **Attributes:** The dataset spans 24 columns, covering a range of attributes such as adult classification, budget, genres, homepage availability, IMDb ID, original language, title, overview, popularity, poster path, production companies, production countries, release date, revenue, runtime, spoken languages, status, tagline, and critical metrics like vote average and vote count.

- **Handling Null Values:** Certain columns, such as "belongs_to_collection," "homepage," and "tagline," exhibit non-null counts that suggest variability in the dataset's completeness. Null values were handled appropriately, and columns irrelevant to the recommendation system were excluded.

#### Ratings Dataset (26,024,289 entries)

- **Attributes:** The dataset comprises four columns: user ID, movie ID, rating assigned by the user, and a timestamp capturing the moment of the rating.

- **Handling Duplicates:** Duplicate entries were removed to ensure the accuracy of user ratings.

### Data Alignment and Enrichment

#### Integration of Datasets

- The "Movies" and "Ratings" datasets were integrated based on the common identifier "ID" to form a consolidated view (df_final) merging movie details with corresponding ratings.

- Essential criteria, such as a minimum vote count, non-null vote averages, and an English language preference, were applied to filter the movies dataset, resulting in df_movie_english.

### Feature Engineering

#### Movies Dataset

- The release year was extracted from the 'release_date' column.
- Data types were adjusted, and genre information was refined using an extraction function.
- The resulting dataset was shuffled to eliminate biases, and subsets (training, testing, and validation) were created using the train_test_split function.

#### Ratings Dataset

- User-centric features were identified, including 'vote_count,' 'vote_average,' 'rating,' and 'year.'
- Movie genres were encoded using a MultiLabelBinarizer to capture their categorical nature.

### Standardization and Clustering

- Feature scaling was applied using a StandardScaler to standardize features and bring them to a comparable scale.
- The KMeans algorithm was employed on the scaled feature set with five clusters.



## Performance

### RBMs Performance

- **MSE (Mean Squared Error):** 0.2144 (lower is better).
- **Training Time:** 30s. (with GPU P100 As accelerator)

### KMeans Performance

- **Silhouette Score:** 0.7577 (higher is better).
- **Processing Time:** 20s.

## Limitations

- **Computational Complexity:** RBMs demand significant computational resources for training.
- **Sparcity Handling:** KMeans may face challenges in handling sparsity in user ratings.


## Conclusion

This model card provides an overview of the Movie Recommendation System with RBMs and KMeans, detailing its intended use, model details, performance metrics, and limitations. It serves as a reference for understanding the project's context, objectives, and potential applications.


