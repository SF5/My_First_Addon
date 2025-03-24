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


from . import scale_relative_to_camera, unwrap_assist

class SFStatisticsPanel(bpy.types.Panel):
    bl_label = 'Statistics'
    bl_idname = 'OBJECT_PT_statistics'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Item"
    
   
    def draw(self, context):
        layout = self.layout

        obj = context.object
        col = layout.column(heading="Show")
        col.prop(obj, "show_name", text="Name")
        col.prop(obj, "show_axis", text="Axes")
        col.prop(obj, "show_in_front", text="In Front")

       
        layout.separator()   
        active_object = context.view_layer.objects.active
        if active_object is None:
            return

        layout.label(text='Visibility')
        row = layout.row(align=True)     
        row.prop(active_object, 'hide_viewport', text='Viewport') #hide viewport is the property
        row.prop(active_object, 'hide_render', text= 'Render')

        layout.label(text='Selected Object')
        name = active_object.name
        layout.label(text=name, icon='OBJECT_DATA')
        
        modifiers_count=str(len(active_object.modifiers)) +  ' modifiers'
        layout.label(text=modifiers_count, icon='MODIFIER')
        
        mode = bpy.context.active_object.mode
        if mode == 'EDIT':
            vertcount=str(active_object.data.total_vert_sel) +  ' vertices selected'
            layout.label(text=vertcount, icon='VERTEXSEL')
        
        layout.separator()

        
class SFFavoritesPanel(bpy.types.Panel):
    bl_label = 'Favorites'
    bl_idname = 'OBJECT_PT_favorites'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Item"
    
    #show panel always
    
    def draw(self, context):
                
        layout = self.layout  
        operator = layout.operator('object.transform_apply', text= 'Apply Object Scale')
        operator.location = False
        operator.rotation = False
        operator.scale = True

        operator = layout.operator('object.duplicates_make_real')
        operator.use_base_parent = True
        operator.use_hierarchy = True
        
        layout.label(text='in edit mode')
        col = layout.column(align=True, heading='my Favorites' ) 

   
        operator = layout.operator('mesh.loop_to_region')
        operator.select_bigger=False
        operator= layout.operator('mesh.normals_make_consistent')
        
        layout.operator(scale_relative_to_camera.ScaleToCameraOperator.bl_idname)
        layout.operator(unwrap_assist.UnwrapAssistOperator.bl_idname)
        
def register():
    bpy.utils.register_class(SFStatisticsPanel)
    bpy.utils.register_class(SFFavoritesPanel)
    
def unregister():
    bpy.utils.unregister_class(SFStatisticsPanel)
    bpy.utils.unregister_class(SFFavoritesPanel)
        

if __name__ == "__main__":
    register()