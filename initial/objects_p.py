import numpy as np
from visbrain.objects import SourceObj  # Import a source object
from visbrain.objects import BrainObj, SceneObj

# object definition ------------------------------------------------#

# Define 100 random 3D (x, y, z) coordinates :
xyz = np.random.rand(100, 3)

# Define a source object :
s_obj = SourceObj('obj_name', xyz, color='green', symbol='square',
                  edge_color='white')

# Object preview with a black background:
# s_obj.preview(bgcolor='black')


# Embedded objects -------------------------------------------------#

# Define a source and a brain objects :
b_obj_1 = BrainObj('white', translucent=False)
b_obj_2 = BrainObj('B1')
s_obj = SourceObj('my_sources', 50 * np.random.uniform(-1, 1, (100, 3)))

# Define a scene with a black background:
sc = SceneObj(bgcolor='black')

# Add the first brain object to the scene :
sc.add_to_subplot(b_obj_1, row=0, col=0)

# Add the source and the first brain object to same subplot :
sc.add_to_subplot(b_obj_2, row=0, col=1)
sc.add_to_subplot(s_obj, row=0, col=1)

# Finally, display the scene :
sc.preview()
