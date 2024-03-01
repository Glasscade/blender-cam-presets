import bpy
import os
import json

loadedpresets = {
    "x_res": 1400,
    "y_res": 1400
}

def saveCamPresetTest():
    with open('presets.json', 'w') as f:
        json.dump(loadedpresets,f, indent=4)

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
    bl_label = "Camera Presets"
    bl_idname = "CAMPRESETS_PT_main_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Camera Presets'

    def draw(self, context):
        self.layout.label(text="Test Panel")

bpy.utils.register_class(CameraPresetPanel)