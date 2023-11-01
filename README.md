First source openfoam, then
Do:
- python extractSTL.py
- cat inlet.stl outlet.stl Wall.stl > tot.stl
- surfaceFeatureEdges tot.stl tot.fms
- change the boundaries in tot.fms from empy to wall in Wall and patch in inlet and outlet
- tetMesh
- buoyantBoussinesqPimpleFoam
- foamToVTK -fields "(p T U p_rgh)"

Use paraFoam for visual inspection
