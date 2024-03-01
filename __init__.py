import bpy
import os
import json

# Basic Preset Format

## Cam Types
# "PERSP", "ORTHO", "PANO"
# To Add: Fisheye Equisolid Options, include default params.


loadedpresets = {
    ## Render Settings
    "x_res": 1400,
    "y_res": 1400,
    ## Camera Settings
    "cam_type": "PERSP",
    "lens_unit": "MILLIMETRES", #/"FOV"
    "focal_length": 51,
    "shift_x": 0.0,
    "shift_y": 0.0,
    "clip_start": 0.0001,
    "clip_end": 100
}




# Write Test
with open('./blender-cam-presets/presets.json', 'w') as f:
    json.dump(loadedpresets,f, indent=4)

# Read Test
with open('./blender-cam-presets/presets.json', 'r') as jfile:
    data = json.load(jfile)

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
setRes(data["x_res"],data["y_res"])

class CameraPresetPanel(bpy.types.Panel):
    bl_label = "Camera Presets"
    bl_idname = "CAMPRESETS_PT_main_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Camera Presets'

    def draw(self, context):
        self.layout.label(text="Test Panel")

bpy.utils.register_class(CameraPresetPanel)