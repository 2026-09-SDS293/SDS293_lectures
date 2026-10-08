# Feedback and Discussion on Various HW



## HW3: DBSCAN and PCA

- Solutions posted in `lec03-1/` and `lec03-2`; be sure to save your own copy and rename it
- Student [reflections](); see summary below

### Summary of student reflections


***


## HW2: Hierarchical clustering

- Solutions posted in `lec02-1/`; be sure to save your own copy and rename it
- Student [reflections](https://docs.google.com/spreadsheets/d/e/2PACX-1vSqP8n3SVX4nqgHFFRZ-Esp7jLZrEnU_cEzYV-yJbTyfzQPVMWioL2sxeFmvLe9Le-OWEd04Tx6Q3TA/pubhtml?gid=2007430057&single=true); see summary below


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




***


## HW1: k-Means Clustering

- Solutions posted in `lec01-2/`; be sure to save your own copy and rename it
- Student [reflections](https://docs.google.com/spreadsheets/d/e/2PACX-1vSqP8n3SVX4nqgHFFRZ-Esp7jLZrEnU_cEzYV-yJbTyfzQPVMWioL2sxeFmvLe9Le-OWEd04Tx6Q3TA/pubhtml?gid=1767179853&single=true); see summary below


