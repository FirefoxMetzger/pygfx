"""
Subdivision
===========

Example showing subdivided polyhedrons.
"""

# sphinx_gallery_pygfx_render = True
# sphinx_gallery_pygfx_target_name = "disp"

import pygfx as gfx


scene = gfx.Group()

material = gfx.MeshBasicMaterial(wireframe=True, side="FRONT")
geometries = [gfx.tetrahedron_geometry(subdivisions=i) for i in range(4)]

for i, geometry in enumerate(geometries):
    polyhedron = gfx.Mesh(geometry, material)
    polyhedron.position.set(6 - i * 3, 0, 0)
    scene.add(polyhedron)


if __name__ == "__main__":
    disp = gfx.Display()
    disp.show(scene, up=gfx.linalg.Vector3(0, 0, 1))
