# Assembled ship files

This folder contains files where various parts are assembled to a make a more complete ship model. These files are also the source of the other files in the other geometry folders (hull, rudder and propeller).

There are currently two versions of the assembled ship, described shortly below:

1) A [Rhino](https://www.rhino3d.com/) file with the name `SOBC-1_full_ship_assembly.3dm`. It contains all CAD parts assembled into a complete ship model. This is the main source of the exported CAD models in the other folders
2) A [Blender](https://www.blender.org/) file with the name `SOBC-1_hull_and_rudder.blend`. It contains an assembly of the hull, rudder and headbox represented as surface meshes. This is the source of the exported `.obj` files in the other folders. This representation is made to make it easy to run simulations with software that do not directly read CAD files, such as [OpenFOAM](https://www.openfoam.com/) and SnappyHexMesh.