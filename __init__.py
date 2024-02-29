import bpy

def getRes():
    current_scene = bpy.context.scene
    x_res = current_scene.render.resolution_x
    y_res = current_scene.render.resolution_y
    print(f"Current Scene Res: {x_res} by {y_res}")

def setRes(x_res, y_res):
    current_scene = bpy.context.scene
    current_scene.render.resolution_x = x_res
    current_scene.render.resolution_y = y_res
getRes()

setRes(1920,1080)

class CameraPresetPanel(bpy.types.Panel):
    bl_label = "Camera Presets Panel"
    bl_idname = "CameraPresets_main_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'Tool'
    bl_category = "CamPresets"

    def draw(self, context):
        self.layout.label(text="Test Panel")

bpy.utils.register_class(CameraPresetPanel)