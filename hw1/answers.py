r"""
Use this module to write your answers to the questions in the notebook.

Note: Inside the answer strings you can use Markdown format and also LaTeX
math (delimited with $$).
"""

# ==============
# Part 1 answers

part1_q1 = r"""
**Your answer:**
1. False - The test-set only allows us to estimate how well the model fits the data. It does not provide an indication for in-sample error.

2. False - Generally, the smaller our train-set is in comparsion to the test-set, the less likely it is for the model to fit the data. 

3. True - The test-set role is evaluating how much our model fits the data. Using it in cross validation means training the model over the test-set,
which should decrease the test-error but at the cost of its reliability in estimating our out-sample error.

4. True - In cross validation, in each iteration we train the model on a different subset of training samples and use the remaining fold to
estimate the generalization error.   

Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

part1_q2 = r"""
**Your answer:**
The approach isn't justified. Our friend uses the test-set for hyperparameter-tuning, essentially training the model with the test-set, which leads to overfitting. So, although adding a regularization term is a good idea in order to improve overfitting in the model, his method of choosing the best $\labda$ is counter-productive.

Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

# ==============
# Part 2 answers

part2_q1 = r"""
**Your answer:**

Up to a certain point, increasing k should improve generalization. The point depends on the dataset of course. In general k needs to strike a balance between allowing enough close - "important" neighbors to affect the classification of a point in the space, and also not being large enough that even neighbors that aren't strictly close to the point can affect the classification. For very large k values, k-NN classification will start to function as a majority-classification where samples are classified as the majority class in the train-set. Generally, very small k values lead to overfitting, and very large k values lead to underfitting.   

Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

part2_q2 = r"""
**Your answer:**
1. The train-set accuracy provides no information whatsoever about how well our model generalizes over the data. With the right model-class it can be very easy to get a model with very high train-accuracy, but without a test-set it is impossible to tell if it also suffers from overfitting. For k-NN, the best value of k for training accuracy (if a point is included as its own neighbor) will always be 1, but a model with k=1 will also overfit the data. k-fold CV is better because it does use a validation-set to estimate the generalization.

2. Using the train-set for hyperparameter-tuning will lead to overfitting. K-fold CV is better than this method because the test-set remains completely
seperated from the training-process. 

Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

# ==============

# ==============
# Part 3 answers

part3_q1 = r"""
**Your answer:**
The margin we choose for our SVM model is arbitrary because it only represents the level of "confidence" in the classification we penalize with respect to. 
For any hyperplane W learned, we can always multiple W by a constant (in a linearly seperable data) to make any sample a support vector. Also, when deriving 
the loss function by $W$, the constant $\Delta$ becomes zero. Hence $\Delta$ has no affect on the minima gradient descent will converge to or on
the steps the algorithm will take towards the minima.

Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

part3_q2 = r"""
**Your answer:**
1. From the image of every class, it looks like the linear model is learning by identifying patterns that correspond to the individual classes. For some classes, there are 
some clear patterns in the weights image that numbers in the class usually exhibit. So, the model develop these patterns over the course of the training process and 
then a prediction is made over a sample based on which patterns fit it best.

2. The interpertation is similar to kNN in the sense that both models rely on geometric properties for classification. In kNN these properites are strictly the distance between
a sample and the other samples in the training set, and in the linear model these properties are where the pixels are more likely to be black\white for each individual class.
The difference is that kNN realizes only on k samples to make its decision, while the linear model decision is always influenced by the entire training set.

Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

part3_q3 = r"""
**Your answer:**
1. The learning rate seems good. The loss function converges smoothly towards 0. From manual testing, a higher learning rate resulted a more jagged convegence that's 
indicative of gradient descent jumping around the minima. A lower learning rate achieved a slightly better result, but took much longer.
2. The model is slightly overfitting the train-set, because as seen in the graph, the train-accuracy is slightly higher than the test-accuracy.

Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

# ==============

# ==============
# Part 4 answers

part4_q1 = r"""
**Your answer:**


Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

part4_q2 = r"""
**Your answer:**


Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

part4_q3 = r"""
**Your answer:**


Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

# ==============
