""" 
A Panel with some statistics and basic operators to learn python code for blender
Copyright (C) 2025 Sheila

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General
 Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; 
without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.
"""


if "node_align" in locals():
    import importlib
    importlib.reload(node_align)
    importlib.reload(unwrap_assist)
    importlib.reload(scale_relative_to_camera)
    importlib.reload(panels)
    
from . import node_align, panels, scale_relative_to_camera, unwrap_assist


def register():
    node_align.register()
    panels.register()
    scale_relative_to_camera.register()
    unwrap_assist.register()

def unregister():
    node_align.unregister()
    panels.unregister()
    scale_relative_to_camera.unregister()
    unwrap_assist.unregister()
