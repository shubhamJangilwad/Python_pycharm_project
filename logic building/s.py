# import matplotlib.pyplot as plt
# import numpy as np
#
# a = np.array([[[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4]]])
# plt.matshow(a)
# plt.gray()
# plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Defined 3D array (shape: 1x5x5)
a = np.array([[0,1,2],[0,1,2]])

# Displays matrix as an image
plt.matshow(a)
plt.gray() # Sets colormap to gray

# Necessary to display the plot
plt.show()
