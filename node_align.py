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


class NodeAlignOperator(bpy.types.Operator):
    """Aligns selected nodes to each other"""
    bl_idname = "node.align"
    bl_label = "Node Align"
    bl_options={'REGISTER' , 'UNDO' }
    
    
    alignment: bpy.props.EnumProperty(
        default =  'X',
        items=[
            ('X', 'Horizontal','Aligns nodes horizontally on the X axis'),
            ('Y', 'Vertically','Aligns nodes vertically on the Y axis'),
        ]
        )

    @classmethod
    def poll(cls, context):
        return hasattr(context, 'selected_nodes') #and context.active_object is not None

    def execute(self, context):
        nodes= context.selected_nodes
        align_val =  self.alignment
        
        if len(nodes) <=1:
            return{'CANCELLED'}
        
        if align_val == 'X':
            y_locations= [ node.location.y for node in nodes]
            value = sum(y_locations)/len(y_locations)
            for node in nodes:
                node.location.y = value
        elif align_val == 'Y':
            x_locations= [ node.location.x for node in nodes]
            value = sum(x_locations)/len(x_locations)
            for node in nodes:
                node.location.x = value
        return {'FINISHED'}


def menu_func(self, context):
    self.layout.separator()
    self.layout.operator_menu_enum(NodeAlignOperator.bl_idname, 'alignment', text='Align')


# Register and add to the "object" menu (required to also use F3 search for quick access).
def register():
    bpy.utils.register_class(NodeAlignOperator)
    bpy.types.NODE_MT_node.append(menu_func)


def unregister():
    bpy.utils.unregister_class(NodeAlignOperator)
    bpy.types.NODE_MT_node.remove(menu_func)


if __name__ == "__main__":
    register()