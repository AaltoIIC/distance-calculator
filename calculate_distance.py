bl_info = {
    "name" : "Calculate Distance",
    "author" : "Joose Lankia",
    "version" : (1, 0),
    "blender" : (3, 3, 0),
    "location" : "View3d > Tool",
    "warning" : "",
    "wiki_url" : "",
    "category" : "Calculate Distance",
    }
    
    

import bpy
import mathutils
import math

min_distance = None

def select_mesh1():
    global mesh1
    
    bpy.ops.object.mode_set(mode='OBJECT')
    obj = bpy.context.active_object
    mesh = obj.data
    mesh1 = [v.co.to_tuple() for v in mesh.vertices if v.select]
    bpy.ops.object.mode_set(mode='EDIT')
    
    
def select_mesh2():
    global mesh2
    
    bpy.ops.object.mode_set(mode='OBJECT')
    obj = bpy.context.active_object
    mesh = obj.data
    mesh2 = [v.co.to_tuple() for v in mesh.vertices if v.select]
    bpy.ops.object.mode_set(mode='EDIT')
    
        
def calculate_distance_smallest():
    global min_distance
    min_distance = float("inf")
    for v1 in mesh1:
        for v2 in mesh2:
            distance = math.sqrt(
                                (v2[0] - v1[0]) ** 2 +
                                (v2[1] - v1[1]) ** 2 + 
                                (v2[2] - v1[2]) ** 2
                                )
            
            if distance < min_distance:
                min_distance = distance
                

def calculate_distance_largest():
    global min_distance
    min_distance = 0
    for v1 in mesh1:
        for v2 in mesh2:
            distance = math.sqrt(
                                (v2[0] - v1[0]) ** 2 +
                                (v2[1] - v1[1]) ** 2 + 
                                (v2[2] - v1[2]) ** 2
                                )
            
            if distance > min_distance:
                min_distance = distance
    
    
class MYADDON_OT_select_mesh1(bpy.types.Operator):
    bl_idname = "obj.select_mesh1"
    bl_label = "Select"
    
    def execute(self, context):
        select_mesh1()
        bpy.ops.mesh.select_all(action='DESELECT')
        return {'FINISHED'} 
    
        
class MYADDON_OT_select_mesh2(bpy.types.Operator):
    bl_idname = "obj.select_mesh2"
    bl_label = "Select"
    
    def execute(self, context):
        select_mesh2()
        bpy.ops.mesh.select_all(action='DESELECT')
        return {'FINISHED'} 
    

class MYADDON_OT_calculate_smallest(bpy.types.Operator):
    bl_idname = "obj.calculate_smallest"
    bl_label = "Smallest"
    
    def execute(self, context):
        calculate_distance_smallest()
        return {'FINISHED'}


class MYADDON_OT_calculate_largest(bpy.types.Operator):
    bl_idname = "obj.calculate_largest"
    bl_label = "Largest"
    
    def execute(self, context):
        calculate_distance_largest()
        return {'FINISHED'}


class MYPANEL_PT_distance(bpy.types.Panel):
    bl_idname = "MYPANEL_PT_distance"
    bl_label = "Calculate Distance"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Calculate Distance"
    
    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.label(text = "Select 1st mesh")
        row.operator("obj.select_mesh1")
        
        row = layout.row()
        row.label(text="Select 2nd mesh")
        row.operator("obj.select_mesh2")
        
        row = layout.row()
        row.label(text = "Calculate Distance")
        row = layout.row()
        row.operator("obj.calculate_smallest")
        row.operator("obj.calculate_largest")
        if min_distance:
            row = layout.row()
            row.scale_y = 1.4
            row.label(text = f"Distance: {min_distance:.6f}")
            

def register():
    bpy.utils.register_class(MYPANEL_PT_distance)
    bpy.utils.register_class(MYADDON_OT_select_mesh1)
    bpy.utils.register_class(MYADDON_OT_select_mesh2)
    bpy.utils.register_class(MYADDON_OT_calculate_smallest)
    bpy.utils.register_class(MYADDON_OT_calculate_largest)
    
def unregister():
    bpy.utils.unregister_class(MYPANEL_PT_distance)
    bpy.utils.unregister_class(MYADDON_OT_select_mesh1)
    bpy.utils.unregister_class(MYADDON_OT_select_mesh2)
    bpy.utils.unregister_class(MYADDON_OT_calculate_smallest)
    bpy.utils.unregister_class(MYADDON_OT_calculate_largest)
    
if __name__ == "__main__":
    register()
