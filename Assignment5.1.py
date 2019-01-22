
# coding: utf-8

# In[ ]:


## Generate a Vandermonde matrix.The columns of the output matrix are powers of the input vector. Theorder of the powers is determined by the `increasing` boolean argument.Specifically, when `increasing` is False, the `i`-th output column isthe input vector raised element-wise to the power of ``N - i - 1``. Sucha matrix with a geometric progression in each row is named for Alexandre-Theophile Vandermonde.Parameters

#Parameters

Parameters:	
x : array_like
1-D input array.

N : int, optional
Number of columns in the output. If N is not specified, a square array is returned (N = len(x)).

increasing : bool, optional
Order of the powers of the columns. If True, the powers increase from left to right, if False (the default) they are reversed.

New in version 1.9.0.

Returns:	
out : ndarray
Vandermonde matrix. If increasing is False, the first column is x^(N-1), the second x^(N-2) and so forth. If increasing is True, the columns are x^0, x^1, ..., x^(N-1).


# In[6]:


import numpy as np
x = np.array([1, 2, 3, 5])
N = 3
np.vander(x, N)


# In[7]:


np.column_stack([x**(N-1-i) for i in range(N)])


# In[8]:


x = np.array([1, 2, 3, 5])
np.vander(x)


# In[9]:


np.vander(x, increasing=True)


# In[10]:


##The determinant of a square Vandermonde matrix is the product of the differences between the values of the input vector:

np.linalg.det(np.vander(x))


# In[11]:


(5-3)*(5-2)*(5-1)*(3-2)*(3-1)*(2-1)

