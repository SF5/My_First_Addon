""" 
A Panel with some statistics and basic operators to learn python code for blender
Copyright (C) 2025 Sheila

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General
 Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; 
without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.
"""


import bpy

class ScaleToCameraOperator(bpy.types.Operator):
    bl_idname= 'transform.resize_to_camera'
    bl_label = 'Scale to Camera'
    bl_description = 'Scale (resize) selected items relative to scene camera'
    bl_options = { 'REGISTER', 'UNDO'} 
    
    #def invoke(self, context, event):
        #camera = context.scene.camera
       # return bpy.ops.transform.resize('INVOKE DEFAULT', center_override=camera.location)

    def invoke(self, context, event):
        camera = context.scene.camera
        if camera is None:
            self.report({'ERROR'}, 'No active camera')
            return {'CANCELLED'}

        return bpy.ops.transform.resize(
            'INVOKE_DEFAULT',
            center_override=camera.location
        )

    def execute(self, context):
        camera = context.scene.camera
        if camera is None:
            self.report({'ERROR'}, 'No active camera')
            return {'CANCELLED'}

        return bpy.ops.transform.resize(
            value=self.value,
            center_override=camera.location
        )
    
    
#instead of adding to panel we add to a menu    
def menu_func(self, context):
    self.layout.operator(ScaleToCameraOperator.bl_idname)


# Register and add to the "object" menu (required to also use F3 search 
# ScaleToCameraOperator for quick access).
def register():
    bpy.utils.register_class(ScaleToCameraOperator)
    bpy.types.VIEW3D_MT_object.append(menu_func) #MT is the category for menu


def unregister():
    bpy.utils.unregister_class(ScaleToCameraOperator)
    bpy.types.VIEW3D_MT_object.remove(menu_func)


if __name__ == "__main__":
    register()