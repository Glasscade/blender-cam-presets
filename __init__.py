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

setRes(1000,1000)