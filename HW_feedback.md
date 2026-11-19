# Feedback and Discussion on Various HW


## HW9: Ensemble Methods & Random Forests

- The median completion time was 2 hours for 11 respondents who reported hours (range 1.5–4; one more wrote about 4 hours in their reflection)
- Student reflections and (anonymized) grader feedback [here](https://docs.google.com/spreadsheets/d/e/2PACX-1vSqP8n3SVX4nqgHFFRZ-Esp7jLZrEnU_cEzYV-yJbTyfzQPVMWioL2sxeFmvLe9Le-OWEd04Tx6Q3TA/pubhtml?gid=393224322&single=true)

Summary table of where students struggled to be posted on Fri 11/20




## HW8: Classifier Performance + Decision Trees

- The median completion time was 4 hours for 14 respondents who reported hours (range 1.2–7; one more wrote about 9 hours in their reflection)
- Student reflections and (anonymized) grader feedback [here](https://docs.google.com/spreadsheets/u/1/d/e/2PACX-1vSqP8n3SVX4nqgHFFRZ-Esp7jLZrEnU_cEzYV-yJbTyfzQPVMWioL2sxeFmvLe9Le-OWEd04Tx6Q3TA/pubhtml?gid=1748562274&single=true)

Summary table of where students struggled to be posted on Fri 11/20






## HW6: Cross-validation

- The median completion time was 2 hours for 14 respondents who reported hours (range 1–5)
- Student reflections and (anonymized) grader feedback [here](https://docs.google.com/spreadsheets/d/e/2PACX-1vSqP8n3SVX4nqgHFFRZ-Esp7jLZrEnU_cEzYV-yJbTyfzQPVMWioL2sxeFmvLe9Le-OWEd04Tx6Q3TA/pubhtml?gid=2004145852&single=true)


| Topic | Students | What they struggled with |
|---|---|---|
| Negative scores: why `neg_root_mean_squared_error`, flipping the sign | 7 | Why sklearn reports a negative RMSE (it maximizes the score); whether "best" still means smallest RMSE; forgetting `-` when building the RMSE column from `mean_test_score`. Most worked it out |
| Finding the right `scoring` string and where it goes | 4 | Reading the docs to find `scoring = ...`; getting RMSE instead of $R^2$ or accuracy. One wrote `neg_mean_squared_error`, which is MSE, not RMSE |
| How `GridSearchCV` works | 3 | What `param_grid`, `cv = 5`, and the averaging of fold scores do; what `best_estimator_`, `best_score_` and `cv_results_` return. The two who explained it in their own words did so well |



## HW5 Part 2: k-Nearest Neighbors Q2

- The median completion time was 2 hours (range 1.5–5)
- Student reflections and (anonymized) grader feedback [here](https://docs.google.com/spreadsheets/d/e/2PACX-1vSqP8n3SVX4nqgHFFRZ-Esp7jLZrEnU_cEzYV-yJbTyfzQPVMWioL2sxeFmvLe9Le-OWEd04Tx6Q3TA/pubhtml?gid=394842597&single=true)

What students struggled with:

| Topic | Students | What they struggled with |
|---|---|---|
| Q1 interpretation: k = 1 vs k = 10, the RMSE ratio, overfitting vs lowest test RMSE | 7 | Why k = 1 has a tiny training RMSE yet is "best" on test data; what the ratio means; reading the table |
| Order of sklearn steps (`fit`, `predict`, RMSE; train vs test) | 3 | Which object is fit on what, and what `.predict()` produces (`y_hat`) |
| Looping over k = 1 to 30 | 3 | Remembering the loop structure; an off-by-one between `x` and `y` for the plot |
| Q1 Part b.3, improving the analysis | 2 | Couldn't think of what to change; one found it by changing the test split |
| Pipeline and function details | 3 | Wrong import location for `StandardScaler`; `np.repeat`; `set_params(model_fit__n_neighbors = ...)`; how Yeo-Johnson interacts with the weights option |
| Data leakage (fitting on test data) | 1 | Found and corrected after submission |
| No difficulty | 2 | "Straight forward"; "I just referenced the lectures and bits from previous homeworks" |



## HW5 Part 1: k-Nearest Neighbors Q1

- The median completion time was 1.61 hours for 9/17 respondants (range 1-2) 
- Student reflections and (anonymized) grader feedback [here](https://docs.google.com/spreadsheets/d/e/2PACX-1vSqP8n3SVX4nqgHFFRZ-Esp7jLZrEnU_cEzYV-yJbTyfzQPVMWioL2sxeFmvLe9Le-OWEd04Tx6Q3TA/pubhtml?gid=1386306763&single=true). 

What students struggled with:

| Topic | Students | What they struggled with |
|---|---|---|
| Part b.1–b.2: choosing a model when overfitting and test error disagree | 3 | k = 1 overfits, yet has the lowest test RMSE; is that a tradeoff? |
| Part b.3: what could improve the analysis | 2 | Couldn't think of anything specific; one went to Claude to find "the answer" |
| Order of sklearn steps on training vs test data | 1 | Set up, fit, predict, RMSE: why the test version looks different |
| Looking up an unfamiliar NumPy function (`np.repeat`) | 1 | Understanding the mean model's code |


## HW4: Transformations, scaling, pipelines

- The median completion time was 2 hours (range 1–5)
- Student reflections and (anonymized) grader feedback [here](https://docs.google.com/spreadsheets/d/e/2PACX-1vSqP8n3SVX4nqgHFFRZ-Esp7jLZrEnU_cEzYV-yJbTyfzQPVMWioL2sxeFmvLe9Le-OWEd04Tx6Q3TA/pubhtml?gid=1423349144&single=true). 

What students struggled with:

| Topic | Students | What they struggled with |
|---|---|---|
| Pipeline; `.fit()` vs `.transform()` vs `.fit_transform()` | 6 | Understanding what each step learns and applies; most resolved it |
| Q3A/B: picking the predictor columns (`ID`, `Label`, `select_dtypes`) | 4 | Order of `select_dtypes()` and `.drop()`; forgetting to drop `ID` |
| Copy-and-adapt errors (`train` vs `train_wbc`, `ic` vs `wbc`) | 3 | Renaming most, but not all, variables from the example |
| Box-Cox needs strictly positive values | 3 | Hit a `ValueError` or worked around the zeros |
| Q3D: converting the pipeline output back to a DataFrame | 2 | Supplying the column names |
| Deciding what to transform or rescale, and judging success | 2 | Which variables need what; "was it successful?" |



## HW3: DBSCAN and PCA

- The median completion time was 5 hours (range 2-10)
- Student reflections and (anonymized) grader feedback [here](https://docs.google.com/spreadsheets/d/e/2PACX-1vSqP8n3SVX4nqgHFFRZ-Esp7jLZrEnU_cEzYV-yJbTyfzQPVMWioL2sxeFmvLe9Le-OWEd04Tx6Q3TA/pubhtml?gid=1505023770&single=true). 

What students struggled with:

| Lab and question | Students | What they struggled with |
|---|---|---|
| 03-1 Q2 (open-ended clustering of `majors`) | 7 | Getting the data into shape, deciding how much is enough, interpreting the clusters |
| 03-1 Q1 (eps search) and demo code | 2 | Missing the starter grid; `[:,0]` indexing |
| 03-2 Q1 (scree and cumulative plots) | 3 | Building the plot from scratch |
| 03-2 Q2 (PC scatter colored by `engnat`) | 3 | Coloring points by group; indexing PCs |
| 03-2 Q3 (loadings) | 4 | What a loading means; sign vs size |
| 03-2 Q4 (dark triad) | 2 | Plots |



## HW2: Hierarchical clustering

- Solutions posted in `lec02-1/`; be sure to save your own copy and rename it
- Student [reflections](https://docs.google.com/spreadsheets/d/e/2PACX-1vSqP8n3SVX4nqgHFFRZ-Esp7jLZrEnU_cEzYV-yJbTyfzQPVMWioL2sxeFmvLe9Le-OWEd04Tx6Q3TA/pubhtml?gid=2007430057&single=true)


### Summary of student reflections

#### 1. `distance_threshold=0` + `n_clusters=None` (5+ students)

The demo code uses these settings to build the *full* dendrogram, but students then
ran `.fit_predict()` with those same settings and got 500 singleton clusters. The
resulting scatter plots looked like meaningless color noise — and, crucially, looked
*identical* across linkage methods.

- Several students assumed their code was broken
- One went to office hours; one concluded `single` and `ward` "are the same"


#### 2. The sklearn estimator workflow: `.fit()` vs `.predict()` vs `.fit_predict()`

One student wrote:

```python
blobs_X = StandardScaler().fit_transform(blobs_X)
my_clusters_blob = KMeans(n_clusters=3, random_state=8)
# ...then plotted, never having fit the model
```

They assumed that fitting the *scaler* had also fit the *model*.


#### 3. No criteria for *comparing* two clusterings

For Q1.c) and Q2.b), students reported the plots "looked similar upon first glance" and they "didn't know
what to look for." They lack vocabulary for judging clustering output.


#### 4. Linkage criteria are being learned from AI, not from lecture

Students used ChatGPT/Claude to get step-by-step explanations of `ward` (SSE-based
merging) and `single` (chaining) — and those who did wrote genuinely good explanations.
That's the system working, but it suggests lecture coverage of linkage was thin
relative to what the lab demanded.



## HW1: k-Means Clustering

- Solutions posted in `lec01-2/`; be sure to save your own copy and rename it
- Student [reflections](https://docs.google.com/spreadsheets/d/e/2PACX-1vSqP8n3SVX4nqgHFFRZ-Esp7jLZrEnU_cEzYV-yJbTyfzQPVMWioL2sxeFmvLe9Le-OWEd04Tx6Q3TA/pubhtml?gid=1767179853&single=true)


