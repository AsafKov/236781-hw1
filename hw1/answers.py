r"""
Use this module to write your answers to the questions in the notebook.

Note: Inside the answer strings you can use Markdown format and also LaTeX
math (delimited with $$).
"""

# ==============
# Part 1 answers

part1_q1 = r"""
**Your answer:**
1. False - The in-sample error is the measure of how well our model preforms on the data used to train it. The test-set is used to measure
how well our final model generalizes over the distribution, and using it to measure in-sample error will defeat the purpose of seperating
the dataset into train and test sets.

2. False - Generally, the smaller our train-set is in comparsion to the test-set, the less likely it is for the model to fit the data. 
As an example: A kNN model with a train set of one sample we classify the entire test-set with the sample class of that sample, which 
will obviously preform poorly for most distributions.

3. True - The test-set role is evaluating how much our model fits the data. Using it in cross validation means training the model over the test-set,
which should decrease the test-error but at the cost of its reliability in estimating our out-sample error.

4. True - In each iteration of CV we train the model on a different subset of training samples and use the remaining fold to
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
The approach isn't justified. Our friend uses the test-set for hyperparameter-tuning, essentially training the model with the test-set, which leads to overfitting over it.
So, although adding a regularization term is a good idea in order to improve overfitting in the model, his method of choosing the best $\lambda$ is counter-productive.

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

Up to a certain point, increasing k should improve generalization, but the further we stem from that point the more likely we are to underfit the data.
The point depends on the dataset of course. In general k needs to strike a balance between allowing enough close - "important" neighbors to affect the classification of a point in the space, and also not being large enough that even neighbors that aren't strictly close to the point can affect the classification.

For very large k values (in comparsion to the train-set size), k-NN classification will start to function like a majority-classifier where samples are classified as the majority class in the train-set.
Generally, very small k values are more likely to overfit (especially if a sample is also its own neighbor), and very large k values lead to underfitting.   

Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

part2_q2 = r"""
**Your answer:**
1. The train-set accuracy provides no information whatsoever about how well our model generalizes over the distribution. With the right model-class it can be very easy to get a model with very high train-accuracy, but without a test-set it is impossible to tell if it also suffers from overfitting. 
For k-NN, the best value of k for training accuracy (if a point is included as its own neighbor) will always be 1, but a model with k=1 will also overfit the data. k-fold CV is better because it uses a validation-set to estimate the generalization.

2. Using the test-set for hyperparameter-tuning will overfit the test-set. K-fold CV is better than this method because the test-set remains completely
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
the loss function by $W$, the constant $\Delta$ becomes zero. Hence $\Delta$ has no affect on the minimum gradient descent will converge to or on
the steps the algorithm will take towards the minimum.

Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

part3_q2 = r"""
**Your answer:**
1. From the image of every class, it looks like the linear model is learning by identifying patterns that correspond to the individual classes (which pixels are most likely to be white\black).
For some classes, there are some clear patterns in the weights image that numbers in the class usually exhibit. So, the model develop these patterns over the course of the training process and 
then a prediction is made over a sample based on which patterns fit it best.

2. kNN model classifies based on distance in the feature-space, so the assumption is that there a distance-based pattern the should yield good classification ("close" samples are more likely to be of the same class).
Our interpertation of the lineaer classifier model also relies on similiarty in geometrical patterns which can also be intereperted as a measure of how close it is to a "representer" of a given class.
The models are different in the senes that kNN relies on non-learned decision boundries, while a lineaer classifier relies on learned hyperplanes to seperate the classes in the feature space.

Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

part3_q3 = r"""
**Your answer:**
1. The learning rate seems good. The loss function converges quite smoothly towards what seems like the minimum. From manual testing, a higher learning rate resulted a more jagged convegence that's 
indicative of gradient descent jumping around the minima. A lower learning rate achieved a similar result and took longer to run.
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
Ideally the residuals should display a random scatter tightly around 0, which indicates that predication error
is small across the entire set. It should also be linear, and the pattern should remain similar (uniform) across the $\hat{y}$ axis.
In the plot of the 5-best features, the residuals aren't as tightly spread around 0 as they are in out final model, and it also displays
a curved pattern which indicates a linear regressor hypotheses class isn't well suited for the learning problem (when limiting it to only those 5 features).


Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

part4_q2 = r"""
**Your answer:**
1. It remains a linear regression model, because the predictions are stil being made using a linear function:
$y_{pred} = W^TX+b$ (in this case $X$ is the modified feature matrix, but that's irrelevent to the prediction rule).
2. Yes, for any non-linear function of the features, we can apply a mapping that will fit the function with the a suitable weight
matrix that will serve to apply coefficents. 
3. It will still be a hyperplane, just in a different space, and the decision boundary will depend on the applied mapping.

Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

part4_q3 = r"""
**Your answer:**
1. logspace allows us to effeciently scour for an estimation for the best $\lambda$ over values with different orders of magnitude.
Achieving the same goal with linespace could potentially take much longer. When we've found an estimation for the order of mantiude suitable for $\lambda$
we can cross validate over a linespace defined range to scour around it.
2. We had two hyperparameters - degree with x=3 possible values, and lambda with y=20 possible values. We applied gridsearch with k=3.
The number of times we fit the data is therefore: $kxy = 3*3*20=180$

Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

# ==============
