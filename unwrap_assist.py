""" 
A Panel with some statistics and basic operators to learn python code for blender
Copyright (C) 2025 Sheila

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General
 Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; 
without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.
"""


import math
import bmesh
import bpy


class UnwrapAssistOperator(bpy.types.Operator):
    """Marks selected sharp edges as seams, then unwraps mesh"""
    bl_idname = "uv.unwrap_assist"
    bl_label = "Unwrap Assist"
    bl_options = {'REGISTER', 'UNDO'}
    
    sharpness: bpy.props.FloatProperty(
        name= 'Sharpness',
        default= math.radians(30),
        min=math.radians(1),
        max= math.radians(180),        
        subtype= 'ANGLE',
        unit='ROTATION'
    )

    @classmethod
    def poll(cls, context):
        return bpy.ops.uv.unwrap.poll()

    def execute(self, context):
        mesh_data = context.edit_object.data
        bmesh_data = bmesh.from_edit_mesh(mesh_data)
        
        max_angle = self.sharpness
        
        #for e in bmesh_data.edges[:]:
        #    if e.seam:
        #        e.seam = False  
        
        #bmesh.update_edit_mesh(mesh_data)

        for edge in bmesh_data.edges:
            if edge.hide and not edge.select:
                continue
            
          
            edge_angle = edge.calc_face_angle(-1)
            if edge_angle > max_angle:
                edge.seam = True
                
        bmesh.update_edit_mesh(mesh_data, loop_triangles=False, destructive=False)
        
        
        bpy.ops.uv.unwrap(method='ANGLE_BASED', margin=0.0530833)

        
        return {'FINISHED'}
        


def menu_func(self, context):
    self.layout.operator(UnwrapAssistOperator.bl_idname)


# Register and add to the "object" menu (required to also use 
#F3 search for quick access).
def register():
    bpy.utils.register_class(UnwrapAssistOperator)
    bpy.types.VIEW3D_MT_uv_map.append(menu_func)


def unregister():
    bpy.utils.unregister_class(UnwrapAssistOperator)
    bpy.types.VIEW3D_MT_uv_map.remove(menu_func)


if __name__ == "__main__":
    register()
