# Feedback and Discussion on Various HW



## HW5: k-Nearest Neighbors

Coming on Thu 10/22


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


