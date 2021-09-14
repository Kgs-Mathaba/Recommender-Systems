import pandas as pd

# https://www.kaggle.com/grouplens/movielens-20m-dataset
df = pd.read_csv("rating.csv")

# note:
# user ids are ordered sequentially from 1 to 138493
# with no missing numbers
# movie ids are intergers from 1 to 131262
# Not all movies ids appear
# only 26744.
print(df.head(5))

# make user ids start from 0
df.userId = df.userId - 1

# create a mapping for movie ids to movie ids
unique_movie_ids = set(df.movieId.values)
movie2idx = {}
count = 0
for movie_id in unique_movie_ids:
    movie2idx[movie_id] = count
    count += 1

#  add them to the data frame
df["movie_idx"] = df.apply(lambda row: movie2idx[row.movieId], axis=1)

# drop the timestamp
df = df.drop(columns=["timestamp"])

df.to_csv("edited_rating.csv")
