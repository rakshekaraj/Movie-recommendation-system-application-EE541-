from flask import Flask, render_template, request
import csv 


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommendations', methods=['POST'])
# def get_recommendations():
#     user_number = int(request.form['user_number'])
#     num_recommendations = int(request.form['num_recommendations'])

#     # Read recommendations from CSV (replace 'output.csv' with your actual CSV file name)
#     recommendations = read_recommendations_from_csv(user_number, num_recommendations)

#     return render_template('recommendations.html', user=user_number, recommendations=recommendations)
def get_recommendations():
    user_number = int(request.form['user_number'])
    num_recommendations = int(request.form['num_recommendations'])

    movie_names, recommendations = read_recommendations_from_csv(user_number, num_recommendations)

    return render_template('recommendations.html', user=user_number, movie_names=movie_names, recommendations=recommendations)

def read_recommendations_from_csv(user_number, num_recommendations):
    recommendations = []
    movie_names = []  # To store the names of movies from the header

    with open('output.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        movie_columns = header[1:]  # Exclude the first column (user column)

        # Store movie names from the header
        movie_names.extend(movie_columns)

        for row in reader:
            current_user = int(row[0])
            if current_user == user_number:
                # Print for debugging
                print("Row:", row)
                recommendations.extend(movie for movie, is_recommendation in zip(movie_columns, row[1:]) if float(is_recommendation) == 1.0)
                if len(recommendations) >= num_recommendations:
                    break

    return movie_names, recommendations[:num_recommendations]



# def read_recommendations_from_csv(user_number, num_recommendations):
#     recommendations = []
#     with open('output.csv', 'r', encoding='utf-8') as csvfile:
#         reader = csv.reader(csvfile)
#         # Assuming the CSV structure is user, movie1, movie2, ..., movieN
#         header = next(reader)
#         movie_columns = header[1:]

#         for row in reader:
#             current_user = int(row[0])
#             if current_user == user_number:
#                 recommendations.extend(movie for movie, is_recommendation in zip(movie_columns, row[1:]) if float(is_recommendation) == 1.0)
#                 if len(recommendations) >= num_recommendations:
#                     break

#     return recommendations[:num_recommendations]



def get_recommendations():
    user_number = int(request.form['user_number'])
    num_recommendations = int(request.form['num_recommendations'])

    # Add your recommendation logic here based on the CSV file

    # Placeholder response
    recommendations = ["Movie 1", "Movie 2", "Movie 3"]

    return render_template('recommendations.html', user=user_number, recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)