import meshio
import numpy as np
mesh=meshio.read("par_minus_cyl_plus_sphere.stl")
triangles=mesh.cells_dict["triangle"]
points=mesh.points


inlet_indices=(np.mean(points[triangles],axis=1)[:,0]<1e-6)
outlet_indices=(np.mean(points[triangles],axis=1)[:,0]>7.99999)
wall_indices=np.logical_not(np.logical_or(inlet_indices,outlet_indices))
meshio.write_points_cells("inlet.stl",points,{"triangle":triangles[inlet_indices]})
meshio.write_points_cells("Wall.stl",points,{"triangle":triangles[wall_indices]})
meshio.write_points_cells("outlet.stl",points,{"triangle":triangles[outlet_indices]})

def add_name(name):
    # Specify the file path
    file_path = name+".stl"

# Word to add to the end of the first line
    word_to_add = name

# Open the file in read mode to read its content
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Modify the first line by adding the word
    if lines:
        lines[0] = lines[0].strip() + " " + word_to_add + "\n"

    # Open the file in write mode to write the modified content back to the file
    with open(file_path, 'w') as file:
        file.writelines(lines)
    
add_name("outlet")
add_name("inlet")
add_name("Wall")
